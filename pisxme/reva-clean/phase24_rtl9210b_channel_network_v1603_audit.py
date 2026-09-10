"""Native saved-board six-net audit for the V1603 channel network.

Connectivity is derived only from KiCad's saved pads/tracks/vias/zones.  The
negative controls remove the actual source-attached track from disposable
copies; no expected graph edges are injected.
"""
from pathlib import Path
import tempfile
import pcbnew

H = Path(__file__).resolve().parent
PCB = H / "PHASE24_RTL9210B_CHANNEL_NETWORK_V1603.kicad_pcb"
NETS = {
    "REFCLK_P": ("55", "55"), "REFCLK_N": ("53", "53"),
    "LANE0_RXP": ("43", "43"), "LANE0_RXN": ("41", "41"),
    "LANE0_TXN": ("47", "47"), "LANE0_TXP": ("49", "49"),
}

def pad(board, ref, number):
    return board.FindFootprintByReference(ref).FindPadByNumber(number)

def connected(board, source, target):
    board.BuildConnectivity()
    return target in board.GetConnectivity().GetConnectedItems(source)

board = pcbnew.LoadBoard(str(PCB))
for net, (j1_number, _) in NETS.items():
    src = pad(board, "U1", {"REFCLK_P":"61", "REFCLK_N":"62",
                             "LANE0_RXP":"64", "LANE0_RXN":"65",
                             "LANE0_TXN":"67", "LANE0_TXP":"68"}[net])
    dst = pad(board, "J1", j1_number)
    assert src.GetNetname() == net and dst.GetNetname() == net, net
    assert connected(board, src, dst), f"native connectivity missing: {net}"

    # Select a real source-attached track, then remove only that item in a
    # disposable saved copy.  This proves the audit is sensitive to copper.
    board.BuildConnectivity()
    victim = next((x for x in board.GetConnectivity().GetConnectedItems(src)
                   if isinstance(x, pcbnew.PCB_TRACK) and x.GetNetname() == net), None)
    assert victim is not None, f"no source track for negative control: {net}"
    neg = pcbnew.LoadBoard(str(PCB))
    neg_victim = next(x for x in neg.GetTracks()
                      if x.GetNetname() == net and
                      x.GetStart() == victim.GetStart() and
                      x.GetEnd() == victim.GetEnd() and
                      x.GetLayer() == victim.GetLayer())
    neg.RemoveNative(neg_victim)
    neg_src = pad(neg, "U1", {"REFCLK_P":"61", "REFCLK_N":"62",
                               "LANE0_RXP":"64", "LANE0_RXN":"65",
                               "LANE0_TXN":"67", "LANE0_TXP":"68"}[net])
    neg_dst = pad(neg, "J1", j1_number)
    assert not connected(neg, neg_src, neg_dst), f"negative control passed unexpectedly: {net}"

print("V1603 native six-net connectivity PASS; six source-track negative controls PASS")
