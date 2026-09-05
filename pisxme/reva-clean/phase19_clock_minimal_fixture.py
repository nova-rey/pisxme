"""Minimal native KiCad fixture for the TUSB9261 crystal clock network."""
from pathlib import Path
import os
import sys
import pcbnew

for _arg in sys.argv[1:]:
    if _arg.startswith('--') and '=' in _arg:
        _key,_value=_arg[2:].split('=',1); os.environ[_key.replace('-','_')]=_value
R=Path(__file__).resolve().parent; KEEP_BOARD=os.environ.get('CLOCK_ACREAGE')=='1'
BASE=R/os.environ.get('CLOCK_BASE','ACREAGE_CLOCK_CANDIDATE5.kicad_pcb')
OUT=R/os.environ.get('CLOCK_OUT',('PHASE19_CLOCK_ACREAGE_RELATIVE.kicad_pcb' if KEEP_BOARD else 'PHASE19_CLOCK_MINIMAL_FIXTURE.kicad_pcb'))
DX,DY=((int(os.environ.get('CLOCK_DX','150')),int(os.environ.get('CLOCK_DY','5'))) if KEEP_BOARD else (0,0))
MIRROR=os.environ.get('CLOCK_MIRROR')=='1'
ROT=int(os.environ.get('CLOCK_ROTATE','0'))
TX=float(os.environ.get('CLOCK_TARGET_X','140')); TY=float(os.environ.get('CLOCK_TARGET_Y','130'))
def TF(p):
    if ROT==90: return (TX-(p[1]-100), TY+(p[0]-100))
    return ((240-p[0],210-p[1]) if MIRROR else (p[0]+DX,p[1]+DY))
def LOCAL(p):
    if ROT==90: return (100+(p[1]-TY), 100-(p[0]-TX))
    return (TF(p) if MIRROR else (p[0]-DX,p[1]-DY))
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def T(b,n,a,z,l):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*TF(a))); t.SetEnd(V(*TF(z))); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); b.Add(t)
def X(b,n,p):
    v=pcbnew.PCB_VIA(b); v.SetPosition(V(*TF(p))); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
def xy(p): return (pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y))
def main():
    b=pcbnew.LoadBoard(str(BASE)); keep={'U7','Y1','R23','C42','C43'}
    footprints=list(b.GetFootprints()); tracks=list(b.GetTracks()); zones=list(b.Zones())
    if not KEEP_BOARD:
        for f in footprints:
            if f.GetReference() not in keep: b.Remove(f)
        for t in tracks: b.Remove(t)
        for z in zones: b.Remove(z)
    u=b.FindFootprintByReference('U7')
    if not KEEP_BOARD: u.SetPosition(V(100,100)); u.SetOrientationDegrees(0)
    if KEEP_BOARD:
        io=pcbnew.PCB_IO_KICAD_SEXPR()
        for ref,lib in (('Y1','Crystal_3225_4Pad'),('R23','R_0402_1005Metric'),('C42','C_0402_1005Metric'),('C43','C_0402_1005Metric')):
            if b.FindFootprintByReference(ref) is None:
                f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),lib); f.SetReference(ref); b.Add(f)
    _support_rot = 90 if ROT==90 else 0
    placements={'Y1':(TF((100,115)),_support_rot),'R23':(TF((100,125)),_support_rot),'C42':(TF((94,125)),_support_rot),'C43':(TF((106,125)),_support_rot)}
    maps={'Y1':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC','3':'/STORAGE/BRIDGE_XO','4':'/STORAGE/BRIDGE_VSSOSC'},'R23':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_XO'},'C42':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC'},'C43':{'1':'/STORAGE/BRIDGE_XO','2':'/STORAGE/BRIDGE_VSSOSC'}}
    nets={x:b.FindNet(x) for x in ('/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC')}
    for name in tuple(nets):
        if nets[name] is None:
            nets[name]=pcbnew.NETINFO_ITEM(b,name); nets[name].SetNetCode(b.GetNetCount()+1); b.Add(nets[name])
    if KEEP_BOARD:
        clock_codes={n.GetNetCode() for n in nets.values()}
        for t in list(b.GetTracks()):
            if t.GetNetCode() in clock_codes: b.Remove(t)
    for ref,(p,rot) in placements.items():
        f=b.FindFootprintByReference(ref); f.SetPosition(V(*p)); f.SetOrientationDegrees(rot)
        for q in f.Pads():
            n=nets[maps[ref][str(q.GetNumber())]]; q.SetNet(n); q.SetNetCode(n.GetNetCode())
    for pin,name in (('52','/STORAGE/BRIDGE_XI'),('53','/STORAGE/BRIDGE_VSSOSC'),('54','/STORAGE/BRIDGE_XO')):
        q=next(q for q in u.Pads() if str(q.GetNumber())==pin); q.SetNet(nets[name]); q.SetNetCode(nets[name].GetNetCode())
    xi,xo,vs=(nets[x] for x in ('/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC'))
    # Serialized U7 clock row at this placement: 52=(97,104.5),
    # 53=(97.5,104.5), 54=(98,104.5). Leave the row perpendicular-first.
    T(b,xi,(97,104.5),(97,112),pcbnew.F_Cu); T(b,xi,(97,112),(96,114.5),pcbnew.F_Cu); T(b,xi,(96,114.5),(98.9,114.15),pcbnew.F_Cu)
    T(b,xi,(98.9,114.15),(97.5,114.15),pcbnew.F_Cu); T(b,xi,(97.5,114.15),(97.5,123),pcbnew.F_Cu); T(b,xi,(97.5,123),(99.5,125),pcbnew.F_Cu); T(b,xi,(98.9,114.15),(96,114.15),pcbnew.F_Cu); T(b,xi,(96,114.15),(93.5,125),pcbnew.F_Cu)
    T(b,xo,(98,104.5),(98,111),pcbnew.F_Cu); T(b,xo,(98,111),(99.5,111),pcbnew.F_Cu); X(b,xo,(99.5,111)); T(b,xo,(99.5,111),(102,116.5),pcbnew.B_Cu); X(b,xo,(102,116.5)); T(b,xo,(102,116.5),(101.1,115.85),pcbnew.F_Cu)
    T(b,xo,(101.1,115.85),(100.5,125),pcbnew.F_Cu); T(b,xo,(101.1,115.85),(105.5,125),pcbnew.F_Cu)
    # VSSOSC is a private B.Cu return. Vias are deliberately outside all SMD pads.
    T(b,vs,(97.5,104.5),(97.5,113.5),pcbnew.F_Cu); X(b,vs,(97.5,113.5)); T(b,vs,(97.5,113.5),(94.5,128),pcbnew.B_Cu); T(b,vs,(94.5,128),(106.5,128),pcbnew.B_Cu)
    for p in ((99.5,117.0),(103.5,116.5),(94.5,126.2),(106.5,126.2)):
        X(b,vs,p)
        T(b,vs,p,(p[0],128),pcbnew.B_Cu)
    # Short top-side dogbones from the B.Cu VSSOSC corridor to each pad.
    f=b.FindFootprintByReference('Y1'); yp={str(q.GetNumber()):xy(q) for q in f.Pads()}
    T(b,vs,(99.5,117.0),LOCAL(yp['2']),pcbnew.F_Cu); T(b,vs,(103.5,116.5),LOCAL(yp['4']),pcbnew.F_Cu)
    f=b.FindFootprintByReference('C42'); cp={str(q.GetNumber()):xy(q) for q in f.Pads()}; T(b,vs,(94.5,126.2),LOCAL(cp['2']),pcbnew.F_Cu)
    f=b.FindFootprintByReference('C43'); cp={str(q.GetNumber()):xy(q) for q in f.Pads()}; T(b,vs,(106.5,126.2),LOCAL(cp['2']),pcbnew.F_Cu)
    # FREQSEL0/FREQSEL1 are both high in the authoritative 40 MHz mode.
    v33=b.FindNet('/STORAGE/BRIDGE_3V3')
    p30=next(q for q in u.Pads() if str(q.GetNumber())=='30'); p31=next(q for q in u.Pads() if str(q.GetNumber())=='31'); p24=next(q for q in u.Pads() if str(q.GetNumber())=='24')
    for q in (p30,p31,p24): q.SetNet(v33); q.SetNetCode(v33.GetNetCode())
    T(b,v33,(98,95.5),(97.5,95.5),pcbnew.F_Cu); T(b,v33,(98,95.5),(98,93.5),pcbnew.F_Cu); T(b,v33,(98,93.5),(101,93.5),pcbnew.F_Cu); T(b,v33,(101,93.5),(101,95.5),pcbnew.F_Cu)
    b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
