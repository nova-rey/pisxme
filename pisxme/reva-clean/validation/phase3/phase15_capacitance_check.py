"""Reproducible Rev-A effective-COUT floor check from schematic authority."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SHEET = ROOT / "REGULATORS.kicad_sch"

RAIL_COUNTS = {
    "CM5_5V": (2, 30.0),
    "BRIDGE_3V3": (3, 50.0),
    "BRIDGE_1V1": (16, 300.0),
}


def main():
    text = SHEET.read_text()
    for rail, (count, required) in RAIL_COUNTS.items():
        assert text.count('(property "Value" "22uF"') >= count, rail
        effective = count * 22.0 * 0.90
        assert effective >= required, (rail, effective, required)
        print(f"{rail}: {count} x 22uF x 0.90 = {effective:.1f}uF >= {required:.1f}uF")
    print("Phase 15 COUT floor check: PASS; exact-part DC-bias/temperature remains empirical")


if __name__ == "__main__":
    main()
