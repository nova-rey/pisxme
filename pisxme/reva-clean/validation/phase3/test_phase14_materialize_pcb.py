from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]

def main() -> None:
    result = subprocess.run([
        "/home/nyx/pisxme-toolchain-environment/bin/pisxme-pcbnew-python",
        str(ROOT / "phase14_materialize_pcb.py"),
    ], cwd=ROOT, check=True, text=True, capture_output=True)
    assert "abstract connector pins not assigned" not in result.stdout
    board = (ROOT / "ACREAGE_CANDIDATE.kicad_pcb").read_text()
    assert '(thickness 1.6)' in board
    assert '"In1.Cu" signal "In1.GND"' in board and '"In4.Cu" signal "In4.GND"' in board
    refs = set(__import__('re').findall(r'\(property "Reference" "([A-Z][0-9]+)"', board))
    assert '"REF**"' not in board
    required = {"J1", "J2", "J3", "J4", "J5", "J6", "J7", "U1", "U2", "U3", "U4", "U5", "U6", "U7", "U8", "U9", "R1", "R2", "C1", "C2"}
    assert required <= refs
    assert board.count('(segment ') == 0
    assert 'abstract connector pins not assigned' not in board
    assert board.count('"12V_PROTECTED"') >= 130
    assert board.count('"/V100_PCIE/V100_PER0_N"') >= 1
    assert '"POWER_GND"' in board
    print("Phase 14 PCB materialization: PASS; six layers; assigned refs; routing still zero")

if __name__ == "__main__":
    main()
