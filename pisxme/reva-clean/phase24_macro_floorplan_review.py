"""Native-loaded Phase 24 macro-floorplan map and disposable candidates."""
from pathlib import Path
import math
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
def xy(item):
 q=item.GetPosition(); return (q.x/1e6,q.y/1e6)
def d(a,z): return math.hypot(a[0]-z[0],a[1]-z[1])
def pads(ref):
 f=b.FindFootprintByReference(ref); return [xy(p) for p in f.Pads()]
def nearest(group,refs):
 src=[xy(p) for p in b.FindFootprintByReference('J7').Pads() if any(k in p.GetNetname() for k in group)]
 dst=[q for r in refs for q in pads(r)]
 return min((d(a,z) for a in src for z in dst),default=float('nan'))
groups={
 'Ethernet':(['CM5_GBE'],['U6','U9','J2']),
 'PCIe':(['CM5_PER','CM5_PET','CM5_REFCLK','CM5_PERST'],['J1']),
 'USB3-storage':(['CM5_USB3'],['U7','J3']),
 'SERVICE-USB2':(['SERVICE_USB2'],['J4']),
}
lines=['# Phase 24 macro-floorplan review','','Baseline: `PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb` (native-loaded last accepted Phase 24 integrated candidate).','All coordinates below are extracted after KiCad transforms; existing copper is not silently treated as valid after a footprint move.','', '| footprint | value | center (mm) | rotation | side | native body bbox |','|---|---|---:|---:|---|---|']
for r in ['J7','J2','U6','U9','U8','J1','U7','J3','J4','J5','J6','F1','F2','U1','U2','U3','U4','U5']:
 f=b.FindFootprintByReference(r); q=f.GetPosition();bb=f.GetBoundingBox()
 lines.append(f'| `{r}` | `{f.GetValue()}` | `{q.x/1e6:.2f},{q.y/1e6:.2f}` | `{f.GetOrientation().AsDegrees():.1f}` | `{f.GetLayerName()}` | `{bb.GetX()/1e6:.2f},{bb.GetY()/1e6:.2f}–{(bb.GetX()+bb.GetWidth())/1e6:.2f},{(bb.GetY()+bb.GetHeight())/1e6:.2f}` |')
lines += ['', '## CM5 pin-group to island distances', '', '| group | CM5 native pads | current island | nearest pad distance (mm) |', '|---|---:|---|---:|']
j7=b.FindFootprintByReference('J7')
for name,(keys,refs) in groups.items():
 count=sum(1 for p in j7.Pads() if any(k in p.GetNetname() for k in keys))
 lines.append(f'| {name} | {count} | {", ".join(refs)} | {nearest(keys,refs):.2f} |')
lines += ['', '## High-speed copper census', '', '| group | routed track items | vias | copper length (mm) | layers |', '|---|---:|---:|---:|---|']
for name,(keys,_) in groups.items():
 ts=[t for t in b.GetTracks() if any(k in t.GetNetname() for k in keys)]
 vias=[t for t in ts if t.Type()==pcbnew.PCB_VIA_T]
 length=sum(t.GetLength()/1e6 for t in ts if t.Type()!=pcbnew.PCB_VIA_T)
 layers=sorted(set(t.GetLayerName() for t in ts if t.Type()!=pcbnew.PCB_VIA_T))
 lines.append(f'| {name} | {len(ts)} | {len(vias)} | {length:.1f} | {", ".join(layers) or "none"} |')
lines += ['', '## Macro-placement candidates', '',
 '`ETH_WEST`: move the complete Ethernet endpoint set to a west-edge neighborhood: J2 `(15,145)`, U6 `(42,88)`, U9 `(48,88)`. This keeps ESD near the CM5 GBE launch, avoids the SERVICE connector body, and gives the MagJack a natural west-edge launch; all affected Ethernet copper must be regenerated.',
 '', '`ETH_SOUTH`: move the MagJack to the south edge `(75,160)` while placing U6/U9 near the CM5 launch at `(42,88)/(48,88)`. This tests a separated source/connector island without consuming the PCIe east corridor; all affected Ethernet copper must be regenerated.',
 '', '`STORAGE_LOCAL`: move U7 to `(95,120)` and retain J3 as the outboard M.2 endpoint `(145,125)`, keeping the long 2280 mechanical envelope while shortening the CM5 USB3 launch. USB3/SATA copper and clock/support routes must be regenerated.',
 '', 'These are disposable placement candidates, not accepted routing. Candidate selection requires native DRC/connectivity, pair metrics, references, mechanical access, and revalidation of every affected frozen subsystem.']
(R/'PHASE24_MACRO_FLOORPLAN_REVIEW.md').write_text('\n'.join(lines)+'\n')

def candidate(name,moves):
 x=pcbnew.LoadBoard(str(BASE))
 for ref,(px,py,rot) in moves.items():
  f=x.FindFootprintByReference(ref); f.SetPosition(pcbnew.VECTOR2I_MM(px,py)); f.SetOrientationDegrees(rot)
 x.Save(str(R/f'PHASE24_MACRO_{name}.kicad_pcb'))
candidate('ETH_WEST',{'J2':(15,145,180),'U6':(42,88,-90),'U9':(48,88,-90)})
candidate('ETH_WEST_OUTBOARD',{'J2':(15,145,180),'U6':(20,104,-90),'U9':(26,104,-90)})
candidate('ETH_SOUTH',{'J2':(75,160,180),'U6':(42,88,-90),'U9':(48,88,-90)})
candidate('STORAGE_LOCAL',{'U7':(95,120,180),'J3':(145,125,90)})
print(R/'PHASE24_MACRO_FLOORPLAN_REVIEW.md')
