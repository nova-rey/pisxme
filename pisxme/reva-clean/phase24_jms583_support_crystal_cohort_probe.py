"""Combine the retained JMS583 support cohort with its production-width crystal."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_JMS583_SUPPORT_COHORT_GROUND_FILLED_V2.kicad_pcb"
OUT = R / "PHASE24_JMS583_SUPPORT_CRYSTAL_COHORT.kicad_pcb"
def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def seg(b, n, layer, a, z):
    t = pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z))
    t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(0.20)); t.SetNet(n)
    t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b, n, p):
    v = pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(0.50))
    v.SetDrill(pcbnew.FromMM(0.30)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b = pcbnew.LoadBoard(str(BASE))
u = b.FindFootprintByReference("U11"); y = b.FindFootprintByReference("Y10")
y.SetPosition(P(150, 125))
for name, up, yp, fp, bp in (
    ("XIN", "50", "1", [(137.4,129), (134,129)], [(147,129), (147,122)]),
    ("XOUT", "51", "2", [(137.8,128), (140,128)], [(146,128), (146,123)]),
):
    n = b.FindNet(name)
    for item in list(b.GetTracks()):
        if item.GetNetCode() == n.GetNetCode(): b.RemoveNative(item)
    s = u.FindPadByNumber(up).GetPosition(); d = y.FindPadByNumber(yp).GetPosition()
    src = (pcbnew.ToMM(s.x), pcbnew.ToMM(s.y)); dst = (pcbnew.ToMM(d.x), pcbnew.ToMM(d.y))
    seg(b, n, pcbnew.F_Cu, src, fp[0]); seg(b, n, pcbnew.F_Cu, fp[0], fp[1]); via(b, n, fp[1])
    seg(b, n, pcbnew.B_Cu, fp[1], bp[0]); seg(b, n, pcbnew.B_Cu, bp[0], bp[1]); via(b, n, bp[1])
    seg(b, n, pcbnew.F_Cu, bp[1], dst)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
