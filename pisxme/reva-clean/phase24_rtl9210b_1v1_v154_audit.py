"""Native V154 RTL_1V1 relocation audit and trace-removal negative control."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
PCB=ROOT/'PHASE24_RTL9210B_1V1_OUTBOARD_HANDOFF_V154.kicad_pcb'
EXPECTED={('C4','1'),('U1','16'),('U1','25'),('U1','36'),('U1','40'),('U1','50'),('U1','55'),('U1','60'),('U1','63')}
def connected(board):
 board.BuildConnectivity();p=board.FindFootprintByReference('U1').FindPadByNumber('55')
 return {(x.GetParentFootprint().GetReference(),x.GetNumber()) for x in board.GetConnectivity().GetConnectedItems(p) if type(x).__name__=='PAD'}
def main():
 b=pcbnew.LoadBoard(str(PCB));got=connected(b)
 if EXPECTED-got: raise AssertionError(f'missing RTL_1V1 pads {sorted(EXPECTED-got)}')
 bad=pcbnew.LoadBoard(str(PCB));removed=0
 for x in list(bad.GetTracks()):
  if x.GetNetname()=='RTL_1V1':bad.RemoveNative(x);removed+=1
 if not removed: raise AssertionError('negative control found no RTL_1V1 route')
 if not EXPECTED-connected(bad): raise AssertionError('negative control unexpectedly passed')
 print('PASS V154 native RTL_1V1 audit and negative control')
if __name__=='__main__':main()
