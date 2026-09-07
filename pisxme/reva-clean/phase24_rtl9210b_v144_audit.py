"""Native V144 support joins and negative controls."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
PCB=ROOT/'PHASE24_RTL9210B_SSD33_ON_V143_V144.kicad_pcb'
def pads(board, ref, num):
 board.BuildConnectivity();p=board.FindFootprintByReference(ref).FindPadByNumber(num)
 return {(x.GetParentFootprint().GetReference(),x.GetNumber()) for x in board.GetConnectivity().GetConnectedItems(p) if type(x).__name__=='PAD'}
def main():
 b=pcbnew.LoadBoard(str(PCB))
 if {('U1','34'),('C3','1'),('R2','2'),('R3','2'),('U1','20')}-pads(b,'U1','34'): raise AssertionError('U1.34 rail join incomplete')
 if {('J1','2'),('J1','4'),('J1','6'),('J1','8')}-pads(b,'J1','2'): raise AssertionError('SSD_3V3 row incomplete')
 bad=pcbnew.LoadBoard(str(PCB));
 for x in list(bad.GetTracks()):
  if x.GetNetname() in ('RTL_3V3','SSD_3V3'): bad.RemoveNative(x)
 if {('U1','34'),('C3','1'),('R2','2'),('R3','2'),('U1','20')}-pads(bad,'U1','34') == set(): raise AssertionError('negative control unexpectedly passed')
 print('PASS V144 native U1.34 and SSD_3V3 support joins')
if __name__=='__main__':main()
