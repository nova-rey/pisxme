"""V792: final co-authored U1-side control departures for PERST/CLKREQ."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_CONTROL_SEPARATED_OUTER_V788.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_CONTROLS_PERST_COAUTHORED_V792.kicad_pcb'
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
T(b,n,F,(101.95,68.4),(102.5,68.4)); T(b,n,F,(102.5,68.4),(102.5,71.0)); T(b,n,F,(102.5,71.0),(107.5,71.0)); V(b,n,(107.5,71.0)); T(b,n,B,(107.5,71.0),(107.5,52)); T(b,n,B,(107.5,52),(110.2,52)); V(b,n,(110.2,52)); T(b,n,F,(110.2,52),(113,52)); T(b,n,F,(113,52),(113,65)); T(b,n,F,(113,65),(111,65)); T(b,n,F,(111,65),(111,62))
n=b.FindNet('PERST_N')
T(b,n,F,(101.95,68.0),(103.0,68.0)); V(b,n,(103.0,68.0)); T(b,n,B,(103.0,68.0),(103.0,76.5)); T(b,n,B,(103.0,76.5),(108.0,76.5)); T(b,n,B,(108.0,76.5),(108.0,48)); T(b,n,B,(108.0,48),(135.0,48)); T(b,n,B,(135.0,48),(135.0,69.5)); V(b,n,(135.0,69.5)); T(b,n,F,(135.0,69.5),(136.0,70.275))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
