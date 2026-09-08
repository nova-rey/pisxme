"""Disposable joint U1.52/XTAL field with staggered rail transitions."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_3V3_C3_JOIN_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_CRYSTAL_3V3_JOINT_V2_PROBE.kicad_pcb'
F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,c,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(W);t.SetNetCode(c);b.Add(t)
def v(b,c,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNetCode(c);b.Add(x)
b=pcbnew.LoadBoard(str(BASE));c3=b.FindNet('RTL_3V3').GetNetCode();ci=b.FindNet('XTAL_IN').GetNetCode();co=b.FindNet('XTAL_OUT').GetNetCode()
for t in list(b.GetTracks()):
 if t.GetNetCode()==c3 and (t.GetStart().x/1e6>100 or t.GetEnd().x/1e6>100): b.Remove(t)
# U1.52/C3 branch, then return around the two retained 1V1 B.Cu corridors to
# the existing U1.39 3V3 via at (96.4,75.2).
s(b,c3,F,(101.95,73.2),(106.0,73.2));v(b,c3,(106.0,73.2));s(b,c3,B,(106.0,73.2),(106.0,72.0));s(b,c3,B,(106.0,72.0),(110.4,72.0));s(b,c3,B,(110.4,72.0),(110.4,75.2));s(b,c3,B,(110.4,75.2),(96.4,75.2));s(b,c3,B,(110.4,72.0),(110.4,69.0));v(b,c3,(110.4,69.0));s(b,c3,F,(110.4,69.0),(110.4,69.0))
# Crystal pair: straight source exits, staggered transitions, short drops at
# the crystal and its two load capacitors.
s(b,ci,F,(101.95,72.8),(104.5,72.8));s(b,ci,F,(104.5,72.8),(104.5,71.0));v(b,ci,(104.5,71.0));s(b,ci,B,(104.5,71.0),(108.3,71.0));v(b,ci,(108.3,71.0));s(b,ci,F,(108.3,71.0),(108.3,75.8));s(b,ci,F,(108.3,75.8),(109.6,78.0))
s(b,co,F,(101.95,72.4),(105.5,72.4));v(b,co,(105.5,72.4));s(b,co,B,(105.5,72.4),(109.7,72.4));v(b,co,(109.7,72.4));s(b,co,F,(109.7,72.4),(109.7,75.8));s(b,co,F,(109.7,75.8),(111.4,78.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
