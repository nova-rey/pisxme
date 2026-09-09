"""V1256 saved-board ascent audit with native negative controls."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_LANE0_PER_PAIR_ASCENT_V1256.kicad_pcb'
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def via_at(b,net,xy):return next(x for x in b.GetTracks() if type(x).__name__=='PCB_VIA' and x.GetNetname()==net and x.GetPosition()==pcbnew.VECTOR2I_MM(*xy))
G=[('LANE0_RXP','64',(106,42),(95,72.4)),('LANE0_RXN','65',(108,43),(92.8,70.8)),('LANE0_TXN','67',(110,44),(92.2,72.6)),('LANE0_TXP','68',(104.5,45),(90.8,76.8))]
b=pcbnew.LoadBoard(str(PCB));p=pads(b);b.BuildConnectivity()
for net,padno,target,_ in G:assert via_at(b,net,target) in b.GetConnectivity().GetConnectedItems(p[('U1',padno)]),net+' ascent endpoint missing'
for net,padno,target,source in G:
 t=pcbnew.LoadBoard(str(PCB));pt=pads(t);sv=via_at(t,net,source)
 for x in list(t.GetTracks()):
  if x.GetNetname()==net and (x is sv or (type(x).__name__!='PCB_VIA' and x.GetStart()==pt[('U1',padno)].GetPosition())):t.RemoveNative(x)
 t.BuildConnectivity();assert via_at(t,net,target) not in t.GetConnectivity().GetConnectedItems(pt[('U1',padno)]),net+' negative control did not disconnect'
print('PASS V1256 native per-pair ascent endpoints; four source negative controls PASS')
