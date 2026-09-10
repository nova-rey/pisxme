"""V1324: V1258 staggered QFN escapes plus separated outboard J1 launches."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ROTATE_U2_SPI_V1058.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_OUTBOARD_J1_COAUTHORED_V1324.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20); VW=pcbnew.FromMM(.60); VD=pcbnew.FromMM(.30)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
    q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def vi(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(VW); q.SetDrill(VD); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); j=next(f for f in b.GetFootprints() if f.GetReference()=='J1'); j.Move(P(20,0))
edge=next(e for e in b.GetDrawings() if e.GetLayer()==pcbnew.Edge_Cuts); edge.SetStartEnd(P(64.9,39.9),P(175.0,95.0))
routes={
 'LANE0_RXP':([(94.05,71.6),(95.0,71.6),(95.0,72.4)],(95.0,72.4),(95.0,82.0),(150.0,82.0),(150.0,68.0),(154.25,68.0),(154.25,62.725)),
 'LANE0_RXN':([(94.05,72.0),(92.8,72.0),(92.8,70.8)],(92.8,70.8),(92.8,83.0),(151.0,83.0),(151.0,65.0),(153.75,65.0),(153.75,62.725)),
 'LANE0_TXN':([(94.05,72.8),(92.2,72.8),(92.2,72.6)],(92.2,72.6),(92.2,84.0),(152.0,84.0),(152.0,64.0),(155.25,64.0),(155.25,62.725)),
 'LANE0_TXP':([(94.05,73.2),(90.8,73.2),(90.8,76.8)],(90.8,76.8),(90.8,85.0),(153.0,85.0),(153.0,61.0),(155.75,61.0),(155.75,62.725)),
}
for name,(src,sv,row,far,mid,endmid,end) in routes.items():
    n=b.FindNet(name)
    for a,z in zip(src,src[1:]): tr(b,n,F,a,z)
    vi(b,n,sv); tr(b,n,B,sv,row); vi(b,n,row); tr(b,n,F,row,far); tr(b,n,F,far,mid); vi(b,n,mid); tr(b,n,B,mid,endmid); vi(b,n,endmid); tr(b,n,F,endmid,end)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
