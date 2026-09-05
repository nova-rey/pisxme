"""Apply the previously validated U7 RX-N pad-field stitch to the cumulative candidate."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_LOCAL_REPAIRS_COMPOSED.kicad_pcb"
OUT = ROOT / "PHASE24_LOCAL_REPAIRS_U7_RXN.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))
n = b.FindNet("/STORAGE/BRIDGE_SATA_RX_N")


def p(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def t(layer, a, z):
    q = pcbnew.PCB_TRACK(b)
    q.SetStart(p(*a)); q.SetEnd(p(*z)); q.SetLayer(layer)
    q.SetWidth(pcbnew.FromMM(0.20)); q.SetNet(n); b.Add(q)


def v(q):
    x = pcbnew.PCB_VIA(b)
    x.SetPosition(p(*q)); x.SetWidth(pcbnew.FromMM(0.50))
    x.SetDrill(pcbnew.FromMM(0.30)); x.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    x.SetNet(n); b.Add(x)


for y1, y2 in zip((142.5, 142.0, 141.5, 141.0), (142.0, 141.5, 141.0, 140.5)):
    t(pcbnew.F_Cu, (124.5, y1), (124.5, y2))
t(pcbnew.F_Cu, (124.5, 140.5), (127.5, 140.5)); v((127.5, 140.5))
t(pcbnew.B_Cu, (127.5, 140.5), (127.5, 132.0))
t(pcbnew.B_Cu, (127.5, 132.0), (119.5, 132.0))
t(pcbnew.B_Cu, (119.5, 132.0), (119.5, 134.5)); v((119.5, 134.5))
t(pcbnew.F_Cu, (119.5, 134.5), (119.5, 135.5))

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
