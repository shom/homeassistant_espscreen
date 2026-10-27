#pragma once
// A page one step away slides (firmware 0.54+). The page leaving is drawn once into a picture in PSRAM, the new page is
// placed under it exactly as before, and the picture moves off the glass: nothing on the new page is laid out or drawn
// for the animation, so a frame copies the picture and the strip of new page it uncovers. It needs LVGL's snapshot
// (LV_USE_SNAPSHOT: features/snapshot.yaml, and camera.yaml for the boards with pictures) and the PSRAM for a full-size
// picture. A board without either, or a card open over the page, keeps the instant switch, which the swipe glow still
// answers; the glow is taken into the picture, so it leaves with the page.
#include "lvgl.h"
#include "esphome/core/log.h"
#include <cstddef>
#include <cstdint>
#if LV_USE_SNAPSHOT && LV_USE_IMAGE && defined(USE_ESP32)
#include "esp_heap_caps.h"
#endif

namespace page_slide {
#if LV_USE_SNAPSHOT && LV_USE_IMAGE && defined(USE_ESP32)
// Quick enough that the finger has not moved on, slow enough to read as one movement (the glow is 420 ms).
constexpr uint32_t SLIDE_MS = 240;
// A widget can draw outside its box (an outline, a shadow): the picture takes that much extra on every side.
constexpr int SLACK = 16;
// The picture shares the PSRAM with the cards and their pictures: no slide that leaves the rest less than this.
constexpr size_t RESERVE = 1 << 20;

inline lv_obj_t *source = nullptr;       // the page the picture was taken from
inline lv_obj_t *picture = nullptr;      // what slides over it
inline lv_draw_buf_t picture_buf;
inline uint8_t *picture_data = nullptr;  // in PSRAM, kept for the next slide
inline size_t picture_room = 0;
inline int direction = 1;
inline bool running = false;
// The gesture that asked for the switch (a swipe, a page key, Back), taken by show_page. A jump by a navigation tile
// asks for none: the pages it crosses are not the way the finger went.
inline int wanted = 0;
inline void wants(int step) { wanted = step < 0 ? -1 : step > 0 ? 1 : 0; }
inline int take_wanted() { const int step = wanted; wanted = 0; return step; }

inline void forget() {
  if (picture) {
    lv_anim_delete(picture, nullptr);
    lv_obj_delete(picture);
    picture = nullptr;
  }
  running = false;
}
inline void cancel() { forget(); source = nullptr; }

// The page about to leave, as it stands: taken here, before the new page takes its place. False when the page has no
// picture, and `show_page` then switches as it always did.
inline bool begin(lv_obj_t *page, int step) {
  cancel();
  if (!page) return false;
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
    return false;
  }
  source = page;
  direction = step < 0 ? -1 : 1;
  ESP_LOGI("slide", "page pictured %ux%u in %u ms", (unsigned) picture_buf.header.w, (unsigned) picture_buf.header.h,
           (unsigned) (lv_tick_get() - started));
  return true;
}

// The new page is placed: the picture goes over it and out of the glass, towards the page the finger asked for.
inline void run() {
  if (!source) return;
  if (!picture) {
    picture = lv_image_create(source);
    lv_obj_remove_style_all(picture);
    lv_obj_remove_flag(picture, LV_OBJ_FLAG_SCROLLABLE);
    lv_obj_add_flag(picture, LV_OBJ_FLAG_IGNORE_LAYOUT);
    // A tap while the page moves is no tap on the page under it, and the card keys of the page leaving are gone.
    lv_obj_add_flag(picture, LV_OBJ_FLAG_CLICKABLE);
  }
  lv_image_set_src(picture, &picture_buf);
  lv_obj_set_size(picture, picture_buf.header.w, picture_buf.header.h);
  // The picture's first pixel is the page's top left, less what the page draws outside its box.
  const int ext = (int) (picture_buf.header.w - lv_obj_get_width(source)) / 2;
  lv_obj_set_pos(picture, -ext, -ext);
  lv_obj_set_style_translate_x(picture, 0, 0);
  lv_obj_move_foreground(picture);
  const int32_t distance = direction > 0 ? -(int32_t) picture_buf.header.w : (int32_t) picture_buf.header.w;
  lv_anim_t move;
  lv_anim_init(&move);
  lv_anim_set_var(&move, picture);
  lv_anim_set_values(&move, 0, distance);
  lv_anim_set_duration(&move, SLIDE_MS);
  // Off at once: the finger has already said where the page goes, so most of the way is shown at the start.
  lv_anim_set_path_cb(&move, lv_anim_path_ease_out);
  lv_anim_set_exec_cb(&move, [](void *object, int32_t value) {
    lv_obj_set_style_translate_x(static_cast<lv_obj_t *>(object), value, 0);
  });
  lv_anim_set_completed_cb(&move, [](lv_anim_t *) { forget(); });
  running = true;
  lv_anim_start(&move);
}
#else
inline bool begin(lv_obj_t *, int) { return false; }
inline void run() {}
inline void cancel() {}
inline void wants(int) {}
inline int take_wanted() { return 0; }
#endif
}  // namespace page_slide
