"""Native U1.34 RTL_3V3 V143 audit and trace-removal negative control."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
PCB=ROOT/'PHASE24_RTL9210B_U134_OUTER_HIGH_V143.kicad_pcb'
EXPECTED={('U1','34'),('U1','20'),('C3','1'),('R2','2'),('R3','2')}
def connected(board):
 board.BuildConnectivity();p=board.FindFootprintByReference('U1').FindPadByNumber('34')
 return {(x.GetParentFootprint().GetReference(),x.GetNumber()) for x in board.GetConnectivity().GetConnectedItems(p) if type(x).__name__=='PAD'}
def main():
 b=pcbnew.LoadBoard(str(PCB));got=connected(b)
 if EXPECTED-got: raise AssertionError(f'missing RTL_3V3 pads {sorted(EXPECTED-got)}')
 bad=pcbnew.LoadBoard(str(PCB));removed=0
 for x in list(bad.GetTracks()):
  if x.GetNetname()=='RTL_3V3': bad.RemoveNative(x);removed+=1
 if not removed: raise AssertionError('negative control found no RTL_3V3 route')
 if not EXPECTED-connected(bad): raise AssertionError('negative control unexpectedly passed')
 print('PASS V143 native U1.34 RTL_3V3 audit and negative control')
if __name__=='__main__':main()
