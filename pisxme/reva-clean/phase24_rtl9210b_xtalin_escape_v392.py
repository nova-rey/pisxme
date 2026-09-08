"""V392: move XTAL_IN's QFN transition away from the exposed GND pad."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_XTALOUT_ESCAPE_V391.kicad_pcb'; out=H/'PHASE24_RTL9210B_XTALIN_ESCAPE_V392.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src))
for x in list(b.GetTracks()):
 if x.GetNetname()=='XTAL_IN': b.RemoveNative(x)
n=b.FindNet('XTAL_IN'); seg(b,n,F,(109.95,64.8),(107.5,64.8)); via(b,n,(107.5,64.8)); seg(b,n,B,(107.5,64.8),(107.5,44.0)); seg(b,n,B,(107.5,44.0),(115.3,44.0)); via(b,n,(115.3,44.0)); seg(b,n,F,(115.3,44.0),(115.3,49.0)); seg(b,n,F,(115.3,49.0),(114.3,49.0)); via(b,n,(114.3,49.0)); seg(b,n,B,(114.3,49.0),(114.3,48.0)); seg(b,n,B,(114.3,48.0),(120.1,48.0)); via(b,n,(120.1,48.0))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
