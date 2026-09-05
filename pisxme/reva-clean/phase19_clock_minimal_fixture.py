"""Minimal native KiCad fixture for the TUSB9261 crystal clock network."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent; BASE=R/'ACREAGE_CLOCK_CANDIDATE5.kicad_pcb'; OUT=R/'PHASE19_CLOCK_MINIMAL_FIXTURE.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def T(b,n,a,z,l):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); b.Add(t)
def X(b,n,p):
    v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
def xy(p): return (pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y))
def main():
    b=pcbnew.LoadBoard(str(BASE)); keep={'U7','Y1','R23','C42','C43'}
    footprints=list(b.GetFootprints()); tracks=list(b.GetTracks()); zones=list(b.Zones())
    for f in footprints:
        if f.GetReference() not in keep: b.Remove(f)
    for t in tracks: b.Remove(t)
    for z in zones: b.Remove(z)
    u=b.FindFootprintByReference('U7'); u.SetPosition(V(100,100)); u.SetOrientationDegrees(0)
    placements={'Y1':((100,115),0),'R23':((100,125),0),'C42':((94,125),0),'C43':((106,125),0)}
    maps={'Y1':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC','3':'/STORAGE/BRIDGE_XO','4':'/STORAGE/BRIDGE_VSSOSC'},'R23':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_XO'},'C42':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC'},'C43':{'1':'/STORAGE/BRIDGE_XO','2':'/STORAGE/BRIDGE_VSSOSC'}}
    nets={x:b.FindNet(x) for x in ('/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC')}
    for ref,(p,rot) in placements.items():
        f=b.FindFootprintByReference(ref); f.SetPosition(V(*p)); f.SetOrientationDegrees(rot)
        for q in f.Pads():
            n=nets[maps[ref][str(q.GetNumber())]]; q.SetNet(n); q.SetNetCode(n.GetNetCode())
    for pin,name in (('52','/STORAGE/BRIDGE_XI'),('53','/STORAGE/BRIDGE_VSSOSC'),('54','/STORAGE/BRIDGE_XO')):
        q=next(q for q in u.Pads() if str(q.GetNumber())==pin); q.SetNet(nets[name]); q.SetNetCode(nets[name].GetNetCode())
    xi,xo,vs=(nets[x] for x in ('/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC'))
    # Serialized U7 clock row at this placement: 52=(97,104.5),
    # 53=(97.5,104.5), 54=(98,104.5). Leave the row perpendicular-first.
    T(b,xi,(97,104.5),(97,112),pcbnew.F_Cu); T(b,xi,(97,112),(98.9,114.15),pcbnew.F_Cu)
    T(b,xi,(98.9,114.15),(97.5,114.15),pcbnew.F_Cu); T(b,xi,(97.5,114.15),(97.5,123),pcbnew.F_Cu); T(b,xi,(97.5,123),(99.5,125),pcbnew.F_Cu); T(b,xi,(97,112),(95,112),pcbnew.F_Cu); T(b,xi,(95,112),(93.5,125),pcbnew.F_Cu)
    T(b,xo,(98,104.5),(98,111),pcbnew.F_Cu); T(b,xo,(98,111),(102,111),pcbnew.F_Cu); T(b,xo,(102,111),(102,115.85),pcbnew.F_Cu); T(b,xo,(102,115.85),(101.1,115.85),pcbnew.F_Cu)
    T(b,xo,(101.1,115.85),(100.5,125),pcbnew.F_Cu); T(b,xo,(101.1,115.85),(105.5,125),pcbnew.F_Cu)
    # VSSOSC is a private B.Cu return. Vias are deliberately outside all SMD pads.
    T(b,vs,(97.5,104.5),(97.5,113.5),pcbnew.F_Cu); X(b,vs,(97.5,113.5)); T(b,vs,(97.5,113.5),(92,128),pcbnew.B_Cu); T(b,vs,(92,128),(108,128),pcbnew.B_Cu)
    for p in ((100.5,117.0),(103.5,116.5),(94.5,126.2),(106.5,126.2)):
        X(b,vs,p)
        T(b,vs,p,(p[0],128),pcbnew.B_Cu)
    # Short top-side dogbones from the B.Cu VSSOSC corridor to each pad.
    f=b.FindFootprintByReference('Y1'); yp={str(q.GetNumber()):xy(q) for q in f.Pads()}
    T(b,vs,(100.5,117.0),yp['2'],pcbnew.F_Cu); T(b,vs,(103.5,116.5),yp['4'],pcbnew.F_Cu)
    f=b.FindFootprintByReference('C42'); cp={str(q.GetNumber()):xy(q) for q in f.Pads()}; T(b,vs,(94.5,126.2),cp['2'],pcbnew.F_Cu)
    f=b.FindFootprintByReference('C43'); cp={str(q.GetNumber()):xy(q) for q in f.Pads()}; T(b,vs,(106.5,126.2),cp['2'],pcbnew.F_Cu)
    b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
