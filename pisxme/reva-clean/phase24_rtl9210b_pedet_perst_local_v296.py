"""V296: translate the local PERST vertical around the PEDET landing."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_PEDET_ROUTE_V292.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_PEDET_PERST_LOCAL_V296.kicad_pcb'
F=pcbnew.F_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('PERST_N')
 for q in list(b.GetTracks()):
  if q.GetNetname()=='PERST_N' and q.GetLayerName()=='F.Cu' and abs(q.GetStart().x/1e6-104.5)<.01 and abs(q.GetEnd().x/1e6-104.5)<.01:
   b.RemoveNative(q)
 tr(b,n,(104.5,60),(107,60));tr(b,n,(107,60),(107,63));tr(b,n,(107,63),(104.5,63))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
