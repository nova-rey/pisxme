"""Disposable transplant of the proven U7 support/clock copper oracle."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_NATIVE_ORACLE_TRANSPLANT.kicad_pcb'
DONOR=R/'PHASE24_U7_STORAGE_3V3_PAD24_CURRENT.kicad_pcb'
OUT=R/'PHASE24_STORAGE_NATIVE_ORACLE_SUPPORT_TRANSPLANT.kicad_pcb'
SUPPORT={'/STORAGE/BRIDGE_3V3','/REGULATORS/BRIDGE_3V3','/STORAGE/BRIDGE_RESET','/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC'}
def xy(p): return pcbnew.VECTOR2I(p.x,p.y)
def spec(t):
 if isinstance(t,pcbnew.PCB_VIA):
  p=t.GetPosition(); return ('via',t.GetNetname(),p.x,p.y,t.GetWidth(t.TopLayer()),t.GetDrill(),t.TopLayer(),t.BottomLayer())
 a=t.GetStart();z=t.GetEnd();return ('track',t.GetNetname(),a.x,a.y,z.x,z.y,t.GetLayer(),t.GetWidth())
b=pcbnew.LoadBoard(str(BASE));d=pcbnew.LoadBoard(str(DONOR)); specs=[spec(t) for t in list(d.GetTracks()) if t.GetNetname() in SUPPORT]
for ref in ('C16','C17','C19','Y1','R23','C42','C43'):
 s=d.FindFootprintByReference(ref);t=b.FindFootprintByReference(ref);t.SetPosition(xy(s.GetPosition()));t.SetOrientationDegrees(s.GetOrientationDegrees())
for t in list(b.GetTracks()):
 if t.GetNetname() in SUPPORT:b.Remove(t)
for q in specs:
 if q[0]=='via':
  _,name,x,y,w,dr,top,bot=q;n=b.FindNet(name);o=pcbnew.PCB_VIA(b);o.SetPosition(pcbnew.VECTOR2I(x,y));o.SetWidth(w);o.SetDrill(dr);o.SetLayerPair(top,bot);o.SetNet(n)
 else:
  _,name,ax,ay,zx,zy,layer,w=q;n=b.FindNet(name);o=pcbnew.PCB_TRACK(b);o.SetStart(pcbnew.VECTOR2I(ax,ay));o.SetEnd(pcbnew.VECTOR2I(zx,zy));o.SetLayer(layer);o.SetWidth(w);o.SetNet(n)
 b.Add(o)
b.BuildListOfNets();b.Save(str(OUT));print(OUT,len(specs))
