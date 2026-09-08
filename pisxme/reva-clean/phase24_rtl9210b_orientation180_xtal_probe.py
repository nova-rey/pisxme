"""Disposable paired XTAL_IN/XTAL_OUT source-to-crystal routing."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_3V3_C3_JOIN_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_XTAL_PROBE.kicad_pcb'
F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def sb(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(B);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(BASE));ni=b.FindNet('XTAL_IN');no=b.FindNet('XTAL_OUT')
s(b,ni,(101.95,72.8),(104.5,72.8));s(b,ni,(104.5,72.8),(104.5,70.8));v(b,ni,(104.5,70.8));sb(b,ni,(104.5,70.8),(108.3,70.8));v(b,ni,(108.3,70.8));s(b,ni,(108.3,70.8),(108.3,75.8));s(b,ni,(108.3,75.8),(109.6,78.0))
s(b,no,(101.95,72.4),(105.0,72.4));v(b,no,(105.0,72.4));sb(b,no,(105.0,72.4),(109.7,72.4));v(b,no,(109.7,72.4));s(b,no,(109.7,72.4),(109.7,75.8));s(b,no,(109.7,75.8),(111.4,78.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
