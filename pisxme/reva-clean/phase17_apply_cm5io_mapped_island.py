"""Apply the CM5IO MDI geometry using the corrected EDAC physical aliases."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_EDAC_CORRECTED_PHASE17.kicad_pcb'
FIX=ROOT/'CM5IO_PISXME_ETHERNET_TRANSPLANT_FIXTURE.kicad_pcb'
OUT=ROOT/'ACREAGE_CM5IO_MAPPED_CM5IO_PHASE17.kicad_pcb'
DX=5.0
MDI=tuple(f'CM5_GBE_TD{i}_{p}' for i in range(4) for p in 'PN')

def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def short(s): return str(s).rsplit('/',1)[-1]
def main():
    # Snapshot before loading the second board; KiCad's Python wrappers share
    # one active BOARD context.
    src=pcbnew.LoadBoard(str(FIX)); tracks=[]
    for item in src.GetTracks():
        n=short(item.GetNetname())
        if n in MDI:
            tracks.append((xy(item.GetStart()),xy(item.GetEnd()),item.GetLayer(),item.GetWidth(),n))
    b=pcbnew.LoadBoard(str(BASE))
    # Reuse the already-authoritative production footprints; only the local
    # Ethernet island is moved to the oracle's compact relative placement.
    # Preserve the validated official CM5IO ESD orientation.  The previous
    # 90-degree local rotation mirrored the USON pad fields relative to the
    # transplanted official tracks and manufactured false U6/U9 shorts.
    for ref,pos,rot in (('U9',(70.1+DX,65.215),270),('U6',(76.1+DX,65.215),270),
                        ('J2',(72.5+DX,53),180)):
        f=b.FindFootprintByReference(ref)
        if f is None: raise RuntimeError(ref)
        f.SetPosition(V(*pos)); f.SetOrientationDegrees(rot)
    nets={n:b.FindNet(n) for n in MDI}
    for item in list(b.GetTracks()):
        if short(item.GetNetname()) in MDI: b.Remove(item)
    for a,z,layer,width,n in tracks:
        q=pcbnew.PCB_TRACK(b)
        q.SetStart(V(a[0]+DX,a[1])); q.SetEnd(V(z[0]+DX,z[1])); q.SetLayer(layer)
        q.SetWidth(width); q.SetNet(nets[n]); b.Add(q)
    b.Save(str(OUT)); print('saved',OUT)
if __name__=='__main__': main()
