#!/usr/bin/env python3
"""Measure USB3 geometry from saved native PCB tracks/vias only."""
from pathlib import Path
import argparse, math
import pcbnew

NETS = ("CM5_USB3_RX_N", "CM5_USB3_RX_P", "CM5_USB3_TX_N", "CM5_USB3_TX_P",
        "USB_RXN1", "USB_RXP1", "USB_TXN1", "USB_TXP1",
        "JMS_USB3_TXN", "JMS_USB3_TXP")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("pcb", type=Path); a=ap.parse_args()
    b=pcbnew.LoadBoard(str(a.pcb)); b.BuildConnectivity()
    out=[]
    for name in NETS:
        length=0.0; layers={}; vias=0
        n=b.FindNet(name)
        if n is None: out.append(f"{name}: MISSING NET"); continue
        for t in b.GetTracks():
            if t.GetNetCode()!=n.GetNetCode(): continue
            if type(t).__name__ == "PCB_VIA": vias += 1; continue
            s,e=t.GetStart(),t.GetEnd(); length += math.hypot(e.x-s.x,e.y-s.y)/1e6
            layers[t.GetLayerName()] = layers.get(t.GetLayerName(),0)+1
        out.append(f"{name}: length_mm={length:.3f} vias={vias} layers={','.join(sorted(layers))}")
    print("\n".join(out))
    for a,bn in (("CM5_USB3_RX_N","CM5_USB3_RX_P"),("CM5_USB3_TX_N","CM5_USB3_TX_P"),
                 ("USB_RXN1","USB_RXP1"),("USB_TXN1","USB_TXP1")):
        # Reuse the printed scalar values without adding synthetic connectivity.
        def total(name):
            n=b.FindNet(name); return sum(math.hypot(t.GetEnd().x-t.GetStart().x,t.GetEnd().y-t.GetStart().y)/1e6
                for t in b.GetTracks() if t.GetNetCode()==n.GetNetCode() and type(t).__name__=='PCB_TRACK')
        delta=abs(total(a)-total(bn)); print(f"skew_proxy {a}/{bn}: {delta:.3f} mm")

if __name__ == "__main__": main()
