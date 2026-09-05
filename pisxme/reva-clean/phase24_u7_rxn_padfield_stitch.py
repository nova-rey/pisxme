"""Disposable U7 repeated-pad SATA RX-N stitch using offset through-vias."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb';OUT=R/'PHASE24_U7_RXN_PADFIELD_STITCH.kicad_pcb'
NET='/STORAGE/BRIDGE_SATA_RX_N'
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,a,z,l=pcbnew.F_Cu):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.2));t.SetNet(n);b.Add(t)
def X(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*q));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);b.Add(v)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet(NET);u=b.FindFootprintByReference('U7')
# Join the five duplicated RX-N pads in the serialized pad column.
for y1,y2 in zip((142.5,142.0,141.5,141.0),(142.0,141.5,141.0,140.5)):T(b,n,(124.5,y1),(124.5,y2))
# Leave the pad field through two offset vias and join the existing external pad.
T(b,n,(124.5,140.5),(127.5,140.5));X(b,n,(127.5,140.5));T(b,n,(127.5,140.5),(127.5,132.0),pcbnew.B_Cu);T(b,n,(127.5,132.0),(119.5,132.0),pcbnew.B_Cu);T(b,n,(119.5,132.0),(119.5,134.5),pcbnew.B_Cu);X(b,n,(119.5,134.5));T(b,n,(119.5,134.5),(119.5,135.5))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
