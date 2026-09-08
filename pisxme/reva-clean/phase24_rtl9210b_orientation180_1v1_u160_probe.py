"""Disposable U1.60-to-C4.1 RTL_1V1 channel on V631."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_RAILS_PROBE_V7.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_1V1_U160_PROBE.kicad_pcb'
F,W=pcbnew.F_Cu,pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1')
s(b,n,(101.95,70.0),(107.0,70.0));s(b,n,(107.0,70.0),(107.0,80.0));s(b,n,(107.0,80.0),(104.0,80.0));s(b,n,(104.0,80.0),(104.0,82.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
