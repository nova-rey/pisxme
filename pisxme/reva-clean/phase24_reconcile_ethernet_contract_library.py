"""Synchronize the canonical Ethernet contract symbol to the live child.

The clean child exposes CM5_GBE, GBE_SHIELD, and ETH_POWER.  The canonical
library retained a stale GBE_LED pin from an older fixture.  This tool replaces
only that complete symbol block, with strict pin-set assertions, and writes a
disposable copy unless --in-place is requested.
"""
from argparse import ArgumentParser
from pathlib import Path
import shutil
import re

LIB_NAME = 'PiSXMe_RevA_Clean_complete.kicad_sym'
CHILD_NAME = 'ETHERNET.kicad_sch'
NEEDLE = '(symbol "PiSXMeRevAClean:ETHERNET_Contract"'
EXPECTED = ['CM5_GBE', 'GBE_SHIELD', 'ETH_POWER']


def end_of_form(text, start):
    depth = 0
    quoted = False
    escaped = False
    for i in range(start, len(text)):
        c = text[i]
        if quoted and escaped:
            escaped = False
        elif quoted and c == '\\':
            escaped = True
        elif c == '"':
            quoted = not quoted
        elif not quoted:
            depth += c == '('
            depth -= c == ')'
            if depth == 0:
                return i + 1
    raise ValueError('unbalanced symbol form')


def pin_names(block):
    return re.findall(r'\(name "([^"]+)"', block)


def reconcile(library, child):
    child_start = child.index(NEEDLE)
    child_block = child[child_start:end_of_form(child, child_start)]
    if pin_names(child_block) != EXPECTED:
        raise ValueError(f'child Ethernet pins are not {EXPECTED}: {pin_names(child_block)}')
    lib_start = library.index(NEEDLE)
    lib_block = library[lib_start:end_of_form(library, lib_start)]
    if pin_names(lib_block) != ['CM5_GBE', 'GBE_LED', 'GBE_SHIELD', 'ETH_POWER']:
        raise ValueError(f'unexpected canonical Ethernet pins: {pin_names(lib_block)}')
    return library[:lib_start] + child_block + library[lib_start + len(lib_block):]


def main():
    ap = ArgumentParser()
    ap.add_argument('--source', type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument('--output', type=Path)
    ap.add_argument('--in-place', action='store_true')
    args = ap.parse_args()
    source = args.source.resolve()
    lib = source / LIB_NAME
    child = source / CHILD_NAME
    if args.in_place:
        output = lib
    else:
        outdir = (args.output or source / '.phase24_ethernet_contract_probe').resolve()
        if outdir.exists():
            raise SystemExit(f'refusing to overwrite disposable output: {outdir}')
        outdir.mkdir()
        output = outdir / LIB_NAME
        shutil.copy2(lib, output)
    before = output.read_text()
    after = reconcile(before, child.read_text())
    output.write_text(after)
    print(output)
    print(f'changed_bytes={len(after) - len(before)}')


if __name__ == '__main__':
    main()
