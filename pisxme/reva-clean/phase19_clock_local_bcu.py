"""Phase 19 disposable local clock-island trial.

The TUSB9261 oscillator is a low-profile local support island.  This variant
keeps only perpendicular top-side dogbones at U7, then carries XI/XO/VSSOSC
on B.Cu to support footprints mounted on the underside.  It is deliberately
parameterized by board coordinates so it is not a PiSXMe-only hand edit.
"""
from pathlib import Path
import os, sys
import pcbnew

R = Path(__file__).resolve().parent
for arg in sys.argv[1:]:
    if arg.startswith('--') and '=' in arg:
        k, v = arg[2:].split('=', 1)
        os.environ[k.replace('-', '_')] = v
BASE = R / os.environ.get('CLOCK_BASE', 'PHASE19_COORDINATED_U7ROT270_RELATIVE2.kicad_pcb')
OUT = R / os.environ.get('CLOCK_OUT', 'PHASE19_CLOCK_LOCAL_BCU.kicad_pcb')
SX = float(os.environ.get('CLOCK_SUPPORT_X', '145'))
SY = float(os.environ.get('CLOCK_SUPPORT_Y', '125'))

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)
def track(b, n, a, z, layer):
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z));
    t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); b.Add(t)
def via(b, n, p):
    v = pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5));
    v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    v.SetNet(n); b.Add(v)

MAP = {
    'Y1': {'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC','3':'/STORAGE/BRIDGE_XO','4':'/STORAGE/BRIDGE_VSSOSC'},
    'R23': {'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_XO'},
    'C42': {'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC'},
    'C43': {'1':'/STORAGE/BRIDGE_XO','2':'/STORAGE/BRIDGE_VSSOSC'},
}

def main():
    b = pcbnew.LoadBoard(str(BASE))
    names = tuple(sorted({n for m in MAP.values() for n in m.values()}))
    nets = {n:b.FindNet(n) for n in names}
    for name in names:
        if nets[name] is None:
            nets[name] = pcbnew.NETINFO_ITEM(b, name)
            nets[name].SetNetCode(b.GetNetCount()+1); b.Add(nets[name])
    codes = {n.GetNetCode() for n in nets.values()}
    for t in list(b.GetTracks()):
        if t.GetNetCode() in codes: b.Remove(t)
    io = pcbnew.PCB_IO_KICAD_SEXPR()
    libs = {'Y1':'Crystal_3225_4Pad','R23':'R_0402_1005Metric','C42':'C_0402_1005Metric','C43':'C_0402_1005Metric'}
    positions = {'Y1':(SX,SY), 'R23':(SX+6,SY), 'C42':(SX,SY+6), 'C43':(SX+6,SY+6)}
    for ref, pos in positions.items():
        f = b.FindFootprintByReference(ref)
        if f is None:
            f = io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'), libs[ref]); f.SetReference(ref); b.Add(f)
        f.SetPosition(V(*pos)); f.SetOrientationDegrees(0); f.SetLayer(pcbnew.B_Cu)
        for p in f.Pads():
            n = nets[MAP[ref][str(p.GetNumber())]]; p.SetNet(n); p.SetNetCode(n.GetNetCode())
    u = b.FindFootprintByReference('U7')
    for pin, name in [('30','/STORAGE/BRIDGE_3V3'),('31','/STORAGE/BRIDGE_3V3'),('52','/STORAGE/BRIDGE_XI'),('53','/STORAGE/BRIDGE_VSSOSC'),('54','/STORAGE/BRIDGE_XO')]:
        p = next(p for p in u.Pads() if str(p.GetNumber()) == pin)
        n = b.FindNet(name)
        p.SetNet(n); p.SetNetCode(n.GetNetCode())
    xi, vs, xo = (nets[x] for x in ('/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_VSSOSC','/STORAGE/BRIDGE_XO'))
    # Exact live U7 rot270 clock row: XI=(155.5,137), VSSOSC=(155.5,137.5), XO=(155.5,138).
    # Three separated transitions exit perpendicular to the row before dropping to B.Cu.
    transitions = [(xi,137.0,(154,133)), (vs,137.5,(152,134)), (xo,138.0,(153,133.5))]
    for n, pad_y, p in transitions:
        # Leave the 0.5 mm-pitch row laterally first; a vertical segment
        # through the adjacent no-connect pads is not a legal QFN escape.
        track(b,n,(155.5,pad_y),(154.8,pad_y),pcbnew.F_Cu)
        track(b,n,(154.8,pad_y),p,pcbnew.F_Cu); via(b,n,p)
    pads = {ref:{str(p.GetNumber()):xy(p) for p in b.FindFootprintByReference(ref).Pads()} for ref in positions}
    # B.Cu monotonic corridors.  The oscillator is entered from opposite
    # sides of the crystal; VSSOSC takes a perimeter bus, avoiding the
    # tempting but non-planar three-net star through the pad field.
    track(b,xi,(154,133),(154,SY-1.1),pcbnew.B_Cu); track(b,xi,(154,SY-1.1),pads['Y1']['1'],pcbnew.B_Cu)
    track(b,xo,(153,133.5),(153,SY+1.1),pcbnew.B_Cu); track(b,xo,(153,SY+1.1),pads['Y1']['3'],pcbnew.B_Cu)
    track(b,vs,(152,134),(SX-3.0,SY+3.0),pcbnew.B_Cu); track(b,vs,(SX-3.0,SY+3.0),(SX-3.0,SY-3.0),pcbnew.B_Cu); track(b,vs,(SX-3.0,SY-3.0),pads['Y1']['2'],pcbnew.B_Cu); track(b,vs,pads['Y1']['2'],pads['Y1']['4'],pcbnew.B_Cu)
    track(b,xi,pads['Y1']['1'],pads['R23']['1'],pcbnew.B_Cu); track(b,xi,pads['Y1']['1'],pads['C42']['1'],pcbnew.B_Cu)
    track(b,xo,pads['Y1']['3'],pads['R23']['2'],pcbnew.B_Cu); track(b,xo,pads['Y1']['3'],pads['C43']['1'],pcbnew.B_Cu)
    track(b,vs,pads['Y1']['2'],pads['C42']['2'],pcbnew.B_Cu); track(b,vs,pads['Y1']['4'],pads['C43']['2'],pcbnew.B_Cu)
    # FREQSEL0/1 high; use live transformed pad locations and a short local loop.
    v33=b.FindNet('/STORAGE/BRIDGE_3V3'); p30=next(p for p in u.Pads() if str(p.GetNumber())=='30'); p31=next(p for p in u.Pads() if str(p.GetNumber())=='31')
    track(b,v33,xy(p30),(xy(p30)[0]-1,xy(p30)[1]),pcbnew.F_Cu); track(b,v33,(xy(p30)[0]-1,xy(p30)[1]),(xy(p31)[0]-1,xy(p31)[1]),pcbnew.F_Cu); track(b,v33,(xy(p31)[0]-1,xy(p31)[1]),xy(p31),pcbnew.F_Cu)
    b.Save(str(OUT)); print(OUT)
main()
