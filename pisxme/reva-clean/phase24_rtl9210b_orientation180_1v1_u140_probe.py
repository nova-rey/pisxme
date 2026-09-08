"""Disposable U1.40-to-C4.1 bottom-edge 1V1 channel."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_1V1_U136_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_1V1_U140_PROBE_V2.kicad_pcb'
F,W=pcbnew.F_Cu,pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
s(b,n,(96.80,73.95),(95.80,74.80));s(b,n,(95.80,74.80),(95.80,77.50));s(b,n,(95.80,77.50),(107.00,77.50));s(b,n,(107.00,77.50),(107.00,70.00))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
