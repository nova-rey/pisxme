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
    for ref, input_net, output_net in (
        ("F1", "/POWER_INPUT/12V_IN_A", "/POWER_INPUT/FUSED_12V_A"),
        ("F2", "/POWER_INPUT/12V_IN_B", "/POWER_INPUT/FUSED_12V_B"),
    ):
        start = board.index(f'(property "Reference" "{ref}"')
        end = board.index('\n\t\t(footprint ', start + 1) if '\n\t\t(footprint ' in board[start + 1:] else len(board)
        block = board[start:end]
        assert block.count(f'"{input_net}"') >= 2
        assert block.count(f'"{output_net}"') >= 2
    print("Phase 14 PCB materialization: PASS; six layers; assigned refs; routing still zero")

if __name__ == "__main__":
    main()
