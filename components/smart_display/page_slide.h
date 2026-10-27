#pragma once
// A page one step away slides (firmware 0.54+). The page leaving is drawn once into a picture in PSRAM, the new page is
// placed and rendered under it exactly as before, and the picture moves off the glass: what it uncovers is the finished
// new page, so the frame the picture leaves is already the frame the live area shows - no handover to arrange. It needs
// LVGL's snapshot (LV_USE_SNAPSHOT: features/snapshot.yaml, and camera.yaml for the boards with pictures) and the PSRAM
// for a full-size picture. A board without either, or a card open over the page, keeps the instant switch, which the
// swipe glow still answers; the glow is taken into the picture, so it leaves with the page.
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
constexpr int STOP = 1000;  // the anim's own clock: one picture's width of travel at its end

#if LV_USE_SNAPSHOT && LV_USE_IMAGE && defined(USE_ESP32)
// The picture shares the PSRAM with the cards and their pictures: no slide that leaves the rest less than this.
constexpr size_t RESERVE = 1 << 20;

inline lv_obj_t *source = nullptr;         // the page the picture was taken from, and the object the picture rides on
inline lv_obj_t *picture = nullptr;        // the page leaving, sliding out over the new one
inline lv_draw_buf_t picture_buf;
inline uint8_t *picture_data = nullptr;    // in PSRAM, kept for the next slide
inline size_t picture_room = 0;
inline int home_x = 0, home_y = 0;         // where the picture rests over its page, slack included
inline int32_t travel_px = 0;              // signed picture width: the side the step asked for
inline uint32_t slide_ms = DEFAULT_SLIDE_MS;
inline void set_duration(uint32_t ms) { slide_ms = ms <= 1000 ? ms : 1000; }  // 0 switches the slide off at its source
// The gesture that asked for the switch (a swipe, a page key, Back), taken by show_page. A jump by a navigation tile
// asks for none: the pages it crosses are not the way the finger went.
inline int wanted = 0;
inline void wants(int step) { wanted = step < 0 ? -1 : step > 0 ? 1 : 0; }
inline int take_wanted() { const int step = wanted; wanted = 0; return step; }

// The moving object goes, and with it the anim: an anim outliving its var would set_x on freed memory. The picture's
// bytes stay for the next slide, which asks for the same room or less; nothing on the glass refers to them now.
inline void forget() {
  if (picture) {
    lv_anim_delete(picture, nullptr);
    lv_obj_delete(picture);
    picture = nullptr;
  }
  source = nullptr;
}

// The page about to leave, as it stands: taken here, before the new page takes its place. False when the page has no
// picture, and `show_page` then switches as it always did.
inline bool begin(lv_obj_t *page, int step) {
  forget();  // a slide still on its way gives up the glass to this one
  picture_buf.header.w = 0;  // until the new picture stands, `run` has nothing it may show
  if (!page || !slide_ms) return false;
  const int width = lv_obj_get_width(page), height = lv_obj_get_height(page);
  if (width <= 0 || height <= 0) return false;
  const uint32_t w = width + SLACK, h = height + SLACK;
  const uint32_t stride = lv_draw_buf_width_to_stride(w, LV_COLOR_FORMAT_RGB565);
  const size_t room = (size_t) stride * h;
  if (picture_room < room) {
    if (heap_caps_get_free_size(MALLOC_CAP_SPIRAM) < room + RESERVE) {
      ESP_LOGW("slide", "PSRAM too low for a %ux%u page picture", (unsigned) w, (unsigned) h);
      return false;
    }
    if (picture_data) heap_caps_free(picture_data);
    picture_data = static_cast<uint8_t *>(heap_caps_malloc(room, MALLOC_CAP_SPIRAM | MALLOC_CAP_8BIT));
    picture_room = picture_data ? room : 0;
    if (!picture_data) {
      ESP_LOGW("slide", "no PSRAM for a %ux%u page picture", (unsigned) w, (unsigned) h);
      return false;
    }
  }
  if (lv_draw_buf_init(&picture_buf, w, h, LV_COLOR_FORMAT_RGB565, stride, picture_data, picture_room) != LV_RESULT_OK)
    return false;
  const uint32_t started = lv_tick_get();
  if (lv_snapshot_take_to_draw_buf(page, LV_COLOR_FORMAT_RGB565, &picture_buf) != LV_RESULT_OK) {
    ESP_LOGW("slide", "the page did not fit its picture");
    picture_buf.header.w = 0;
    return false;
  }
  source = page;
  // The picture is the page's own child: its first pixel is the page's top left, less what the page draws outside its box.
  home_x = -((int) (picture_buf.header.w - (uint32_t) width) / 2);
  home_y = -((int) (picture_buf.header.h - (uint32_t) height) / 2);
  travel_px = step < 0 ? (int32_t) picture_buf.header.w : -(int32_t) picture_buf.header.w;
  ESP_LOGI("slide", "page pictured %ux%u in %u ms", (unsigned) picture_buf.header.w, (unsigned) picture_buf.header.h,
           (unsigned) (lv_tick_get() - started));
  return true;
}

// The new page is placed and rendered: the picture goes over it and out of the glass, towards the page the finger
// asked for. Only now does the object exist - `begin` took the picture, `show_page` drew what the slide uncovers.
inline void run() {
  if (!source || !picture_buf.header.w) return;
  picture = lv_image_create(source);
  lv_obj_remove_style_all(picture);
  lv_obj_remove_flag(picture, LV_OBJ_FLAG_SCROLLABLE);
  lv_obj_add_flag(picture, LV_OBJ_FLAG_IGNORE_LAYOUT);
  // A tap while the page moves is no tap on the page under it, and the card keys of the page leaving are gone.
  lv_obj_add_flag(picture, LV_OBJ_FLAG_CLICKABLE);
  lv_image_set_src(picture, &picture_buf);
  lv_obj_set_size(picture, picture_buf.header.w, picture_buf.header.h);
  lv_obj_set_pos(picture, home_x, home_y);
  lv_obj_move_foreground(picture);
  lv_anim_t move;
  lv_anim_init(&move);
  lv_anim_set_var(&move, picture);
  lv_anim_set_values(&move, 0, STOP);
  lv_anim_set_duration(&move, slide_ms);
  // Off at once: the finger has already said where the page goes, so most of the way is shown at the start.
  lv_anim_set_path_cb(&move, lv_anim_path_ease_out);
  lv_anim_set_exec_cb(&move, [](void *object, int32_t value) {
    (void) object;
    if (picture) lv_obj_set_x(picture, home_x + travel_px * value / STOP);
  });
  lv_anim_set_completed_cb(&move, [](lv_anim_t *) { forget(); });
  lv_anim_start(&move);
}
#else
inline bool begin(lv_obj_t *, int) { return false; }
inline void run() {}
inline void forget() {}
inline void wants(int) {}
inline int take_wanted() { return 0; }
inline void set_duration(uint32_t) {}
#endif
}  // namespace page_slide
