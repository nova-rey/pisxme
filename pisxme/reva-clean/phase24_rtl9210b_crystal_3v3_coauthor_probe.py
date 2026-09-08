"""Disposable co-authoring of U1.52 3V3 and crystal source exits."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_3V3_C3_JOIN_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_CRYSTAL_3V3_COAUTHOR_PROBE.kicad_pcb'
F,B,W=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,code,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(W);t.SetNetCode(code);b.Add(t)
def v(b,code,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNetCode(code);b.Add(x)
b=pcbnew.LoadBoard(str(BASE));n3=b.FindNet('RTL_3V3');n3c=n3.GetNetCode();nic=b.FindNet('XTAL_IN').GetNetCode();noc=b.FindNet('XTAL_OUT').GetNetCode()
for t in list(b.GetTracks()):
 if t.GetNetCode()==n3c and (t.GetStart().x/1e6>100 or t.GetEnd().x/1e6>100): b.Remove(t)
s(b,n3c,F,(101.95,73.2),(106.0,73.2));v(b,n3c,(106.0,73.2));s(b,n3c,B,(106.0,73.2),(106.0,68.5));s(b,n3c,B,(106.0,68.5),(110.4,68.5));v(b,n3c,(110.4,68.5));s(b,n3c,F,(110.4,68.5),(110.4,69.0))
s(b,nic,F,(101.95,72.8),(104.5,72.8));s(b,nic,F,(104.5,72.8),(104.5,70.8));v(b,nic,(104.5,70.8));s(b,nic,B,(104.5,70.8),(108.3,70.8));v(b,nic,(108.3,70.8));s(b,nic,F,(108.3,70.8),(108.3,75.8));s(b,nic,F,(108.3,75.8),(109.6,78.0))
s(b,noc,F,(101.95,72.4),(105.5,72.4));v(b,noc,(105.5,72.4));s(b,noc,B,(105.5,72.4),(109.7,72.4));v(b,noc,(109.7,72.4));s(b,noc,F,(109.7,72.4),(109.7,75.8));s(b,noc,F,(109.7,75.8),(111.4,78.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
