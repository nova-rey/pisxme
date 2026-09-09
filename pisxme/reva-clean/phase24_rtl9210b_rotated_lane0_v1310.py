"""V1310: disposable four-lane launch from the rotated-QFN V735 oracle."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_U1_ROTATE90_SPICS_SPISO_V735.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ROTATED_LANE0_V1310.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps):
    for a,z in zip(ps,ps[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l)
        q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30))
    q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U1'); j=b.FindFootprintByReference('J1')
# Distinct source-side rows preserve pair integrity while allowing the
# RX pair's connector-side order reversal without a same-layer crossover.
routes=[('LANE0_RXP','64',99.6,76.0,132.0,'43'),
        ('LANE0_RXN','65',100.0,77.5,131.5,'41'),
        ('LANE0_TXN','67',100.8,80.0,133.0,'47'),
        ('LANE0_TXP','68',101.2,82.5,134.0,'49')]
for name,padnum,x,row,xout,jpad in routes:
    n=b.FindNet(name); p=u.FindPadByNumber(padnum).GetPosition(); src=(pcbnew.ToMM(p.x),pcbnew.ToMM(p.y))
    sv=(x,row); s(b,n,F,[src,(x,src[1]),sv]); v(b,n,sv)
    ev=(xout,row); s(b,n,B,[sv,ev]); v(b,n,ev)
    d=j.FindPadByNumber(jpad).GetPosition(); dst=(pcbnew.ToMM(d.x),pcbnew.ToMM(d.y))
    final=(dst[0],60.0); s(b,n,B,[ev,final]); v(b,n,final); s(b,n,F,[final,dst])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
