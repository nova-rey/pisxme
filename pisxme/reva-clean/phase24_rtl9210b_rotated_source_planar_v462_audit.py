"""Native saved-board audit for V462's six rotated source escapes."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
PCB=ROOT/'PHASE24_RTL9210B_ROTATED_SOURCE_PLANAR_V462.kicad_pcb'
NETS={'REFCLK_P':'61','REFCLK_N':'62','LANE0_RXP':'64','LANE0_RXN':'65','LANE0_TXN':'67','LANE0_TXP':'68'}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def source_vias(b,net): return [v for v in b.GetTracks() if isinstance(v,pcbnew.PCB_VIA) and v.GetNetname()==net and 98<=pcbnew.ToMM(v.GetPosition().x)<=117 and 52<=pcbnew.ToMM(v.GetPosition().y)<=78]
def connected(b,item): b.BuildConnectivity(); return b.GetConnectivity().GetConnectedItems(item)
def main():
 b=pcbnew.LoadBoard(str(PCB)); ps=pads(b); result={}
 for net,num in NETS.items():
  vs=source_vias(b,net); assert len(vs)==1,(net,len(vs)); result[net]=ps[('U1',num)] in connected(b,vs[0]); assert result[net],net
 for net,num in NETS.items():
  t=pcbnew.LoadBoard(str(PCB)); ps=pads(t); vs=source_vias(t,net); assert vs
  victims=[x for x in t.GetTracks() if x.GetNetname()==net and not isinstance(x,pcbnew.PCB_VIA) and 98<=pcbnew.ToMM(x.GetPosition().x)<=117]
  assert victims,net; t.RemoveNative(victims[0]); assert ps[('U1',num)] not in connected(t,vs[0]),net
 print('PASS V462 native saved-board source audit:',result)
 print('PASS V462 six trace-removal negative controls')
if __name__=='__main__': main()
