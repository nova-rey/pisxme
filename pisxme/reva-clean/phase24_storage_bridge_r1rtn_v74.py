"""V74: BRIDGE_R1RTN B.Cu shelf with earlier F.Cu endpoint return."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V54_STORAGE_GND_SOLID.kicad_pcb'
OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V74_BRIDGE_R1RTN_STAGGERED_RETURN.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('BRIDGE_R1RTN'); assert n
for t in list(b.GetTracks()):
 if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
def seg(a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(p):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
seg((92.2,123.4),(90.5,123.4),F); via((90.5,123.4)); seg((90.5,123.4),(90.5,118.0),B); seg((90.5,118.0),(120.0,118.0),B); via((120.0,118.0)); seg((120.0,118.0),(138.0,122.0),F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
