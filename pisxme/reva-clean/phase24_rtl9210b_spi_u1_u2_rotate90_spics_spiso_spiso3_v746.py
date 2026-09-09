"""V746: early SPISO handoff plus separate B.Cu SPISO3 corridor."""
from pathlib import Path
import pcbnew
H = Path(__file__).resolve().parent
BASE = H / 'PHASE24_RTL9210B_SPI_U1_ROTATE90_PROBE_V730.kicad_pcb'
OUT = H / 'PHASE24_RTL9210B_SPI_U1_ROTATE90_SPICS_SPISO_SPISO3_V746.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.20)
def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def tr(b, n, layer, a, z):
    q = pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
    q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b, n, a):
    q = pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.60))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(n)
    q.SetNetCode(n.GetNetCode()); b.Add(q)
def chain(b, n, layer, pts):
    for a, z in zip(pts, pts[1:]): tr(b, n, layer, a, z)
b = pcbnew.LoadBoard(str(BASE))

# SPICS: retained clean F.Cu outer-channel path.
n = b.FindNet('SPICS')
chain(b, n, F, [(98.8,66.05),(98.8,63.5),(104.0,63.5),(104.0,80.0),(105.0,80.0)])

# SPISO: move the handoff ahead of the SPISO3 source escape; remain on its
# own B.Cu vertical shelf and return at the U2 endpoint.
n = b.FindNet('SPISO')
chain(b, n, F, [(99.2,66.05),(99.2,64.0)])
via(b, n, (99.2,64.0))
chain(b, n, B, [(99.2,64.0),(102.5,64.0),(102.5,81.5),(106.2,81.5)])
via(b, n, (106.2,81.5))
chain(b, n, F, [(106.2,81.5),(106.2,80.0)])

# SPISO3: short F.Cu source escape, then a dedicated B.Cu shelf above the
# SPISO endpoint corridor and a separate return dogbone.
n = b.FindNet('SPISO3')
chain(b, n, F, [(99.6,66.05),(99.6,61.5)])
via(b, n, (99.6,61.5))
chain(b, n, B, [(99.6,61.5),(112.2,61.5),(112.2,82.5)])
via(b, n, (112.2,82.5))
chain(b, n, F, [(112.2,82.5),(112.2,80.0)])

b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT))
print(OUT)
