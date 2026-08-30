from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[2]
def main() -> None:
    text = (ROOT / 'PiSXMe_RevA_Clean.pretty/JAE_SM3ZS067U410ABR1000_BKEY.kicad_mod').read_text()
    nums = [int(n) for n in re.findall(r'\(pad "(\d+)" smd rect', text)]
    assert len(nums) == 67 and set(nums) == set(range(1, 12)) | set(range(20, 76))
    assert 'B-key void 12-19 per SATA-IO TP053' in text
    assert 'PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000_BKEY' in (ROOT / 'STORAGE.kicad_sch').read_text()
    print('Phase 14 M.2 B-key authority: PASS; contacts=67; void=12-19')
if __name__ == '__main__': main()
