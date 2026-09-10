"""V1313: pad-adjacent rotated-QFN escapes with allocated pair transitions."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_SPI_U1_ROTATE90_SPICS_SPISO_V735.kicad_pcb';OUT=H/'PHASE24_RTL9210B_ROTATED_LANE0_PAD_ESCAPE_V1313.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U1');j=b.FindFootprintByReference('J1')
R=[('LANE0_RXP','64',(97.5,76.0),(130.0,76.0),(134.25,60.0),'43'),('LANE0_RXN','65',(100.0,77.5),(131.5,77.5),(133.75,58.0),'41'),('LANE0_TXN','67',(100.8,80.0),(133.0,80.0),(135.25,56.0),'47'),('LANE0_TXP','68',(102.0,74.5),(134.0,82.5),(135.75,54.0),'49')]
for name,padnum,sv,ev,fv,jpad in R:
 n=b.FindNet(name);p=u.FindPadByNumber(padnum).GetPosition();src=(pcbnew.ToMM(p.x),pcbnew.ToMM(p.y))
 if name=='LANE0_TXP':
  s(b,n,F,[src,sv]);v(b,n,sv);mid=(102.0,78.5);s(b,n,B,[sv,mid]);v(b,n,mid);s(b,n,F,[mid,(104.5,78.5)]);v(b,n,(104.5,78.5));s(b,n,B,[(104.5,78.5),ev]);v(b,n,ev);s(b,n,B,[ev,(ev[0],54.0),fv]);v(b,n,fv)
 elif name=='LANE0_RXP':
  s(b,n,F,[src,(sv[0],src[1]),sv]);v(b,n,sv);mid=(101.5,sv[1]);s(b,n,B,[sv,mid]);v(b,n,mid);s(b,n,F,[mid,(104.5,sv[1])]);v(b,n,(104.5,sv[1]));s(b,n,B,[(104.5,sv[1]),ev]);v(b,n,ev);s(b,n,B,[ev,(ev[0],60.0),fv]);v(b,n,fv)
 else:
  s(b,n,F,[src,(sv[0],src[1]),sv]);v(b,n,sv);s(b,n,B,[sv,ev]);v(b,n,ev);s(b,n,F,[ev,(ev[0],fv[1])]);v(b,n,(ev[0],fv[1]));s(b,n,B,[(ev[0],fv[1]),fv]);v(b,n,fv)
 d=j.FindPadByNumber(jpad).GetPosition();dst=(pcbnew.ToMM(d.x),pcbnew.ToMM(d.y));s(b,n,F,[fv,dst])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
