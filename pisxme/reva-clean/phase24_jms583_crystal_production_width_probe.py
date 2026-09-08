"""Disposable JMS583 crystal escape with the active 0.20 mm route width."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb"
OUT = R / "PHASE24_JMS583_CRYSTAL_PRODUCTION_WIDTH_PROBE.kicad_pcb"
def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def add(b, net, layer, a, z):
    t = pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z));
    t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(0.20)); t.SetNet(net)
    t.SetNetCode(net.GetNetCode()); b.Add(t)
def via(b, net, p):
    v = pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(0.50))
    v.SetDrill(pcbnew.FromMM(0.30)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    v.SetNet(net); v.SetNetCode(net.GetNetCode()); b.Add(v)
b = pcbnew.LoadBoard(str(BASE)); u = b.FindFootprintByReference("U11")
y = b.FindFootprintByReference("Y10"); y.SetPosition(P(150, 125))
for name, up, yp, fp, bp in (
    ("XIN", "50", "1", ((137.4,129.0),(134.0,129.0)), ((147.0,129.0),(147.0,122.0))),
    ("XOUT", "51", "2", ((137.8,128.0),(140.0,128.0)), ((146.0,128.0),(146.0,123.0))),
):
    n = b.FindNet(name)
    for item in list(b.GetTracks()):
        if item.GetNetCode() == n.GetNetCode(): b.RemoveNative(item)
    src = u.FindPadByNumber(up).GetPosition(); dst = y.FindPadByNumber(yp).GetPosition()
    f = [pcbnew.ToMM(src.x), pcbnew.ToMM(src.y)]
    add(b,n,pcbnew.F_Cu,tuple(f),fp[0]); add(b,n,pcbnew.F_Cu,fp[0],fp[1]); via(b,n,fp[1])
    add(b,n,pcbnew.B_Cu,fp[1],bp[0]); add(b,n,pcbnew.B_Cu,bp[0],bp[1]); via(b,n,bp[1])
    add(b,n,pcbnew.F_Cu,bp[1],(pcbnew.ToMM(dst.x),pcbnew.ToMM(dst.y)))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
