"""Disposable native-pad-aware replacement for the four M.2 lane-0 routes."""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
base = R / os.environ.get("P24_M2_BASE", "PHASE24_STORAGE_MODEAUTH_USB3_ALIGNED_SATA_SUPPORT_ZONES_V1.kicad_pcb")
out = R / os.environ.get("P24_M2_OUT", "PHASE24_STORAGE_M2_LAUNCH_V1.kicad_pcb")
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.20)
def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)
def pad(ref, number): return b.FindFootprintByReference(ref).FindPadByNumber(str(number))
def seg(n, a, z, layer):
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def path(n, points, layer):
    for a, z in zip(points, points[1:]): seg(n, a, z, layer)
def via(n, p):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)

b = pcbnew.LoadBoard(str(base))
if b is None: raise SystemExit("cannot load base")
specs = (
    ("M2_SATA_A_P_PCIE_TXP0", "2", "49", B,
     [(176.5,130.5),(190,124),(205,124),(222.75,151),(222.75,157)]),
    ("M2_SATA_A_N_PCIE_TXN0", "3", "47", B,
     [(175.5,134.5),(190,126),(205,126),(222.25,150),(222.25,156)]),
    ("M2_SATA_B_P_PCIE_RXN0", "6", "41", B,
     [(176.5,136.5),(170,170),(205,170),(220.75,162)]),
    ("M2_SATA_B_N_PCIE_RXP0", "7", "43", B,
     [(175.5,138.5),(168,172),(205,172),(221.25,163)]),
)
for name, up, jp, layer, points in specs:
    n = b.FindNet(name)
    if n is None: raise SystemExit(f"missing net {name}")
    for item in list(b.GetTracks()):
        if item.GetNetCode() == n.GetNetCode(): b.RemoveNative(item)
    src, dst = xy(pad("U13", up)), xy(pad("J3", jp))
    # Every transition is outside both source and connector pad fields.
    if layer == B:
        path(n, [src, points[0]], F); via(n, points[0]); path(n, points, B)
        via(n, points[-1]); path(n, [points[-1], dst], F)
    else:
        path(n, [src] + points + [dst], F)
b.BuildListOfNets(); b.Save(str(out)); print(out)
