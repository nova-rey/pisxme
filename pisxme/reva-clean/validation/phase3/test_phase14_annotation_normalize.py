from pathlib import Path
import re
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
    assert len(refs) == len(set(refs)), refs
    assert all(re.fullmatch(r'[A-Z]+\d+', ref) for ref in refs)
    print(f'Phase 14 annotation normalization: PASS; legal_unique_refs={len(refs)}')

if __name__ == '__main__':
    main()
