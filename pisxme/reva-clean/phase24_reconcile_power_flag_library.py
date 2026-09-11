"""Replace embedded PWR_FLAG copies with the installed KiCad authority."""
from argparse import ArgumentParser
from pathlib import Path
import shutil

CHILDREN = ("CORE_CM5", "POWER_INPUT", "V100_POWER")
NEEDLE = '(symbol "power:PWR_FLAG"'
OFFICIAL = '(symbol "PWR_FLAG"'


def end_form(text, start):
    depth = 0; quoted = False; escaped = False
    for i in range(start, len(text)):
        c = text[i]
        if quoted and escaped: escaped = False
        elif quoted and c == '\\': escaped = True
        elif c == '"': quoted = not quoted
        elif not quoted:
            depth += c == '('
            depth -= c == ')'
            if depth == 0: return i + 1
    raise ValueError('unbalanced KiCad form')


def replace_one(text, authority):
    start = text.index(NEEDLE)
    end = end_form(text, start)
    return text[:start] + authority + text[end:]


def main():
    ap = ArgumentParser()
    ap.add_argument('--source', type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument('--library-source', type=Path, required=True)
    ap.add_argument('--output', type=Path)
    ap.add_argument('--in-place', action='store_true')
    args = ap.parse_args()
    source = args.source.resolve()
    official_text = args.library_source.read_text()
    a = official_text.index(OFFICIAL)
    authority = official_text[a:end_form(official_text, a)]
    if authority.count('(pin ') != 1:
        raise ValueError('unexpected official PWR_FLAG shape')
    if args.in_place:
        out = source
    else:
        out = (args.output or source / '.phase24_power_flag_probe').resolve()
        if out.exists(): raise SystemExit(f'refusing to overwrite {out}')
        out.mkdir()
    for child in CHILDREN:
        path = out / f'{child}.kicad_sch'
        text = path.read_text()
        count = text.count(NEEDLE)
        if count < 1:
            raise ValueError(f'{child}: expected at least one embedded PWR_FLAG')
        for _ in range(count):
            text = replace_one(text, authority)
        path.write_text(text)
        print(f'{child}: replaced {count} embedded PWR_FLAG definitions')
    print(out)


if __name__ == '__main__':
    main()
