"""Apply a serialized official CM5IO MDI geometry snapshot to acreage."""
from pathlib import Path
import json
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_EDAC_CORRECTED_PHASE17.kicad_pcb'
GEOM=ROOT/'cm5io_mdi_geometry.json'
OUT=ROOT/'ACREAGE_CM5IO_EDAC_CORRECTED_PHASE17.kicad_pcb'
DX=5.0
MDI=tuple(f'CM5_GBE_TD{i}_{p}' for i in range(4) for p in 'PN')
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def main():
    rows=json.loads(GEOM.read_text())
    b=pcbnew.LoadBoard(str(BASE))
    for ref,pos,rot in (('U6',(76.1+DX,65.215),90),('U9',(70.1+DX,65.215),90),('J2',(72.5+DX,53),180)):
        f=b.FindFootprintByReference(ref)
        if f is None: raise RuntimeError(ref)
        f.SetPosition(V(*pos)); f.SetOrientationDegrees(rot)
    for item in list(b.GetTracks()):
        if str(item.GetNetname()).rsplit('/',1)[-1] in MDI: b.Remove(item)
    for row in rows:
        n=b.FindNet(row['net'])
        if n is None: raise RuntimeError(row['net'])
        q=pcbnew.PCB_TRACK(b); q.SetStart(V(row['a'][0]+DX,row['a'][1])); q.SetEnd(V(row['z'][0]+DX,row['z'][1]))
        q.SetLayer(row['layer']); q.SetWidth(pcbnew.FromMM(row['width'])); q.SetNetCode(n.GetNetCode()); b.Add(q)
    b.Save(str(OUT)); print('saved',OUT)
if __name__=='__main__': main()
