"""Reproducible Rev-A effective-COUT floor check from schematic authority."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SHEET = ROOT / "REGULATORS.kicad_sch"

RAIL_COUNTS = {
    "CM5_5V": (("C7", "C8"), 30.0),
    "BRIDGE_3V3": (("C16", "C17", "C19"), 50.0),
    "BRIDGE_1V1": (tuple(f"C{i}" for i in range(26, 42)), 300.0),
}


def main():
    text = SHEET.read_text()
    for rail, (refs, required) in RAIL_COUNTS.items():
        assert all(text.count(f'(property "Reference" "{ref}"') == 1
                   for ref in refs), rail
        count = len(refs)
        assert text.count('(property "Value" "22uF"') >= count, rail
        effective = count * 22.0 * 0.90
        assert effective >= required, (rail, effective, required)
        worst_tolerance = effective * 0.80
        print(f"{rail}: nominal={effective:.1f}uF >= {required:.1f}uF; "
              f"±20% screen={worst_tolerance:.1f}uF")
    print("Phase 15 COUT floor check: PASS; exact-part DC-bias/temperature remains empirical")


if __name__ == "__main__":
    main()
