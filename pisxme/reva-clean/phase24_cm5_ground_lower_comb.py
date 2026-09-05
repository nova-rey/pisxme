"""Disposable lower-bank CM5-ground comb, excluding active high-speed rows."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_BRIDGE_3V3_CAP_CHAIN_V2.kicad_pcb';OUT=R/'PHASE24_CM5_GROUND_LOWER_COMB.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('/CORE_CM5/POWER_GND');f=b.FindFootprintByReference('J7')
V=lambda x,y:pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(a,z):
    t=pcbnew.PCB_TRACK(b);t.SetLayer(pcbnew.F_Cu);t.SetNet(n);t.SetWidth(pcbnew.FromMM(.20));t.SetStart(V(*a));t.SetEnd(V(*z));b.Add(t)
rows={}
for p in f.Pads():
    q=p.GetPosition();x=round(q.x/1e6,2);y=round(q.y/1e6,2)
    if p.GetNetCode()==n.GetNetCode() and 102.7<=y<=117.9 and x in (32.96,36.04): rows.setdefault(y,[]).append(x)
left=sorted(y for y,xs in rows.items() if 32.96 in xs);right=sorted(y for y,xs in rows.items() if 36.04 in xs)
for y,xs in rows.items():
    if 32.96 in xs: tr((32.96,y),(31.4,y))
    if 36.04 in xs: tr((36.04,y),(37.6,y))
for ys,x in ((left,31.4),(right,37.6)):
    for a,z in zip(ys,ys[1:]): tr((x,a),(x,z))
for y,xs in rows.items():
    if len(xs)==2: tr((31.4,y),(37.6,y))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
