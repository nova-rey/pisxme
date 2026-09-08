"""Disposable crystal-support relocation and local routing trial."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_3V3_C3_JOIN_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_CRYSTAL_LOCAL_RELOCATION_PROBE.kicad_pcb'
F,W=pcbnew.F_Cu,pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(BASE))
b.FindFootprintByReference('Y1').SetPosition(p(105.0,76.0))
b.FindFootprintByReference('C1').SetPosition(p(103.0,78.0))
b.FindFootprintByReference('C2').SetPosition(p(107.0,78.0))
ni=b.FindNet('XTAL_IN');no=b.FindNet('XTAL_OUT')
s(b,ni,(101.95,72.8),(104.3,74.5));s(b,ni,(104.3,74.5),(104.3,76.0));s(b,ni,(104.3,76.0),(103.6,78.0))
s(b,no,(101.95,72.4),(105.7,74.5));s(b,no,(105.7,74.5),(105.7,76.0));s(b,no,(105.7,76.0),(106.4,78.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
