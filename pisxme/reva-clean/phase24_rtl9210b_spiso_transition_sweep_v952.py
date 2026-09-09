"""V952: sweep SPISO source-transition cells around U1."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V942_U120_CLEANFIELD_V944.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
    for a,z in zip(pts,pts[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def make(tag,xy,esc):
    b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('SPISO3')
    tr(b,n,[(99.6,66.05),(99.6,62.5),(97.2,62.5),(97.2,60.5)],F); via(b,n,(97.2,60.5)); tr(b,n,[(97.2,60.5),(97.2,56.5),(102.5,56.5),(106.5,60.5),(106.5,72.8)],B); via(b,n,(106.5,72.8)); tr(b,n,[(106.5,72.8),(105,72.8)],F)
    n=b.FindNet('SPISO'); tr(b,n,[(99.2,66.05),*esc,xy],F); via(b,n,xy); tr(b,n,[xy,(xy[0],84),(104.5,84),(104.5,78.8)],B); via(b,n,(104.5,78.8)); tr(b,n,[(104.5,78.8),(105,78.8)],F); b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); out=H/f'PHASE24_RTL9210B_SPISO_SWEEP_{tag}.kicad_pcb'; b.Save(str(out)); print(out)
for tag,xy,esc in [('A',(101.2,65.0),[(99.2,66.05),(100.2,65.4)]),('B',(101.2,64.0),[(99.2,66.05),(100.2,65.4)]),('C',(97.2,65.0),[(99.2,66.05),(98.2,65.2)]),('D',(97.2,64.0),[(99.2,66.05),(98.2,65.2)])]: make(tag,xy,esc)
