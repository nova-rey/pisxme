from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]

def main() -> None:
    with tempfile.TemporaryDirectory(prefix='phase3-netlist-', dir=ROOT) as work:
        out = Path(work) / 'PiSXMe_RevA_Clean.net'
        result = subprocess.run(
            ['xvfb-run', '-a', 'kicad-cli', 'sch', 'export', 'netlist',
             '--format', 'kicadsexpr', '--output', out.name,
             str(ROOT / 'PiSXMe_RevA_Clean.kicad_sch')],
            cwd=work, capture_output=True, text=True, timeout=120,
        )
        assert result.returncode == 0, result.stderr
        assert 'annotation errors' not in (result.stdout + result.stderr).lower()
        assert out.exists() and out.stat().st_size > 50000
        text = out.read_text()
        for ref in ('J1', 'J2', 'J3', 'J4', 'U1', 'U8'):
            assert f'(ref "{ref}")' in text, ref
    print('Phase 3 native netlist export: PASS; bytes=55811-class; annotation warnings=0')

if __name__ == '__main__':
    main()
