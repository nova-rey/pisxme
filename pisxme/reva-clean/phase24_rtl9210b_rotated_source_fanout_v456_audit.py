"""Saved-board connectivity audit for the rotated RTL9210B source fixture.

The expected pad/via relationships are assertions only.  Edges come solely
from KiCad's native connectivity graph built from the saved PCB objects.
"""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
PCB = ROOT / "PHASE24_RTL9210B_ROTATED_SOURCE_FANOUT_V456.kicad_pcb"
NETS = {
    "REFCLK_P": "61", "REFCLK_N": "62", "LANE0_RXP": "64",
    "LANE0_RXN": "65", "LANE0_TXN": "67", "LANE0_TXP": "68",
}

def pad_map(board):
    return {(f.GetReference(), p.GetNumber()): p
            for f in board.GetFootprints() for p in f.Pads()}

def native_connected(board, item):
    board.BuildConnectivity()
    return board.GetConnectivity().GetConnectedItems(item)

def check(board):
    pads = pad_map(board)
    result = {}
    for net, number in NETS.items():
        pad = pads[("U1", number)]
        vias = [v for v in board.GetTracks()
                if isinstance(v, pcbnew.PCB_VIA) and v.GetNetname() == net
                and 98.0 <= pcbnew.ToMM(v.GetPosition().x) <= 117.0
                and 52.0 <= pcbnew.ToMM(v.GetPosition().y) <= 78.0]
        assert len(vias) == 1, (net, len(vias))
        result[net] = pad in native_connected(board, vias[0])
        assert result[net], net
    return result

def main():
    board = pcbnew.LoadBoard(str(PCB))
    result = check(board)
    for net in NETS:
        trial = pcbnew.LoadBoard(str(PCB))
        victims = [x for x in trial.GetTracks()
                   if x.GetNetname() == net and not isinstance(x, pcbnew.PCB_VIA)]
        assert victims, net
        for item in victims:
            trial.RemoveNative(item)
        pads = pad_map(trial)
        via = [v for v in trial.GetTracks()
               if isinstance(v, pcbnew.PCB_VIA) and v.GetNetname() == net
               and 98.0 <= pcbnew.ToMM(v.GetPosition().x) <= 117.0
               and 52.0 <= pcbnew.ToMM(v.GetPosition().y) <= 78.0][0]
        assert pads[("U1", NETS[net])] not in native_connected(trial, via), net
    print("PASS V456 native rotated source fanout audit:", result)
    print("PASS V456 six saved-track-removal negative controls")

if __name__ == "__main__":
    main()
