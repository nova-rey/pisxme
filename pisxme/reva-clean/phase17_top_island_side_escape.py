"""Disposable Phase 17 trial: official CM5IO island with side escapes at J7."""
from pathlib import Path
import json
import os
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_EDAC_CORRECTED_PHASE17.kicad_pcb'
GEOM=ROOT/'cm5io_mdi_geometry.json'
OUT=ROOT/'ACREAGE_CM5IO_TOP_ISLAND_SIDE_ESCAPE_PHASE17.kicad_pcb'
DX,DY=-42.5,-8.0
if os.environ.get('PISXME_LANE_ORDER') == 'LEFT_EDGE':
    DX,DY=-62.5,62.0
if os.environ.get('PISXME_LANE_ORDER') == 'RIGHT_SHELF':
    DX,DY=197.5,-33.0
if os.environ.get('PISXME_LANE_ORDER') == 'RIGHT_CHANNEL':
    DX,DY=197.5,-33.0
if os.environ.get('PISXME_LANE_ORDER') == 'RIGHT_CHANNEL_STAGGERED':
    DX,DY=197.5,-33.0
if os.environ.get('PISXME_LANE_ORDER') == 'RIGHT_CHANNEL_WEST_SPLIT':
    DX,DY=197.5,-33.0
if os.environ.get('PISXME_LANE_ORDER') == 'LOCAL_BOTTOM':
    # CM5IO-relative island below the frozen cooler reservation.  The
    # official ESD-to-MagJack graph remains rigid; only the CM5-to-ESD legs
    # are regenerated from PiSXMe's actual J7 anchors.
    DX,DY=49.9,84.8
if os.environ.get('PISXME_LANE_ORDER') == 'LOCAL_BOTTOM_SPLIT':
    DX,DY=49.9,84.8
if os.environ.get('PISXME_LANE_ORDER') == 'ROTATED_LOCAL':
    # Rigidly rotate the complete official ESD/MagJack island 180 degrees
    # about the source-facing reference transform.  The CM5/J7 remains
    # frozen; only the Ethernet-local island and its internal MDI graph move.
    DX,DY=0.0,0.0
if os.environ.get('PISXME_LANE_ORDER') == 'TD3_OUTER':
    OUT=ROOT/'ACREAGE_CM5IO_TOP_ISLAND_TD3_OUTER_PHASE17.kicad_pcb'
if os.environ.get('PISXME_LANE_ORDER') == 'LEFT_EDGE':
    OUT=ROOT/'ACREAGE_CM5IO_LEFT_EDGE_PHASE17.kicad_pcb'
if os.environ.get('PISXME_LANE_ORDER') == 'RIGHT_SHELF':
    OUT=ROOT/'ACREAGE_CM5IO_RIGHT_SHELF_PHASE17.kicad_pcb'
if os.environ.get('PISXME_LANE_ORDER') == 'RIGHT_CHANNEL':
    OUT=ROOT/'ACREAGE_CM5IO_RIGHT_CHANNEL_PHASE17.kicad_pcb'
if os.environ.get('PISXME_LANE_ORDER') == 'RIGHT_CHANNEL_STAGGERED':
    OUT=ROOT/'ACREAGE_CM5IO_RIGHT_CHANNEL_STAGGERED_PHASE17.kicad_pcb'
if os.environ.get('PISXME_LANE_ORDER') == 'RIGHT_CHANNEL_WEST_SPLIT':
    OUT=ROOT/'ACREAGE_CM5IO_RIGHT_CHANNEL_WEST_SPLIT_PHASE17.kicad_pcb'
if os.environ.get('PISXME_LANE_ORDER') == 'LOCAL_BOTTOM':
    OUT=ROOT/'ACREAGE_CM5IO_LOCAL_BOTTOM_PHASE17.kicad_pcb'
if os.environ.get('PISXME_LANE_ORDER') == 'LOCAL_BOTTOM_SPLIT':
    OUT=ROOT/'ACREAGE_CM5IO_LOCAL_BOTTOM_SPLIT_PHASE17.kicad_pcb'
if os.environ.get('PISXME_LANE_ORDER') == 'ROTATED_LOCAL':
    OUT=ROOT/'ACREAGE_CM5IO_ROTATED_LOCAL_PHASE17.kicad_pcb'

def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def add(b,n,pts,layer=pcbnew.F_Cu):
    for a,z in zip(pts,pts[1:]):
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z));
        t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(.127)); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.45)); q.SetDrill(pcbnew.FromMM(.20)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)

def main():
    rows=json.loads(GEOM.read_text()); b=pcbnew.LoadBoard(str(BASE))
    nets={n:b.FindNet(n) for n in set(r['net'] for r in rows)}
    for n in nets.values():
        if n is None: raise RuntimeError('missing MDI net')
    # DX=-42.5 places the official island at U9=(27.6,57.215),
    # U6=(33.6,57.215), and J2=(30,45); keep the footprints and translated
    # connector-side vectors on the same rigid transform.
    if os.environ.get('PISXME_LANE_ORDER') in ('LOCAL_BOTTOM','LOCAL_BOTTOM_SPLIT','LEFT_EDGE','RIGHT_SHELF','RIGHT_CHANNEL','RIGHT_CHANNEL_STAGGERED','RIGHT_CHANNEL_WEST_SPLIT'):
        island_positions=(('U9',(70.1+DX,65.215+DY),270),('U6',(76.1+DX,65.215+DY),270),
                          ('J2',(72.5+DX,53+DY),180))
    elif os.environ.get('PISXME_LANE_ORDER') == 'ROTATED_LOCAL':
        island_positions=(('U9',(124.4,149.785),90),('U6',(118.4,149.785),90),
                          ('J2',(122.0,162.0),0))
    else:
        island_positions=(('U6',(33.6,57.215),270),('U9',(27.6,57.215),270),('J2',(30,45),180))
    for ref,pos,rot in island_positions:
        f=b.FindFootprintByReference(ref)
        if f is None: raise RuntimeError(ref)
        f.SetPosition(V(*pos)); f.SetOrientationDegrees(rot)
    mdi=set(nets)
    for t in list(b.GetTracks()):
        if str(t.GetNetname()).rsplit('/',1)[-1] in mdi: b.Remove(t)
    # Keep the official connector-to-protector geometry, omitting only the
    # long CM5-side legs and J7-side fanout.  The short USON internal graph
    # remains authoritative and is translated rigidly with the island.
    for r in rows:
        a,z=r['a'],r['z']; length=((a[0]-z[0])**2+(a[1]-z[1])**2)**.5
        if max(a[1],z[1]) >= 70 or length >= 5: continue
        if os.environ.get('PISXME_LANE_ORDER') == 'ROTATED_LOCAL':
            aa=(194.5-a[0],215.0-a[1]); zz=(194.5-z[0],215.0-z[1])
        else:
            aa=(a[0]+DX,a[1]+DY); zz=(z[0]+DX,z[1]+DY)
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*aa)); t.SetEnd(V(*zz))
        t.SetLayer(r['layer']); t.SetWidth(pcbnew.FromMM(r['width'])); t.SetNetCode(nets[r['net']].GetNetCode()); b.Add(t)
    # Landing points are the ESD-side endpoints of the omitted official legs.
    land={
      'CM5_GBE_TD3_P':(68.704119,67.210), 'CM5_GBE_TD3_N':(68.861524,67.590),
      'CM5_GBE_TD2_N':(69.521298,68.110), 'CM5_GBE_TD2_P':(69.678701,68.490),
      'CM5_GBE_TD1_P':(75.16,66.871297), 'CM5_GBE_TD1_N':(75.539999,67.028702),
      'CM5_GBE_TD0_N':(76.66,66.571298), 'CM5_GBE_TD0_P':(77.039999,66.728702)}
    if os.environ.get('PISXME_LANE_ORDER') == 'ROTATED_LOCAL':
        land={name:(194.5-x,215.0-y) for name,(x,y) in land.items()}
    # Exit left/right of J7 before rising above its NPTH field.  Pair order
    # is monotonic on each side; no signal uses a plane layer or via-in-pad.
    paths={
      'CM5_GBE_TD3_P':[(32.96,99.10),(27.0,99.10),(27.0,72.0),(26.204119,59.210)],
      'CM5_GBE_TD3_N':[(32.96,99.50),(27.5,99.50),(27.5,71.5),(26.361524,59.590)],
      'CM5_GBE_TD2_N':[(32.96,100.30),(24.0,100.30),(24.0,70.0),(27.021298,60.110)],
      'CM5_GBE_TD2_P':[(32.96,100.70),(24.5,100.70),(24.5,69.5),(27.178701,60.490)],
      'CM5_GBE_TD1_P':[(36.04,99.10),(40.0,99.10),(40.0,72.0),(32.66,58.871297)],
      'CM5_GBE_TD1_N':[(36.04,99.50),(40.5,99.50),(40.5,71.5),(33.039999,59.028702)],
      'CM5_GBE_TD0_N':[(36.04,100.30),(43.0,100.30),(43.0,70.0),(34.16,58.571298)],
      'CM5_GBE_TD0_P':[(36.04,100.70),(43.5,100.70),(43.5,69.5),(34.539999,58.728702)]}
    # On the left side of J7, the CM5IO source order is TD3P, TD3N,
    # TD2N, TD2P from top to bottom.  The prior monotonic trial inverted
    # the two pair lanes (TD2 outside TD3), creating the documented source
    # crossings.  This variant keeps TD3 outer/left and TD2 inner/right.
    if os.environ.get('PISXME_LANE_ORDER') == 'TD3_OUTER':
        paths['CM5_GBE_TD3_P'][1:3]=[(24.0,99.10),(24.0,69.5)]
        paths['CM5_GBE_TD3_N'][1:3]=[(24.5,99.50),(24.5,70.0)]
        paths['CM5_GBE_TD2_N'][1:3]=[(27.0,100.30),(27.0,70.5)]
        paths['CM5_GBE_TD2_P'][1:3]=[(27.5,100.70),(27.5,71.0)]
    if os.environ.get('PISXME_LANE_ORDER') == 'LEFT_EDGE':
        # Complete island at the open left/bottom acreage edge.  Left J7
        # pairs descend on the west side; right J7 pairs use a lower return
        # corridor, avoiding the regulator/PCIe/cooler reservations.
        paths={
          'CM5_GBE_TD3_P':[(32.96,99.10),(24.0,99.10),(24.0,115.0),(5.204119,129.210)],
          'CM5_GBE_TD3_N':[(32.96,99.50),(23.5,99.50),(23.5,115.5),(5.361524,129.590)],
          'CM5_GBE_TD2_N':[(32.96,100.30),(22.0,100.30),(22.0,116.0),(7.021298,130.110)],
          'CM5_GBE_TD2_P':[(32.96,100.70),(21.5,100.70),(21.5,116.5),(7.178701,130.490)],
          'CM5_GBE_TD1_P':[(36.04,99.10),(43.0,99.10),(43.0,145.0),(12.660000,128.871297)],
          'CM5_GBE_TD1_N':[(36.04,99.50),(43.5,99.50),(43.5,145.5),(13.039999,129.028702)],
          'CM5_GBE_TD0_N':[(36.04,100.30),(44.0,100.30),(44.0,146.0),(14.160000,128.571298)],
          'CM5_GBE_TD0_P':[(36.04,100.70),(44.5,100.70),(44.5,146.5),(14.539999,128.728702)]}
    if os.environ.get('PISXME_LANE_ORDER') == 'RIGHT_SHELF':
        # CM5IO-relative connector-side island on the open right shelf.
        # The two source groups leave J7 on opposite sides, rise above the
        # cooler reservation, then enter the translated official graph.
        paths={
          'CM5_GBE_TD3_P':[(32.96,99.10),(24.0,99.10),(24.0,38.0),(266.204119,34.210)],
          'CM5_GBE_TD3_N':[(32.96,99.50),(24.5,99.50),(24.5,38.5),(266.361524,34.590)],
          'CM5_GBE_TD2_N':[(32.96,100.30),(25.0,100.30),(25.0,39.0),(267.021298,35.110)],
          'CM5_GBE_TD2_P':[(32.96,100.70),(25.5,100.70),(25.5,39.5),(267.178701,35.490)],
          'CM5_GBE_TD1_P':[(36.04,99.10),(74.0,99.10),(74.0,38.0),(272.660000,33.871297)],
          'CM5_GBE_TD1_N':[(36.04,99.50),(74.5,99.50),(74.5,38.5),(273.039999,34.028702)],
          'CM5_GBE_TD0_N':[(36.04,100.30),(75.0,100.30),(75.0,39.0),(274.160000,33.571298)],
          'CM5_GBE_TD0_P':[(36.04,100.70),(75.5,100.70),(75.5,39.5),(274.539999,33.728702)]}
    if os.environ.get('PISXME_LANE_ORDER') == 'RIGHT_CHANNEL':
        # Parametric source breakout: unique pad dogbones first, then ordered
        # parallel lanes, then an upper corridor. This avoids the prior
        # hand-fan diagonals and preserves pair/group order.
        paths={
          'CM5_GBE_TD3_P':[(32.96,99.10),(30.0,99.10),(30.0,75.0),(60.0,75.0),(60.0,38.0),(266.204119,34.210)],
          'CM5_GBE_TD3_N':[(32.96,99.50),(30.5,99.50),(30.5,75.4),(60.5,75.4),(60.5,38.4),(266.361524,34.590)],
          'CM5_GBE_TD1_P':[(36.04,99.10),(37.5,99.10),(37.5,76.0),(66.0,76.0),(66.0,38.0),(272.660000,33.871297)],
          'CM5_GBE_TD1_N':[(36.04,99.50),(38.0,99.50),(38.0,76.4),(66.5,76.4),(66.5,38.4),(273.039999,34.028702)],
          'CM5_GBE_TD2_N':[(32.96,100.30),(31.0,100.30),(31.0,78.0),(62.0,78.0),(62.0,39.0),(267.021298,35.110)],
          'CM5_GBE_TD2_P':[(32.96,100.70),(31.5,100.70),(31.5,78.4),(62.5,78.4),(62.5,39.4),(267.178701,35.490)],
          'CM5_GBE_TD0_N':[(36.04,100.30),(38.5,100.30),(38.5,79.0),(68.0,79.0),(68.0,39.0),(274.160000,33.571298)],
          'CM5_GBE_TD0_P':[(36.04,100.70),(39.0,100.70),(39.0,79.4),(68.5,79.4),(68.5,39.4),(274.539999,33.728702)]}
    if os.environ.get('PISXME_LANE_ORDER') == 'RIGHT_CHANNEL_STAGGERED':
        # Pair-specific source vias and independent B.Cu lanes.  The return
        # vias are deliberately spread well beyond the 0.8 mm minimum before
        # the short F.Cu dogbones into the official ESD landing points.
        paths={
          'CM5_GBE_TD3_P':[(32.96,99.10),(28.0,98.0),(28.0,75.0),(60.0,75.0),(60.0,38.0),land['CM5_GBE_TD3_P']],
          'CM5_GBE_TD3_N':[(32.96,99.50),(27.0,99.5),(27.0,75.4),(60.5,75.4),(60.5,38.4),land['CM5_GBE_TD3_N']],
          'CM5_GBE_TD2_N':[(32.96,100.30),(26.0,101.5),(26.0,76.0),(62.0,76.0),(62.0,39.0),land['CM5_GBE_TD2_N']],
          'CM5_GBE_TD2_P':[(32.96,100.70),(25.0,103.0),(25.0,76.4),(62.5,76.4),(62.5,39.4),land['CM5_GBE_TD2_P']],
          'CM5_GBE_TD1_P':[(36.04,99.10),(41.0,98.0),(41.0,78.0),(66.0,78.0),(66.0,38.0),land['CM5_GBE_TD1_P']],
          'CM5_GBE_TD1_N':[(36.04,99.50),(42.0,99.5),(42.0,78.4),(66.5,78.4),(66.5,38.4),land['CM5_GBE_TD1_N']],
          'CM5_GBE_TD0_N':[(36.04,100.30),(43.0,101.5),(43.0,79.0),(68.0,79.0),(68.0,39.0),land['CM5_GBE_TD0_N']],
          'CM5_GBE_TD0_P':[(36.04,100.70),(44.0,103.0),(44.0,79.4),(68.5,79.4),(68.5,39.4),land['CM5_GBE_TD0_P']]}
    if os.environ.get('PISXME_LANE_ORDER') == 'RIGHT_CHANNEL_WEST_SPLIT':
        # Keep the left and right source groups on independent B.Cu
        # approaches.  Their horizontal lanes do not pierce the other
        # group's vertical escape; both groups only share the separated top
        # corridor above the frozen power/cooler region.
        paths={
          'CM5_GBE_TD3_P':[(32.96,99.10),(28.0,98.0),(28.0,75.0),(15.0,75.0),(15.0,30.0),(260.0,30.0),land['CM5_GBE_TD3_P']],
          'CM5_GBE_TD3_N':[(32.96,99.50),(27.0,99.5),(27.0,75.4),(15.0,75.4),(15.0,30.5),(260.0,30.5),land['CM5_GBE_TD3_N']],
          'CM5_GBE_TD2_N':[(32.96,100.30),(26.0,101.5),(26.0,76.0),(15.0,76.0),(15.0,31.0),(260.0,31.0),land['CM5_GBE_TD2_N']],
          'CM5_GBE_TD2_P':[(32.96,100.70),(25.0,103.0),(25.0,76.4),(15.0,76.4),(15.0,31.5),(260.0,31.5),land['CM5_GBE_TD2_P']],
          'CM5_GBE_TD1_P':[(36.04,99.10),(41.0,98.0),(41.0,78.0),(60.0,78.0),(60.0,32.0),(270.0,32.0),land['CM5_GBE_TD1_P']],
          'CM5_GBE_TD1_N':[(36.04,99.50),(42.0,99.5),(42.0,78.4),(60.0,78.4),(60.0,32.5),(270.0,32.5),land['CM5_GBE_TD1_N']],
          'CM5_GBE_TD0_N':[(36.04,100.30),(43.0,101.5),(43.0,79.0),(60.0,79.0),(60.0,33.0),(270.0,33.0),land['CM5_GBE_TD0_N']],
          'CM5_GBE_TD0_P':[(36.04,100.70),(44.0,103.0),(44.0,79.4),(60.0,79.4),(60.0,33.5),(270.0,33.5),land['CM5_GBE_TD0_P']]}
    if os.environ.get('PISXME_LANE_ORDER') == 'LOCAL_BOTTOM':
        # Pair-preserving source lanes descend below J7, then run beneath
        # the cooler reservation to the official ESD source-side lands.
        # The right group is intentionally kept as a separate trial because
        # its official ESD entry order differs from the CM5 source order.
        paths={
          'CM5_GBE_TD3_P':[(32.96,99.10),(25.0,99.10),(25.0,136.0),(70.0,140.0),(105.0,140.0),(118.604119,151.995)],
          'CM5_GBE_TD3_N':[(32.96,99.50),(24.5,99.50),(24.5,136.5),(70.5,140.5),(105.5,140.5),(118.761524,152.375)],
          'CM5_GBE_TD2_N':[(32.96,100.30),(24.0,100.30),(24.0,137.0),(71.0,141.0),(106.0,141.0),(119.421298,152.895)],
          'CM5_GBE_TD2_P':[(32.96,100.70),(23.5,100.70),(23.5,137.5),(71.5,141.5),(106.5,141.5),(119.578701,153.275)],
          'CM5_GBE_TD1_P':[(36.04,99.10),(45.0,99.10),(45.0,140.0),(90.0,140.0),(110.0,140.0),(125.060000,151.656297)],
          'CM5_GBE_TD1_N':[(36.04,99.50),(45.5,99.50),(45.5,140.5),(90.5,140.5),(110.5,140.5),(125.440000,151.813702)],
          'CM5_GBE_TD0_N':[(36.04,100.30),(46.0,100.30),(46.0,141.0),(91.0,141.0),(111.0,141.0),(126.560000,151.356297)],
          'CM5_GBE_TD0_P':[(36.04,100.70),(46.5,100.70),(46.5,141.5),(91.5,141.5),(111.5,141.5),(126.940000,151.513702)]}
    if os.environ.get('PISXME_LANE_ORDER') == 'LOCAL_BOTTOM_SPLIT':
        paths={
          'CM5_GBE_TD3_P':[(32.96,99.10),(25.0,99.10),(25.0,136.0),(70.0,140.0),(105.0,140.0),(118.604119,151.995)],
          'CM5_GBE_TD3_N':[(32.96,99.50),(24.5,99.50),(24.5,136.5),(70.5,140.5),(105.5,140.5),(118.761524,152.375)],
          'CM5_GBE_TD2_N':[(32.96,100.30),(24.0,100.30),(24.0,137.0),(71.0,141.0),(106.0,141.0),(119.421298,152.895)],
          'CM5_GBE_TD2_P':[(32.96,100.70),(23.5,100.70),(23.5,137.5),(71.5,141.5),(106.5,141.5),(119.578701,153.275)],
          'CM5_GBE_TD1_P':[(36.04,99.10),(45.0,99.10),(45.0,136.0),(90.0,140.0),(110.0,140.0),(125.060000,151.656297)],
          'CM5_GBE_TD1_N':[(36.04,99.50),(45.5,99.50),(45.5,136.5),(90.5,140.5),(110.5,140.5),(125.440000,151.813702)],
          'CM5_GBE_TD0_N':[(36.04,100.30),(46.0,100.30),(46.0,137.0),(91.0,141.0),(111.0,141.0),(126.560000,151.356297)],
          'CM5_GBE_TD0_P':[(36.04,100.70),(46.5,100.70),(46.5,137.5),(91.5,141.5),(111.5,141.5),(126.940000,151.513702)]}
    if os.environ.get('PISXME_LANE_ORDER') == 'ROTATED_LOCAL':
        paths={
          'CM5_GBE_TD3_P':[(32.96,99.10),(24.0,99.10),(24.0,136.0),(75.0,140.0),(105.0,140.0),land['CM5_GBE_TD3_P']],
          'CM5_GBE_TD3_N':[(32.96,99.50),(24.5,99.50),(24.5,136.5),(75.5,140.5),(105.5,140.5),land['CM5_GBE_TD3_N']],
          'CM5_GBE_TD2_N':[(32.96,100.30),(25.0,100.30),(25.0,137.0),(76.0,141.0),(106.0,141.0),land['CM5_GBE_TD2_N']],
          'CM5_GBE_TD2_P':[(32.96,100.70),(25.5,100.70),(25.5,137.5),(76.5,141.5),(106.5,141.5),land['CM5_GBE_TD2_P']],
          'CM5_GBE_TD1_P':[(36.04,99.10),(45.0,99.10),(45.0,136.0),(85.0,145.0),(105.0,145.0),land['CM5_GBE_TD1_P']],
          'CM5_GBE_TD1_N':[(36.04,99.50),(45.5,99.50),(45.5,136.5),(85.5,145.5),(105.5,145.5),land['CM5_GBE_TD1_N']],
          'CM5_GBE_TD0_N':[(36.04,100.30),(46.0,100.30),(46.0,137.0),(86.0,146.0),(106.0,146.0),land['CM5_GBE_TD0_N']],
          'CM5_GBE_TD0_P':[(36.04,100.70),(46.5,100.70),(46.5,137.5),(86.5,146.5),(106.5,146.5),land['CM5_GBE_TD0_P']]}
    staggered=os.environ.get('PISXME_LANE_ORDER')=='RIGHT_CHANNEL_STAGGERED'
    west_split=os.environ.get('PISXME_LANE_ORDER')=='RIGHT_CHANNEL_WEST_SPLIT'
    if staggered or west_split:
        return_v={
          'CM5_GBE_TD3_P':(260.0,33.0),'CM5_GBE_TD3_N':(260.0,34.5),
          'CM5_GBE_TD2_N':(260.0,36.0),'CM5_GBE_TD2_P':(260.0,37.5),
          'CM5_GBE_TD1_P':(270.0,33.0),'CM5_GBE_TD1_N':(270.0,34.5),
          'CM5_GBE_TD0_N':(270.0,36.0),'CM5_GBE_TD0_P':(270.0,37.5)}
        for name,pts in paths.items():
            end=(land[name][0]+DX,land[name][1]+DY)
            source_v=pts[1]
            add(b,nets[name],[pts[0],source_v],pcbnew.F_Cu)
            via(b,nets[name],source_v)
            rv=return_v[name]
            if west_split:
                add(b,nets[name],[source_v,*pts[2:6],rv],pcbnew.B_Cu)
            else:
                entry,lane,corridor=pts[2:5]
                add(b,nets[name],[source_v,entry,lane,corridor,rv],pcbnew.B_Cu)
            via(b,nets[name],rv)
            add(b,nets[name],[rv,end],pcbnew.F_Cu)
        b.Save(str(OUT)); print('saved',OUT); return
    split=os.environ.get('PISXME_LANE_ORDER') in ('LOCAL_BOTTOM_SPLIT','ROTATED_LOCAL')
    if split:
        # Immediate source transitions keep long Ethernet legs off the
        # frozen F.Cu power/regulator copper.  Left TD3/TD2 and right TD0
        # use B.Cu corridors; right TD1 returns to F.Cu for the official
        # ESD landing corridor.  Every transition is outside a pad.
        for name,pts in paths.items():
            end=(land[name][0]+DX,land[name][1]+DY)
            x,y=pts[0]; source_v=pts[1]; entry=pts[2]
            add(b,nets[name],[(x,y),source_v])
            via(b,nets[name],source_v)
            is_fcu=name in ('CM5_GBE_TD1_P','CM5_GBE_TD1_N','CM5_GBE_TD0_P','CM5_GBE_TD0_N') if os.environ.get('PISXME_LANE_ORDER') == 'ROTATED_LOCAL' else name in ('CM5_GBE_TD1_P','CM5_GBE_TD1_N')
            add(b,nets[name],[source_v,entry],pcbnew.B_Cu)
            via(b,nets[name],entry)
            if is_fcu:
                add(b,nets[name],[entry,pts[3],pts[4],end],pcbnew.F_Cu)
            else:
                add(b,nets[name],[entry,pts[3],pts[4]],pcbnew.B_Cu)
                vend=(end[0]-1.5,end[1]-0.6)
                add(b,nets[name],[pts[4],vend],pcbnew.B_Cu)
                via(b,nets[name],vend)
                add(b,nets[name],[vend,end],pcbnew.F_Cu)
        b.Save(str(OUT)); print('saved',OUT); return
    bcu=os.environ.get('PISXME_BCU_ESCAPE')=='1'
    for name,pts in paths.items():
        end=(land[name][0]+DX,land[name][1]+DY)
        if not bcu:
            add(b,nets[name],pts[:-1]+[end])
            continue
        # Keep only the pad breakout on F.Cu, then use a pair-preserving
        # B.Cu corridor around the fixed J7 body. Both transitions are
        # outside pads; the endpoint via lands on the short official USON
        # graph rather than placing via-in-pad.
        start=pts[2]
        add(b,nets[name],pts[:3])
        via(b,nets[name],start)
        via_end=(end[0],end[1]+0.75)
        add(b,nets[name],[start,via_end],pcbnew.B_Cu)
        via(b,nets[name],via_end)
        add(b,nets[name],[via_end,end])
    b.Save(str(OUT)); print('saved',OUT)
if __name__=='__main__': main()
