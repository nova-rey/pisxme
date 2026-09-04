"""Disposable Phase-17 power-entry relocation trials.

Moves only F1 from the Phase-16 ancestor, preserves the existing connector and
downstream FUSED_12V_A trunks, and reconnects the old F1 pad anchors with
ordinary B.Cu high-current copper.  Outputs are experiments, never release
artifacts.
"""
from pathlib import Path
import os
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = Path(os.environ.get("PISXME_BASE", ROOT / "ACREAGE_PCIE_PHASE16.kicad_pcb"))
OUT = Path(os.environ.get("PISXME_OUT", ROOT / "ACREAGE_PHASE17_F1_TRIAL.kicad_pcb"))
TARGET = tuple(float(x) for x in os.environ.get("PISXME_F1_TARGET", "20,40").split(","))
OLD = (55.0, 40.0)

def V(x, y):
    return pcbnew.VECTOR2I_MM(x, y)

def add_track(board, net, a, b, width=2.0):
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(V(*a)); t.SetEnd(V(*b)); t.SetLayer(pcbnew.B_Cu)
    t.SetWidth(pcbnew.FromMM(width)); t.SetNet(net); board.Add(t)

def pad_xy(fp, number):
    for p in fp.Pads():
        if p.GetNumber() == number:
            q = p.GetPosition()
            return (pcbnew.ToMM(q.x), pcbnew.ToMM(q.y))
    raise RuntimeError(f"F1 pad {number} missing")

def main():
    board = pcbnew.LoadBoard(str(BASE))
    fp = board.FindFootprintByReference("F1")
    if fp is None:
        raise RuntimeError("F1 not found")
    old_pads = {n: pad_xy(fp, n) for n in ("1", "2", "3", "4", "5", "6", "7", "8")}
    old_x, old_y = OLD
    # Remove copper attached directly to the old F1 pads.  This removes the
    # old local bridges and trunk launch, while leaving the remote connector
    # and protected-load ends intact for deterministic reconnection.
    for item in list(board.GetTracks()):
        if item.GetLayer() != pcbnew.B_Cu or item.GetNetname() not in (
                "/POWER_INPUT/12V_IN_A", "/POWER_INPUT/FUSED_12V_A"):
            continue
        pts = [(pcbnew.ToMM(item.GetStart().x), pcbnew.ToMM(item.GetStart().y)),
               (pcbnew.ToMM(item.GetEnd().x), pcbnew.ToMM(item.GetEnd().y))]
        if any(min(abs(x-px)+abs(y-py) for px, py in old_pads.values()) < 0.2
               for x, y in pts):
            board.Remove(item)
    fp.SetPosition(V(*TARGET))
    dx, dy = TARGET[0] - OLD[0], TARGET[1] - OLD[1]
    new_pads = {n: (x + dx, y + dy) for n, (x, y) in old_pads.items()}
    net_in = board.FindNet("/POWER_INPUT/12V_IN_A")
    net_out = board.FindNet("/POWER_INPUT/FUSED_12V_A")
    for n in ("1", "2", "3", "4"):
        add_track(board, net_in, new_pads[n], new_pads["1"])
    for n in ("6", "7", "8"):
        add_track(board, net_out, new_pads[n], new_pads["5"])
    # Two separated doglegs reconnect to the fixed board-level entry and
    # protected-load endpoints.  The high-current output is taken above the
    # Ethernet CT island before descending to the existing load trunk.
    ni = new_pads["1"]; no = new_pads["5"]
    add_track(board, net_in, ni, (ni[0], 18.0))
    add_track(board, net_in, (ni[0], 18.0), (12.0, 25.0))
    add_track(board, net_out, no, (no[0], 18.0))
    add_track(board, net_out, (no[0], 18.0), (212.46, 30.0))
    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    board.Save(str(OUT))
    print(f"saved {OUT} target={TARGET} old_pads={old_pads} new_pads={new_pads}")

if __name__ == "__main__":
    main()
