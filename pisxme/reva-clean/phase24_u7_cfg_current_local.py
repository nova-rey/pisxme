"""Disposable native BRIDGE_CFG join on the current Phase 24 candidate."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_POWER_GND_CURRENT_LOCAL.kicad_pcb'; OUT=R/'PHASE24_U7_CFG_CURRENT_LOCAL.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/STORAGE/BRIDGE_CFG')
def pad(ref,num):
    f=b.FindFootprintByReference(ref)
    return next(p for p in f.Pads() if p.GetNumber()==num)
V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
src=pad('U7','21').GetPosition(); dst=pad('U7','1').GetPosition()
# Escape downward from both pads, then join on B.Cu below the U7 field.
sx,sy=src.x/1e6,src.y/1e6; dx,dy=dst.x/1e6,dst.y/1e6
lane_y=145.5
for a,z in [((sx,sy),(sx,lane_y)),((sx,lane_y),(114.0,lane_y)),
            ((dx,dy),(dx,lane_y)),((dx,lane_y),(129.0,lane_y)),
            ((114.0,lane_y),(129.0,lane_y))]:
    layer=pcbnew.B_Cu if a[1]==lane_y and z[1]==lane_y else pcbnew.F_Cu
    t=pcbnew.PCB_TRACK(b); t.SetLayer(layer); t.SetNet(n); t.SetWidth(pcbnew.FromMM(.20)); t.SetStart(V(*a)); t.SetEnd(V(*z)); b.Add(t)
for x in (114.0,129.0):
    v=pcbnew.PCB_VIA(b); v.SetNet(n); v.SetPosition(V(x,lane_y)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); b.Add(v)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
