"""Disposable native stitch for U7's repeated BRIDGE_3V3 pads."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_U7_CLOCK_PAD_NET_AUTHORITY.kicad_pcb'; OUT=R/'PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/STORAGE/BRIDGE_3V3'); V=lambda x,y:pcbnew.VECTOR2I_MM(float(x),float(y))
def P(num): return next(x for x in b.FindFootprintByReference('U7').Pads() if x.GetNumber()==num).GetPosition()
def T(a,z):
 q=pcbnew.PCB_TRACK(b);q.SetLayer(pcbnew.F_Cu);q.SetNet(n);q.SetWidth(pcbnew.FromMM(.20));q.SetStart(a);q.SetEnd(z);b.Add(q)
p24,p30,p31=P('24'),P('30'),P('31')
T(p30,p31); T(p24,V(119.0,146.5)); T(V(119.0,146.5),V(122.5,146.5)); T(V(122.5,146.5),p31)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
