"""V398: move XTAL_OUT transition rightward beside U1.59."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_XTALIN_VIA_REPOSITIONED_V397.kicad_pcb'; out=H/'PHASE24_RTL9210B_XTALOUT_VIA_RIGHT_V398.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src))
for x in list(b.GetTracks()):
 if x.GetNetname()=='XTAL_OUT': b.RemoveNative(x)
n=b.FindNet('XTAL_OUT'); seg(b,n,F,(109.95,64.4),(109.2,64.4)); seg(b,n,F,(109.2,64.4),(109.2,62.4)); via(b,n,(109.2,62.4)); seg(b,n,B,(109.2,62.4),(109.2,46.0)); seg(b,n,B,(109.2,46.0),(116.7,46.0)); via(b,n,(116.7,46.0)); seg(b,n,F,(116.7,46.0),(116.7,49.0)); seg(b,n,F,(116.7,49.0),(118.0,49.0)); via(b,n,(118.0,49.0)); seg(b,n,B,(118.0,49.0),(120.4,49.0)); seg(b,n,B,(120.4,49.0),(120.4,53.0)); via(b,n,(120.4,53.0))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
