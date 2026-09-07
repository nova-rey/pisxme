#!/usr/bin/env python3
"""V3: separate TX/RX layers and use an ordered J3 target-via column."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_PATHA_M2_LANE0_LAUNCH_ISOLATED_V1.kicad_pcb"
OUT = ROOT / "PHASE24_PATHA_M2_LANE0_LAUNCH_ISOLATED_V3.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)

def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p):
    q = p.GetPosition()
    return pcbnew.ToMM(q.x), pcbnew.ToMM(q.y)
def track(b, n, a, z, layer):
    t = pcbnew.PCB_TRACK(b)
    t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def path(b, n, pts, layer):
    for a, z in zip(pts, pts[1:]): track(b, n, a, z, layer)
def via(b, n, p):
    v = pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.6))
    v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F, B)
    v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)

def main():
    b = pcbnew.LoadBoard(str(BASE))
    u = b.FindFootprintByReference("U13")
    j = b.FindFootprintByReference("J3")
    specs = {
        # TX remains on F.Cu and occupies the upper target-via columns.
        "TXP": ("M2_SATA_A_P_PCIE_TXP0", "2", "49", (222.0, 153.5), F,
                [(181.0, 139.0), (214.0, 139.0), (222.0, 153.5)]),
        "TXN": ("M2_SATA_A_N_PCIE_TXN0", "3", "47", (220.5, 153.5), F,
                [(183.0, 141.0), (212.0, 141.0), (220.5, 153.5)]),
        # RX uses B.Cu after an early source transition, avoiding TX crossings.
        "RXN": ("M2_SATA_B_P_PCIE_RXN0", "6", "41", (215.0, 153.5), B,
                [(184.0, 151.0), (208.0, 151.0), (215.0, 153.5)]),
        "RXP": ("M2_SATA_B_N_PCIE_RXP0", "7", "43", (216.5, 153.5), B,
                [(186.0, 153.0), (210.0, 153.0), (216.5, 153.5)]),
    }
    for _, (net_name, up, jp, target, post_layer, branch) in specs.items():
        n = b.FindNet(net_name)
        for item in list(b.GetTracks()):
            if item.GetNetname() == net_name:
                b.RemoveNative(item)
        src = xy(u.FindPadByNumber(up)); dst = xy(j.FindPadByNumber(jp))
        if post_layer == F:
            path(b, n, [src, (branch[0][0], src[1]), branch[0]], F)
            path(b, n, branch, F)
        else:
            sv = (src[0] + 1.5, src[1])
            path(b, n, [src, sv], F); via(b, n, sv)
            path(b, n, [sv] + branch, B)
        via(b, n, target)
        path(b, n, [target, dst], F)
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)

if __name__ == "__main__": main()
