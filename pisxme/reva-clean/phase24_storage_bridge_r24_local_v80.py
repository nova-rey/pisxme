"""V80: co-locate and rotate the U7 R1/RTN support resistor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V79_M2_POWER_OWNER.kicad_pcb'
OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V80_R24_LOCAL.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.15)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
r=b.FindFootprintByReference('R24'); assert r
r.SetPosition(P(96.0,123.2)); r.SetOrientationDegrees(90)
for name in ('BRIDGE_R1','BRIDGE_R1RTN'):
 n=b.FindNet(name); assert n
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
def seg(n,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
for name,u,pad in (('BRIDGE_R1',(92.2,123.0),'1'),('BRIDGE_R1RTN',(92.2,123.4),'2')):
 n=b.FindNet(name); p=r.FindPadByNumber(pad); q=p.GetPosition(); q=(q.x/1e6,q.y/1e6)
 x=q[0]; y=q[1]
 seg(n,(u[0],u[1]),(93.8,u[1])); seg(n,(93.8,u[1]),(x,y))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
