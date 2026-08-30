"""Native regression for the authoritative two-unit 200-pin CM5 module."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]

def main() -> None:
    sheet = (ROOT / "CORE_CM5.kicad_sch").read_text()
    assert sheet.count('(lib_id "PiSXMeRevAClean:ComputeModule5-CM5")') == 2
    assert '(unit 1)' in sheet and '(unit 2)' in sheet
    assert sheet.count('(property "Reference" "J7"') == 2
    assert sheet.count('(pin "') >= 200
    assert sheet.count('(no_connect ') >= 100
    with __import__('tempfile').TemporaryDirectory(prefix='cm5-erc-', dir='/tmp') as td:
        report = Path(td) / 'erc.rpt'
        r = subprocess.run(['kicad-cli', 'sch', 'erc', '--exit-code-violations',
                            '--severity-error', '--output', str(report),
                            str(ROOT / 'PiSXMe_RevA_Clean.kicad_sch')],
                           cwd=ROOT, text=True, capture_output=True)
        assert r.returncode == 0, r.stdout + r.stderr
        assert 'Found 0 violations' in r.stdout
    print('Phase 14 CM5 native authority: PASS; two units, 200 pins, ERC=0')

if __name__ == '__main__':
    main()
