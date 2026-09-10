"""V51: move selector-side TUSB_SATA_TXP above the M.2 launch corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V50_U7_RXN_RIGHTDOGLEG.kicad_pcb'; OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V51_SELECTOR_TXP_UPPER.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('TUSB_SATA_TXP'); assert n
def route(pts,l):
 for a,z in zip(pts,pts[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(p):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
for t in list(b.GetTracks()):
 if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
route([(104,116),(106,116)],F); via((106,116)); route([(106,116),(120,105),(180,105),(184,130.8)],B); via((184,130.8)); route([(184,130.8),(181.5,131.8)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
