#!/usr/bin/env python3
"""Regression for the KiCad 10 serializer boundary used by generated sheets."""
from pathlib import Path
import os
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
BRIDGE_PYTHON = Path('/home/nyx/venvs/pisxme-bridge/bin/python')
SYMBOL_DIR = '/var/lib/flatpak/runtime/org.kicad.KiCad.Library.Symbols/x86_64/stable/3a924b56e06b39f412abb4658eb067570651f94fe9b0dbc3bc671fb75562d253/files/symbols'

def main() -> None:
    with tempfile.TemporaryDirectory(prefix='pisxme-native-roundtrip-', dir=ROOT) as tmp:
        work = Path(tmp)
        for path in ROOT.glob('*.kicad_sch'):
            shutil.copy2(path, work / path.name)
        env = os.environ | {'PYTHONPATH': str(ROOT), 'KICAD_SYMBOL_DIR': SYMBOL_DIR}
        subprocess.run([str(BRIDGE_PYTHON), str(ROOT / 'phase14_native_roundtrip.py'),
                        'REGULATORS.kicad_sch'], cwd=work, env=env, check=True)
        out = work / 'netlist.net'
        result = subprocess.run(
            ['xvfb-run', '-a', 'kicad-cli', 'sch', 'export', 'netlist',
             '--format', 'kicadsexpr', '--output', out.name,
             str(work / 'PiSXMe_RevA_Clean.kicad_sch')],
            cwd=work, capture_output=True, text=True, check=False,
        )
        assert result.returncode == 0, result.stderr
        assert 'annotation errors' not in (result.stdout + result.stderr).lower()
        text = out.read_text()
        for ref in ('U3', 'U4', 'U5', 'C5', 'C14', 'R11', 'R19'):
            assert f'(ref "{ref}")' in text, ref
    print('Phase 14 native serializer round-trip: PASS')

if __name__ == '__main__':
    main()
