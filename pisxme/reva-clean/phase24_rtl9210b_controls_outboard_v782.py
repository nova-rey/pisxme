"""V782: route PEDET/CLKREQ_N in outboard B.Cu control corridors."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_CONTROL_ABOVE_SPI_PLACEMENT_V777.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_CONTROL_OUTBOARD_V782.kicad_pcb'
F=pcbnew.F_Cu; B=pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def T(b,n,l,a,z,w=.20):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(pcbnew.FromMM(w)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def V(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
n=b.FindNet('PEDET'); T(b,n,F,(101.95,70.4),(102.5,70.4)); V(b,n,(102.5,70.4)); T(b,n,B,(102.5,70.4),(110,70.4)); T(b,n,B,(110,70.4),(110,60)); V(b,n,(110,60)); T(b,n,F,(110,60),(108,60))
n=b.FindNet('CLKREQ_N'); T(b,n,F,(101.95,68.4),(102.5,68.4)); V(b,n,(102.5,68.4)); T(b,n,B,(102.5,68.4),(111,68.4)); T(b,n,B,(111,68.4),(111,63)); V(b,n,(111,63)); T(b,n,F,(111,63),(108,63))
n=b.FindNet('RTL_3V3'); T(b,n,F,(109.2,60),(109.2,63))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
