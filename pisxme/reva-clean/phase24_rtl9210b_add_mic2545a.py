"""Add the corrected MIC2545A SSD-power switch to an isolated Path-B board.

The accepted V1603/V1517 candidate is never overwritten.  This generator
creates a new integration candidate and uses only native saved-board objects.
"""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / "PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb"
OUT = HERE / "PHASE24_RTL9210B_PATHB_MIC2545A_ISOLATEB.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
P = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))
W = pcbnew.FromMM(0.25)

def getnet(board, name):
    n = board.FindNet(name)
    if n:
        return n
    n = pcbnew.NETINFO_ITEM(board, name); board.Add(n); return n

def add_pad(fp, number, x, y, n, size=(1.55, 0.60)):
    q = pcbnew.PAD(fp); q.SetNumber(str(number)); q.SetPosition(P(x, y))
    q.SetSize(P(*size)); q.SetShape(pcbnew.PAD_SHAPE_ROUNDRECT)
    q.SetRoundRectRadiusRatio(0.18); q.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
    q.SetLocalSolderMaskMargin(pcbnew.FromMM(0.0))
    q.SetLocalSolderPasteMargin(pcbnew.FromMM(-0.05))
    q.SetLocalSolderPasteMarginRatio(0.0)
    ls = pcbnew.LSET(); ls.AddLayer(F); q.SetLayerSet(ls)
    q.SetNet(n); q.SetNetCode(n.GetNetCode()); fp.Add(q); return q

def add_fp(board, ref, value, x, y):
    fp = pcbnew.FOOTPRINT(board); fp.SetReference(ref); fp.SetValue(value)
    fp.SetLayer(F); fp.SetPosition(P(x, y)); board.Add(fp); return fp

def wire(board, n, a, z, layer=F, width=W):
    q = pcbnew.PCB_TRACK(board); q.SetStart(P(*a)); q.SetEnd(P(*z))
    q.SetLayer(layer); q.SetWidth(width); q.SetNet(n); q.SetNetCode(n.GetNetCode())
    board.Add(q); return q

def via(board, n, x, y):
    q = pcbnew.PCB_VIA(board); q.SetPosition(P(x, y)); q.SetWidth(pcbnew.FromMM(0.7))
    q.SetDrill(pcbnew.FromMM(0.35)); q.SetLayerPair(F, B)
    q.SetNet(n); q.SetNetCode(n.GetNetCode()); board.Add(q); return q

def rect(fp, x0, y0, x1, y1, layer):
    for a, z in [((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)),
                 ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))]:
        q = pcbnew.PCB_SHAPE(fp); q.SetShape(pcbnew.SHAPE_T_SEGMENT)
        q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
        q.SetWidth(pcbnew.FromMM(0.05)); fp.Add(q)

b = pcbnew.LoadBoard(str(BASE))
isolate = getnet(b, "ISOLATEB"); inrail = getnet(b, "RTL_3V3")
ssd = getnet(b, "SSD_3V3"); gnd = getnet(b, "GND"); ilim = getnet(b, "MIC2545_ILIM")

# U3 centered at (130,85), using Microchip's current 3BX recommended contact
# geometry.  Left pins 1..4, right pins 5..8, counter-clockwise numbering.
u3 = add_fp(b, "U3", "MIC2545A-1YM", 130, 85)
ul, ur = 127.3, 132.7
for num, x, y, n in [
    (1, ul, 83.095, isolate), (2, ul, 84.365, gnd),
    (3, ul, 85.635, gnd), (4, ul, 86.905, ilim),
    (5, ur, 86.905, inrail), (6, ur, 85.635, ssd),
    (7, ur, 84.365, inrail), (8, ur, 83.095, ssd)]:
    add_pad(u3, num, x, y, n)
rect(u3, 127.05, 82.05, 132.95, 87.95, pcbnew.F_CrtYd)
rect(u3, 127.15, 82.15, 132.85, 87.85, pcbnew.F_SilkS)

# EN: U1 pin 12 -> U3 pin 1, with an ordinary through-via at each pad escape.
via(b, isolate, 101.8, 74.8); wire(b, isolate, (99.2, 73.95), (101.8, 74.8))
wire(b, isolate, (101.8, 74.8), (106, 81.5), B)
wire(b, isolate, (106, 81.5), (127.3, 83.095), B); via(b, isolate, 127.3, 83.095)

# Source rail: both MIC2545A IN pins are physically tied, then join existing
# RTL_3V3 support at R2.2.  This intentionally uses a separate rail branch.
wire(b, inrail, (132.7, 86.905), (136, 86.905))
wire(b, inrail, (132.7, 84.365), (136, 84.365))
wire(b, inrail, (136, 84.365), (136, 86.905))
wire(b, inrail, (136, 84.365), (136, 80))
wire(b, inrail, (136, 80), (121.2, 80))

# Switched output: both OUT pins are tied on B.Cu, then returned to the real
# M.2 SSD_3V3 contacts at J1.2.  The final F.Cu segment is the connector launch.
wire(b, ssd, (132.7, 85.635), (134, 85.635))
wire(b, ssd, (132.7, 83.095), (134, 83.095))
via(b, ssd, 134, 85.635); via(b, ssd, 134, 83.095)
wire(b, ssd, (134, 83.095), (134, 85.635), B)
wire(b, ssd, (134, 84.365), (124, 90), B)
wire(b, ssd, (124, 90), (116, 80), B)
wire(b, ssd, (116, 80), (116, 72), B); via(b, ssd, 116, 72)
wire(b, ssd, (116, 72), (114.75, 62.725), F)

# ILIM and ground support.  Ground vias are explicit physical endpoints; no
# synthetic plane connectivity is introduced.
r15 = add_fp(b, "R15", "76.8R_1PCT", 124, 88)
add_pad(r15, 1, 124, 86.8, ilim, (0.8, 0.6)); add_pad(r15, 2, 124, 89.2, gnd, (0.8, 0.6))
wire(b, ilim, (127.3, 86.905), (124, 86.8)); wire(b, gnd, (124, 89.2), (124, 90), F); via(b, gnd, 124, 90)
c18 = add_fp(b, "C18", "100nF_IN_BYPASS", 136, 90)
add_pad(c18, 1, 136, 89.2, inrail, (0.8, 0.8)); add_pad(c18, 2, 136, 90.8, gnd, (0.8, 0.8))
wire(b, inrail, (136, 86.905), (136, 89.2)); wire(b, gnd, (136, 90.8), (136, 92)); via(b, gnd, 136, 92)

pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
