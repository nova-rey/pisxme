"""V795: split QFN departures with CLKREQ_N rising outside the pad field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_CONTROL_SEPARATED_OUTER_V788.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_CONTROLS_PERST_QFN_SPLIT_V795.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
n=b.FindNet('CLKREQ_N')
for item in list(b.GetTracks()):
 if item.GetNetname()=='CLKREQ_N': b.RemoveNative(item)
T(b,n,F,(101.95,68.4),(102.8,68.4)); T(b,n,F,(102.8,68.4),(102.8,65.5)); T(b,n,F,(102.8,65.5),(107.5,65.5)); V(b,n,(107.5,65.5)); T(b,n,B,(107.5,65.5),(107.5,52)); T(b,n,B,(107.5,52),(110.2,52)); V(b,n,(110.2,52)); T(b,n,F,(110.2,52),(113,52)); T(b,n,F,(113,52),(113,65)); T(b,n,F,(113,65),(111,65)); T(b,n,F,(111,65),(111,62))
n=b.FindNet('PERST_N'); T(b,n,F,(101.95,68.0),(103.8,68.0)); V(b,n,(103.8,68)); T(b,n,B,(103.8,68),(103.8,77)); T(b,n,B,(103.8,77),(108,77)); T(b,n,B,(108,77),(108,48)); T(b,n,B,(108,48),(135,48)); T(b,n,B,(135,48),(135,69.5)); V(b,n,(135,69.5)); T(b,n,F,(135,69.5),(136,70.275))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
