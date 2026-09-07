"""Isolated native-coordinate RTL_1V1 fanout probe from the V11 footprint."""
from pathlib import Path
import pcbnew

BASE=Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V11_NATIVE_RSET.kicad_pcb")
OUT=Path("PHASE24_RTL9210B_1V1_NATIVE_FANOUT_V1.kicad_pcb")
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,a):
 v=pcbnew.PCB_VIA(b);v.SetPosition(p(*a));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet("RTL_1V1")
 for item in list(b.GetTracks()):
  if item.GetNetname()=="RTL_1V1": b.Remove(item)
 branches=[((82.8,58.05),(82.8,55.5)),((81.2,58.05),(81.2,55.5)),((77.2,58.05),(77.2,55.5)),
           ((76.05,60.0),(74.8,60.0)),((76.05,62.0),(74.8,62.0)),((76.05,63.2),(74.8,63.2)),
           ((82.8,65.95),(82.8,67.2)),((83.95,62.4),(85.2,62.4))]
 for a,z in branches: seg(b,n,F,a,z);via(b,n,z)
 for a,z in [((77.2,55.5),(82.8,55.5)),((82.8,55.5),(85.2,55.5)),((85.2,55.5),(85.2,67.2)),
             ((85.2,67.2),(82.8,67.2)),((85.2,55.5),(74.8,55.5)),((74.8,55.5),(74.8,63.2)),
             ((74.8,55.5),(74.8,42.0)),((74.8,42.0),(123.4,42.0))]: seg(b,n,B,a,z)
 via(b,n,(123.4,42.0));seg(b,n,F,(123.4,42.0),(123.4,51.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
