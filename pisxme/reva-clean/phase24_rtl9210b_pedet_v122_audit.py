"""Native PEDET endpoint audit and disposable negative control for V122."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
PCB=ROOT/'PHASE24_RTL9210B_PEDET_R2_RIGHT_RETURN_V122.kicad_pcb'
EXPECTED={('R2','1'),('U1','8'),('J1','69')}
def audit(board):
    board.BuildConnectivity()
    p=board.FindFootprintByReference('R2').FindPadByNumber('1')
    got={(x.GetParentFootprint().GetReference(),x.GetNumber())
         for x in board.GetConnectivity().GetConnectedItems(p)
         if type(x).__name__=='PAD'}
    missing=EXPECTED-got
    if missing: raise AssertionError(f'PEDET missing {sorted(missing)}; got {sorted(got)}')
def main():
    audit(pcbnew.LoadBoard(str(PCB)))
    bad=pcbnew.LoadBoard(str(PCB)); n=bad.FindNet('PEDET'); removed=0
    for item in list(bad.GetTracks()):
        if item.GetNetname()=='PEDET': bad.RemoveNative(item); removed+=1
    if not removed: raise AssertionError('negative control found no PEDET route')
    try: audit(bad)
    except AssertionError: pass
    else: raise AssertionError('negative control unexpectedly passed')
    print('PASS V122 native PEDET endpoint audit and negative control')
if __name__=='__main__': main()
