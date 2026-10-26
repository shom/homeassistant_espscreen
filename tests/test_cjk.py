"""The CJK glyphs (docs/CJK.md): which boards carry them, that the fonts and the add-on agree on the set, and that
the zh texts keep to it. The default build pays nothing: FONT_CJK_GLYPHS is one glyph the fonts already draw."""
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import profiles  # noqa: E402
sys.path.insert(0, str(ROOT / 'screen_manager' / 'app'))
import header_bar  # noqa: E402

HARDWARE = ROOT / 'packages' / 'hardware' / 'guition-esp32p4.yaml'
CJK_BOARD = 'checkout/jc4880p443.yaml'
BASE_BOARDS = ('checkout/cyd.yaml', 'checkout/guition.yaml')
TEXT_FONTS = ('headline', 'watch_value', 'label', 'sublabel', 'sublabel_big')
# watch_value stays Latin: at its size the whole set would cost more than the other four together (docs/CJK.md).
CJK_FONTS = ('headline', 'label', 'sublabel', 'sublabel_big')


def hardware_glyphs():
    """The FONT_CJK_GLYPHS substitution of the one hardware package that states it, as a set."""
    found = re.search(r'FONT_CJK_GLYPHS: "([^"]*)"', HARDWARE.read_text(encoding='utf-8'))
    return set(found.group(1))


def font_set(name, font):
    found = profiles.glyphs(profiles.resolved(name), font)
    return found if found is not None else set()


class FontTests(unittest.TestCase):
    def test_the_cjk_board_carries_the_set_in_four_of_the_five_text_fonts(self):
        cjk = hardware_glyphs()
        self.assertTrue(cjk)
        for font in CJK_FONTS:
            self.assertTrue(cjk <= font_set(CJK_BOARD, font), font)

    def test_the_base_boards_stay_as_they_were(self):
        for name in BASE_BOARDS:
            for font in TEXT_FONTS:
                self.assertEqual(font_set(name, font), header_bar.GLYPHS, (name, font))

    def test_the_cjk_board_draws_exactly_base_plus_the_set(self):
        cjk = hardware_glyphs()
        for font in CJK_FONTS:
            self.assertEqual(font_set(CJK_BOARD, font), header_bar.GLYPHS | cjk, font)
        self.assertEqual(font_set(CJK_BOARD, 'watch_value'), header_bar.GLYPHS, 'watch_value')


class AddonTests(unittest.TestCase):
    def test_the_addons_set_is_the_boards(self):
        self.assertEqual(header_bar.CJK_GLYPHS, hardware_glyphs())

    def test_clean_text_keeps_cjk_only_for_a_screen_that_draws_it(self):
        samples = '客厅的灯打开了吗'
        try:
            header_bar.set_cjk_screen(frozenset())
            self.assertEqual(header_bar.clean_text(samples), '')
            header_bar.set_cjk_screen({'cjk'})
            self.assertEqual(header_bar.clean_text(samples), samples)
            # None is the app's own firmware, the preview: it draws what the newest build does.
            header_bar.set_cjk_screen(None)
            self.assertEqual(header_bar.clean_text(samples), samples)
            # Latin behaviour unchanged, flag on or off.
            self.assertEqual(header_bar.clean_text('Ångström ✓'), 'Ångström')
        finally:
            header_bar.set_cjk_screen(frozenset())


class HelloTests(unittest.TestCase):
    def test_the_hello_names_the_feature_only_where_a_board_states_it(self):
        core = (ROOT / 'packages' / 'core.yaml').read_text(encoding='utf-8')
        self.assertIn('if (std::string("${SCREEN_CJK}") == "true") features.add("cjk");', core)
        self.assertIn('SCREEN_CJK: "false"', core)
        self.assertIn('SCREEN_CJK: "true"', HARDWARE.read_text(encoding='utf-8'))


class ZhTextTests(unittest.TestCase):
    def test_the_zh_texts_keep_to_the_glyphs_the_cjk_board_draws(self):
        zh = json.loads((ROOT / 'screen_manager' / 'translations' / 'zh.json').read_text(encoding='utf-8'))
        allowed = header_bar.GLYPHS | header_bar.CJK_GLYPHS

        def walk(node, path):
            if isinstance(node, dict):
                for key, value in node.items():
                    walk(value, f'{path}.{key}')
            elif isinstance(node, list):
                for index, value in enumerate(node):
                    walk(value, f'{path}.{index}')
            elif isinstance(node, str):
                bad = {char for char in node if ord(char) > 0x7f and char not in allowed}
                self.assertFalse(bad, f'{path}: {"".join(sorted(bad))}')

        walk(zh['screen'], 'screen')


if __name__ == '__main__':
    unittest.main()
