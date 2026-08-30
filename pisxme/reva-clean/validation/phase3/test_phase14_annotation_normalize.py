from pathlib import Path
import re
from collections import Counter
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from phase14_annotation_normalize import REFERENCE_MAP

ROOT = Path(__file__).resolve().parents[2]

def main() -> None:
    refs = []
    for path in ROOT.glob('*.kicad_sch'):
        text = path.read_text()
        for old in REFERENCE_MAP:
            assert f'property "Reference" "{old}"' not in text, (path.name, old)
        refs.extend(re.findall(r'\(property "Reference" "([A-Z]+\d+)"', text))
    duplicates = {ref for ref, count in Counter(refs).items() if count > 1}
    # CM5 is an authoritative two-unit symbol; KiCad intentionally repeats
    # its reference for units 1 and 2.
    assert duplicates <= {'J7'}, refs
    assert all(re.fullmatch(r'[A-Z]+\d+', ref) for ref in refs)
    print(f'Phase 14 annotation normalization: PASS; legal_unique_refs={len(refs)}')

if __name__ == '__main__':
    main()
