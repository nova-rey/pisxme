"""Disposable native STORAGE_3V3 trunk trial from regulator support to J3."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_STORAGE_CM5_USB4_MONOTONIC_V79_M2_POWER_OWNER.kicad_pcb"
OUT = R / "PHASE24_STORAGE_M2_POWER_TRUNK_V82.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
b = pcbnew.LoadBoard(str(BASE)); n = b.FindNet("STORAGE_3V3"); assert n
def tr(layer, pts, width=0.25):
    for a, z in zip(pts, pts[1:]):
        q = pcbnew.PCB_TRACK(b); q.SetLayer(layer); q.SetStart(P(*a)); q.SetEnd(P(*z))
        q.SetWidth(pcbnew.FromMM(width)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(x, y):
    q = pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetNet(n); q.SetNetCode(n.GetNetCode())
    q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); b.Add(q)

# Source/support pad escapes, kept outside the QFN pads (no via-in-pad).
for pad, q in [((153.5,136.6),(152.5,136.6)), ((154.8,139.5),(154.8,140.5)),
               ((156.5,135.0),(157.5,135.0)), ((178.5,133.4),(177.5,133.4)),
               ((179.8,139.5),(179.8,140.5)), ((181.5,135.0),(182.5,135.0)),
               ((125.5,145.0),(125.5,146.0))]:
    tr(F, [pad,q]); via(*q)

# Join each connector power group on the component side, then transition.
tr(F, [(211.0,167.275),(211.5,167.275)], .25)
tr(F, [(213.5,167.275),(214.0,167.275),(214.5,167.275),(215.0,167.275)], .25)
tr(F, [(228.0,167.275),(228.5,167.275),(229.0,167.275)], .25)
for q in ((211.5,168.4),(215.0,168.4),(229.0,168.4)):
    tr(F, [(q[0],167.275),q]); via(*q)

# Broad underside trunk; the corridor is intentionally acreage-sized.
tr(B, [(211.5,168.4),(211.5,174.0),(190.0,174.0),(182.5,135.0)], .35)
tr(B, [(215.0,168.4),(215.0,176.0),(190.0,176.0),(190.0,174.0)], .35)
tr(B, [(229.0,168.4),(229.0,178.0),(190.0,178.0),(190.0,176.0)], .35)
tr(B, [(182.5,135.0),(182.5,174.0),(190.0,174.0)], .35)
tr(B, [(177.5,133.4),(170.0,133.4),(170.0,174.0),(182.5,174.0)], .35)
tr(B, [(152.5,136.6),(145.0,136.6),(145.0,174.0),(170.0,174.0)], .35)
tr(B, [(154.8,140.5),(154.8,174.0)], .35)
tr(B, [(157.5,135.0),(160.0,135.0),(160.0,174.0)], .35)
tr(B, [(179.8,140.5),(179.8,174.0)], .35)
tr(B, [(125.5,146.0),(125.5,174.0),(145.0,174.0)], .35)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
