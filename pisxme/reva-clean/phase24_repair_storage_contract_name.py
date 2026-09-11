"""Fail-closed repair for the stale STORAGE contract pin name.

Only the embedded STORAGE_Contract pin-4 name is changed. Root/child label
coordinates, UUIDs, wires, instance pins, PCB assets, and the separate bridge
rail ports are intentionally untouched.
"""
from argparse import ArgumentParser
from pathlib import Path
import shutil

OLD = '(name "M2_3V3" (effects (font (size 1.27 1.27))))'
NEW = '(name "STORAGE_3V3" (effects (font (size 1.27 1.27))))'
MARKER = '(symbol "STORAGE_Contract_1_1"'


def repair(text):
    start = text.index(MARKER)
    end = text.index('\n      )', start)
    block = text[start:end]
    if block.count(OLD) != 1:
        raise ValueError(f"expected exactly one stale STORAGE contract pin, found {block.count(OLD)}")
    return text[:start] + block.replace(OLD, NEW) + text[end:]


def main():
    parser = ArgumentParser()
    parser.add_argument('--source', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--in-place', action='store_true')
    args = parser.parse_args()
    source = args.source.resolve()
    input_path = source / 'STORAGE.kicad_sch'
    if args.in_place:
        output = input_path
    else:
        output_dir = (args.output or source / '.phase24_storage_contract_probe').resolve()
        if output_dir.exists():
            raise SystemExit(f'refusing to overwrite disposable output: {output_dir}')
        output_dir.mkdir()
        output = output_dir / input_path.name
        shutil.copy2(input_path, output)
    before = output.read_text()
    after = repair(before)
    output.write_text(after)
    print(output)
    print(f'changed_bytes={len(after) - len(before)}')


if __name__ == '__main__':
    main()
