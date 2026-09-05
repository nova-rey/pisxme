"""Apply a serialized official CM5IO MDI geometry snapshot to acreage."""
from pathlib import Path
import json
import os
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=Path(os.environ.get('PISXME_BASE',ROOT/'ACREAGE_EDAC_CORRECTED_PHASE17.kicad_pcb'))
GEOM=ROOT/'cm5io_mdi_geometry.json'
OUT=Path(os.environ.get('PISXME_OUT',ROOT/'ACREAGE_CM5IO_EDAC_CORRECTED_PHASE17.kicad_pcb'))
DX=5.0
DY=float(os.environ.get('PISXME_DY','0'))
MDI=tuple(f'CM5_GBE_TD{i}_{p}' for i in range(4) for p in 'PN')
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def main():
    rows=json.loads(GEOM.read_text())
    b=pcbnew.LoadBoard(str(BASE))
    # Resolve net codes before footprint transforms; KiCad 10's SWIG binding
    # can expose FindNet results as opaque wrappers after footprint edits.
    netcodes={name:b.FindNet(name).GetNetCode() for name in MDI}
    # The clean schematic/footprint authority maps U6=TD0/TD1 and
    # U9=TD2/TD3.  The official CM5IO escape reaches the opposite USON
    # channel side after the 180-degree board transform, so the local
    # footprint must be 270 degrees here; assigning swapped net labels to a
    # 90-degree footprint would make the fixture appear to pass while
    # violating the clean pin-to-pad authority.
    for ref,pos,rot in (('U6',(76.1+DX,65.215),270),('U9',(70.1+DX,65.215),270),('J2',(72.5+DX,53),180)):
        f=b.FindFootprintByReference(ref)
        if f is None: raise RuntimeError(ref)
        f.SetPosition(V(pos[0],pos[1]+DY)); f.SetOrientationDegrees(rot)
    for item in list(b.GetTracks()):
        if str(item.GetNetname()).rsplit('/',1)[-1] in MDI: b.Remove(item)
    for row in rows:
        if row['net'] not in netcodes: raise RuntimeError(row['net'])
        q=pcbnew.PCB_TRACK(b); q.SetStart(V(row['a'][0]+DX,row['a'][1]+DY)); q.SetEnd(V(row['z'][0]+DX,row['z'][1]+DY))
        q.SetLayer(row['layer']); q.SetWidth(pcbnew.FromMM(row['width'])); q.SetNetCode(netcodes[row['net']]); b.Add(q)
    # When the official corridor is translated vertically to clear the
    # regulator island, bridge its source-side endpoints to the fixed J7
    # contacts with short, same-net F.Cu dogbones.  The source endpoint is
    # selected from the serialized oracle, not synthesized from a new pair
    # ordering.
    source_pads={
        'CM5_GBE_TD3_P':(32.96,99.10),'CM5_GBE_TD3_N':(32.96,99.50),
        'CM5_GBE_TD2_N':(32.96,100.30),'CM5_GBE_TD2_P':(32.96,100.70),
        'CM5_GBE_TD1_P':(36.04,99.10),'CM5_GBE_TD1_N':(36.04,99.50),
        'CM5_GBE_TD0_N':(36.04,100.30),'CM5_GBE_TD0_P':(36.04,100.70)}
    for name,pad in source_pads.items():
        target=(pad[0]-DX,pad[1])
        points=[]
        for row in rows:
            if row['net'] != name: continue
            for key in ('a','z'):
                point=row[key]
                if point[1] > 90: points.append(point)
        if not points: raise RuntimeError('no source endpoint '+name)
        point=min(points,key=lambda p:(p[0]-target[0])**2+(p[1]-target[1])**2)
        q=pcbnew.PCB_TRACK(b); q.SetStart(V(*pad)); q.SetEnd(V(point[0]+DX,point[1]+DY))
        q.SetLayer(pcbnew.F_Cu); q.SetWidth(pcbnew.FromMM(.127)); q.SetNetCode(netcodes[name]); b.Add(q)
    b.Save(str(OUT)); print('saved',OUT)
if __name__=='__main__': main()
