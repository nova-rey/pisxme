"""V1183: merge the accepted U1.16 and U1.25 1V1 primitives."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_1V1_U116_SOUTH_DIRECT_V1174.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_1V1_U116_U125_MERGED_V1183.kicad_pcb'
F,L=pcbnew.F_Cu,pcbnew.In2_Cu; WF=pcbnew.FromMM(.20); WP=pcbnew.FromMM(1.0)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,c,l,ps,w):
    for a,z in zip(ps,ps[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(w); q.SetNetCode(c); b.Add(q)
def via(b,c,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(F,pcbnew.B_Cu); q.SetNetCode(c); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1').GetNetCode()
add(b,n,F,[(101.95,70.4),(103.0,70.4),(104.0,68.5),(109.5,68.5)],WF)
via(b,n,(109.5,68.5)); add(b,n,L,[(109.5,68.5),(91.8,69.0)],WP)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
