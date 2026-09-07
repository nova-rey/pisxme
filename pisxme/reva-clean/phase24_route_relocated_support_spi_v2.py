#!/usr/bin/env python3
"""Disposable Path-B SPI reroute using the known-clean V6 source escape."""
from pathlib import Path
import re
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_SUPPORT_BRANCH_RELOCATED_V1.kicad_pcb"
SCRUB = HERE / ".phase24_relocated_spi_scrub.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_SUPPORT_BRANCH_RELOCATED_SPI_V2.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.20)
SPI = {"SPICS", "SPISO", "SPISI", "SPICLK", "SPISO3"}

def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def tr(b, name, layer, a, z):
    n = b.FindNet(name); t = pcbnew.PCB_TRACK(b)
    t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer); t.SetWidth(W)
    t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b, name, p):
    n = b.FindNet(name); q = pcbnew.PCB_VIA(b); q.SetPosition(P(*p))
    q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30))
    q.SetLayerPair(F, B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def scrub_spi(src):
    text = src.read_text(); remove = []; i = 0
    while i < len(text):
        if text.startswith('\t(segment', i) or text.startswith('\t(via', i):
            depth = 0; j = i
            while j < len(text):
                if text[j] == '(':
                    depth += 1
                elif text[j] == ')':
                    depth -= 1
                    if depth == 0:
                        block = text[i:j + 1]
                        if any(f'(net "{n}")' in block for n in SPI):
                            remove.append((i, j + 1))
                        i = j
                        break
                j += 1
        i += 1
    for a, z in reversed(remove): text = text[:a] + text[z:]
    SCRUB.write_text(text)
def route(b, name, source, bend, corridor, target):
    tr(b,name,F,source,bend); via(b,name,bend)
    last = bend
    for point in corridor:
        tr(b,name,B,last,point); last = point
    via(b,name,last); tr(b,name,F,last,target)
def main():
    scrub_spi(BASE); b = pcbnew.LoadBoard(str(SCRUB))
    # V6's source-side escapes are retained geometrically; only the B.Cu
    # corridor and final landing are extended to the translated U2 at y=80.
    route(b,'SPICS',(83.95,62.8),(85,61),[(86,61),(86,75),(90.8,75)],(90.8,80))
    route(b,'SPISO',(83.95,63.2),(85.5,62),[(87,62),(87,75),(92,75)],(92,80))
    route(b,'SPISO3',(83.95,63.6),(86,63),[(88,63),(88,77),(98,77)],(98,80))
    route(b,'SPICLK',(83.95,64.8),(89,64.8),[(89,70),(96.8,70)],(96.8,80))
    # SPISI uses the wide lower F.Cu departure from the V6 oracle, then a
    # single ordinary-via transition before the relocated U2 landing.
    tr(b,'SPISI',F,(83.95,65.2),(85.5,70)); tr(b,'SPISI',F,(85.5,70),(94,70))
    via(b,'SPISI',(94,70)); tr(b,'SPISI',B,(94,70),(94,79)); via(b,'SPISI',(94,79))
    tr(b,'SPISI',F,(94,79),(95.6,80))
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__ == '__main__': main()
