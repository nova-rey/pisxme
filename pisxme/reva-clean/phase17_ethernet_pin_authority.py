"""Repair generated Ethernet symbol/footprint pin identity generically."""
from pathlib import Path
import re
from phase3_scaffold import balanced, make_uuid
from uuid import UUID

ROOT = Path(__file__).resolve().parent
SCHEMATIC = ROOT / "ETHERNET.kicad_sch"
PIN_BASES = {
    "PiSXMeRevAClean:EDAC_A70_112_331N126_Ethernet": (0x60000000000000000000000000000000, 18),
    "PiSXMeRevAClean:TPD4E004DRYR": (0x61000000000000000000000000000000, 6),
}


def stable_pin(base, number):
    return make_uuid(base + number - 1)


def add_library_pin_uuids(text, lib_id, base, count):
    symbol_name = lib_id.split(":", 1)[1]
    start = text.index(f'(symbol "{lib_id}"')
    end = start + len(balanced(text, start))
    block = text[start:end]
    block = re.sub(r' \(uuid [0-9a-f-]+\)(?=\))', '', block)
    if block.count('(pin passive line') < count:
        raise SystemExit(f"library pins missing for {symbol_name}")
    return text[:start] + block + text[end:]


def repair_instances(text, lib_id, base, count):
    marker = f'(symbol (lib_id "{lib_id}")'
    cursor = 0
    while True:
        start = text.find(marker, cursor)
        if start < 0:
            return text
        end = start + len(balanced(text, start))
        block = text[start:end]
        instance_match = re.search(r'\(uuid ([0-9a-f-]+)\)', block)
        if not instance_match:
            raise SystemExit(f"instance UUID missing for {lib_id}")
        instance_base = UUID(instance_match.group(1)).int
        for number in range(1, count + 1):
            block, changed = re.subn(
                rf'\(pin "{number}" \(uuid [^)]+\)\)',
                f'(pin "{number}" (uuid {make_uuid(instance_base + 0x100 + number - 1)}))',
                block,
                count=1,
            )
            if not changed:
                raise SystemExit(f"instance pin {lib_id}.{number} not found")
        text = text[:start] + block + text[end:]
        cursor = start + len(block)


def main():
    text = SCHEMATIC.read_text()
    for lib_id, (base, count) in PIN_BASES.items():
        text = add_library_pin_uuids(text, lib_id, base, count)
        text = repair_instances(text, lib_id, base, count)
        start = text.index(f'(symbol "{lib_id}"')
        end = start + len(balanced(text, start))
        block = text[start:end]
        block = re.sub(
            r'\(at 20 (-?[0-9]+(?:\.[0-9]+)?) 180\)',
            lambda m: f'(at 20 {-float(m.group(1)):g} 180)',
            block,
        )
        text = text[:start] + block + text[end:]
    SCHEMATIC.write_text(text)
    print("Phase 17 Ethernet pin authority: stable library/instance UUIDs applied")


if __name__ == "__main__":
    main()
