"""Regression tests for the Phase 24 U5 native-connectivity audit."""
from pathlib import Path
from phase24_u5_layer_connectivity_audit import audit, negative_controls

BOARD = Path(__file__).resolve().parent / "PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb"

def test_saved_board_passes_native_connectivity():
    assert audit(BOARD)

def test_disposable_trace_removal_fails_native_connectivity():
    result = negative_controls(BOARD)
    assert result["trace_removal_fails"] is True

if __name__ == "__main__":
    test_saved_board_passes_native_connectivity()
    test_disposable_trace_removal_fails_native_connectivity()
    print("Phase24 U5 connectivity regression tests: PASS")
