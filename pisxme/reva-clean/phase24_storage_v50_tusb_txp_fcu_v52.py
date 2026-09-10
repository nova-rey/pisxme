"""V52: test a direct F.Cu TUSB_SATA_TXP corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V50_U7_RXN_RIGHTDOGLEG.kicad_pcb'; OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V52_TUSB_TXP_FCU.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('TUSB_SATA_TXP'); assert n
def route(pts):
 for a,z in zip(pts,pts[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
for t in list(b.GetTracks()):
 if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
route([(104,116),(120,116),(160,116),(175,124),(181.5,131.8)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
