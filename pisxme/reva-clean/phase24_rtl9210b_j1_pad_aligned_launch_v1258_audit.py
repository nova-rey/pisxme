"""V1258 saved-board four-lane endpoint audit with negative controls."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_J1_PAD_ALIGNED_LAUNCH_V1258.kicad_pcb'
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def via_at(b,net,xy):return next(x for x in b.GetTracks() if type(x).__name__=='PCB_VIA' and x.GetNetname()==net and x.GetPosition()==pcbnew.VECTOR2I_MM(*xy))
G=[('LANE0_RXP','64','43',(95,72.4)),('LANE0_RXN','65','41',(92.8,70.8)),('LANE0_TXN','67','47',(92.2,72.6)),('LANE0_TXP','68','49',(90.8,76.8))]
b=pcbnew.LoadBoard(str(PCB));p=pads(b);b.BuildConnectivity()
for net,up,jp,src in G:
 assert p[('J1',jp)] in b.GetConnectivity().GetConnectedItems(p[('U1',{'LANE0_RXP':'64','LANE0_RXN':'65','LANE0_TXN':'67','LANE0_TXP':'68'}[net])]),net+' endpoint missing'
 assert via_at(b,net,src) in b.GetConnectivity().GetConnectedItems(p[('U1',{'LANE0_RXP':'64','LANE0_RXN':'65','LANE0_TXN':'67','LANE0_TXP':'68'}[net])]),net+' source missing'
for net,padno,jp,src in G:
 t=pcbnew.LoadBoard(str(PCB));pt=pads(t);sv=via_at(t,net,src)
 for x in list(t.GetTracks()):
  if x.GetNetname()==net and (x is sv or (type(x).__name__!='PCB_VIA' and x.GetStart()==pt[('U1',padno)].GetPosition())):t.RemoveNative(x)
 t.BuildConnectivity();assert pt[('J1',jp)] not in t.GetConnectivity().GetConnectedItems(pt[('U1',padno)]),net+' negative control did not disconnect'
print('PASS V1258 native four-lane endpoints and four source-cohort negative controls')
