"""Disposable current-candidate CM5 ground launch/plane test.

All geometry is derived from the saved J7 footprint.  The CM5 ground net is
kept distinct from global POWER_GND; this tests only physical access to its
own In1 island.
"""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb"
OUT = R / "PHASE24_CM5_GROUND_CURRENT_PLANE.kicad_pcb"
b = pcbnew.LoadBoard(str(BASE))
n = b.FindNet("/CORE_CM5/POWER_GND")
j7 = b.FindFootprintByReference("J7")
V = lambda x, y: pcbnew.VECTOR2I_MM(float(x), float(y))

def add_track(a, z, layer=pcbnew.F_Cu, width=.20):
    t = pcbnew.PCB_TRACK(b); t.SetLayer(layer); t.SetNet(n)
    t.SetWidth(pcbnew.FromMM(width)); t.SetStart(V(*a)); t.SetEnd(V(*z)); b.Add(t)

def add_via(x, y):
    v = pcbnew.PCB_VIA(b); v.SetNet(n); v.SetPosition(V(x, y))
    v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30));
    v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); b.Add(v)

# Leave the high-speed/reference rows untouched.  Launch the lower CM5
# ground banks outward, then join only by a separate same-net plane island.
points = []
for pad in j7.Pads():
    if pad.GetNetCode() != n.GetNetCode(): continue
    q = pad.GetPosition(); x, y = q.x/1e6, q.y/1e6
    if y < 102.7: continue
    vx = x - 1.46 if x < 50 else x + 1.46
    add_track((x, y), (vx, y)); add_via(vx, y); points.append((vx, y))

z = pcbnew.ZONE(b); z.SetLayer(pcbnew.In1_Cu); z.SetNet(n); z.SetNetCode(n.GetNetCode())
z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL); z.SetZoneName("REV_A_CM5_GND_CURRENT")
poly = pcbnew.VECTOR_VECTOR2I()
for xy in ((30.7, 102.0), (72.8, 102.0), (72.8, 119.0), (30.7, 119.0)): poly.append(V(*xy))
z.AddPolygon(poly); b.Add(z)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
