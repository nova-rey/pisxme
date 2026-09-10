"""V77: coordinated BRIDGE_R1/R1RTN source-field allocation."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V54_STORAGE_GND_SOLID.kicad_pcb'
OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V77_BRIDGE_R1_PAIR.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
def N(s):
 n=b.FindNet(s); assert n; return n
def rm(s):
 n=N(s)
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
def seg(s,a,z,l):
 n=N(s); t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(s,p):
 n=N(s); v=pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
for s in ('BRIDGE_R1','BRIDGE_R1RTN'): rm(s)
seg('BRIDGE_R1',(92.2,123.0),(89.5,123.0),F); seg('BRIDGE_R1',(89.5,123.0),(89.5,121.5),F); via('BRIDGE_R1',(89.5,121.5)); seg('BRIDGE_R1',(89.5,121.5),(134.0,116.0),B); via('BRIDGE_R1',(134.0,116.0)); seg('BRIDGE_R1',(134.0,116.0),(134.0,119.0),F); seg('BRIDGE_R1',(134.0,119.0),(137.0,122.0),F)
seg('BRIDGE_R1RTN',(92.2,123.4),(90.5,123.4),F); via('BRIDGE_R1RTN',(90.5,123.4)); seg('BRIDGE_R1RTN',(90.5,123.4),(90.5,118.0),B); seg('BRIDGE_R1RTN',(90.5,118.0),(134.0,118.0),B); via('BRIDGE_R1RTN',(134.0,118.0)); seg('BRIDGE_R1RTN',(134.0,118.0),(134.0,120.0),F); seg('BRIDGE_R1RTN',(134.0,120.0),(140.0,120.0),F); seg('BRIDGE_R1RTN',(140.0,120.0),(140.0,122.0),F); seg('BRIDGE_R1RTN',(140.0,122.0),(138.0,122.0),F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
