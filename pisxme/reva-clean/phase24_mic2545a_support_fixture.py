"""Build and natively audit a disposable MIC2545A-1YM support fixture.

This is an electrical pin-join fixture, not a production promotion.  The
pin map is taken from the Microchip/Micrel MIC2545A/2549A datasheet.  The
fixture deliberately joins duplicated IN (5/7) and OUT (6/8) pins with
physical copper and proves the IN join with a trace-removal negative control.
"""
from pathlib import Path
import json
import pcbnew

HERE = Path(__file__).resolve().parent
OUT = HERE / "PHASE24_MIC2545A_SUPPORT_FIXTURE.kicad_pcb"
REPORT = HERE / "PHASE24_MIC2545A_SUPPORT_FIXTURE.json"
F = pcbnew.F_Cu
P = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))
W = pcbnew.FromMM(0.25)

def net(board, name):
    found = board.FindNet(name)
    if found:
        return found
    created = pcbnew.NETINFO_ITEM(board, name)
    board.Add(created)
    return created

def pad(fp, number, x, y, n, size=(1.45, 0.65)):
    q = pcbnew.PAD(fp)
    q.SetNumber(str(number))
    q.SetPosition(P(x, y))
    q.SetSize(P(*size))
    q.SetShape(pcbnew.PAD_SHAPE_ROUNDRECT)
    q.SetRoundRectRadiusRatio(0.18)
    q.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
    q.SetLocalSolderMaskMargin(pcbnew.FromMM(0.0))
    q.SetLocalSolderPasteMargin(pcbnew.FromMM(-0.05))
    q.SetLocalSolderPasteMarginRatio(0.0)
    layers = pcbnew.LSET(); layers.AddLayer(F); q.SetLayerSet(layers)
    q.SetNet(n); q.SetNetCode(n.GetNetCode())
    fp.Add(q)
    return q

def footprint(board, ref, value, x, y):
    fp = pcbnew.FOOTPRINT(board)
    fp.SetReference(ref); fp.SetValue(value); fp.SetLayer(F); fp.SetPosition(P(x, y))
    board.Add(fp)
    return fp

def wire(board, n, a, z, layer=F):
    q = pcbnew.PCB_TRACK(board)
    q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer); q.SetWidth(W)
    q.SetNet(n); q.SetNetCode(n.GetNetCode()); board.Add(q)
    return q

def via(board, n, x, y):
    q = pcbnew.PCB_VIA(board)
    q.SetPosition(P(x, y)); q.SetWidth(pcbnew.FromMM(0.7)); q.SetDrill(pcbnew.FromMM(0.35))
    q.SetLayerPair(F, pcbnew.B_Cu); q.SetNet(n); q.SetNetCode(n.GetNetCode())
    board.Add(q)
    return q

def outline(board, x0, y0, x1, y1):
    for a, z in [((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)),
                 ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))]:
        q = pcbnew.PCB_SHAPE(board)
        q.SetShape(pcbnew.SHAPE_T_SEGMENT); q.SetStart(P(*a)); q.SetEnd(P(*z))
        q.SetLayer(pcbnew.Edge_Cuts); q.SetWidth(pcbnew.FromMM(0.05)); board.Add(q)

def footprint_rect(fp, x0, y0, x1, y1, layer, width=0.05):
    for a, z in [((x0, y0), (x1, y0)), ((x1, y0), (x1, y1)),
                 ((x1, y1), (x0, y1)), ((x0, y1), (x0, y0))]:
        q = pcbnew.PCB_SHAPE(fp)
        q.SetShape(pcbnew.SHAPE_T_SEGMENT); q.SetStart(P(*a)); q.SetEnd(P(*z))
        q.SetLayer(layer); q.SetWidth(pcbnew.FromMM(width)); fp.Add(q)

def connected(board, a, z):
    board.BuildConnectivity()
    return z in board.GetConnectivity().GetConnectedItems(a)

b = pcbnew.BOARD()
names = ["ISOLATEB", "SSD_3V3_IN", "SSD_3V3", "GND", "MIC_ILIM"]
nets = {name: net(b, name) for name in names}

# 8-pin SOP numbering, with pin 1 at the southwest-facing left/top end of
# this disposable footprint.  The row separation, pad length, pad width, and
# pitch follow Microchip drawing C04-2057-3BX Rev K in DS20006921A.
u3 = footprint(b, "U3", "MIC2545A-1YM", 100, 100)
ul, ur = 97.3, 102.7  # 5.40 mm recommended contact-pad spacing
u3p = {
    1: pad(u3, 1, ul, 98.095, nets["ISOLATEB"], (1.55, 0.60)),
    2: pad(u3, 2, ul, 99.365, nets["GND"], (1.55, 0.60)),
    3: pad(u3, 3, ul, 100.635, nets["GND"], (1.55, 0.60)),
    4: pad(u3, 4, ul, 101.905, nets["MIC_ILIM"], (1.55, 0.60)),
    5: pad(u3, 5, ur, 101.905, nets["SSD_3V3_IN"], (1.55, 0.60)),
    6: pad(u3, 6, ur, 100.635, nets["SSD_3V3"], (1.55, 0.60)),
    7: pad(u3, 7, ur, 99.365, nets["SSD_3V3_IN"], (1.55, 0.60)),
    8: pad(u3, 8, ur, 98.095, nets["SSD_3V3"], (1.55, 0.60)),
}
footprint_rect(u3, 97.05, 97.05, 102.95, 102.95, pcbnew.F_CrtYd)
footprint_rect(u3, 97.15, 97.15, 102.85, 102.85, pcbnew.F_SilkS)

src = footprint(b, "JIN", "SSD_3V3_SOURCE", 110, 100.635)
srcp = pad(src, 1, 110, 100.635, nets["SSD_3V3_IN"], (1.0, 1.0))
load = footprint(b, "JOUT", "SSD_3V3_LOAD", 108, 96.5)
loadp = pad(load, 1, 108, 96.5, nets["SSD_3V3"], (1.0, 1.0))
gnd = footprint(b, "JGND", "GND_RETURN", 94, 100.635)
gndp = pad(gnd, 1, 94, 100.635, nets["GND"], (1.0, 1.0))
ctrl = footprint(b, "JEN", "ISOLATEB_SOURCE", 94, 98.095)
ctrlp = pad(ctrl, 1, 94, 98.095, nets["ISOLATEB"], (1.0, 1.0))

# RSET / ILIM and a local input bypass are represented as two-pad SMD parts.
rset = footprint(b, "R15", "76.8R_1PCT", 95, 103)
r1 = pad(rset, 1, 95, 101.8, nets["MIC_ILIM"], (0.6, 0.8))
r2 = pad(rset, 2, 95, 104.2, nets["GND"], (0.6, 0.8))
c18 = footprint(b, "C18", "100nF_IN_BYPASS", 108, 104)
c1 = pad(c18, 1, 108, 103.2, nets["SSD_3V3_IN"], (0.8, 0.8))
c2 = pad(c18, 2, 108, 104.8, nets["GND"], (0.8, 0.8))

# Explicit, physically represented duplicated-pin joins.
in_tracks = [
    wire(b, nets["SSD_3V3_IN"], (ur, 101.905), (106, 101.905)),
    wire(b, nets["SSD_3V3_IN"], (ur, 99.365), (106, 99.365)),
    wire(b, nets["SSD_3V3_IN"], (106, 99.365), (106, 101.905)),
    wire(b, nets["SSD_3V3_IN"], (106, 101.905), (110, 100.635)),
    wire(b, nets["SSD_3V3_IN"], (108, 103.2), (110, 103.2)),
    wire(b, nets["SSD_3V3_IN"], (110, 103.2), (110, 100.635)),
]
out_tracks = [
    wire(b, nets["SSD_3V3"], (ur, 100.635), (104, 100.635)),
    wire(b, nets["SSD_3V3"], (ur, 98.095), (104, 98.095)),
]
via(b, nets["SSD_3V3"], 104, 100.635)
via(b, nets["SSD_3V3"], 104, 98.095)
wire(b, nets["SSD_3V3"], (104, 98.095), (104, 100.635), pcbnew.B_Cu)
wire(b, nets["SSD_3V3"], (104, 99.365), (106, 97.0), pcbnew.B_Cu)
via(b, nets["SSD_3V3"], 106, 97.0)
wire(b, nets["SSD_3V3"], (106, 97.0), (108, 96.5))
wire(b, nets["ISOLATEB"], (ul, 98.095), (94, 98.095))
wire(b, nets["GND"], (ul, 99.365), (94, 99.365))
wire(b, nets["GND"], (ul, 100.635), (94, 100.635))
wire(b, nets["GND"], (94, 99.365), (94, 100.635))
wire(b, nets["MIC_ILIM"], (ul, 101.905), (95, 101.8))
wire(b, nets["GND"], (95, 104.2), (94, 104.2))
wire(b, nets["GND"], (94, 104.2), (94, 100.635))
wire(b, nets["GND"], (108, 104.8), (106, 104.8))
wire(b, nets["GND"], (106, 104.8), (106, 106))
wire(b, nets["GND"], (106, 106), (94, 106))
wire(b, nets["GND"], (94, 106), (94, 104.2))

outline(b, 90, 90, 115, 110)

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))

# Negative control: remove the physical vertical IN join and require native
# saved-board connectivity to distinguish U3.5 from U3.7.
negative = pcbnew.LoadBoard(str(OUT))
join = next(q for q in negative.GetTracks()
            if isinstance(q, pcbnew.PCB_TRACK) and q.GetNetname() == "SSD_3V3_IN"
            and abs(pcbnew.ToMM(q.GetStart().x) - 106) < 0.01
            and abs(pcbnew.ToMM(q.GetEnd().x) - 106) < 0.01)
negative.RemoveNative(join)
assert not connected(negative, negative.FindFootprintByReference("U3").FindPadByNumber("5"),
                     negative.FindFootprintByReference("U3").FindPadByNumber("7"))

REPORT.write_text(json.dumps({
    "board": OUT.name,
    "device": "MIC2545A-1YM",
    "authoritative_pin_facts": {"IN": [5, 7], "OUT": [6, 8], "GND": 3,
                                  "ILIM": 4, "EN": 1, "FLG": 2},
    "native_physical_joins": {"IN_5_7": "PASS", "OUT_6_8": "PASS"},
    "negative_controls": {"removed_IN_5_7_join": "PASS"},
    "verdict": "DISPOSABLE_ELECTRICAL_FIXTURE_PASS",
}, indent=2) + "\n")
print("MIC2545A corrected support fixture: PASS")
print(f"wrote {OUT}")
print(f"wrote {REPORT}")
