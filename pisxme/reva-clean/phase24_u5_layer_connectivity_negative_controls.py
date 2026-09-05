"""Disposable negative controls for the native U5 connectivity audit."""
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
import sys
import pcbnew
from phase24_u5_layer_connectivity_audit import audit, pads_by_token

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb"
NET = "/REGULATORS/BRIDGE_1V1"

def item_signature(item):
    if type(item).__name__ == "PCB_VIA":
        p = item.GetPosition()
        return ("PCB_VIA", item.GetNetname(), p.x, p.y)
    return ("PCB_TRACK", item.GetNetname(), int(item.GetLayer()),
            item.GetStart().x, item.GetStart().y,
            item.GetEnd().x, item.GetEnd().y, item.GetWidth())

def remove_and_expect_failure(label, wanted):
    board = pcbnew.LoadBoard(str(BASE))
    victim = next((item for item in board.GetTracks()
                   if item_signature(item) == wanted), None)
    assert victim is not None, f"negative control could not find {label} item"
    board.RemoveNative(victim)
    with TemporaryDirectory(dir=R, prefix=".phase24-negative-") as directory:
        candidate = Path(directory) / f"missing-{label}.kicad_pcb"
        board.Save(str(candidate))
        try:
            audit(candidate)
        except AssertionError:
            print(f"negative control {label}: PASS")
            return
    raise AssertionError(f"audit incorrectly passed missing {label} control")

def find_required_item(kind):
    board = pcbnew.LoadBoard(str(BASE))
    board.BuildConnectivity()
    pads = pads_by_token(board)
    # C44.1 is a required target and its native connected-item component is
    # the source of candidates; expected topology supplies no graph edges.
    connected = board.GetConnectivity().GetConnectedItems(pads["C44.1"])
    for item in connected:
        if kind == "trace" and type(item).__name__ == "PCB_TRACK":
            yield item_signature(item)
        if kind == "via" and type(item).__name__ == "PCB_VIA":
            yield item_signature(item)

def main():
    labels = sys.argv[1:] or ["trace"]
    for label in labels:
        for wanted in find_required_item(label):
            try:
                remove_and_expect_failure(label, wanted)
                break
            except AssertionError as error:
                last = error
        else:
            raise AssertionError(f"no necessary {label} removal made audit fail")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main()
    else:
        result = subprocess.run([sys.executable, __file__, "trace"],
                                check=False, capture_output=True, text=True)
        print(result.stdout, end="")
        if result.returncode:
            raise SystemExit(result.stderr)
