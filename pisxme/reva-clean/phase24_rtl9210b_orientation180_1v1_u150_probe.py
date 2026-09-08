"""Disposable U1.50-to-C4.1 1V1 extension on V636."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_1V1_U125_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_1V1_U150_PROBE.kicad_pcb'
F,W=pcbnew.F_Cu,pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
s(b,n,(100.80,73.95),(100.80,78.00));s(b,n,(100.80,78.00),(107.00,78.00));s(b,n,(107.00,78.00),(107.00,70.00))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
