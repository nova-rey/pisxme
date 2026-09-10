#!/usr/bin/env python3
"""Transplant the native-clean V154 USB3 support primitive onto V127."""
from pathlib import Path
import sys
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_STORAGE_USB3_R80_RELOCATED_V127.kicad_pcb"
DONOR = R / "PHASE24_STORAGE_SUPPORT_U12_COAUTHOR_TX_RX_FAR_V154.kicad_pcb"
OUT = R / "PHASE24_STORAGE_SUPPORT_V154_INTEGRATED.kicad_pcb"
NETS = {"USB_TXP1", "USB_TXN1", "JMS_USB3_TXP", "JMS_USB3_TXN",
        "USB_RXP1", "USB_RXN1"}

def mm(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def leaf(name): return name.rsplit("/", 1)[-1]

if len(sys.argv) > 1: BASE = R / sys.argv[1]
if len(sys.argv) > 2: DONOR = R / sys.argv[2]
if len(sys.argv) > 3: OUT = R / sys.argv[3]
b, d = pcbnew.LoadBoard(str(BASE)), pcbnew.LoadBoard(str(DONOR))

# The donor moved the series capacitors as part of the coherent local island.
for ref in ("C86", "C87"):
    src, dst = d.FindFootprintByReference(ref), b.FindFootprintByReference(ref)
    if src is None or dst is None: raise RuntimeError("missing " + ref)
    x, y = mm(src.GetPosition())
    dst.SetPosition(V(x, y)); dst.SetOrientationDegrees(src.GetOrientationDegrees())

for item in list(b.GetTracks()):
    if leaf(item.GetNetname()) in NETS:
        b.RemoveNative(item)

for item in d.GetTracks():
    if leaf(item.GetNetname()) not in NETS:
        continue
    name = leaf(item.GetNetname())
    n = b.FindNet(name) or b.FindNet("/STORAGE/" + name)
    if n is None: raise RuntimeError("missing target net " + name)
    if isinstance(item, pcbnew.PCB_VIA):
        q = pcbnew.PCB_VIA(b)
        q.SetPosition(item.GetPosition()); q.SetWidth(item.GetWidth(pcbnew.F_Cu))
        q.SetDrill(item.GetDrill()); q.SetLayerPair(item.TopLayer(), item.BottomLayer())
    else:
        q = pcbnew.PCB_TRACK(b)
        q.SetStart(item.GetStart()); q.SetEnd(item.GetEnd())
        q.SetLayer(item.GetLayer()); q.SetWidth(item.GetWidth())
    q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)

b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.BuildConnectivity()
b.Save(str(OUT)); print(OUT)
