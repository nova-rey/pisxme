"""Apply the generic root-level direct PCIe links to an existing clean root.

The Phase 3 scaffold owns the same link contract for newly generated roots;
this migration applies it to the already-authorized Rev-A root without
regenerating later-phase child content. PET0 remains split at C1/C2.
"""
from pathlib import Path
from phase3_scaffold import PCIE_DIRECT_ROOT_LINKS, make_uuid

ROOT = Path(__file__).resolve().parent
SCHEMATIC = ROOT / "PiSXMe_RevA_Clean.kicad_sch"
MARKER = "  (sheet_instances (path \"/\" (page \"1\")))"


def wire_block(points, index):
    blocks = []
    for segment, (a, b) in enumerate(zip(points, points[1:])):
        pts = f"(xy {a[0]} {a[1]}) (xy {b[0]} {b[1]})"
        blocks.append(
            f"  (wire\n    (pts {pts})\n"
            "    (stroke (width 0) (type default))\n"
            f"    (uuid {make_uuid(0xc1000000000000000000000000000000 + index * 2 + segment)}))\n"
        )
    return "".join(blocks)


def main():
    text = SCHEMATIC.read_text()
    if "c1000000-0000-0000-0000-000000000000" in text:
        print("Phase 16 PCIe root links already present")
        return
    if MARKER not in text:
        raise SystemExit("root sheet_instances marker not found")
    links = "".join(wire_block(points, index)
                     for index, points in enumerate(PCIE_DIRECT_ROOT_LINKS))
    SCHEMATIC.write_text(text.replace(MARKER, links + MARKER, 1))
    print("Phase 16 PCIe root authority: 5 direct links added; PET0 remains split")


if __name__ == "__main__":
    main()
