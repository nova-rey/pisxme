"""V298: increase clearance in the PEDET below-endpoint loop."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_ROUTE_SPISI_V289.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_PEDET_PERST_LOCAL_V298.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.50));q.SetDrill(pcbnew.FromMM(.25));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));p=b.FindNet('PEDET');r=b.FindNet('PERST_N')
 tr(b,p,F,(90.9,53),(88,53));tr(b,p,F,(88,53),(88,46));via(b,p,(88,46));tr(b,p,B,(88,46),(108,46));tr(b,p,B,(108,46),(108,59.5));via(b,p,(108,59.5));tr(b,p,F,(108,59.5),(108,64.5));tr(b,p,F,(108,64.5),(106.5,64.5));tr(b,p,F,(106.5,64.5),(106.5,62.4));tr(b,p,F,(106.5,62.4),(101.95,62.4));via(b,p,(108,62.4));tr(b,p,B,(108,62.4),(139,62.4));via(b,p,(139,62.4));tr(b,p,F,(139,62.4),(140.75,62.725))
 for q in list(b.GetTracks()):
  if q.GetNetname()=='PERST_N' and q.GetLayerName()=='F.Cu' and abs(q.GetStart().x/1e6-104.5)<.01 and abs(q.GetEnd().x/1e6-104.5)<.01: b.RemoveNative(q)
 tr(b,r,F,(104.5,60),(107,60));tr(b,r,F,(107,60),(107,63));tr(b,r,F,(107,63),(104.5,63))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
