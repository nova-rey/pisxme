"""Native endpoint and negative-control audit for the V282 SPI pair."""
from pathlib import Path
import sys
import pcbnew

HERE = Path(__file__).resolve().parent
DEFAULT = HERE / "PHASE24_RTL9210B_SUPPORT_ROUTE_SPISO_V282.kicad_pcb"
TARGETS = {"SPICS": ("U1.24", "U2.1"), "SPISO": ("U1.23", "U2.2")}


def ep(p): return f"{p.GetParentFootprint().GetReference()}.{p.GetNumber()}"
def load(path): return pcbnew.LoadBoard(str(path))
def padmap(b): return {ep(p): p for f in b.GetFootprints() for p in f.Pads()}
def connected(b, p):
    b.BuildConnectivity()
    return {ep(x) for x in b.GetConnectivity().GetConnectedItems(p)
            if type(x).__name__ == "PAD"} | {ep(p)}


def audit(path):
    b = load(path); ps = padmap(b)
    for net, ends in TARGETS.items():
        for e in ends:
            assert e in ps and str(ps[e].GetNetname()) == net, (net, e)
        for e in ends: assert set(ends) <= connected(b, ps[e]), (net, e)
        print(f"{net} native {ends[0]} <-> {ends[1]}: PASS")


def negative(path):
    for net, ends in TARGETS.items():
        b = load(path); ps = padmap(b); b.BuildConnectivity()
        tracks = [x for x in b.GetConnectivity().GetConnectedItems(ps[ends[0]])
                  if type(x).__name__ == "PCB_TRACK" and x.GetNetname() == net]
        assert tracks, net
        b.RemoveNative(tracks[0])
        b.BuildConnectivity()
        if set(ends) <= connected(b, padmap(b)[ends[0]]):
            raise AssertionError(f"{net} removal did not fail")
        print(f"{net} trace-removal negative control: PASS")


if __name__ == "__main__":
    p = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    audit(p)
    if "--negative-controls" in sys.argv[2:]: negative(p)
