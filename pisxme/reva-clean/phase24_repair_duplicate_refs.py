"""Remove duplicate cross-sheet capacitor references before native export.

The four 22 uF regulator capacitors were accidentally assigned the same
references as STORAGE's four SATA AC capacitors.  They are distinct schematic
components, so they receive the next unused capacitor references.  No net,
value, footprint, or topology is changed.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
PATH = ROOT / "REGULATORS.kicad_sch"


def main() -> None:
    text = PATH.read_text()
    changed = 0
    for old, new in zip(("C30", "C31", "C32", "C33"), ("C44", "C45", "C46", "C47")):
        before = text
        text = text.replace(f'"{old}"', f'"{new}"')
        changed += text != before
    PATH.write_text(text)
    print(f"renumbered regulator duplicate references: {changed}")


if __name__ == "__main__":
    main()
