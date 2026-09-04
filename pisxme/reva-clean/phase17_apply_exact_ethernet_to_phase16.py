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
CT1_LAYER_OVERRIDE = os.environ.get("PISXME_CT1_LAYER", "F.Cu")
CT2_LAYER_OVERRIDE = os.environ.get("PISXME_CT2_LAYER", "")
SAFE_CT_LAUNCH = os.environ.get("PISXME_SAFE_CT_LAUNCH", "") == "1"
SAFE_CT_CLEAR = os.environ.get("PISXME_SAFE_CT_CLEAR", "1") == "1"
ETH_DX = float(os.environ.get("PISXME_ETH_DX", "0"))
ETH_DY = float(os.environ.get("PISXME_ETH_DY", "0"))
ETH_REFS = {"J2", "U6", "U9", "CCT", "CCT1", "CCT2", "CCT3", "CCT4",
            "RCT1", "RCT2", "RCT3", "RCT4"}


def short(name):
    return str(name).rsplit("/", 1)[-1]


def xy(p):
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)


def V(x, y):
    return pcbnew.VECTOR2I_MM(x, y)


def island_point(point):
    """Translate fixture geometry once it leaves the fixed J7 source."""
    x, y = xy(point)
    if ETH_DX or ETH_DY:
        # CM5IO fixture geometry uses x>60 for the ESD/MagJack island.  A
        # segment crossing the boundary therefore retains its J7 endpoint
        # and moves only its island endpoint.
        if x > 60.0:
            return V(x + ETH_DX, y + ETH_DY)
    return point


def target_net(board, name):
    name = short(name)
    # The official CM5IO ESD ground is board GND.  Map the fixture's legacy
    # source label to the clean hierarchy's POWER_GND authority.
    if name == "ETH_GND":
        n = board.FindNet("POWER_GND") or board.FindNet("/POWER_GND")
        if n is not None:
            return n
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
            # Do not use the SWIG copy constructor here: KiCad 10 can retain
            # zeroed geometry in a copied PCB_TRACK.  Store scalar geometry
            # and recreate each item on the destination board explicitly.
            if isinstance(item, pcbnew.PCB_VIA):
                tracks.append(("via", item.GetPosition(), item.GetWidth(pcbnew.F_Cu),
                               item.GetDrill(), item.GetNetname()))
            else:
                tracks.append(("track", item.GetStart(), item.GetEnd(),
                               item.GetLayer(), item.GetWidth(), item.GetNetname()))

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
        if ETH_DX or ETH_DY:
            fp.SetPosition(V(xy(fp.GetPosition())[0] + ETH_DX,
                             xy(fp.GetPosition())[1] + ETH_DY))
        board.Add(fp)
        for pad in fp.Pads():
            pname = short(pad.GetNetname())
            if pname:
                pad.SetNet(target_net(board, pname))

    for record in tracks:
        kind = record[0]
        pname = short(record[-1])
        n = target_net(board, pname)
        if kind == "via":
            _, position, width, drill, _ = record
            position = island_point(position)
            if pname == "ETH_GND" and abs(pcbnew.ToMM(position.x) - 103.0) < 0.01 and abs(pcbnew.ToMM(position.y) - 50.0) < 0.01:
                # CM5IO source artifact: this via has no B.Cu copper and is
                # flagged dangling when transplanted.  The connected ESD
                # return/stitching vias remain authoritative in the fixture.
                continue
            if pname.startswith(("ETH_", "GBE_")):
                drill = pcbnew.FromMM(0.30)
            q = pcbnew.PCB_VIA(board)
            q.SetPosition(position)
            q.SetWidth(max(width, pcbnew.FromMM(0.50)))
            q.SetDrill(drill)
            q.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
            q.SetNet(n)
        else:
            _, start, end, layer, width, _ = record
            start, end = island_point(start), island_point(end)
            pname0 = pname
            if start == end:
                # Do not reproduce a zero-length source artifact; it is not
                # a physical connection and native DRC correctly flags it as
                # dangling in the integrated board.
                continue
            if pname == "ETH_GND" and layer == pcbnew.B_Cu and any(
                    pcbnew.ToMM(p.y) >= 70.0 for p in (start, end)):
                # Paired with the source-artifact via above; this isolated
                # B.Cu tail has no second copper endpoint in the transplant.
                continue
            if pname0.startswith("CM5_GBE_TD"):
                # The CM5IO source uses 0.127 mm copper.  PiSXMe's current
                # JLC six-layer 100-ohm basis is 5.2 mil = 0.13208 mm; retain
                # the source topology but emit the PiSXMe fabrication target
                # for the disposable integrated candidate.
                width = pcbnew.FromMM(0.13208)
            if pname0.startswith(("ETH_", "GBE_")):
                width = pcbnew.FromMM(0.13208)
            if SAFE_CT_CLEAR and layer == pcbnew.B_Cu and pname0 in {"ETH_CT2", "ETH_CT3"}:
                s = (pcbnew.ToMM(start.x), pcbnew.ToMM(start.y))
                e = (pcbnew.ToMM(end.x), pcbnew.ToMM(end.y))
                doglegs = {
                    "ETH_CT2": (s, (78.0, 55.56), (78.0, 50.8), (93.8, 50.8), (93.8, 46.0), e),
                    "ETH_CT3": (s, (74.325, 50.8), (66.0, 50.8), (66.0, 46.0), e),
                }
                for a0, z0 in zip(doglegs[pname0], doglegs[pname0][1:]):
                    q = pcbnew.PCB_TRACK(board); q.SetStart(V(*a0)); q.SetEnd(V(*z0))
                    q.SetLayer(pcbnew.B_Cu); q.SetWidth(width); q.SetNet(n); board.Add(q)
                continue
            if SAFE_CT_LAUNCH and layer == pcbnew.B_Cu and pname0 in {"ETH_CT2", "ETH_CT3"}:
                s = (pcbnew.ToMM(start.x), pcbnew.ToMM(start.y))
                e = (pcbnew.ToMM(end.x), pcbnew.ToMM(end.y))
                # The source CT launches are electrically correct but the
                # straight integrated copies graze the EDAC mounting holes.
                # Preserve the official pad/support endpoints and add only a
                # local B.Cu dogleg around the authoritative hole envelope.
                launch = {
                    "ETH_CT1": ((86.0,58.5),),
                    "ETH_CT2": ((84.5,57.0),),
                    "ETH_CT3": ((68.0,58.0),),
                    "ETH_CT4": ((69.0,58.5),),
                }.get(pname0, ())
                if launch and min(s[0], e[0]) > 60 and max(s[1], e[1]) > 50:
                    pts = (s,) + launch + (e,)
                    for a0, z0 in zip(pts, pts[1:]):
                        q = pcbnew.PCB_TRACK(board); q.SetStart(V(*a0)); q.SetEnd(V(*z0))
                        q.SetLayer(pcbnew.B_Cu); q.SetWidth(width); q.SetNet(n); board.Add(q)
                    continue
            # The CM5IO center-tap branches are low-speed support copper.  A
            # caller may move only CT1 to the opposite permitted signal layer
            # to remove a board-context crossing; all MDI geometry remains an
            # exact CM5IO transplant.
            override = CT1_LAYER_OVERRIDE if pname == "ETH_CT1" else CT2_LAYER_OVERRIDE if pname == "ETH_CT2" else ""
            if override:
                layer = {"F.Cu": pcbnew.F_Cu, "B.Cu": pcbnew.B_Cu}.get(override, layer)
                if layer == pcbnew.F_Cu:
                    # Keep the through-hole/SMD endpoint launches on their
                    # original B.Cu side and put only the crossing middle
                    # corridor on F.Cu.  The offset vias are ordinary
                    # through-vias, deliberately outside the source pads.
                    # Move the transition away from the neighboring EDAC CT2
                    # through-hole launch; the first offset was too close to
                    # J2 pad 12 in the acreage context.
                    if pname == "ETH_CT1":
                        va = (pcbnew.ToMM(start.x) + 1.5, pcbnew.ToMM(start.y) + 1.5)
                        vz = (pcbnew.ToMM(end.x) + 0.8, pcbnew.ToMM(end.y) - 0.8)
                    else:
                        va = (pcbnew.ToMM(start.x) - 1.5, pcbnew.ToMM(start.y) + 1.5)
                        vz = (pcbnew.ToMM(end.x) + 0.8, pcbnew.ToMM(end.y) - 0.8)
                    for p0 in (va, vz):
                        v = pcbnew.PCB_VIA(board); v.SetPosition(V(*p0))
                        v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30))
                        v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); v.SetNet(n); board.Add(v)
                    b0 = (pcbnew.ToMM(start.x), pcbnew.ToMM(start.y))
                    b1 = (pcbnew.ToMM(end.x), pcbnew.ToMM(end.y))
                    for a0, z0, l0 in ((b0, va, pcbnew.B_Cu), (va, vz, pcbnew.F_Cu), (vz, b1, pcbnew.B_Cu)):
                        q = pcbnew.PCB_TRACK(board); q.SetStart(V(*a0)); q.SetEnd(V(*z0))
                        q.SetLayer(l0); q.SetWidth(width); q.SetNet(n); board.Add(q)
                    continue
            q = pcbnew.PCB_TRACK(board)
            q.SetStart(start)
            q.SetEnd(end)
            q.SetLayer(layer)
            q.SetWidth(width)
            q.SetNet(n)
        board.Add(q)
    # The Phase 16 ancestor carries filled GND zones.  Refill after replacing
    # the Ethernet through-hole launch; otherwise stale copper is reported as
    # false signal/plane collisions at the new J2/CT geometry.
    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    board.Save(str(OUT))
    print(f"saved {OUT}; copied {len(footprints)} Ethernet footprints and {len(tracks)} copper items")


if __name__ == "__main__":
    main()
