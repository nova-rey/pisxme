"""V76: add the native BRIDGE_R1 U7-to-R24 support connection to V75."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V75_BRIDGE_R1RTN_R24_SIDE.kicad_pcb'
OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V76_BRIDGE_R1.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('BRIDGE_R1'); assert n
def seg(a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(p):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
for t in list(b.GetTracks()):
 if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
seg((92.2,123.0),(90.5,123.0),F); via((90.5,123.0)); seg((90.5,123.0),(90.5,117.0),B); seg((90.5,117.0),(134.0,117.0),B); via((134.0,117.0)); seg((134.0,117.0),(134.0,120.0),F); seg((134.0,120.0),(137.0,122.0),F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
