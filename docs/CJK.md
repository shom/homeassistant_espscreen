# Chinese (CJK) text on the screens

The screens' five text fonts are a fixed set (docs/RESPONSIVE.md, "One set of fonts") that carries Latin and the
letters European languages write with. This page is about the CJK glyphs a board may add on top, and the `zh`
translation that goes with them.

## How it is gated

- `packages/core.yaml` states the defaults: `FONT_CJK_FILE` (the face), `FONT_CJK_GLYPHS` (empty, so an extra that
  carries no glyphs and costs nothing) and `SCREEN_CJK` (false).
- Four of the five text fonts (`headline`, `label`, `sublabel`, `sublabel_big`) take a second `extras:` entry whose
  glyphs are `${FONT_CJK_GLYPHS}`. `watch_value` stays Latin: at its size the whole set would cost more than the
  other four together, and a large value is a number anyway.
- A board that has the flash for Chinese states the set and the flag. Today only `packages/hardware/guition-esp32p4.yaml`
  does, so the ESP32-P4 boards (Guition 10.1-inch, 7-inch and 4.3-inch, CrowPanel 10.1) draw Chinese; every other
  board builds exactly as before, and the four base glyph lists are unchanged (tests/test_cjk.py holds this).
- The set lives in `fonts/NotoSansSC-Regular-cjk.ttf` (Noto Sans SC, SIL OFL 1.1), cut with fontTools' pyftsubset to
  the 1 500 most common hanzi by frequency, CJK punctuation, and the words of the zh translation - 1 553 glyphs,
  about 420 KB. Rasterised at the four sizes with bpp 4 it costs roughly 2 MB of flash on a P4 build. Trim the set by
  stating a smaller `FONT_CJK_GLYPHS` in a screen's own YAML.
- ESPHome refuses a glyph that appears twice in one font, so the set must not repeat a character the main list
  already carries. `tests/test_cjk.py` holds the add-on's copy of the set against the board's.
- A build with `SCREEN_CJK: "true"` says `cjk` in its hello (packages/core.yaml, next to `battery`), and the app
  keeps Chinese text through `clean_text` only for a screen that said so (header_bar.CJK_GLYPHS, header_bar.set_cjk_screen);
  other screens keep their old behaviour, and the editor's preview always draws what the newest build does.

## The zh translation

`screen_manager/translations/zh.json` follows docs/TRANSLATING.md (plural rule `none`, 24-hour clock). Its `screen`
section - Home Assistant's state words, the boot and status texts, the dates - is translated and keeps to the CJK
set; keys this file still lacks are filled from English, so the screens show a mix until someone finishes it, and
`_meta.checked` stays false. Choose it per screen under Settings - Language & region; set that only on a board that
carries the CJK glyphs, or the texts show as boxes.

## Regenerating the set

```sh
pyftsubset NotoSansSC-Regular.ttf --text-file=chars.txt --output-file=fonts/NotoSansSC-Regular-cjk.ttf \
  --layout-features='*' --name-IDs='*' --name-legacy --name-languages='*' \
  --notdef-glyph --notdef-outline --recommended-glyphs --glyph-names --symbol-cmap --legacy-cmap
```

`chars.txt` is the frequency-ordered hanzi list plus punctuation; the same characters, minus the ones the main lists
already carry, are the `FONT_CJK_GLYPHS` value in the P4 hardware package and `header_bar.CJK_GLYPHS` in the app.
