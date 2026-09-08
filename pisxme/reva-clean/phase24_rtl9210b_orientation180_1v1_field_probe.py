"""Disposable coordinated RTL_1V1 perimeter field on the V631 rail basis."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / 'PHASE24_RTL9210B_ORIENTATION180_RAILS_PROBE_V7.kicad_pcb'
OUT = H / 'PHASE24_RTL9210B_ORIENTATION180_1V1_FIELD_PROBE.kicad_pcb'
F, B, W = pcbnew.F_Cu, pcbnew.B_Cu, pcbnew.FromMM(.20)
def p(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def s(b, n, l, a, z):
    t = pcbnew.PCB_TRACK(b); t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(l)
    t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def v(b, n, q):
    x = pcbnew.PCB_VIA(b); x.SetPosition(p(*q)); x.SetWidth(pcbnew.FromMM(.60))
    x.SetDrill(pcbnew.FromMM(.30)); x.SetLayerPair(F, B); x.SetNet(n); x.SetNetCode(n.GetNetCode()); b.Add(x)

b = pcbnew.LoadBoard(str(BASE)); n = b.FindNet('RTL_1V1')
# All source departures are allocated before joining on a B.Cu collector.
paths = [
    ((95.20,66.05), [(93.00,66.05),(93.00,85.00)]),
    ((94.05,69.60), [(92.00,69.60),(92.00,85.00)]),
    ((95.20,73.95), [(94.00,75.00),(94.00,85.00)]),
    ((96.80,73.95), [(96.80,78.00),(96.80,85.00)]),
    ((100.80,73.95), [(100.80,78.00),(100.80,85.00)]),
    ((101.95,72.00), [(103.00,72.00),(103.00,85.00)]),
    ((101.95,70.00), [(105.00,70.00),(105.00,85.00)]),
    ((101.95,68.80), [(106.00,68.80),(106.00,85.00)]),
]
for src, points in paths:
    last = src
    for q in points: s(b,n,F,last,q); last=q
    v(b,n,last)
s(b,n,B,(92.00,85.00),(106.00,85.00)); v(b,n,(104.00,85.00))
s(b,n,F,(104.00,85.00),(104.00,82.00))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
