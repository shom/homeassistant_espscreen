#pragma once
// A page one step away slides (firmware 0.54+; both sides since the fork's page work). The page leaving is drawn once
// into a picture in PSRAM and the new page is drawn into a second one - rendered before the switch in the plain path,
// or filled in batches under the crossing pictures when the fill is staggered (甲·错峰, PAGE_SLIDE_STAGGER); the two
// pictures then slide over the glass in lockstep while the live tile area rests hidden, and the area shows again the
// frame the fill hands it over: the last picture and the live area draw the same state, so the handover does not jump.
// The old one-picture slide (the leaving page over the new one) stays as the fallback when the second picture does not
// fit. It needs LVGL's snapshot (LV_USE_SNAPSHOT: features/snapshot.yaml, and camera.yaml for the boards with pictures)
// and the PSRAM for two full-size pictures. A board without either, or a card open over the page, keeps the instant
// switch, which the swipe glow still answers; the glow is taken into the picture, so it leaves with the page.
#include "lvgl.h"
#include "esphome/core/log.h"
#include <cstddef>
#include <cstdint>
#if LV_USE_SNAPSHOT && LV_USE_IMAGE && defined(USE_ESP32)
#include "esp_heap_caps.h"
#endif

namespace page_slide {
// The board states the length (PAGE_SLIDE_MS in features/snapshot.yaml, core passes it at boot); this is the default.
constexpr uint32_t DEFAULT_SLIDE_MS = 240;
// A widget can draw outside its box (an outline, a shadow): the picture takes that much extra on every side.
constexpr int SLACK = 16;
constexpr int STOP = 1000;  // the shared clock of the two pictures: one screen width of travel at its end

#if LV_USE_SNAPSHOT && LV_USE_IMAGE && defined(USE_ESP32)
// The picture shares the PSRAM with the cards and their pictures: no slide that leaves the rest less than this.
constexpr size_t RESERVE = 1 << 20;

inline lv_obj_t *source = nullptr;         // the tile area the pictures were taken from
inline lv_obj_t *picture = nullptr;        // the page leaving, sliding out
inline lv_draw_buf_t picture_buf;
inline uint8_t *picture_data = nullptr;    // in PSRAM, kept for the next slide
inline size_t picture_room = 0;
inline lv_obj_t *picture_in = nullptr;     // the new page, sliding in beside the other
inline lv_draw_buf_t buf_in;
inline uint8_t *data_in = nullptr;
inline size_t room_in = 0;
inline int base_x = 0, base_y = 0;         // where the area's picture rests on the page, slack included
inline int32_t travel_px = 0;              // signed screen width: the direction the step asked for
inline int last_value = STOP;              // the anim's last step of `picture`, so a late join hangs where the glass stands
inline uint32_t slide_ms = DEFAULT_SLIDE_MS;
inline uint32_t stagger_ms = 0;            // a batch of the new page's cards every N ms under the slide (甲·错峰)
inline bool running = false;
inline void set_duration(uint32_t ms) { slide_ms = ms <= 1000 ? ms : 1000; }  // 0 switches the slide off at its source
inline void set_stagger(uint32_t ms) { stagger_ms = ms <= 200 ? ms : 200; }    // 0: the content pass stays before the slide
inline bool staggered() { return stagger_ms > 0 && slide_ms > 0; }
inline void reveal() { if (source) lv_obj_remove_flag(source, LV_OBJ_FLAG_HIDDEN); }
// The gesture that asked for the switch (a swipe, a page key, Back), taken by show_page. A jump by a navigation tile
// asks for none: the pages it crosses are not the way the finger went.
inline int wanted = 0;
inline void wants(int step) { wanted = step < 0 ? -1 : step > 0 ? 1 : 0; }
inline int take_wanted() { const int step = wanted; wanted = 0; return step; }

inline void forget() {
  if (picture) {
    lv_anim_delete(picture, nullptr);  // the one anim of the pair, whichever picture it rides on
    lv_obj_delete(picture);
    picture = nullptr;
  }
  if (picture_in) {
    lv_obj_delete(picture_in);
    picture_in = nullptr;
  }
  // The live area stays as it is: under a staggered slide its fill may still run, and `join` reveals it at the end.
  running = false;
}
inline void cancel() { forget(); source = nullptr; }  // a new switch pictures the leaving page in `begin`

// One page's state goes into `buf` as it stands - taken while nothing moves on the glass, before anything slides.
// The live area may rest hidden between these lines and the `join`: a hidden area pictures blank, so `join` shows it
// for the capture inside one loop iteration (no render runs between the two flag writes). False without room.
inline bool capture(lv_draw_buf_t &buf, uint8_t *&data, size_t &room, lv_obj_t *page) {
  const int width = lv_obj_get_width(page), height = lv_obj_get_height(page);
  if (width <= 0 || height <= 0) return false;
  const uint32_t w = width + SLACK, h = height + SLACK;
  const uint32_t stride = lv_draw_buf_width_to_stride(w, LV_COLOR_FORMAT_RGB565);
  const size_t need = (size_t) stride * h;
  if (room < need) {
    if (heap_caps_get_free_size(MALLOC_CAP_SPIRAM) < need + RESERVE) {
      ESP_LOGW("slide", "PSRAM too low for a %ux%u page picture", (unsigned) w, (unsigned) h);
      return false;
    }
    if (data) heap_caps_free(data);
    data = static_cast<uint8_t *>(heap_caps_malloc(need, MALLOC_CAP_SPIRAM | MALLOC_CAP_8BIT));
    room = data ? need : 0;
    if (!data) {
      ESP_LOGW("slide", "no PSRAM for a %ux%u page picture", (unsigned) w, (unsigned) h);
      return false;
    }
  }
  if (lv_draw_buf_init(&buf, w, h, LV_COLOR_FORMAT_RGB565, stride, data, room) != LV_RESULT_OK) return false;
  const uint32_t started = lv_tick_get();
  if (lv_snapshot_take_to_draw_buf(page, LV_COLOR_FORMAT_RGB565, &buf) != LV_RESULT_OK) {
    ESP_LOGW("slide", "the page did not fit its picture");
    return false;
  }
  ESP_LOGI("slide", "page pictured %ux%u in %u ms", (unsigned) buf.header.w, (unsigned) buf.header.h,
           (unsigned) (lv_tick_get() - started));
  return true;
}

// The page about to leave, before the new page takes its place. False when there is no picture, and `show_page`
// then switches as it always did.
inline bool begin(lv_obj_t *page, int step) {
  cancel();
  if (!page || !slide_ms) return false;
  buf_in.header.w = 0;  // the new page is not pictured yet: `take` decides whether this slide crosses a pair
  if (!capture(picture_buf, picture_data, picture_room, page)) return false;
  source = page;
  // The picture's first pixel is the area's top left, less what the area draws outside its box.
  base_x = lv_obj_get_x(page) - (int) SLACK / 2;
  base_y = lv_obj_get_y(page) - (int) SLACK / 2;
  travel_px = step < 0 ? (int32_t) picture_buf.header.w : -(int32_t) picture_buf.header.w;
  return true;
}

// The picture of the new page for a slide that starts now: its finished state in the plain path (show_page has
// rendered before calling), the area's skeleton under a staggered fill - `join` replaces it with the finished one.
// False without room for the second picture; the switch then slides one-sided over the live area as it did before.
inline bool take() {
  if (!source) return false;
  if (!capture(buf_in, data_in, room_in, source)) return false;
  // The live area drew both pictures: it rests while they cross, so no state change lands between a frame and the next.
  lv_obj_add_flag(source, LV_OBJ_FLAG_HIDDEN);
  return true;
}

// A picture over the area it was taken from, at the end of the step it starts from. A tap while the pages move is no
// tap on the area under them, and the card keys of the page leaving are gone with its picture.
inline lv_obj_t *lay(lv_draw_buf_t &buf, int x) {
  lv_obj_t *o = lv_image_create(lv_obj_get_parent(source));
  lv_obj_remove_style_all(o);
  lv_obj_remove_flag(o, LV_OBJ_FLAG_SCROLLABLE);
  lv_obj_add_flag(o, LV_OBJ_FLAG_IGNORE_LAYOUT);
  lv_obj_add_flag(o, LV_OBJ_FLAG_CLICKABLE);
  lv_image_set_src(o, &buf);
  lv_obj_set_size(o, buf.header.w, buf.header.h);
  lv_obj_set_pos(o, x, base_y);
  lv_obj_move_foreground(o);
  return o;
}

// Where each picture rests at the start of the step: the pair sits one picture apart, the old page on the side the
// finger came from, the new one on the side it asked for. In the one-sided fallback `out_home` is the area's home
// when the step goes forward, and the old page slides off it as the original slide did.
inline int32_t out_home() {
  const int32_t w = (int32_t) picture_buf.header.w;
  return base_x - (travel_px < 0 ? w : 0);  // going to the next page, the old one leaves from its place
}
inline int32_t in_home() { return base_x + travel_px; }
// The value a picture joins at when the fill finishes mid-flight: where the glass stands right now, not where the
// step started. The share `last_value * width` is the step already travelled, so the picture hangs over its own end.
inline int32_t join_anchor() { return (int32_t) buf_in.header.w * (STOP - last_value) / STOP; }

// The pictures slide: both ride the one anim's progress, so they cannot drift apart.
inline void run() {
  if (!source) return;
  picture = lay(picture_buf, out_home());
  if (buf_in.header.w) picture_in = lay(buf_in, in_home());
  lv_anim_t move;
  lv_anim_init(&move);
  lv_anim_set_var(&move, picture);
  lv_anim_set_values(&move, 0, STOP);
  lv_anim_set_duration(&move, slide_ms);
  // Even at both ends, quick through the middle: two sides moving reads as one gesture, not as a page fleeing.
  lv_anim_set_path_cb(&move, lv_anim_path_ease_in_out);
  lv_anim_set_exec_cb(&move, [](void *object, int32_t value) {
    (void) object;
    last_value = value;
    const int32_t dx = travel_px * value / STOP;
    if (picture) lv_obj_set_x(picture, out_home() + dx);
    if (picture_in) lv_obj_set_x(picture_in, in_home() + join_anchor() + dx);
  });
  lv_anim_set_completed_cb(&move, [](lv_anim_t *) { forget(); });
  running = true;
  lv_anim_start(&move);
}

// The new page is rendered (before the slide in the plain path, under it when the fill was staggered): picture it and
// hang it beside the crossing pair. Without the second picture there is nothing to join: the area shows as it stands.
inline void join() {
  if (!source) return;
  // The snapshot draws what stands on the glass: a hidden area would picture blank, so it shows for the capture and
  // goes back under the pictures until the handover.
  lv_obj_remove_flag(source, LV_OBJ_FLAG_HIDDEN);
  const bool has = capture(buf_in, data_in, room_in, source);
  if (!running || !has) {  // the glass crossed without us (or no second picture): the live area takes over now
    if (!has) buf_in.header.w = 0;
    forget();
    return;  // shown, unrevealed work is none: the fill ended or never joined
  }
  lv_obj_add_flag(source, LV_OBJ_FLAG_HIDDEN);  // the fill ran out of the slide: it waits below until the pair is gone
  picture_in = lay(buf_in, in_home() + join_anchor());
  buf_in.header.w = 0;  // laid: the buffer belongs to the object now, and a re-`run` must not lay it twice
}
#else
inline bool begin(lv_obj_t *, int) { return false; }
inline bool take() { return false; }
inline void run() {}
inline void join() {}
inline void cancel() {}
inline void wants(int) {}
inline int take_wanted() { return 0; }
inline void set_duration(uint32_t) {}
inline void set_stagger(uint32_t) {}
inline bool staggered() { return false; }
inline void reveal() {}
#endif
}  // namespace page_slide
