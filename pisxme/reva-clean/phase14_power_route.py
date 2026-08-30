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


def rectangle_zone(board, net_name, layer, x0, y0, x1, y1, name):
    net = board.FindNet(net_name)
    if net is None:
        raise SystemExit(f"missing required net: {net_name}")
    zone = pcbnew.ZONE(board)
    zone.SetLayer(layer)
    zone.SetNet(net)
    zone.SetIsRuleArea(False)
    zone.SetMinThickness(pcbnew.FromMM(0.25))
    zone.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL)
    zone.SetZoneName(name)
    points = pcbnew.VECTOR_VECTOR2I()
    for x, y in ((x0, y0), (x1, y0), (x1, y1), (x0, y1)):
        points.append(pcbnew.VECTOR2I_MM(x, y))
    zone.AddPolygon(points)
    board.Add(zone)


def main():
    board = pcbnew.LoadBoard(str(INPUT))
    # The protected copper feed is confined to the V100 power corridor and
    # stops well short of unrelated high-speed/storage neighborhoods.
    rectangle_zone(board, "12V_PROTECTED", pcbnew.F_Cu,
                   115, 30, 190, 130, "V100_PROTECTED_FEED")
    # Keep both adjacent inner layers as solid return references, per the
    # frozen Phase 13 stack role.  The board edge is intentionally inset.
    for layer, name in ((pcbnew.In1_Cu, "V100_RETURN_PLANE_L2"),
                        (pcbnew.In4_Cu, "V100_RETURN_PLANE_L5")):
        rectangle_zone(board, "POWER_GND", layer, 1, 1, 299, 179, name)
    pcbnew.ZONE_FILLER(board).Fill(board.Zones())
    board.Save(str(OUTPUT))
    print("Phase 14 V100 power candidate: PASS; protected feed zone plus return references created")


if __name__ == "__main__":
    main()
