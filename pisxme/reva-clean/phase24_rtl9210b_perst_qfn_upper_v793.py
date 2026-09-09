"""V793: upper PERST_N QFN escape, preserving the V788 controls."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_CONTROL_SEPARATED_OUTER_V788.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_PERST_QFN_UPPER_V793.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('PERST_N')
T(b,n,F,(101.95,68.0),(102.8,67.5)); V(b,n,(102.8,67.5)); T(b,n,B,(102.8,67.5),(102.8,50)); T(b,n,B,(102.8,50),(108,50)); T(b,n,B,(108,50),(108,48)); T(b,n,B,(108,48),(135,48)); T(b,n,B,(135,48),(135,69.5)); V(b,n,(135,69.5)); T(b,n,F,(135,69.5),(136,70.275))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
