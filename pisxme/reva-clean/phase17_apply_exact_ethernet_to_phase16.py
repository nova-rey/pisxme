"""Overlay the electrically closed CM5IO Ethernet fixture on the Phase 16 ancestor.

This is intentionally a disposable promotion step: all non-Ethernet Phase 16
copper and mechanics are preserved, while the Ethernet-local footprints and
copper are replaced by the exact fixture geometry at the shared J7 datum.
"""
from pathlib import Path
import os
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = Path(os.environ.get("PISXME_BASE", ROOT / "ACREAGE_PCIE_PHASE16.kicad_pcb"))
FIXTURE = ROOT / "CM5IO_DIRECT_J7_ETHERNET_FIXTURE.kicad_pcb"
OUT = Path(os.environ.get("PISXME_OUT", ROOT / "ACREAGE_PHASE17_CM5IO_EDAC_RC.kicad_pcb"))
PREFIXES = ("CM5_GBE_TD", "ETH_", "GBE_")
ETH_REFS = {"J2", "U6", "U9", "CCT", "CCT1", "CCT2", "CCT3", "CCT4",
            "RCT1", "RCT2", "RCT3", "RCT4"}


def short(name):
    return str(name).rsplit("/", 1)[-1]


def xy(p):
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)


def V(x, y):
    return pcbnew.VECTOR2I_MM(x, y)


def target_net(board, name):
    name = short(name)
    for candidate in (name, "/ETHERNET/" + name, "/" + name):
        n = board.FindNet(candidate)
        if n is not None:
            return n
    n = pcbnew.NETINFO_ITEM(board, name)
    board.Add(n)
    return n


def main():
    source = pcbnew.LoadBoard(str(FIXTURE))
    footprints = []
    for fp in source.GetFootprints():
        if fp.GetReference() in ETH_REFS:
            footprints.append(pcbnew.FOOTPRINT(fp))
    tracks = []
    for item in source.GetTracks():
        if short(item.GetNetname()).startswith(PREFIXES):
            tracks.append(pcbnew.PCB_VIA(item) if isinstance(item, pcbnew.PCB_VIA)
                          else pcbnew.PCB_TRACK(item))

    board = pcbnew.LoadBoard(str(BASE))
    for item in list(board.GetTracks()):
        if short(item.GetNetname()).startswith(PREFIXES):
            board.Remove(item)
    for ref in ETH_REFS:
        old = board.FindFootprintByReference(ref)
        if old is not None:
            board.Remove(old)

    for fp in footprints:
        ref = fp.GetReference()
        board.Add(fp)
        for pad in fp.Pads():
            pname = short(pad.GetNetname())
            if pname:
                pad.SetNet(target_net(board, pname))

    for item in tracks:
        pname = short(item.GetNetname())
        n = target_net(board, pname)
        if isinstance(item, pcbnew.PCB_VIA):
            q = pcbnew.PCB_VIA(board)
            q.SetPosition(item.GetPosition())
            q.SetWidth(item.GetWidth())
            q.SetDrill(item.GetDrill())
            q.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
            q.SetNet(n)
        else:
            q = pcbnew.PCB_TRACK(board)
            q.SetStart(item.GetStart())
            q.SetEnd(item.GetEnd())
            q.SetLayer(item.GetLayer())
            q.SetWidth(item.GetWidth())
            q.SetNet(n)
        board.Add(q)
    board.Save(str(OUT))
    print(f"saved {OUT}; copied {len(footprints)} Ethernet footprints and {len(tracks)} copper items")


if __name__ == "__main__":
    main()
