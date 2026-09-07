#!/usr/bin/env python3
"""Disposable follow-up: route the relocated SPI flash branch."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_BRANCH_RELOCATED_V1.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SUPPORT_BRANCH_RELOCATED_SPI_V1.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def track(b, n, layer, a, z):
    t = pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z))
    t.SetLayer(layer); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b, n, p):
    v = pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.60))
    v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F, B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def path(b, name, points):
    n = b.FindNet(name)
    for a, z in zip(points, points[1:]):
        if a == z and len(points) > 2: via(b, n, a)
        else: track(b, n, F if len(points) == 2 else B, a, z)
def main():
    b = pcbnew.LoadBoard(str(BASE))
    # Each route has F.Cu pad dogbones, a dedicated B.Cu corridor, and an F.Cu
    # landing.  Corridors are deliberately separated by 1 mm in this probe.
    jobs = {
        'SPICS': ((83.95,62.8),(86,62.8),(86,75),(90.8,75),(90.8,80)),
        'SPISO': ((83.95,63.2),(86.5,63.2),(86.5,76),(92,76),(92,80)),
        'SPISI': ((83.95,65.2),(87,65.2),(87,73),(95.6,73),(95.6,80)),
        'SPICLK': ((83.95,64.8),(87.5,64.8),(87.5,71),(96.8,71),(96.8,80)),
        'SPISO3': ((83.95,63.6),(88,63.6),(88,78),(98,78),(98,80)),
    }
    for name, pts in jobs.items():
        n = b.FindNet(name)
        track(b,n,F,pts[0],pts[1]); via(b,n,pts[1])
        for a,z in zip(pts[1:-2],pts[2:-1]): track(b,n,B,a,z)
        via(b,n,pts[-2]); track(b,n,F,pts[-2],pts[-1])
    # Keep the bring-up test pads physically attached to the relocated U2.
    for name, a, z in [('SPICS',(90.8,80),(88,78)),('SPISO',(92,80),(100,78)),
                       ('SPISI',(95.6,80),(96,78)),('SPICLK',(96.8,80),(92,78)),
                       ('SPISO3',(98,80),(104,78))]:
        track(b,b.FindNet(name),F,a,z)
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__ == '__main__': main()
