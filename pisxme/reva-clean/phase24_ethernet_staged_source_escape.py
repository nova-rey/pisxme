"""Staged split-layer J7-to-ESD Ethernet escape probe.

This probe deliberately validates only source-to-protection escape geometry.
All nets and pads come from the saved PCB; duplicate ESD-pad joins and the
MagJack launch are not fabricated here and remain explicitly unconnected.
"""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb'
OUT=R/'PHASE24_ETHERNET_STAGED_SOURCE_ESCAPE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=pcbnew.FromMM(0.127)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def pos(p):
 q=p.GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def track(b,net,a,z,layer):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(layer);t.SetWidth(W);t.SetNet(net);b.Add(t)
def via(b,net,x,y):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(x,y));v.SetWidth(pcbnew.FromMM(.45));v.SetDrill(pcbnew.FromMM(.20));v.SetLayerPair(F,B);v.SetNet(net);b.Add(v)
b=pcbnew.LoadBoard(str(BASE))
for ref,xy0 in [('U6',(20,104)),('U9',(26,104))]:
 f=b.FindFootprintByReference(ref);f.SetPosition(V(*xy0));f.SetOrientationDegrees(0)
for item in list(b.GetTracks()):
 if 'CM5_GBE_TD' in item.GetNetname(): b.Remove(item)
# Source order is native J7 top-to-bottom.  The staged lanes deliberately
# widen before entering the ESD pad fields.
rows=[
 ('CM5_GBE_TD3_P','3','U9','10',31.0,74.0,27.8),
 ('CM5_GBE_TD3_N','5','U9','9',30.2,75.0,26.6),
 ('CM5_GBE_TD2_N','9','U9','7',29.4,76.0,25.4),
 ('CM5_GBE_TD2_P','11','U9','6',28.6,77.0,24.2),
 ('CM5_GBE_TD1_P','4','U6','10',37.0,74.0,22.0),
 ('CM5_GBE_TD1_N','6','U6','9',37.8,75.0,20.7),
 ('CM5_GBE_TD0_N','10','U6','7',38.6,76.0,19.4),
 ('CM5_GBE_TD0_P','12','U6','6',39.4,77.0,18.1),
]
for name,sp,er,ep,xv,yt,xend in rows:
 net=b.FindNet(name);s=pos(pad(b,'J7',sp));e=pos(pad(b,er,ep))
 # Native F.Cu departure, transition outside the J7 source pad columns.
 track(b,net,s,(xv,s[1]),F);via(b,net,xv,s[1])
 # B.Cu staged lane around the dense module/pad field.
 track(b,net,(xv,s[1]),(xv,yt),B);track(b,net,(xv,yt),(xend,yt),B)
 # Return to F.Cu outside the ESD footprint, then short dogbone to target.
 via(b,net,xend,102.0);track(b,net,(xend,102.0),(xend,e[1]),F);track(b,net,(xend,e[1]),e,F)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
