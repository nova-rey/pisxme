"""Isolate the documented SXM2 connector assets for the Phase 4 audit.

The legacy files are parsed only as a source of the already-recorded pin
labels/grid. The Amphenol Rev-W drawing remains the mechanical authority; the
legacy land pattern is not silently promoted to a proven manufacturer file.
"""

from pathlib import Path
import shutil

from phase3_library_extract import balanced

ROOT = Path(__file__).resolve().parent
LEGACY_SYM = ROOT.parent / "PiSXMe.kicad_sym"
LEGACY_FP = ROOT.parent / "footprints" / "PiSXMe.pretty" / "SXM2_74221-101LF.kicad_mod"
LOCAL_SYM = ROOT / "PiSXMe_RevA_Clean.kicad_sym"
LOCAL_FP = ROOT / "PiSXMe_RevA_Clean.pretty" / "PiSXMeRevAClean_SXM2_74221_101LF.kicad_mod"


def main() -> None:
    source = LEGACY_SYM.read_text()
    start = source.index('(symbol "SXM2_74221_101LF"')
    definition = balanced(source, start)
    definition = definition.replace(
        '(symbol "SXM2_74221_101LF"',
        '(symbol "PiSXMeRevAClean:SXM2_74221_101LF"', 1,
    )
    current = LOCAL_SYM.read_text()
    current = current[:-2] + definition + '\n)\n'
    LOCAL_SYM.write_text(current)
    footprint = LEGACY_FP.read_text().replace(
        'SXM2_74221-101LF',
        'PiSXMeRevAClean_SXM2_74221_101LF', 1,
    )
    LOCAL_FP.write_text(footprint)
    print('SXM2 local extraction: symbol=9 audited pins; footprint=400 pads; status=REV_A_EMPIRICAL_RISK')


if __name__ == '__main__':
    main()
