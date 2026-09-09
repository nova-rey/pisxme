"""V791: co-authored U1-side CLKREQ_N/PERST_N escape."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_CONTROL_SEPARATED_OUTER_V788.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_CONTROLS_PERST_COAUTHORED_V791.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
# Replace the prior CLKREQ_N route, keeping its validated R3 placement.
n=b.FindNet('CLKREQ_N')
for item in list(b.GetTracks()):
 if item.GetNetname()=='CLKREQ_N': b.RemoveNative(item)
T(b,n,F,(101.95,68.4),(102.5,68.4)); T(b,n,F,(102.5,68.4),(102.5,69.5)); T(b,n,F,(102.5,69.5),(107,69.5)); V(b,n,(107,69.5)); T(b,n,B,(107,69.5),(107,52)); T(b,n,B,(107,52),(110.2,52)); V(b,n,(110.2,52)); T(b,n,F,(110.2,52),(113,52)); T(b,n,F,(113,52),(113,65)); T(b,n,F,(113,65),(111,65)); T(b,n,F,(111,65),(111,62))
# PERST_N uses a lower local jog to get around the endpoint-field columns.
n=b.FindNet('PERST_N')
T(b,n,F,(101.95,68.0),(104,68.0)); V(b,n,(104,68)); T(b,n,B,(104,68),(104,76)); T(b,n,B,(104,76),(108,76)); T(b,n,B,(108,76),(108,48)); T(b,n,B,(108,48),(135,48)); T(b,n,B,(135,48),(135,69.5)); V(b,n,(135,69.5)); T(b,n,F,(135,69.5),(136,70.275))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
