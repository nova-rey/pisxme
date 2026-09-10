"""V1314: source-coauthored rotated-QFN lane trial."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_U1_ROTATE90_SPICS_SPISO_V735.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_LANE0_SOURCE_COAUTHOR_V1314.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,ps):
    for a,z in zip(ps,ps[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for q in list(b.GetTracks()):
    if q.GetNetname() in {'LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP'}: b.RemoveNative(q)
u=b.FindFootprintByReference('U1'); j=b.FindFootprintByReference('J1')
def dst(n,pad):
    q=j.FindPadByNumber(pad).GetPosition(); return (pcbnew.ToMM(q.x),pcbnew.ToMM(q.y))
def finish(n,ev,fp,pad):
    via(b,n,ev); seg(b,n,F,[ev,(ev[0],fp[1])]); via(b,n,(ev[0],fp[1])); seg(b,n,B,[(ev[0],fp[1]),fp]); via(b,n,fp); d=dst(n,pad); seg(b,n,F,[fp,d])
def source(n,pad,sv):
    q=u.FindPadByNumber(pad).GetPosition(); src=(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)); seg(b,n,F,[src,(sv[0],src[1]),sv]); via(b,n,sv)
n=b.FindNet('LANE0_RXP'); source(n,'64',(98.8,75.0)); seg(b,n,B,[(98.8,75.0),(101.5,75.0)]); via(b,n,(101.5,75.0)); seg(b,n,F,[(101.5,75.0),(104.0,75.0)]); via(b,n,(104.0,75.0)); seg(b,n,B,[(104.0,75.0),(130.0,75.0)]); finish(n,(130.0,75.0),(134.25,60.0),'43')
n=b.FindNet('LANE0_RXN'); source(n,'65',(100.0,77.0)); seg(b,n,B,[(100.0,77.0),(131.0,77.0)]); finish(n,(131.0,77.0),(133.75,58.0),'41')
n=b.FindNet('LANE0_TXN'); source(n,'67',(100.8,79.5)); seg(b,n,B,[(100.8,79.5),(133.0,79.5)]); finish(n,(133.0,79.5),(135.25,56.0),'47')
n=b.FindNet('LANE0_TXP'); source(n,'68',(101.2,78.0)); seg(b,n,F,[(101.2,78.0),(103.0,78.0)]); via(b,n,(103.0,78.0)); seg(b,n,F,[(103.0,78.0),(103.0,82.5)]); via(b,n,(103.0,82.5)); seg(b,n,B,[(103.0,82.5),(134.0,82.5)]); finish(n,(134.0,82.5),(135.75,54.0),'49')
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
