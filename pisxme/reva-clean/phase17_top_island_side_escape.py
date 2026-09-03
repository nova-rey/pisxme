"""Disposable Phase 17 trial: official CM5IO island with side escapes at J7."""
from pathlib import Path
import json
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_EDAC_CORRECTED_PHASE17.kicad_pcb'
GEOM=ROOT/'cm5io_mdi_geometry.json'
OUT=ROOT/'ACREAGE_CM5IO_TOP_ISLAND_SIDE_ESCAPE_PHASE17.kicad_pcb'
DX,DY=-42.5,-8.0

def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def add(b,n,pts):
    for a,z in zip(pts,pts[1:]):
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z));
        t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.127)); t.SetNetCode(n.GetNetCode()); b.Add(t)

def main():
    rows=json.loads(GEOM.read_text()); b=pcbnew.LoadBoard(str(BASE))
    nets={n:b.FindNet(n) for n in set(r['net'] for r in rows)}
    for n in nets.values():
        if n is None: raise RuntimeError('missing MDI net')
    for ref,pos,rot in (('U6',(45.6,57.215),270),('U9',(39.6,57.215),270),('J2',(42,45),180)):
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
      'CM5_GBE_TD3_P':[(32.96,99.10),(30.0,99.10),(24.0,97.0),(24.0,72.0),(26.204119,59.210)],
      'CM5_GBE_TD3_N':[(32.96,99.50),(29.5,99.50),(24.5,97.5),(24.5,71.5),(26.361524,59.590)],
      'CM5_GBE_TD2_N':[(32.96,100.30),(27.0,100.30),(25.0,98.0),(25.0,71.0),(27.021298,60.110)],
      'CM5_GBE_TD2_P':[(32.96,100.70),(26.5,100.70),(25.5,98.5),(25.5,70.5),(27.178701,60.490)],
      'CM5_GBE_TD1_P':[(36.04,99.10),(40.0,99.10),(39.0,97.0),(39.0,72.0),(32.66,58.871297)],
      'CM5_GBE_TD1_N':[(36.04,99.50),(40.5,99.50),(39.5,97.5),(39.5,71.5),(33.039999,59.028702)],
      'CM5_GBE_TD0_N':[(36.04,100.30),(41.0,100.30),(40.0,98.0),(40.0,71.0),(34.16,58.571298)],
      'CM5_GBE_TD0_P':[(36.04,100.70),(41.5,100.70),(40.5,98.5),(40.5,70.5),(34.539999,58.728702)]}
    for name,pts in paths.items():
        end=(land[name][0]+DX,land[name][1]+DY)
        add(b,nets[name],pts[:-1]+[end])
    b.Save(str(OUT)); print('saved',OUT)
if __name__=='__main__': main()
