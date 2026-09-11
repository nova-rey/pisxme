"""Qualify storage-instance footprints against the project's local library.

The storage child schematic is the source authority.  Only the four bare
standard-package names used by its passive/crystal instances are changed; the
script fails closed if the expected source shape is not present.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "STORAGE.kicad_sch"
REPLACEMENTS = {
    '"R_0402_1005Metric"': '"PiSXMeRevAClean:R_0402_1005Metric"',
    '"C_0402_1005Metric"': '"PiSXMeRevAClean:C_0402_1005Metric"',
    '"C_0603_1608Metric"': '"PiSXMeRevAClean:C_0603_1608Metric"',
    '"L_2520_6332Metric"': '"PiSXMeRevAClean:L_2520_6332Metric"',
    '"Crystal_SMD_3225-4Pin_3.2x2.5mm"':
        '"PiSXMeRevAClean:Crystal_3225_4Pad"',
}


def main():
    text = TARGET.read_text()
    counts = {old: text.count(old) for old in REPLACEMENTS}
    expected = {
        '"R_0402_1005Metric"': 4,
        '"C_0402_1005Metric"': 13,
        '"C_0603_1608Metric"': 1,
        '"L_2520_6332Metric"': 1,
        '"Crystal_SMD_3225-4Pin_3.2x2.5mm"': 1,
    }
    if counts != expected:
        raise SystemExit(f"unexpected footprint source counts: {counts}")
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    TARGET.write_text(text)
    print(f"qualified {sum(counts.values())} storage footprint references")


if __name__ == "__main__":
    main()
