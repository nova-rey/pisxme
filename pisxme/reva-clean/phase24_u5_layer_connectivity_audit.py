"""Physical U5 connectivity audit from serialized PCB copper only."""
from pathlib import Path
import sys
import pcbnew

R = Path(__file__).resolve().parent
DEFAULT_BOARD = R / "PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb"
TARGET = {
    "/REGULATORS/BRIDGE_1V1": ["U5.9", "C44.1", "C45.1", "C46.1", "C47.1"],
    "POWER_GND": ["R20.2", "C44.2", "C45.2", "C46.2", "C47.2"],
}


def node(net, layer, point):
    return (net, int(layer), int(point.x), int(point.y))


def orient(a, b, c):
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)


def between(a, b, c):
    return min(a.x, b.x) <= c.x <= max(a.x, b.x) and min(a.y, b.y) <= c.y <= max(a.y, b.y)


def intersects(a, b, c, d):
    # Exact integer geometry is sufficient for the orthogonal KiCad tracks in
    # this island, including endpoint-to-interior T junctions.
    return ((orient(a, b, c) == 0 and between(a, b, c)) or
            (orient(a, b, d) == 0 and between(a, b, d)) or
            (orient(c, d, a) == 0 and between(c, d, a)) or
            (orient(c, d, b) == 0 and between(c, d, b)) or
            (orient(a, b, c) > 0) != (orient(a, b, d) > 0) and
            (orient(c, d, a) > 0) != (orient(c, d, b) > 0))


def pad_layers(pad):
    layers = pad.GetLayerSet()
    return [layer for layer in (pcbnew.F_Cu, pcbnew.B_Cu) if layers.Contains(layer)]


def audit(board_path=DEFAULT_BOARD):
    board = pcbnew.LoadBoard(str(board_path))
    # KiCad's Python binding uses a board layer object for B.Cu in some
    # releases; normalize all layer IDs through the serialized item layer.
    parent = {}

    def find(value):
        parent.setdefault(value, value)
        if parent[value] != value:
            parent[value] = find(parent[value])
        return parent[value]

    def join(left, right):
        left, right = find(left), find(right)
        if left != right:
            parent[right] = left

    segments = []
    # Edges come only from serialized track geometry and via transitions.
    # Net identity is part of each node, so unlike nets cannot join.
    for item in board.GetTracks():
        net = item.GetNetname()
        if not net:
            continue
        if isinstance(item, pcbnew.PCB_VIA):
            join(node(net, pcbnew.F_Cu, item.GetPosition()),
                 node(net, pcbnew.B_Cu, item.GetPosition()))
        else:
            layer = item.GetLayer()
            join(node(net, layer, item.GetStart()), node(net, layer, item.GetEnd()))
            segments.append((net, layer, item.GetStart(), item.GetEnd()))

    # Join same-net track segments that physically intersect, not just those
    # whose endpoints coincide.  This captures serialized T-junctions without
    # assuming any expected route or adding synthetic edges.
    for i, (net_a, layer_a, a, b) in enumerate(segments):
        for net_c, layer_c, c, d in segments[i + 1:]:
            if net_a == net_c and layer_a == layer_c and intersects(a, b, c, d):
                join(node(net_a, layer_a, a), node(net_c, layer_c, c))

    # A pad joins copper only on its actual layer set and only at its exact
    # serialized position.  No expected edge is injected here.
    pad_nodes = {}
    for footprint in board.GetFootprints():
        for pad in footprint.Pads():
            net = pad.GetNetname()
            if not net:
                continue
            key = f"{footprint.GetReference()}.{pad.GetNumber()}"
            pad_nodes[key] = [node(net, layer, pad.GetPosition()) for layer in pad_layers(pad)]
            for pad_node in pad_nodes[key]:
                find(pad_node)

    # Zone contact is represented by filled geometry.  A same-net copper point
    # receives a zone edge only when its serialized point is inside that fill.
    for zone in board.Zones():
        net = zone.GetNetname()
        if not net or not zone.IsFilled():
            continue
        layer = zone.GetLayer()
        filled = zone.GetFilledPolysList(layer)
        zone_key = (net, int(layer), "ZONE", id(zone))
        find(zone_key)
        for item in board.GetTracks():
            if isinstance(item, pcbnew.PCB_VIA) and item.GetNetname() == net:
                if filled.Contains(item.GetPosition()):
                    join(node(net, layer, item.GetPosition()), zone_key)
        for key, points in pad_nodes.items():
            for point in points:
                if point[0] == net and point[1] == int(layer):
                    if filled.Contains(pcbnew.VECTOR2I(point[2], point[3])):
                        join(point, zone_key)

    for net, members in TARGET.items():
        roots = []
        for token in members:
            if token not in pad_nodes:
                raise AssertionError(f"missing serialized pad {token}")
            if not pad_nodes[token]:
                raise AssertionError(f"pad has no copper layer {token}")
            if any(pad_node[0] != net for pad_node in pad_nodes[token]):
                raise AssertionError(f"wrong net on {token}: {pad_nodes[token]}")
            roots.extend(find(pad_node) for pad_node in pad_nodes[token])
        if len(set(roots)) != 1:
            raise AssertionError(f"{net} target pads are not physically connected: {set(roots)}")
    return True


if __name__ == "__main__":
    audit(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_BOARD)
    print("Phase24 U5 physical connectivity audit: PASS; serialized pads/tracks/vias/zones prove both target groups")
