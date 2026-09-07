"""V84: co-author U1.39/U1.40 3V3 source field on the retained JLC rule basis."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_REALLOCATE_3V3_U140_V79.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_QFN_ESCAPE_JLC_V84.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(item):
 p=item.GetPosition(); return p.x/1e6,p.y/1e6
def tr(b,n,l,a,z,w=.15):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy0):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy0));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n3=b.FindNet('RTL_3V3'); n1=b.FindNet('RTL_1V1')
 d=b.GetDesignSettings(); d.m_MinClearance=pcbnew.FromMM(.15); d.m_TrackMinWidth=pcbnew.FromMM(.13208)
 # Remove only the old left source-field copper; retain the downstream B.Cu rail and via.
 for x in list(b.GetTracks()):
  if x.GetNetCode()!=n3.GetNetCode(): continue
  a=xy(x); z=(x.GetEnd().x/1e6,x.GetEnd().y/1e6)
  if max(a[0],z[0])<=94.1 and min(a[0],z[0])>=91.9 and max(a[1],z[1])<=69.1 and min(a[1],z[1])>=65.0:
   if type(x).__name__=='PCB_TRACK': b.Remove(x)
 # Rebuild 3V3 from U1.39 to the retained 92.0,68.4 through-via.
 tr(b,n3,F,(94.05,68.4),(93.2,68.4));tr(b,n3,F,(93.2,68.4),(93.2,65.0));tr(b,n3,F,(93.2,65.0),(92.0,65.0));tr(b,n3,F,(92.0,65.0),(92.0,68.4),.20)
 # Rebuild U1.40 with a JLC-rule fine-pitch dogbone and existing B.Cu collector.
 tr(b,n1,F,(94.05,68.8),(92.8,69.0));vi(b,n1,(92.8,69.0));tr(b,n1,B,(92.8,69.0),(92.8,72.8))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
