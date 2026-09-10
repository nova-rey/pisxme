"""V78: separated BRIDGE_R1 escape beside the accepted V75 return route."""
from pathlib import Path
import pcbnew
H = Path(__file__).resolve().parent
BASE = H / "PHASE24_STORAGE_CM5_USB4_MONOTONIC_V75_BRIDGE_R1RTN_R24_SIDE.kicad_pcb"
OUT = H / "PHASE24_STORAGE_CM5_USB4_MONOTONIC_V78_BRIDGE_R1_SEPARATED.kicad_pcb"
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.20)
def P(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
b = pcbnew.LoadBoard(str(BASE))
n = b.FindNet("BRIDGE_R1")
assert n
for t in list(b.GetTracks()):
    if t.GetNetCode() == n.GetNetCode(): b.RemoveNative(t)
def seg(a, z, layer):
    t = pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(p):
    v = pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.6))
    v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F, B); v.SetNet(n)
    v.SetNetCode(n.GetNetCode()); b.Add(v)
# U7.38 is immediately above U7.39.  Use a separate x-column and a B.Cu
# shelf two millimetres above V75's BRIDGE_R1RTN shelf.
seg((92.2,123.0), (89.5,123.0), F); via((89.5,123.0))
seg((89.5,123.0), (89.5,116.0), B)
seg((89.5,116.0), (135.5,116.0), B); via((135.5,116.0))
seg((135.5,116.0), (135.5,121.0), F)
seg((135.5,121.0), (137.0,122.0), F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
