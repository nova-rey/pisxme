"""V1464: correct the native U1.65 pad coordinate while joining U1.66 GND."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_ACCEPTED_PRIMITIVES_V1428.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_U166_JOIN_CORRECT_RXP_V1464.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)
b = pcbnew.LoadBoard(str(BASE))

def n(name):
    value = b.FindNet(name)
    assert value is not None, name
    return value
def p(x, y): return pcbnew.VECTOR2I_MM(x, y)
def remove(name):
    code = n(name).GetNetCode()
    for item in list(b.GetTracks()):
        if item.GetNetCode() == code: b.RemoveNative(item)
def seg(name, a, z, layer):
    nn = n(name); t = pcbnew.PCB_TRACK(b)
    t.SetStart(p(*a)); t.SetEnd(p(*z)); t.SetLayer(layer); t.SetWidth(W)
    t.SetNet(nn); t.SetNetCode(nn.GetNetCode()); b.Add(t)
def via(name, xy):
    nn = n(name); v = pcbnew.PCB_VIA(b); v.SetPosition(p(*xy))
    v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30))
    v.SetLayerPair(F, B); v.SetNet(nn); v.SetNetCode(nn.GetNetCode()); b.Add(v)

# Native-loaded pad centers are U1.65=(94.05,72.00), U1.66=(94.05,72.40).
# The parent RXP source was at y=71.60, so it was not a valid pad-centered
# departure.  Rebuild only RXP against the actual pad and preserve its remote
# corridor; the direct GND trace terminates on the exposed-pad edge.
remove("LANE0_RXP")
seg("LANE0_RXP", (94.05,72.00), (92.80,72.00), F)
seg("LANE0_RXP", (92.80,72.00), (92.80,70.80), F)
via("LANE0_RXP", (92.80,70.80))
seg("LANE0_RXP", (92.80,70.80), (92.80,82.00), B)
via("LANE0_RXP", (92.80,82.00))
seg("LANE0_RXP", (92.80,82.00), (95.00,82.00), F)
seg("GND", (94.05,72.40), (95.60,72.40), F)

b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT))
print(OUT)
