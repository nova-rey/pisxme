"""Native-loaded Phase 24 macro-floorplan map and disposable candidates."""
from pathlib import Path
import math
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
def xy(item):
 q=item.GetPosition(); return (q.x/1e6,q.y/1e6)
def d(a,z): return math.hypot(a[0]-z[0],a[1]-z[1])
def pads(ref):
 f=b.FindFootprintByReference(ref); return [xy(p) for p in f.Pads()]
def source_points(keys):
 return [xy(p) for p in b.FindFootprintByReference('J7').Pads() if any(k in p.GetNetname() for k in keys)]
def centroid(points):
 return (sum(x for x,y in points)/len(points),sum(y for x,y in points)/len(points)) if points else (float('nan'),float('nan'))
def nearest(group,refs):
 src=source_points(group)
 dst=[q for r in refs for q in pads(r)]
 return min((d(a,z) for a in src for z in dst),default=float('nan'))
def source_centroid(group): return centroid(source_points(group))
def island_centroid(refs): return centroid([q for r in refs for q in pads(r)])
groups={
 'Ethernet':(['CM5_GBE_'],['U6','U9','J2']),
 'PCIe':(['CM5_PER0','CM5_PET0','CM5_REFCLK','CM5_PERST'],['J1']),
 'USB3-storage':(['CM5_USB3_'],['U7','J3','Y1','R23','C42','C43']),
 'SERVICE-USB2':(['SERVICE_USB2_'],['J4']),
}
lines=['# Phase 24 macro-floorplan review','','Baseline: `PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb` (native-loaded current integrated candidate).','All coordinates below are extracted after KiCad transforms; existing copper is not silently treated as valid after a footprint move.','', '| footprint | value | center (mm) | rotation | side | native body bbox |','|---|---|---:|---:|---|---|']
for r in ['J7','J2','U6','U9','U8','J1','U7','J3','J4','J5','J6','F1','F2','U1','U2','U3','U4','U5']:
 f=b.FindFootprintByReference(r); q=f.GetPosition();bb=f.GetBoundingBox()
 lines.append(f'| `{r}` | `{f.GetValue()}` | `{q.x/1e6:.2f},{q.y/1e6:.2f}` | `{f.GetOrientation().AsDegrees():.1f}` | `{f.GetLayerName()}` | `{bb.GetX()/1e6:.2f},{bb.GetY()/1e6:.2f}–{(bb.GetX()+bb.GetWidth())/1e6:.2f},{(bb.GetY()+bb.GetHeight())/1e6:.2f}` |')
lines += ['', '## CM5 pin-group to island distances', '', '| group | CM5 native pads | CM5 launch centroid (mm) | island centroid (mm) | centroid distance (mm) | nearest pad distance (mm) |', '|---|---:|---:|---:|---:|---:|']
j7=b.FindFootprintByReference('J7')
for name,(keys,refs) in groups.items():
 count=sum(1 for p in j7.Pads() if any(k in p.GetNetname() for k in keys))
 sc=source_centroid(keys); ic=island_centroid(refs)
 lines.append(f'| {name} | {count} | ({sc[0]:.2f},{sc[1]:.2f}) | ({ic[0]:.2f},{ic[1]:.2f}) | {d(sc,ic):.2f} | {nearest(keys,refs):.2f} |')
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
 '', '`SWAP_ETH_STORAGE`: move the complete Ethernet endpoint set to the south-west/CM5 side and move the complete storage island north-west/mid-acreage, explicitly testing whether both interfaces gain monotonic corridors without consuming the PCIe launch region.',
 '', '`CM5_NEIGHBORHOODS`: place ESD/support near the GBE launch, U7/clock near USB3, SERVICE near its USB2 launch, and retain J1 at the PCIe launch. This is a placement-only topology candidate.',
 '', 'These are disposable placement candidates, not accepted routing. Candidate selection requires native DRC/connectivity, pair metrics, references, mechanical access, and revalidation of every affected frozen subsystem.']
(R/'PHASE24_MACRO_FLOORPLAN_REVIEW.md').write_text('\n'.join(lines)+'\n')

def candidate(name,moves):
 x=pcbnew.LoadBoard(str(BASE))
 for ref,(px,py,rot) in moves.items():
  f=x.FindFootprintByReference(ref); f.SetPosition(pcbnew.VECTOR2I_MM(px,py)); f.SetOrientationDegrees(rot)
 x.Save(str(R/f'PHASE24_MACRO_{name}.kicad_pcb'))
candidate('ETH_WEST',{'J2':(15,145,180),'U6':(42,88,-90),'U9':(48,88,-90)})
candidate('ETH_WEST_OUTBOARD',{'J2':(15,145,180),'U6':(20,104,-90),'U9':(26,104,-90)})
candidate('ETH_EAST_ESD_WEST_JACK',{'J2':(15,145,180),'U6':(82,104,-90),'U9':(76,104,-90)})
candidate('ETH_SOUTH',{'J2':(75,160,180),'U6':(42,88,-90),'U9':(48,88,-90)})
candidate('STORAGE_LOCAL',{'U7':(95,120,180),'J3':(145,125,90)})
candidate('SWAP_ETH_STORAGE',{'J2':(15,145,180),'U6':(42,88,-90),'U9':(48,88,-90),'U7':(95,120,180),'J3':(145,125,90),'Y1':(82,120,0),'R23':(76,120,0),'C42':(76,116,0),'C43':(76,124,0)})
candidate('CM5_NEIGHBORHOODS',{'J2':(18,102,180),'U6':(44,102,-90),'U9':(50,102,-90),'U7':(96,124,180),'J3':(138,124,90),'Y1':(88,136,0),'R23':(82,136,0),'C42':(82,132,0),'C43':(82,140,0),'J4':(84,100,90)})
candidate('ETH_WEST_LOCAL_STORAGE',{'J2':(12,100,180),'U6':(25,94,-90),'U9':(25,106,-90),'U7':(96,124,180),'J3':(138,124,90),'C30':(103,116,180),'C31':(103,132,180),'C32':(103,120,180),'C33':(103,128,180),'Y1':(88,136,0),'R23':(82,136,0),'C42':(82,132,0),'C43':(82,140,0)})
print(R/'PHASE24_MACRO_FLOORPLAN_REVIEW.md')

# Placement-only quantitative comparison; moved copper is deliberately not
# counted as valid routing evidence.
candidate_names=['CURRENT','ETH_WEST','ETH_WEST_OUTBOARD','ETH_EAST_ESD_WEST_JACK','ETH_SOUTH','STORAGE_LOCAL','SWAP_ETH_STORAGE','CM5_NEIGHBORHOODS','ETH_WEST_LOCAL_STORAGE']
out=(R/'PHASE24_MACRO_FLOORPLAN_REVIEW.md').read_text().splitlines()
out += ['', '## Candidate centroid comparison', '', '| candidate | Ethernet island centroid | Storage island centroid | SERVICE centroid | Ethernet source distance (mm) | USB3 source distance (mm) |', '|---|---:|---:|---:|---:|---:|']
for name in candidate_names:
 cb=b if name=='CURRENT' else pcbnew.LoadBoard(str(R/f'PHASE24_MACRO_{name}.kicad_pcb'))
 def cgroup(refs): return centroid([(p.GetPosition().x/1e6,p.GetPosition().y/1e6) for r in refs for p in cb.FindFootprintByReference(r).Pads()])
 ec=cgroup(['U6','U9','J2']); sc=cgroup(['U7','J3','Y1','R23','C42','C43']); vc=cgroup(['J4'])
 out.append(f'| `{name}` | ({ec[0]:.1f},{ec[1]:.1f}) | ({sc[0]:.1f},{sc[1]:.1f}) | ({vc[0]:.1f},{vc[1]:.1f}) | {d(source_centroid(groups["Ethernet"][0]),ec):.1f} | {d(source_centroid(groups["USB3-storage"][0]),sc):.1f} |')
out += ['', '## Whole-board interpretation', '',
'- `J7` is on B.Cu at `(35.0,130.0)`; Ethernet exits the left mating-side column at `(32.96–36.04,99.1–100.7)`, while PCIe/USB3/SERVICE exit the right column at approximately `(66.96–70.04,99.3–106.7)`.',
'- PCIe `J1` is the closest high-speed endpoint to its CM5 launch and remains the anchor; moving it would spend the most sensitive validated geometry for little gain.',
'- SERVICE `J4` is the only currently local interface. Ethernet and storage are both materially remote; the current top Ethernet island and mid-board storage island occupy corridors that compete with PCIe/power and expose the clock/SATA congestion.',
'- The migration/swap candidates are topology probes only. They intentionally invalidate affected copper and require complete regeneration before any promotion.']
(R/'PHASE24_MACRO_FLOORPLAN_REVIEW.md').write_text('\n'.join(out)+'\n')
