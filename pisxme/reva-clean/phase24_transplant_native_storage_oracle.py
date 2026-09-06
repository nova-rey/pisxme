"""Disposable transplant of the preserved native USB3/SATA route oracle.

Only actual donor tracks/vias for storage data nets are copied.  The base
board remains the authority for nets and all other circuitry.
"""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_ISLAND_COHERENT_USB3_REPAIRED.kicad_pcb'
DONOR=R/'PHASE19_V3_USB_PROVEN_SPLIT_SATA_REFILL.kicad_pcb'
OUT=R/'PHASE24_STORAGE_NATIVE_ORACLE_TRANSPLANT.kicad_pcb'
def mm(p): return pcbnew.VECTOR2I(p.x,p.y)
def names(n): return ('/CORE_CM5/CM5_USB3_' in n or '/STORAGE/BRIDGE_SATA_' in n or '/STORAGE/SATA_M2_' in n)
b=pcbnew.LoadBoard(str(BASE)); d=pcbnew.LoadBoard(str(DONOR))
donor_specs=[]
for t in list(d.GetTracks()):
 if not names(t.GetNetname()): continue
 if isinstance(t,pcbnew.PCB_VIA):
  p=t.GetPosition(); donor_specs.append(('via',t.GetNetname(),p.x,p.y,t.GetWidth(t.TopLayer()),t.GetDrill(),t.TopLayer(),t.BottomLayer()))
 else:
  a=t.GetStart(); z=t.GetEnd(); donor_specs.append(('track',t.GetNetname(),a.x,a.y,z.x,z.y,t.GetLayer(),t.GetWidth()))
for ref in ('U7','J3','C30','C31','C32','C33'):
 s=d.FindFootprintByReference(ref); t=b.FindFootprintByReference(ref)
 t.SetPosition(mm(s.GetPosition())); t.SetOrientationDegrees(s.GetOrientationDegrees())
for t in list(b.Tracks()):
 if names(t.GetNetname()): b.Remove(t)
for spec in donor_specs:
 if spec[0]=='via':
  _,name,x,y,width,drill,top,bottom=spec; n=b.FindNet(name)
  q=pcbnew.PCB_VIA(b);q.SetPosition(pcbnew.VECTOR2I(x,y));q.SetWidth(width);q.SetDrill(drill);q.SetLayerPair(top,bottom);q.SetNet(n)
 else:
  _,name,ax,ay,zx,zy,layer,width=spec; n=b.FindNet(name)
  q=pcbnew.PCB_TRACK(b);q.SetStart(pcbnew.VECTOR2I(ax,ay));q.SetEnd(pcbnew.VECTOR2I(zx,zy));q.SetLayer(layer);q.SetWidth(width);q.SetNet(n)
 b.Add(q)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
