"""V1321: co-author V1258 source/connector escapes around V1058 support rows."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ROTATE_U2_SPI_V1058.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V1058_SUPPORT_LANE_COAUTHORED_SOUTH_V1321.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); VW=pcbnew.FromMM(.60); VD=pcbnew.FromMM(.30)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def vi(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(VW); q.SetDrill(VD); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
data={
 'LANE0_RXP': {'src':[(94.05,71.6),(95.0,71.6),(95.0,72.4)],'sv':(95.0,72.4),'row':(95.0,82.0),'fv':(130.0,42.0),'launch':[(130.0,42.0),(130.0,68.0)],'mid':(130.0,68.0),'endmid':(134.25,68.0),'end':(134.25,62.725)},
 'LANE0_RXN': {'src':[(94.05,72.0),(92.8,72.0),(92.8,70.8)],'sv':(92.8,70.8),'row':(92.8,84.0),'fv':(131.0,43.0),'launch':[(131.0,43.0),(131.0,65.0)],'mid':(131.0,65.0),'endmid':(132.75,65.0),'end':(133.75,62.725)},
 'LANE0_TXN': {'src':[(94.05,72.8),(92.2,72.8),(92.2,72.6)],'sv':(92.2,72.6),'row':(92.2,86.0),'fv':(132.0,44.0),'launch':[(132.0,44.0),(132.0,64.0)],'mid':(132.0,64.0),'endmid':(135.25,64.0),'end':(135.25,62.725)},
 'LANE0_TXP': {'src':[(94.05,73.2),(90.8,73.2),(90.8,76.8)],'sv':(90.8,76.8),'row':(90.8,88.0),'fv':(133.0,45.0),'launch':[(133.0,45.0),(133.0,61.0)],'mid':(133.0,61.0),'endmid':(135.75,61.0),'end':(135.75,62.725)},
}
for name,d in data.items():
    n=b.FindNet(name)
    for a,z in zip(d['src'],d['src'][1:]): tr(b,n,F,a,z)
    vi(b,n,d['sv']); tr(b,n,B,d['sv'],d['row']); tr(b,n,B,d['row'],d['fv']); vi(b,n,d['fv'])
    tr(b,n,F,*d['launch']); vi(b,n,d['mid']); tr(b,n,B,d['mid'],d['endmid']); vi(b,n,d['endmid']); tr(b,n,F,d['endmid'],d['end'])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
