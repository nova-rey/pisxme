"""Native M.2 SSD_3V3 contact-row audit and negative control."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
PCB=ROOT/'PHASE24_RTL9210B_SSD33_SOCKET_JOIN_V141.kicad_pcb'
EXPECTED={('J1','2'),('J1','4'),('J1','6'),('J1','8')}

def connected(board):
    board.BuildConnectivity()
    p=board.FindFootprintByReference('J1').FindPadByNumber('2')
    return {(x.GetParentFootprint().GetReference(),x.GetNumber())
            for x in board.GetConnectivity().GetConnectedItems(p)
            if type(x).__name__=='PAD'}

def main():
    b=pcbnew.LoadBoard(str(PCB)); got=connected(b)
    if EXPECTED-got: raise AssertionError(f'missing SSD_3V3 pads {sorted(EXPECTED-got)}')
    bad=pcbnew.LoadBoard(str(PCB)); removed=0
    for x in list(bad.GetTracks()):
        if x.GetNetname()=='SSD_3V3': bad.RemoveNative(x); removed+=1
    if not removed: raise AssertionError('negative control found no SSD_3V3 route')
    if not EXPECTED-connected(bad): raise AssertionError('negative control unexpectedly passed')
    print('PASS V141 native SSD_3V3 socket-row audit and negative control')

if __name__=='__main__': main()
