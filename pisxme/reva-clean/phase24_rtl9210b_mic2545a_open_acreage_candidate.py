"""Create one disposable full-board MIC2545A/ISOLATEB candidate.

The source board is the accepted V1603/V1517 integration.  This generator
does not rotate or relocate U1 and does not modify the source board.  All
new geometry is authored through KiCad's native pcbnew Python API.
"""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_PATHB_V1603_V1517_MIC2545A_OPEN_ACREAGE_U1LOCAL015_CANDIDATE.kicad_pcb"

F, B = pcbnew.F_Cu, pcbnew.B_Cu
P = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))
NORMAL = pcbnew.FromMM(0.20)
LOCAL = pcbnew.FromMM(0.15)


def net(board, name):
    found = board.FindNet(name)
    if found:
        return found
    found = pcbnew.NETINFO_ITEM(board, name)
    board.Add(found)
    return found


def footprint(board, ref, value):
    fp = pcbnew.FOOTPRINT(board)
    fp.SetReference(ref)
    fp.SetValue(value)
    fp.SetLayer(F)
    fp.SetPosition(P(0, 0))
    board.Add(fp)
    try:
        fp.Reference().SetVisible(False)
        fp.Value().SetVisible(False)
    except Exception:
        pass
    return fp


def pad(fp, number, x, y, assigned_net=None, size=(1.55, 0.60)):
    item = pcbnew.PAD(fp)
    item.SetNumber(str(number))
    item.SetPosition(P(x, y))
    item.SetSize(P(*size))
    item.SetShape(pcbnew.PAD_SHAPE_ROUNDRECT)
    item.SetRoundRectRadiusRatio(0.18)
    item.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
    item.SetLocalSolderMaskMargin(pcbnew.FromMM(0.0))
    item.SetLocalSolderPasteMargin(pcbnew.FromMM(-0.05))
    item.SetLocalSolderPasteMarginRatio(0.0)
    layers = pcbnew.LSET()
    layers.AddLayer(F)
    item.SetLayerSet(layers)
    if assigned_net is None:
        item.SetNet(None)
        item.SetNetCode(0)
    else:
        item.SetNet(assigned_net)
        item.SetNetCode(assigned_net.GetNetCode())
    fp.Add(item)
    return item


def segment(board, assigned_net, start, end, layer=F, width=NORMAL):
    if start == end:
        return
    item = pcbnew.PCB_TRACK(board)
    item.SetStart(P(*start))
    item.SetEnd(P(*end))
    item.SetLayer(layer)
    item.SetWidth(width)
    item.SetNet(assigned_net)
    item.SetNetCode(assigned_net.GetNetCode())
    board.Add(item)


def via(board, assigned_net, x, y):
    item = pcbnew.PCB_VIA(board)
    item.SetPosition(P(x, y))
    item.SetWidth(pcbnew.FromMM(0.60))
    item.SetDrill(pcbnew.FromMM(0.30))
    item.SetLayerPair(F, B)
    item.SetNet(assigned_net)
    item.SetNetCode(assigned_net.GetNetCode())
    board.Add(item)


def via_small(board, assigned_net, x, y):
    item = pcbnew.PCB_VIA(board)
    item.SetPosition(P(x, y))
    item.SetWidth(pcbnew.FromMM(0.40))
    item.SetDrill(pcbnew.FromMM(0.20))
    item.SetLayerPair(F, B)
    item.SetNet(assigned_net)
    item.SetNetCode(assigned_net.GetNetCode())
    board.Add(item)


def rectangle(parent, layer, x0, y0, x1, y1):
    for start, end in [((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)),
                       ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))]:
        item = pcbnew.PCB_SHAPE(parent)
        item.SetShape(pcbnew.SHAPE_T_SEGMENT)
        item.SetStart(P(*start))
        item.SetEnd(P(*end))
        item.SetLayer(layer)
        item.SetWidth(pcbnew.FromMM(0.05))
        parent.Add(item)


board = pcbnew.LoadBoard(str(BASE))
if board is None:
    raise RuntimeError(f"Could not load accepted board: {BASE}")
if board.FindFootprintByReference("U3") is not None:
    raise RuntimeError("Source unexpectedly already contains U3")

isolateb = net(board, "ISOLATEB")
rtl_3v3 = net(board, "RTL_3V3")
ssd_3v3 = net(board, "SSD_3V3")
gnd = net(board, "GND")
ilim = net(board, "MIC2545_ILIM")
clkreq = net(board, "CLKREQ_N")

# Authorized local exception applies only to the immediate U1 source escape.
# The adjacent south-row pads are local context; the global board rule is not
# changed and downstream geometry is ordinary 0.20 mm.
u1 = board.FindFootprintByReference("U1")
for number in ("9", "10", "11", "12", "13", "14", "15", "16", "17"):
    u1.FindPadByNumber(number).SetLocalClearance(pcbnew.FromMM(0.15))

# Disposable local source-funnel trial: move the inherited CLKREQ_N F.Cu jog
# to a 0.40/0.20 mm through-via just outside the QFN pad field.  The general
# board via remains 0.60/0.30 mm; this smaller via is local to the QFN escape.
for item in list(board.GetTracks()):
    if item.GetNetCode() != clkreq.GetNetCode() or item.GetLayer() != F:
        continue
    a, z = item.GetStart(), item.GetEnd()
    coords = tuple(pcbnew.ToMM(v) for v in (a.x, a.y, z.x, z.y))
    if max(coords[0], coords[2]) <= 100.1 and min(coords[1], coords[3]) >= 73.8 and max(coords[1], coords[3]) <= 76.1:
        board.Remove(item)
segment(board, clkreq, (99.6, 73.95), (99.6, 72.8), F, NORMAL)
via_small(board, clkreq, 99.6, 72.8)
segment(board, clkreq, (99.6, 72.8), (98.8, 76.0), B)

# U3 is in the measured vacant interior pocket, centered at (151.5, 82.0).
# The pad coordinates are the native 3BX pattern: 5.40 mm row spacing,
# 1.27 mm pitch, and 1.55 x 0.60 mm contacts.
u3 = footprint(board, "U3", "MIC2545A-1YM")
ul, ur = 148.8, 154.2
for number, x, y, assigned_net in [
    (1, ul, 80.095, isolateb),  # EN
    (2, ul, 81.365, None),      # FLG intentionally NC
    (3, ul, 82.635, gnd),       # GND
    (4, ul, 83.905, ilim),      # ILIM
    (5, ur, 83.905, rtl_3v3),   # IN
    (6, ur, 82.635, ssd_3v3),   # OUT
    (7, ur, 81.365, rtl_3v3),   # IN
    (8, ur, 80.095, ssd_3v3),   # OUT
]:
    pad(u3, number, x, y, assigned_net)
rectangle(u3, pcbnew.F_CrtYd, 148.0, 78.0, 155.0, 86.0)
rectangle(u3, pcbnew.F_SilkS, 148.2, 78.2, 154.8, 85.8)

# Corrected MIC2545A support: both IN pins join physically, both OUT pins
# join physically, ILIM uses 76.8 ohm to ground, and C18 bypasses IN to GND.
r15 = footprint(board, "R15", "76.8R_1PCT")
pad(r15, 1, 144.5, 87.8, ilim, (0.8, 0.6))
pad(r15, 2, 144.5, 90.2, gnd, (0.8, 0.6))
c18 = footprint(board, "C18", "100nF_IN_BYPASS")
pad(c18, 1, 160.5, 88.0, rtl_3v3, (0.8, 0.8))
pad(c18, 2, 160.5, 89.6, gnd, (0.8, 0.8))
rectangle(r15, pcbnew.F_CrtYd, 143.8, 87.1, 145.2, 90.9)
rectangle(c18, pcbnew.F_CrtYd, 159.9, 87.4, 161.1, 90.2)

# U1.12 ISOLATEB: the only 0.15-mm geometry is the immediate pad-end
# departure.  It then uses ordinary through-vias and ordinary-width routing.
segment(board, isolateb, (99.2, 73.95), (99.2, 84.0), F, LOCAL)
via(board, isolateb, 99.2, 84.0)
segment(board, isolateb, (99.2, 84.0), (104.2, 86.8), B)
segment(board, isolateb, (104.2, 86.8), (146.8, 86.8), B)
segment(board, isolateb, (146.8, 86.8), (146.8, 80.095), B)
via(board, isolateb, 146.8, 80.095)
segment(board, isolateb, (146.8, 80.095), (148.8, 80.095), F)

# Source rail from U3.5/U3.7 to C18 and the existing RTL_3V3 pad R2.2.
segment(board, rtl_3v3, (154.2, 83.905), (158.0, 83.905), F)
segment(board, rtl_3v3, (154.2, 81.365), (158.0, 81.365), F)
segment(board, rtl_3v3, (158.0, 81.365), (158.0, 88.0), F)
segment(board, rtl_3v3, (158.0, 88.0), (160.5, 88.0), F)
via(board, rtl_3v3, 158.0, 88.0)
segment(board, rtl_3v3, (158.0, 88.0), (158.0, 90.0), B)
segment(board, rtl_3v3, (158.0, 90.0), (122.5, 90.0), B)
via(board, rtl_3v3, 122.5, 90.0)
segment(board, rtl_3v3, (122.5, 90.0), (122.5, 82.0), F)
segment(board, rtl_3v3, (122.5, 82.0), (121.2, 80.0), F)

# Switched output: explicit U3.6/U3.8 B.Cu join, then a clear right-side
# corridor to a normal-width F.Cu access into the existing SSD_3V3 J1 pad bus.
segment(board, ssd_3v3, (154.2, 82.635), (156.0, 82.635), F)
segment(board, ssd_3v3, (154.2, 80.095), (156.0, 80.095), F)
via(board, ssd_3v3, 156.0, 80.095)
segment(board, ssd_3v3, (156.0, 80.095), (156.0, 82.635), B)
via(board, ssd_3v3, 156.0, 82.635)
segment(board, ssd_3v3, (156.0, 82.635), (156.0, 66.0), B)
segment(board, ssd_3v3, (156.0, 66.0), (140.0, 66.0), B)
segment(board, ssd_3v3, (140.0, 66.0), (140.0, 54.0), B)
segment(board, ssd_3v3, (140.0, 54.0), (114.75, 54.0), B)
via(board, ssd_3v3, 114.75, 54.0)
segment(board, ssd_3v3, (114.75, 54.0), (114.75, 62.725), F)

# ILIM and ground support.  Ground vias are tied by explicit copper to a
# ground-zone-covered stitch at (142,84); no synthetic graph edge is used.
segment(board, ilim, (148.8, 83.905), (144.5, 87.8), F)
segment(board, gnd, (144.5, 90.2), (142.0, 92.0), F)
via(board, gnd, 142.0, 92.0)
segment(board, gnd, (142.0, 92.0), (160.5, 92.0), B)
via(board, gnd, 160.5, 92.0)
segment(board, gnd, (160.5, 89.6), (160.5, 92.0), F)
segment(board, gnd, (142.0, 92.0), (97.5, 92.0), B)
segment(board, gnd, (97.5, 92.0), (97.5, 83.0), B)
segment(board, gnd, (97.5, 83.0), (142.0, 83.0), B)
segment(board, gnd, (142.0, 83.0), (142.0, 84.0), B)
via(board, gnd, 142.0, 84.0)
segment(board, gnd, (142.0, 84.0), (142.0, 78.0), B)
segment(board, gnd, (142.0, 78.0), (115.6, 78.0), B)
segment(board, gnd, (148.8, 82.635), (142.0, 84.0), F)

pcbnew.ZONE_FILLER(board).Fill(board.Zones())
board.Save(str(OUT))
print(OUT)
