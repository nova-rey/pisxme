"""Staged 1V1 fanout routed around the proven crystal/RSET corridors."""
from pathlib import Path
import pcbnew
BASE=Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V11_NATIVE_RSET.kicad_pcb")
OUT=Path("PHASE24_RTL9210B_1V1_CRYSTAL_RSET_STAGED_V3.kicad_pcb")
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def p(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(p(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet("RTL_1V1")
 for item in list(b.GetTracks()):
  if item.GetNetname() not in {"XTAL_IN","XTAL_OUT","RSET"}:b.Remove(item)
 # Left-side pads join one F.Cu collector and transition once below the crystal.
 for a,z in [((76.05,60.0),(74.8,60.0)),((76.05,62.0),(74.8,62.0)),((76.05,63.2),(74.8,63.2))]:s(b,n,F,a,z)
 s(b,n,F,(74.8,60.0),(74.8,63.2));v(b,n,(74.8,63.2))
 # Top/right and bottom pads use edge-normal dogbones to a right collector.
 for a,z in [((77.2,58.05),(77.2,55.5)),((81.2,58.05),(81.2,55.5)),((82.8,58.05),(82.8,55.5)),
             ((83.95,62.4),(85.2,62.4)),((82.8,65.95),(82.8,67.2))]:s(b,n,F,a,z);v(b,n,z)
 for a,z in [((77.2,55.5),(74.8,55.5)),((74.8,55.5),(74.8,63.2)),((74.8,63.2),(85.2,63.2)),
             ((81.2,55.5),(85.2,55.5)),((82.8,55.5),(85.2,55.5)),((85.2,55.5),(85.2,67.2)),
             ((85.2,67.2),(82.8,67.2)),((74.8,55.5),(74.8,41.0)),((74.8,41.0),(123.4,41.0))]:s(b,n,B,a,z)
 v(b,n,(123.4,41.0));s(b,n,F,(123.4,41.0),(123.4,51.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
