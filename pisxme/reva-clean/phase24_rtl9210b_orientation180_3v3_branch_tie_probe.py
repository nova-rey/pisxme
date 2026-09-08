"""Disposable physical tie for the separated lower RTL_3V3 branches."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_GND_RETURN_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_3V3_BRANCH_TIE_PROBE.kicad_pcb'
B,W=pcbnew.B_Cu,pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(B);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
# Existing vias are at the ends of the U1.34 and U1.39 source exits.
s(b,n,(90.0,73.2),(90.0,76.5));s(b,n,(90.0,76.5),(96.4,76.5));s(b,n,(96.4,76.5),(96.4,75.2))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
