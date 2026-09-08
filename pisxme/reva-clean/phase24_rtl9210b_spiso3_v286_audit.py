"""Native SPISO3 endpoint and trace-removal negative-control audit."""
from pathlib import Path
import sys
import pcbnew
DEFAULT=Path(__file__).resolve().parent/'PHASE24_RTL9210B_SUPPORT_ROUTE_SPISO3_V286.kicad_pcb'
def k(p): return f'{p.GetParentFootprint().GetReference()}.{p.GetNumber()}'
def main(path):
 b=pcbnew.LoadBoard(str(path)); ps={k(p):p for f in b.GetFootprints() for p in f.Pads()}; ends=('U1.22','U2.7')
 for e in ends: assert e in ps and str(ps[e].GetNetname())=='SPISO3',e
 b.BuildConnectivity(); assert set(ends)<=({k(x) for x in b.GetConnectivity().GetConnectedItems(ps[ends[0]]) if type(x).__name__=='PAD'}|{ends[0]})
 print('SPISO3 native U1.22 <-> U2.7: PASS')
 t=next(x for x in b.GetConnectivity().GetConnectedItems(ps[ends[0]]) if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='SPISO3')
 b.RemoveNative(t); b.BuildConnectivity(); ps={k(p):p for f in b.GetFootprints() for p in f.Pads()}
 assert not set(ends)<=({k(x) for x in b.GetConnectivity().GetConnectedItems(ps[ends[0]]) if type(x).__name__=='PAD'}|{ends[0]})
 print('SPISO3 trace-removal negative control: PASS')
if __name__=='__main__': main(Path(sys.argv[1]) if len(sys.argv)>1 else DEFAULT)
