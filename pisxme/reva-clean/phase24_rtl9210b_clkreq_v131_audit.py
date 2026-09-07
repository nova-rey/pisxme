"""Native CLKREQ endpoint audit and negative control for V131."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
PCB=ROOT/'PHASE24_RTL9210B_CLKREQ_R3_RAIL_OVERPASS_V131.kicad_pcb'
EXPECTED={('R3','1'),('U1','13'),('J1','52')}
def audit(board):
    board.BuildConnectivity(); p=board.FindFootprintByReference('R3').FindPadByNumber('1')
    got={(x.GetParentFootprint().GetReference(),x.GetNumber()) for x in board.GetConnectivity().GetConnectedItems(p) if type(x).__name__=='PAD'}
    if EXPECTED-got: raise AssertionError(f'CLKREQ missing {sorted(EXPECTED-got)}')
def main():
    audit(pcbnew.LoadBoard(str(PCB))); bad=pcbnew.LoadBoard(str(PCB)); removed=0
    for item in list(bad.GetTracks()):
        if item.GetNetname()=='CLKREQ_N': bad.RemoveNative(item); removed+=1
    if not removed: raise AssertionError('negative control found no CLKREQ route')
    try: audit(bad)
    except AssertionError: pass
    else: raise AssertionError('negative control unexpectedly passed')
    print('PASS V131 native CLKREQ endpoint audit and negative control')
if __name__=='__main__': main()
