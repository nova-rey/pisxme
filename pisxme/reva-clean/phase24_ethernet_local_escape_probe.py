"""Focused source-to-ESD Ethernet escape probe on the selected macro basis.

This is intentionally not a production route: it tests the local CM5/J7 to
ESD topology before connector-field launch. Every endpoint and net is read
from the saved board; no synthetic connectivity is introduced.
"""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb'
OUT=R/'PHASE24_ETHERNET_LOCAL_ESCAPE_PROBE.kicad_pcb'
F=pcbnew.F_Cu
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def pos(p):
    q=p.GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def add(b,net,a,z):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(0.127));t.SetNet(net);b.Add(t)
b=pcbnew.LoadBoard(str(BASE))
# A 0-degree orientation presents each four-channel ESD group as a vertical,
# monotonic pad field relative to the native J7 source lanes.
b.FindFootprintByReference('U6').SetOrientationDegrees(0)
b.FindFootprintByReference('U9').SetOrientationDegrees(0)
for item in list(b.GetTracks()):
    if 'CM5_GBE_TD' in item.GetNetname(): b.Remove(item)
mapping=[('CM5_GBE_TD3_P','3','U9','10'),('CM5_GBE_TD3_N','5','U9','9'),('CM5_GBE_TD2_N','9','U9','7'),('CM5_GBE_TD2_P','11','U9','6'),('CM5_GBE_TD1_P','4','U6','10'),('CM5_GBE_TD1_N','6','U6','9'),('CM5_GBE_TD0_N','10','U6','7'),('CM5_GBE_TD0_P','12','U6','6')]
for name,sp,er,ep in mapping:
    net=b.FindNet(name); a=pos(pad(b,'J7',sp)); e=pad(b,er,ep); z=pos(e)
    add(b,net,a,z)
    # The ESD package duplicates each signal on the opposite row. Join only
    # the same-net duplicate within the manufacturer footprint field.
    for q in b.FindFootprintByReference(er).Pads():
        if q.GetNetname()==name and q.GetNumber()!=ep: add(b,net,z,pos(q))
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
