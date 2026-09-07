"""V87: co-author U1.36 with a short 3V3 layer handoff on V86."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_QFN_ESCAPE_JLC_V86.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_U136_QFN_CELL_V87.kicad_pcb'
F=pcbnew.F_Cu;B=pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(i):p=i.GetPosition();return p.x/1e6,p.y/1e6
def tr(b,n,l,a,z,w=.15):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n3=b.FindNet('RTL_3V3');n1=b.FindNet('RTL_1V1')
 ds=b.GetDesignSettings();ds.m_TrackMinWidth=pcbnew.FromMM(.13208);ds.m_MinClearance=pcbnew.FromMM(.15);nc=ds.m_NetSettings.GetDefaultNetclass();nc.SetTrackWidth(pcbnew.FromMM(.13208));nc.SetClearance(pcbnew.FromMM(.15));ds.m_NetSettings.SetDefaultNetclass(nc);ds.m_NetSettings.RecomputeEffectiveNetclasses()
 # Replace only the local 3V3 F.Cu source field, keeping its existing 92.0,68.4 via and B.Cu collector.
 for x in list(b.GetTracks()):
  if x.GetNetCode()==n3.GetNetCode() and type(x).__name__=='PCB_TRACK':
   a=xy(x);z=(x.GetEnd().x/1e6,x.GetEnd().y/1e6)
   if max(a[0],z[0])<=94.1 and min(a[0],z[0])>=91.9 and max(a[1],z[1])<=69.1 and min(a[1],z[1])>=65.0:b.Remove(x)
 # 3V3 U1.39 -> local via -> existing 3V3 via, entirely off the U1.36 F.Cu corridor.
 tr(b,n3,F,(94.05,68.4),(93.4,68.4),.20);via(b,n3,(93.4,68.4));tr(b,n3,B,(93.4,68.4),(92.0,68.4),.20)
 # U1.36 -> B.Cu handoff -> existing RTL_1V1 U1.40 via.
 tr(b,n1,F,(94.05,67.2),(92.8,67.2),.15);via(b,n1,(92.8,67.2));tr(b,n1,B,(92.8,67.2),(92.8,69.0),.15)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
