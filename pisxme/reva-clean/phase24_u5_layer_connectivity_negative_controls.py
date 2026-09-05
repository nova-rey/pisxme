"""Negative controls for the physical U5 connectivity audit."""
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
import sys
import pcbnew
from phase24_u5_layer_connectivity_audit import audit

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb"


def near(point, x, y):
    return abs(pcbnew.ToMM(point.x) - x) < 0.001 and abs(pcbnew.ToMM(point.y) - y) < 0.001


def expect_failure(label, predicate):
    board = pcbnew.LoadBoard(str(BASE))
    removed = False
    for item in list(board.GetTracks()):
        if predicate(item):
            board.Remove(item)
            removed = True
            break
    assert removed, f"negative control could not find required {label}"
    with TemporaryDirectory(dir=R, prefix=".phase24-negative-") as directory:
        candidate = Path(directory) / f"missing-{label}.kicad_pcb"
        board.Save(str(candidate))
        try:
            audit(candidate)
        except AssertionError:
            print(f"negative control {label}: PASS (audit failed after required conductor removal)")
        else:
            raise AssertionError(f"audit incorrectly passed missing {label} control")


def main():
    controls = {
        "trace": lambda item: (not isinstance(item, pcbnew.PCB_VIA)
                                and item.GetNetname() == "/REGULATORS/BRIDGE_1V1"
                                and near(item.GetEnd(), 251.2, 129.35)),
        "via": lambda item: (isinstance(item, pcbnew.PCB_VIA)
                              and item.GetNetname() == "/REGULATORS/BRIDGE_1V1"
                              and near(item.GetPosition(), 251.2, 129.35)),
    }
    if len(sys.argv) > 1:
        expect_failure(sys.argv[1], controls[sys.argv[1]])
        return
    # KiCad's binding is process-global; isolate each disposable copy in its
    # own interpreter so one board load cannot contaminate the next control.
    for label in controls:
        result = subprocess.run([sys.executable, __file__, label], check=False,
                                capture_output=True, text=True)
        print(result.stdout, end="")
        assert result.returncode == 0, result.stderr


if __name__ == "__main__":
    main()
