"""Create the Phase 14 V100 power-plane candidate from the acreage board.

The protected V100 feed is deliberately a broad top-copper polygon spanning
the two ideal-diode outputs, their branch FETs, and the SXM2 endpoint.  The
solid inner GND planes are the return reference for later signal routing. This
is a candidate artifact, not a claim that copper loss or endpoint contact
sharing has been measured.
"""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "ACREAGE_CANDIDATE.kicad_pcb"
OUTPUT = ROOT / "ACREAGE_POWER_PHASE14.kicad_pcb"
POWER_TRACK_WIDTH_MM = 2.0

# J6's through-hole return contact is immediately below its input contact, and
# the CM5 service connector occupies the direct diagonal escape.  The input
# escape rises above that connector before heading into the acreage.
ROUTE_BENDS = {
    ("J6", "1", "F2", "1"): ((20.0, 45.0), (20.0, 90.0), (45.0, 90.0)),
}

# Resolve the current placement through references and exact nets rather than
# baking board coordinates into the routing prototype.
POWER_CONTINUITY = (
    ("J5", "1", "F1", "1", "/POWER_INPUT/12V_IN_A"),
    ("J6", "1", "F2", "1", "/POWER_INPUT/12V_IN_B"),
    ("F1", "5", "Q1", "1", "/POWER_INPUT/FUSED_12V_A"),
    ("F2", "5", "Q2", "1", "/POWER_INPUT/FUSED_12V_B"),
)

DUPLICATE_CONTACTS = (
    ("F1", "1", "F1", "2", "/POWER_INPUT/12V_IN_A"),
    ("F1", "1", "F1", "3", "/POWER_INPUT/12V_IN_A"),
    ("F1", "1", "F1", "4", "/POWER_INPUT/12V_IN_A"),
    ("F1", "5", "F1", "6", "/POWER_INPUT/FUSED_12V_A"),
    ("F1", "5", "F1", "7", "/POWER_INPUT/FUSED_12V_A"),
    ("F1", "5", "F1", "8", "/POWER_INPUT/FUSED_12V_A"),
    ("F2", "1", "F2", "2", "/POWER_INPUT/12V_IN_B"),
    ("F2", "1", "F2", "3", "/POWER_INPUT/12V_IN_B"),
    ("F2", "1", "F2", "4", "/POWER_INPUT/12V_IN_B"),
    ("F2", "5", "F2", "6", "/POWER_INPUT/FUSED_12V_B"),
    ("F2", "5", "F2", "7", "/POWER_INPUT/FUSED_12V_B"),
    ("F2", "5", "F2", "8", "/POWER_INPUT/FUSED_12V_B"),
)


def find_net(board, net_name):
    # BOARD.FindNet performs fuzzy/legacy lookup in this KiCad Python ABI;
    # exact dictionary lookup prevents a similarly named hierarchical net
    # from being assigned to a power via or zone.
    return next((net for key, net in board.GetNetsByName().items()
                 if str(key) == net_name), None)


def rectangle_zone(board, net_name, layer, x0, y0, x1, y1, name):
    net = find_net(board, net_name)
    if net is None:
        raise SystemExit(f"missing required net: {net_name}")
    zone = pcbnew.ZONE(board)
    zone.SetLayer(layer)
    zone.SetNet(net)
    zone.SetNetCode(net.GetNetCode())
    zone.SetIsRuleArea(False)
    zone.SetMinThickness(pcbnew.FromMM(0.25))
    zone.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL)
    zone.SetZoneName(name)
    points = pcbnew.VECTOR_VECTOR2I()
    for x, y in ((x0, y0), (x1, y0), (x1, y1), (x0, y1)):
        points.append(pcbnew.VECTOR2I_MM(x, y))
    zone.AddPolygon(points)
    board.Add(zone)


def find_pad(board, reference, pad_number, net_name):
    footprint = board.FindFootprintByReference(reference)
    if footprint is None:
        raise SystemExit(f"missing required footprint: {reference}")
    pads = [pad for pad in footprint.Pads()
            if str(pad.GetNumber()) == pad_number
            and str(pad.GetNetname()) == net_name]
    if len(pads) != 1:
        raise SystemExit(
            f"expected one {reference}.{pad_number} pad on {net_name}, found {len(pads)}"
        )
    return pads[0]


def add_power_track(board, start, end, net_name, bend=None):
    if str(start.GetNetname()) != net_name or str(end.GetNetname()) != net_name:
        raise SystemExit(f"power track endpoint net mismatch on {net_name}")
    points = [start.GetPosition()]
    points.extend(pcbnew.VECTOR2I_MM(x, y) for x, y in (bend or ()))
    points.append(end.GetPosition())
    for first, last in zip(points, points[1:]):
        track = pcbnew.PCB_TRACK(board)
        track.SetStart(first)
        track.SetEnd(last)
        track.SetLayer(pcbnew.B_Cu)
        track.SetNetCode(start.GetNetCode())
        track.SetWidth(pcbnew.FromMM(POWER_TRACK_WIDTH_MM))
        board.Add(track)


def assert_protected_zone_connection(board, zone):
    filled = zone.GetFilledPolysList(pcbnew.F_Cu)
    for reference in ("Q1", "Q2"):
        pad = find_pad(board, reference, "2", "12V_PROTECTED")
        if not filled.PointInside(pad.GetPosition()):
            raise SystemExit(f"{reference}.2 is not connected to the filled protected zone")


def main():
    board = pcbnew.LoadBoard(str(INPUT))
    # The protected copper feed is confined to the V100 power corridor and
    # stops well short of unrelated high-speed/storage neighborhoods.
    rectangle_zone(board, "12V_PROTECTED", pcbnew.F_Cu,
                   115, 20, 245, 160, "V100_PROTECTED_FEED")
    # Keep both adjacent inner layers as solid return references, per the
    # frozen Phase 13 stack role.  The board edge is intentionally inset.
    for layer, name in ((pcbnew.In1_Cu, "V100_RETURN_PLANE_L2"),
                        (pcbnew.In4_Cu, "V100_RETURN_PLANE_L5")):
        rectangle_zone(board, "POWER_GND", layer, 1, 1, 299, 179, name)
    for start_ref, start_number, end_ref, end_number, net_name in POWER_CONTINUITY:
        add_power_track(
            board,
            find_pad(board, start_ref, start_number, net_name),
            find_pad(board, end_ref, end_number, net_name),
            net_name,
            ROUTE_BENDS.get((start_ref, start_number, end_ref, end_number)),
        )
    for start_ref, start_number, end_ref, end_number, net_name in DUPLICATE_CONTACTS:
        add_power_track(
            board,
            find_pad(board, start_ref, start_number, net_name),
            find_pad(board, end_ref, end_number, net_name),
            net_name,
        )
    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    protected_zone = next(
        zone for zone in board.Zones()
        if zone.GetZoneName() == "V100_PROTECTED_FEED"
    )
    assert_protected_zone_connection(board, protected_zone)
    board.Save(str(OUTPUT))
    print("Phase 14 V100 power candidate: PASS; nineteen B.Cu power segments and protected feed zone created")


if __name__ == "__main__":
    main()
