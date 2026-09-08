"""Disposable U1.55/U1.63 right-edge 1V1 extensions on V637."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_1V1_U150_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_1V1_U155_U163_PROBE_V2.kicad_pcb'
F,W=pcbnew.F_Cu,pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
s(b,n,(101.95,72.00),(107.00,72.00));s(b,n,(107.00,72.00),(107.00,70.00))
s(b,n,(101.95,68.80),(108.00,68.80));s(b,n,(108.00,68.80),(108.00,70.00))
s(b,n,(108.00,70.00),(107.00,70.00))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
