"""V85: V84 corrected for native netclass persistence and duplicate removal."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_REALLOCATE_3V3_U140_V79.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_QFN_ESCAPE_JLC_V85.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def pos(i):
 p=i.GetPosition();return (p.x/1e6,p.y/1e6)
def endpoints(x):
 a=x.GetStart();z=x.GetEnd();return {(round(a.x/1e6,3),round(a.y/1e6,3)),(round(z.x/1e6,3),round(z.y/1e6,3))}
def tr(b,n,l,a,z,w=.15):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n3=b.FindNet('RTL_3V3');n1=b.FindNet('RTL_1V1')
 ds=b.GetDesignSettings(); ds.m_TrackMinWidth=pcbnew.FromMM(.13208);ds.m_MinClearance=pcbnew.FromMM(.15)
 nc=ds.m_NetSettings.GetDefaultNetclass();nc.SetTrackWidth(pcbnew.FromMM(.13208));nc.SetClearance(pcbnew.FromMM(.15));ds.m_NetSettings.SetDefaultNetclass(nc);ds.m_NetSettings.RecomputeEffectiveNetclasses()
 tracks=list(b.GetTracks())
 for x in tracks:
  if x.GetNetCode()==n1.GetNetCode():
   a=endpoints(x)
   if a in ({(94.05,68.8),(92.8,69.0)},{(92.8,69.0),(92.8,72.8)}): b.Remove(x)
 for x in tracks:
  if type(x).__name__=='PCB_VIA' and x.GetNetCode()==n1.GetNetCode() and all(abs(v-w)<.002 for v,w in zip(pos(x),(92.8,69.0))): b.Remove(x)
 # Replace the prior local 3V3 field, retaining only the downstream collector/via.
 for x in list(b.GetTracks()):
  if x.GetNetCode()!=n3.GetNetCode(): continue
  a=pos(x);z=(x.GetEnd().x/1e6,x.GetEnd().y/1e6)
  if max(a[0],z[0])<=94.1 and min(a[0],z[0])>=91.9 and max(a[1],z[1])<=69.1 and min(a[1],z[1])>=65.0:
   b.Remove(x)
 tr(b,n3,F,(94.05,68.4),(93.2,68.4),.20);tr(b,n3,F,(93.2,68.4),(93.2,65.0),.20);tr(b,n3,F,(93.2,65.0),(92.0,65.0),.20);tr(b,n3,F,(92.0,65.0),(92.0,68.4),.20)
 tr(b,n1,F,(94.05,68.8),(92.8,69.0),.15);vi(b,n1,(92.8,69.0));tr(b,n1,B,(92.8,69.0),(92.8,72.8),.15)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
