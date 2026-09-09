"""V789: disposable outer PERST_N route between RTL9210B and CM5/J1."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_CONTROL_SEPARATED_OUTER_V788.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_PERST_OUTER_V789.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('PERST_N')
T(b,n,F,(101.95,68.0),(103.0,68.0)); V(b,n,(103.0,68.0)); T(b,n,B,(103.0,68.0),(103.0,48.0)); T(b,n,B,(103.0,48.0),(135.0,48.0)); T(b,n,B,(135.0,48.0),(135.0,69.5)); V(b,n,(135.0,69.5)); T(b,n,F,(135.0,69.5),(136.0,70.275))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
