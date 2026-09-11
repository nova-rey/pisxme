"""Disposable identity-preserving native hierarchy contract probe.

The live children contain complete circuit content but stale contract
definitions/instances.  This probe regenerates only the hierarchy contract
objects from the authoritative root sheet names and child label UUIDs.  It
does not invent graph edges or alter real circuit symbols.  Output is always
written to a disposable directory and must pass native ERC plus exact
netlist comparison before any production consideration.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / ".phase24_native_contract_identity_probe"
ROOT_NAME = "PiSXMe_RevA_Clean.kicad_sch"
CHILDREN = (
    "CORE_CM5", "V100_PCIE", "V100_POWER", "POWER_INPUT", "REGULATORS",
    "ETHERNET", "STORAGE", "SERVICE", "COOLING", "DEBUG",
)


def end_expr(text: str, start: int) -> int:
    depth = 0
    quoted = escaped = False
    for pos in range(start, len(text)):
        char = text[pos]
        if quoted and escaped:
            escaped = False
        elif quoted and char == "\\":
            escaped = True
        elif char == '"':
            quoted = not quoted
        elif not quoted:
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    return pos + 1
    raise ValueError(f"unbalanced expression at {start}")


def root_sheet(text: str, child: str) -> tuple[int, int, list[tuple[str, float, float]]]:
    search = 0
    while True:
        start = text.find("(sheet\n", search)
        if start < 0:
            raise ValueError(f"missing root sheet {child}")
        stop = end_expr(text, start)
        block = text[start:stop]
        if f'(property "Sheetname" "{child}"' in block:
            pins = [
                (name, float(x), float(y))
                for name, x, y in re.findall(
                    r'\(pin "([^"]+)"[^\n]*\(at ([0-9.+-]+) ([0-9.+-]+) 180\)',
                    block,
                )
            ]
            return start, stop, pins
        search = stop


def replace_xy(block: str, old_x: float, old_y: float, new_x: float, new_y: float) -> str:
    def fmt(value: float) -> str:
        return f"{value:g}"

    ox, oy, nx, ny = map(fmt, (old_x, old_y, new_x, new_y))
    block = block.replace(f"(xy {ox} {oy})", f"(xy {nx} {ny})")
    block = block.replace(f"(at {ox} {oy} 180)", f"(at {nx} {ny} 180)")
    block = block.replace(f"(at {ox} {oy})", f"(at {nx} {ny})")
    return block


def transform_root(text: str) -> str:
    spans: list[tuple[int, int, str]] = []
    coordinate_map: list[tuple[float, float, float, float]] = []
    for child in CHILDREN:
        start, stop, pins = root_sheet(text, child)
        block = text[start:stop]
        if pins:
            first_y = pins[0][2]
            for index, (_, old_x, old_y) in enumerate(pins):
                new_y = first_y + 2.54 * index
                coordinate_map.append((old_x, old_y, old_x, new_y))
                # The root-side contract pin is ten millimetres to the left
                # of the sheet pin.  Its wire/label endpoint is a separate
                # top-level object and must follow the same identity.
                coordinate_map.append((old_x - 10, old_y, old_x - 10, new_y))
                block = replace_xy(block, old_x, old_y, old_x, new_y)
        spans.append((start, stop, block))
    for start, stop, block in reversed(spans):
        text = text[:start] + block + text[stop:]
    # Root wires are top-level objects, outside the sheet expressions.  Move
    # their sheet-pin endpoints with the pins; otherwise native ERC sees the
    # transformed sheet pins as dangling even though the child is intact.
    for old_x, old_y, new_x, new_y in coordinate_map:
        text = replace_xy(text, old_x, old_y, new_x, new_y)
    return text


def label_data(text: str) -> tuple[list[str], dict[str, str], dict[str, tuple[float, float]]]:
    names = re.findall(r'\(hierarchical_label "([^"]+)"', text)
    uuids: dict[str, str] = {}
    coords: dict[str, tuple[float, float]] = {}
    for name in names:
        match = re.search(
            rf'\(hierarchical_label "{re.escape(name)}"([\s\S]*?)\(uuid "?([^\)" ]+)"?\)',
            text,
        )
        at = re.search(
            rf'\(hierarchical_label "{re.escape(name)}"[\s\S]*?\(at ([0-9.+-]+) ([0-9.+-]+) 180\)',
            text,
        )
        if not match or not at:
            raise ValueError(f"incomplete label {name}")
        uuids[name] = match.group(2)
        coords[name] = (float(at.group(1)), float(at.group(2)))
    return names, uuids, coords


def contract_block(text: str, child: str) -> tuple[int, int, str]:
    start = text.index(f'(symbol "{child}_Contract_1_1"')
    stop = end_expr(text, start)
    return start, stop, text[start:stop]


def regenerate_child(text: str, child: str, root_names: list[str]) -> str:
    labels, uuids, coords = label_data(text)
    missing = [name for name in root_names if name not in labels]
    extra = [name for name in labels if name not in root_names]
    if missing or extra:
        raise ValueError(f"{child}: root/child name mismatch missing={missing} extra={extra}")

    dstart, dstop, old_def = contract_block(text, child)
    rectangle = re.search(r'\(rectangle[\s\S]*?\n\s*\)', old_def)
    if not rectangle:
        raise ValueError(f"{child}: contract rectangle missing")
    height = max(7.27, 2.54 * len(root_names) / 2 + 1.27)
    definition = [
        f'(symbol "{child}_Contract_1_1"',
        f'  (rectangle (start -1.27 {-height:g}) (end 1.27 1.27)',
        '    (stroke (width 0.254) (type default)) (fill (type background)))',
    ]
    for index, name in enumerate(root_names):
        definition.extend([
            '  (pin passive line',
            f'    (at -5.08 {-2.54 * index:g} 0)',
            '    (length 3.81)',
            f'    (name "{name}" (effects (font (size 1.27 1.27))))',
            f'    (number "{index + 1}" (effects (font (size 1.27 1.27)))))',
        ])
    definition.append(')')
    text = text[:dstart] + "\n".join(definition) + text[dstop:]

    marker = f'(lib_id "PiSXMeRevAClean:{child}_Contract")'
    lib_pos = text.index(marker)
    istart = text.rfind('(symbol', 0, lib_pos)
    istop = end_expr(text, istart)
    instance = text[istart:istop]
    instance = re.sub(r'\n\s*\(pin "[^"]+" \(uuid "?[^") ]+"?\)\)', '', instance)
    pin_lines = "\n".join(
        f'    (pin "{index + 1}" (uuid {uuids[name]}))'
        for index, name in enumerate(root_names)
    )
    insertion = instance.index('(instances')
    instance = instance[:insertion] + pin_lines + "\n    " + instance[insertion:]
    text = text[:istart] + instance + text[istop:]

    for index, name in enumerate(labels):
        old_x, old_y = coords[name]
        new_y = 10.16 + 2.54 * index
        text = replace_xy(text, old_x, old_y, 5.08, new_y)
        # Contract pins are at x=20.32 after the instance is translated to
        # the native 2.54-mm origin.  Keep the complete contract wire attached
        # to its pin rather than moving only the label endpoint.
        text = replace_xy(text, 19.92, old_y, 20.32, new_y)
    # Move the placed contract instance with its regenerated definition.  The
    # instance UUID and serialized pin UUIDs remain untouched.
    marker = f'(lib_id "PiSXMeRevAClean:{child}_Contract")'
    lib_pos = text.index(marker)
    istart = text.rfind('(symbol', 0, lib_pos)
    istop = end_expr(text, istart)
    instance = text[istart:istop].replace('(at 25 10 0)', '(at 25.4 10.16 0)')
    text = text[:istart] + instance + text[istop:]
    return text


def main() -> None:
    if OUT.exists():
        raise SystemExit(f"refusing to overwrite {OUT}")
    OUT.mkdir()
    source_root = (HERE / ROOT_NAME).read_text()
    root = transform_root(source_root)
    for child in CHILDREN:
        _, _, root_names = root_sheet(source_root, child)
        names = [name for name, _, _ in root_names]
        source = (HERE / f"{child}.kicad_sch").read_text()
        (OUT / f"{child}.kicad_sch").write_text(regenerate_child(source, child, names))
    (OUT / ROOT_NAME).write_text(root)
    for name in (
        "sym-lib-table", "fp-lib-table", "PiSXMe_RevA_Clean_complete.kicad_sym",
        "Storage_DualMode.kicad_sym", "PiSXMe_RevA_Clean.kicad_pro",
    ):
        source = HERE / name
        if source.exists():
            shutil.copy2(source, OUT / name)
    pretty = HERE / "PiSXMe_RevA_Clean.pretty"
    if pretty.exists():
        shutil.copytree(pretty, OUT / pretty.name)
    print(OUT)


if __name__ == "__main__":
    main()
