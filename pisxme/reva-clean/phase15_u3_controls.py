"""Candidate complete U3 FB/RT/PG control island with deliberate transitions."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "ACREAGE_REGULATOR_POWER_ESCAPE_PHASE15.kicad_pcb"
OUTPUT = ROOT / "ACREAGE_U3_CONTROLS_PHASE15.kicad_pcb"


def p(x, y):
    return pcbnew.VECTOR2I_MM(x, y)


def n(board, name):
    return next(x for x in board.GetNetsByName().values() if x.GetNetname() == name)


def track(board, a, b, net, layer=pcbnew.F_Cu, width=0.20):
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(p(*a)); t.SetEnd(p(*b)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(width)); t.SetNet(net); board.Add(t)


def via(board, xy, net):
    q = pcbnew.PCB_VIA(board)
    q.SetPosition(p(*xy)); q.SetWidth(pcbnew.FromMM(0.50)); q.SetDrill(pcbnew.FromMM(0.30))
    q.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); q.SetNet(net); board.Add(q)


def main():
    b = pcbnew.LoadBoard(str(INPUT))
    positions = {"C9": (73, 62, 0), "R3": (78, 62, 180),
                 "R4": (82, 62, 0), "R5": (61, 66, 0), "R6": (73, 69, 180)}
    for ref, (x, y, angle) in positions.items():
        fp = b.FindFootprintByReference(ref)
        fp.SetPosition(p(x, y)); fp.SetOrientationDegrees(angle)

    fb = n(b, "/REGULATORS/FB_CM5_5V")
    rt = n(b, "/REGULATORS/RT_CM5_5V")
    pg = n(b, "/REGULATORS/PG_CM5_5V")
    out = n(b, "/REGULATORS/CM5_5V")

    # F.Cu package exits to three separated transition vias.
    track(b, (54.70, 79.25), (56.0, 79.25), fb)
    via(b, (56.0, 79.25), fb)
    track(b, (54.70, 78.25), (58.0, 78.25), rt)
    via(b, (58.0, 78.25), rt)
    track(b, (54.70, 77.75), (55.50, 77.75), pg)
    track(b, (55.50, 77.75), (55.50, 76.50), pg)
    track(b, (55.50, 76.50), (62.0, 76.50), pg)
    track(b, (62.0, 76.50), (62.0, 77.75), pg)
    via(b, (62.0, 77.75), pg)

    # Isolated B.Cu quiet corridors: FB at y=60, RT at y=66, PG at y=69.
    track(b, (56.0, 79.25), (56.0, 60.0), fb, pcbnew.B_Cu)
    track(b, (56.0, 60.0), (81.5, 60.0), fb, pcbnew.B_Cu)
    for xy in ((71.65, 61.0), (77.5, 61.0), (81.5, 61.0)):
        via(b, xy, fb)
        track(b, xy, (xy[0], 60.0), fb, pcbnew.B_Cu)
    for xy in ((71.65, 62.0), (77.5, 62.0), (81.5, 62.0)):
        # The F.Cu stubs terminate on the actual passive pads.
        track(b, xy, (xy[0], 61.0), fb)

    track(b, (58.0, 78.25), (58.0, 66.0), rt, pcbnew.B_Cu)
    track(b, (58.0, 66.0), (60.5, 65.0), rt, pcbnew.B_Cu)
    via(b, (60.5, 65.0), rt)
    track(b, (60.5, 65.0), (60.5, 66.0), rt)

    track(b, (62.0, 77.75), (62.0, 69.0), pg, pcbnew.B_Cu)
    track(b, (62.0, 69.0), (72.5, 70.0), pg, pcbnew.B_Cu)
    via(b, (72.5, 70.0), pg)
    track(b, (72.5, 70.0), (72.5, 69.0), pg)

    # Dedicated VOUT compensation corridor on F.Cu, below the package.
    track(b, (54.95, 80.0), (60.0, 80.0), out)
    track(b, (60.0, 80.0), (60.0, 92.0), out)
    track(b, (60.0, 92.0), (70.0, 92.0), out)
    for xy in ((74.35, 62.0), (78.5, 62.0), (73.5, 69.0)):
        track(b, (70.0, 92.0), (xy[0], 92.0), out)
        track(b, (xy[0], 92.0), xy, out)
    pcbnew.ZONE_FILLER(b).Fill(b.Zones())
    b.Save(str(OUTPUT))
    print("Phase 15 U3 controls: candidate generated with FB/RT/PG transitions")


if __name__ == "__main__":
    main()
