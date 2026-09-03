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
if os.environ.get('PISXME_LANE_ORDER') == 'TD3_OUTER':
    OUT=ROOT/'ACREAGE_CM5IO_TOP_ISLAND_TD3_OUTER_PHASE17.kicad_pcb'

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
    for ref,pos,rot in (('U6',(33.6,57.215),270),('U9',(27.6,57.215),270),('J2',(30,45),180)):
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
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(a[0]+DX,a[1]+DY)); t.SetEnd(V(z[0]+DX,z[1]+DY))
        t.SetLayer(r['layer']); t.SetWidth(pcbnew.FromMM(r['width'])); t.SetNetCode(nets[r['net']].GetNetCode()); b.Add(t)
    # Landing points are the ESD-side endpoints of the omitted official legs.
    land={
      'CM5_GBE_TD3_P':(68.704119,67.210), 'CM5_GBE_TD3_N':(68.861524,67.590),
      'CM5_GBE_TD2_N':(69.521298,68.110), 'CM5_GBE_TD2_P':(69.678701,68.490),
      'CM5_GBE_TD1_P':(75.16,66.871297), 'CM5_GBE_TD1_N':(75.539999,67.028702),
      'CM5_GBE_TD0_N':(76.66,66.571298), 'CM5_GBE_TD0_P':(77.039999,66.728702)}
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
