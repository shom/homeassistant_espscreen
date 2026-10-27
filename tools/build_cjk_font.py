#!/usr/bin/env python3
"""Rebuild the three Source Han Sans SC subsets the text fonts use (docs/CJK.md).

The screens can only draw the characters the subsets carry, and Home Assistant entity names are not known when this
repository is written: run this after adding names, with a file of the extra characters (or "text" with anything):

    python3 tools/build_cjk_font.py --source fonts/private/shs --add names.txt

`--source` holds the unmodified Source Han Sans SC OTFs (Regular, Medium, Bold), for example from
https://github.com/adobe-fonts/source-han-sans/releases (09_SourceHanSansSC.zip). The glyph lists, the substitution in
packages/hardware/guition-esp32p4.yaml and header_bar.CJK_GLYPHS are updated with the fonts, so a build picks them up.
Every character costs about 1 KB of flash across the four text steps; the script prints the running total.
"""
import argparse
import pathlib
import re
import subprocess
import sys

from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
HARDWARE = ROOT / 'packages/hardware/guition-esp32p4.yaml'
HEADER_BAR = ROOT / 'screen_manager/app/header_bar.py'
FONTS = ROOT / 'fonts'
WEIGHTS = ('Regular', 'Medium', 'Bold')
ASCII = ''.join(chr(code) for code in range(0x20, 0x7f))
SYMBOLS = '°²³µ–×©®™¢¥§·…—“”‘’€£'
# The ratios of Roboto, the line box every card was designed with (docs/CJK.md).
ASCENT, DESCENT = 928, -244


def current_cjk() -> str:
    """The characters the build carries today: header_bar.CJK_GLYPHS."""
    text = HEADER_BAR.read_text(encoding='utf-8')
    found = re.search(r"CJK_GLYPHS = frozenset\('([^']*)'\)", text)
    if not found:
        sys.exit('header_bar.CJK_GLYPHS not found')
    return found.group(1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--source', default=str(ROOT / 'fonts/private/shs'), help='folder with the Source Han Sans SC OTFs')
    parser.add_argument('--add', action='append', default=[], help='a file whose Chinese characters are added (repeatable)')
    args = parser.parse_args()

    cjk = set(current_cjk())
    before = len(cjk)
    for path in args.add:
        cjk |= {ch for ch in pathlib.Path(path).read_text(encoding='utf-8') if '\u4e00' <= ch <= '\u9fff'}
    cjk = ''.join(sorted(cjk))
    chars = ''.join(sorted(set(ASCII + SYMBOLS + cjk)))
    print(f'{len(cjk)} Chinese characters (+{len(cjk) - before}), {len(chars)} glyphs per weight')

    chars_file = ROOT / '.cjk-chars.txt'
    chars_file.write_text(chars, encoding='utf-8')
    try:
        for weight in WEIGHTS:
            source = pathlib.Path(args.source) / f'SourceHanSansSC-{weight}.otf'
            if not source.is_file():
                sys.exit(f'missing {source}')
            target = FONTS / f'SourceHanSansSC-{weight}.otf'
            run = subprocess.run(
                [sys.executable, '-m', 'fontTools.subset', str(source), f'--text-file={chars_file}',
                 f'--output-file={target}', '--layout-features=*', '--name-IDs=*', '--name-legacy',
                 '--name-languages=*', '--notdef-glyph', '--notdef-outline', '--recommended-glyphs',
                 '--glyph-names', '--symbol-cmap', '--legacy-cmap'],
                capture_output=True, text=True)
            if run.returncode:
                sys.exit(run.stderr.strip())
            font = TTFont(target)
            font['hhea'].ascent, font['hhea'].descent, font['hhea'].lineGap = ASCENT, DESCENT, 0
            os2 = font['OS/2']
            os2.sTypoAscender, os2.sTypoDescender, os2.sTypoLineGap = ASCENT, DESCENT, 0
            os2.usWinAscent, os2.usWinDescent = ASCENT, abs(DESCENT)
            font.save(target)
            cmap = TTFont(target).getBestCmap()
            missing = [ch for ch in chars if ord(ch) not in cmap]
            if missing:
                sys.exit(f'{weight} lacks {len(missing)} glyphs: {"".join(missing[:20])}')
            print(f'  {weight}: {target.name}, {target.stat().st_size // 1024} KB')
    finally:
        chars_file.unlink(missing_ok=True)

    text = HARDWARE.read_text(encoding='utf-8')
    text = re.sub(r'  FONT_CJK_GLYPHS: "[^"]*"', lambda _: f'  FONT_CJK_GLYPHS: "{cjk}"', text, count=1)
    HARDWARE.write_text(text, encoding='utf-8')
    text = HEADER_BAR.read_text(encoding='utf-8')
    text, count = re.subn(r"CJK_GLYPHS = frozenset\('.*?'\)",
                          lambda _: "CJK_GLYPHS = frozenset(" + repr(cjk) + ")", text, count=1, flags=re.S)
    if count != 1:
        sys.exit('header_bar.CJK_GLYPHS not replaced')
    HEADER_BAR.write_text(text, encoding='utf-8')
    print(f'about {round(len(cjk) * 1.1)} KB of flash across the four text steps; run the tests after it')
    return 0


if __name__ == '__main__':
    sys.exit(main())
