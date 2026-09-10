"""V105: disposable outer-corridor rehome of STORAGE_SEL."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_AUTHORITY_J3_VERTICAL_V94.kicad_pcb'; OUT=R/'PHASE24_STORAGE_SEL_OUTER_V105.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('STORAGE_SEL'); assert n
for x in list(b.GetTracks()):
 if x.GetNetname()=='STORAGE_SEL': b.RemoveNative(x)
def tr(layer,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetLayer(layer); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetWidth(pcbnew.FromMM(.15)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
for a,z in zip([(153.5,135),(150,128),(175,128),(178.5,135)],[(150,128),(175,128),(178.5,135)]): tr(pcbnew.F_Cu,a,z)
for a,z in zip([(211.1,150.95),(218,150.95),(218,118),(175,118),(175,128)],[(218,150.95),(218,118),(175,118),(175,128),(175,128)]): tr(pcbnew.F_Cu,a,z)
b.Save(str(OUT)); print(OUT)
