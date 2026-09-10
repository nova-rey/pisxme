"""V47: move only BRIDGE_SATA_RX_N around the U7 TX_N source field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V46_CM5_TXN_SOURCE.kicad_pcb'; OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V47_U7_RXN_ESCAPE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('BRIDGE_SATA_RX_N'); assert n
def route(pts,l):
 for a,z in zip(pts,pts[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(p):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
for t in list(b.GetTracks()):
 if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
route([(95.0,127.8),(95.0,128.7),(94.3,130.0)],F); via((94.3,130.0)); route([(94.3,130.0),(100.0,134.0),(103.0,128.0)],B); via((103.0,128.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
