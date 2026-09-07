"""Disposable pad-field-aware RTL_1V1 QFN escape, V9."""
from pathlib import Path
import pcbnew

BASE = Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V5_NO_FIXTURE_STUBS.kicad_pcb")
OUT = Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V9_QFN_ESCAPE.kicad_pcb")
F, B = pcbnew.F_Cu, pcbnew.B_Cu; W = pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b); v.SetPosition(p(*a)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)

def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet("RTL_1V1")
 # Remove only old local fanout geometry; retain the proven outboard C4 spine.
 for item in list(b.GetTracks()):
  if item.GetNetname()=="RTL_1V1":
   pts=[item.GetStart(),item.GetEnd()]
   if any(q.x/1e6 < 90 and q.y/1e6 > 54 for q in pts): b.Remove(item)
 branches=[((77.2,58.05),(77.2,56.5)),((81.2,58.05),(82.2,56.5)),
           ((76.05,60.0),(73.8,61.2)),((76.05,62.0),(73.8,62.0)),
           ((76.05,63.2),(73.8,63.2)),((82.8,65.95),(84.5,66.0))]
 for a,z in branches: seg(b,n,F,a,z); via(b,n,z)
 for a,z in [((77.2,56.5),(82.2,56.5)),((82.2,56.5),(84.5,56.5)),
             ((84.5,56.5),(84.5,66.0)),((84.5,66.0),(73.8,66.0)),
             ((73.8,66.0),(73.8,61.2)),((73.8,61.2),(73.8,38.5)),
             ((73.8,38.5),(123.4,38.5))]: seg(b,n,B,a,z)
 via(b,n,(123.4,38.5)); seg(b,n,F,(123.4,38.5),(123.4,44.0))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
