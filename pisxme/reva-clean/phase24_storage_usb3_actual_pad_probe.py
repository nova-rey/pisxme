#!/usr/bin/env python3
"""Disposable USB3 J7-to-U12 corridor from native saved pad coordinates."""
from pathlib import Path
import argparse
import pcbnew


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("input", type=Path); ap.add_argument("output", type=Path)
    a = ap.parse_args(); b = pcbnew.LoadBoard(str(a.input))
    if b is None: raise SystemExit("cannot load board")
    F, B = pcbnew.F_Cu, pcbnew.B_Cu
    jobs = [("CM5_USB3_RX_N", "J7", "128", "U12", "16", 82.0, 149.0),
            ("CM5_USB3_RX_P", "J7", "130", "U12", "15", 82.6, 149.4),
            ("CM5_USB3_TX_N", "J7", "140", "U12", "12", 78.0, 150.0),
            ("CM5_USB3_TX_P", "J7", "142", "U12", "11", 78.6, 150.4)]
    for item in list(b.GetTracks()):
        if item.GetNetname() in {x[0] for x in jobs}: b.RemoveNative(item)

    def pos(ref, num):
        f = b.FindFootprintByReference(ref); p = f.FindPadByNumber(num)
        if p is None: raise SystemExit(f"missing {ref}.{num}")
        q = p.GetPosition(); return q, (pcbnew.ToMM(q.x), pcbnew.ToMM(q.y))
    def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
    def tr(net, x, y, w=0.20, layer=F):
        t = pcbnew.PCB_TRACK(b); t.SetStart(V(*x)); t.SetEnd(V(*y)); t.SetLayer(layer)
        t.SetWidth(pcbnew.FromMM(w)); t.SetNet(net); t.SetNetCode(net.GetNetCode()); b.Add(t)
    def via(net, x, y):
        v = pcbnew.PCB_VIA(b); v.SetPosition(V(x, y)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F, B); v.SetNet(net); v.SetNetCode(net.GetNetCode()); b.Add(v)
    for name, sr, sp, dr, dp, sx, tx in jobs:
        n = b.FindNet(name)
        if n is None: raise SystemExit(f"missing net {name}")
        _, s = pos(sr, sp); _, d = pos(dr, dp)
        sy = s[1]; dy = d[1]
        sv = (sx, sy); tv = (tx, dy)
        tr(n, s, sv); via(n, *sv)
        tr(n, sv, (sx, dy), layer=B); tr(n, (sx, dy), tv, layer=B); via(n, *tv)
        tr(n, tv, d)
    b.BuildListOfNets(); b.Save(str(a.output)); print(a.output)


if __name__ == "__main__": main()
