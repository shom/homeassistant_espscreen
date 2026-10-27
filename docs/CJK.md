# Chinese (CJK) text on the screens

This fork draws two languages on the screens: English and Chinese. The text fonts are one family for both, so a
label that mixes them keeps one baseline and one line box.

## The face

- `fonts/SourceHanSansSC-Regular.otf`, `-Medium.otf` and `-Bold.otf` are Source Han Sans SC subsets (SIL OFL 1.1,
  see `fonts/SourceHanSansSC-OFL.txt`). They carry the printable ASCII characters, the punctuation the screens use,
  and the 1 566 Chinese glyphs the app and the zh translation need - 1 682 glyphs each, about 720 KB.
- `packages/core.yaml` states the three faces as `FONT_TEXT_REGULAR`, `FONT_TEXT_MEDIUM` and `FONT_TEXT_BOLD`; the five
  text fonts use them (`label` is the bold face, `headline` and `watch_value` the medium, `sublabel` and
  `sublabel_big` the regular). The Chinese glyphs of the four CJK-enabled fonts come from the same face through
  `extras:` (`FONT_CJK_GLYPHS`), which is what keeps the two scripts on one baseline.
- The subsets' vertical metrics are normalised to the line box the cards were designed with (hhea/OS/2 ascent 928 and
  descent -244 per 1000 upm, the ratios of Roboto, which every card size was tuned against), so the switch does not
  move any layout. Their outlines are unchanged.
- Only English and Chinese ship in this fork: the European letters are not in the glyph lists, so `clean_text` folds an
  accent to its base letter or drops it. One rare letter, `ŀ` (U+0140), no available face carries; it is gone from the
  lists. The digit steps and the brand wordmark are still Roboto.
- **Entity names are not known here.** A tile shows the name Home Assistant gives it, and a character the subsets do
  not carry shows as a box. The set covers the app's own texts and a common home vocabulary (rooms, appliances,
  family, states); after adding names with rarer characters, extend the set and rebuild the faces:

  ```sh
  python3 tools/build_cjk_font.py --source fonts/private/shs --add names.txt
  ```

  `names.txt` is any text: the script keeps its Chinese characters, rebuilds the three OTFs (metrics normalised as
  above), updates `FONT_CJK_GLYPHS` and `header_bar.CJK_GLYPHS`, and says what the flash costs (about 1 KB per
  character across the four steps).

## How the Chinese reaches a screen

- `SCREEN_CJK` states whether a build carries the Chinese glyphs; `packages/hardware/guition-esp32p4.yaml` turns it on
  for the ESP32-P4 boards, which have the flash. A build with it says `cjk` in its hello, and the app keeps Chinese
  text through `clean_text` only for a screen that said so (`header_bar.CJK_GLYPHS`, `header_bar.set_cjk_screen`);
  other screens keep their old behaviour, and the editor's preview always draws what the newest build does.
- The `zh` translation is `screen_manager/translations/zh.json`, next to `en.json`, the only two language files. Every
  `screen.*` text keeps to the glyph set (`tests/test_cjk.py`), and `tools/i18n.py check` proves it.
- The browser preview (web/wasm) draws the same Chinese: `generate_host_ui.py` gives its fonts the set from the P4
  hardware package whatever board's profile a variant is drawn from, so a rebuilt preview shows Chinese too.

## Regenerating the face

```sh
pyftsubset SourceHanSansSC-Regular.otf --text-file=chars.txt --output-file=fonts/SourceHanSansSC-Regular.otf \
  --layout-features='*' --name-IDs='*' --name-legacy --name-languages='*' \
  --notdef-glyph --notdef-outline --recommended-glyphs --glyph-names --symbol-cmap --legacy-cmap
```

Then set `hhea.ascent/descent/lineGap` and the OS/2 typo and win metrics to 928, -244 and 0, as the table above says.
`chars.txt` is printable ASCII, the punctuation the five lists carry, and the Chinese characters of
`header_bar.CJK_GLYPHS`.
