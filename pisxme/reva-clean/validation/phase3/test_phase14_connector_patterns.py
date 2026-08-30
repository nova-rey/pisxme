from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PRETTY = ROOT / "PiSXMe_RevA_Clean.pretty"

def pads(path: Path) -> int:
    return path.read_text().count('(pad "')

def main() -> None:
    cm5 = PRETTY / "PiSXMeRevAClean_Raspberry_Pi_5_Compute_Module.kicad_mod"
    mag = PRETTY / "EDAC_A70_112_331N126.kicad_mod"
    cm5_text = cm5.read_text()
    mag_text = mag.read_text()
    assert pads(cm5) == 204
    assert len(re.findall(r'\(pad "\d+" smd rect', cm5_text)) == 200
    assert '10164227-1001a1rlf.stp' in cm5_text
    assert pads(mag) == 26
    assert len(re.findall(r'\(pad "\d+" thru_hole', mag_text)) == 18
    assert 'TRJG0926HENL' not in mag_text
    assert 'PiSXMeRevAClean:EDAC_A70_112_331N126' in (ROOT / 'ETHERNET.kicad_sch').read_text()
    print('Phase 14 connector patterns: PASS; CM5=200 pads/model; EDAC=18 pads')

if __name__ == '__main__':
    main()
