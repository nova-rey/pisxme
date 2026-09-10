"""V112: source-owned selector escape using the retained left/top corridor."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_AUTHORITY_J3_VERTICAL_V94.kicad_pcb'; OUT=R/'PHASE24_STORAGE_SEL_U13LEFT_V112.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('STORAGE_SEL'); assert n
for x in list(b.GetTracks()):
 if x.GetNetname()=='STORAGE_SEL': b.RemoveNative(x)
def tr(l,a,z,w=.2):
 q=pcbnew.PCB_TRACK(b); q.SetLayer(l); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetWidth(pcbnew.FromMM(w)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetWidth(pcbnew.FromMM(.55)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
tr(pcbnew.F_Cu,(153.5,135),(178.5,135))
tr(pcbnew.F_Cu,(178.5,135),(176,135)); tr(pcbnew.F_Cu,(176,135),(176,125)); via((176,125))
tr(pcbnew.B_Cu,(176,125),(220,125)); tr(pcbnew.B_Cu,(220,125),(220,151)); via((220,151)); tr(pcbnew.F_Cu,(220,151),(211.1,150.95))
b.Save(str(OUT)); print(OUT)
