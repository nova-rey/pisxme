"""V420: move PEDET's source escape clear of the CLKREQ transition."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_CLKREQ_QFN_CLEARANCE_V419.kicad_pcb'; out=H/'PHASE24_RTL9210B_PEDET_QFN_CLEARANCE_V420.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src))
for x in list(b.GetTracks()):
 if x.GetNetname()=='PEDET': b.RemoveNative(x)
n=b.FindNet('PEDET'); seg(b,n,F,(106.4,58.05),(107.0,58.05)); seg(b,n,F,(107.0,58.05),(107.0,54.5)); via(b,n,(107.0,54.5)); seg(b,n,B,(107.0,54.5),(95.5,54.5)); seg(b,n,B,(95.5,54.5),(95.5,78.0)); seg(b,n,B,(95.5,78.0),(140.75,78.0)); via(b,n,(140.75,78.0)); seg(b,n,F,(140.75,78.0),(140.75,62.725)); via(b,n,(98.9,54.5)); seg(b,n,F,(98.9,54.5),(98.9,53.0))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
