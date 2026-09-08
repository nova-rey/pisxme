"""Co-author JMS583 XIN/XOUT/XAVDDH bottom-edge exits."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_JMS583_SUPPORT_COHORT_GROUND_FILLED_V2.kicad_pcb'
OUT=R/'PHASE24_JMS583_THREE_EXIT_COAUTHOR.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*p));v.SetWidth(pcbnew.FromMM(.50));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U11');y=b.FindFootprintByReference('Y10');y.SetPosition(P(130,125));y.SetOrientationDegrees(180)
for netname in ('XIN','XOUT','JMS_XAVDDH'):
 n=b.FindNet(netname)
 for item in list(b.GetTracks()):
  if item.GetNetCode()==n.GetNetCode(): b.RemoveNative(item)
for name,up,yp,esc,via_xy,bend,pad_xy in [
 ('XIN','50','1',[(137.4,130.5),(135,130.5),(134,129)],(134,129),(130,127.5),(131.1,125.85)),
 ('XOUT','51','2',[(137.8,129.8),(135.8,129.8)],(135.8,129.8),(133,123.5),(131.1,124.15)),
]:
 n=b.FindNet(name);s=u.FindPadByNumber(up).GetPosition();src=(pcbnew.ToMM(s.x),pcbnew.ToMM(s.y));seg(b,n,pcbnew.F_Cu,src,esc[0])
 for a,z in zip(esc,esc[1:]): seg(b,n,pcbnew.F_Cu,a,z)
 via(b,n,via_xy);seg(b,n,pcbnew.B_Cu,via_xy,bend);seg(b,n,pcbnew.B_Cu,bend,pad_xy);via(b,n,pad_xy)
 d=y.FindPadByNumber(yp).GetPosition();seg(b,n,pcbnew.F_Cu,pad_xy,(pcbnew.ToMM(d.x),pcbnew.ToMM(d.y)))
n=b.FindNet('JMS_XAVDDH');s=u.FindPadByNumber('52').GetPosition();src=(pcbnew.ToMM(s.x),pcbnew.ToMM(s.y));esc=[src,(138.2,130.5),(139.5,130.5)]
for a,z in zip(esc,esc[1:]): seg(b,n,pcbnew.F_Cu,a,z)
via(b,n,(139.5,130.5));seg(b,n,pcbnew.B_Cu,(139.5,130.5),(139.5,140));seg(b,n,pcbnew.B_Cu,(139.5,140),(149,121.5));via(b,n,(149,121.5));seg(b,n,pcbnew.F_Cu,(149,121.5),(149.5,120))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
