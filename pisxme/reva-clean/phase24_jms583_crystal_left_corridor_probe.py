"""Try a left-side JMS583 crystal corridor clear of the XAVDDH diagonal."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_JMS583_SUPPORT_COHORT_GROUND_FILLED_V2.kicad_pcb'
OUT=R/'PHASE24_JMS583_CRYSTAL_LEFT_CORRIDOR.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*p));v.SetWidth(pcbnew.FromMM(.50));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U11');y=b.FindFootprintByReference('Y10');y.SetPosition(P(130,125));y.SetOrientationDegrees(180)
for name,up,yp,escape,exitp,endp in [('XIN','50','1',[(137.4,130.5),(135,130.5),(134,129)],(134,129),(131.1,125.85)),('XOUT','51','2',[(137.8,129.5),(136,129.5),(136,128)],(136,128),(131.1,124.15))]:
 n=b.FindNet(name)
 for item in list(b.GetTracks()):
  if item.GetNetCode()==n.GetNetCode(): b.RemoveNative(item)
 s=u.FindPadByNumber(up).GetPosition();src=(pcbnew.ToMM(s.x),pcbnew.ToMM(s.y));seg(b,n,pcbnew.F_Cu,src,escape[0]);seg(b,n,pcbnew.F_Cu,escape[0],escape[1]);via(b,n,exitp)
 mid=(exitp[0],endp[1]);seg(b,n,pcbnew.B_Cu,exitp,mid);seg(b,n,pcbnew.B_Cu,mid,endp);via(b,n,endp)
 d=y.FindPadByNumber(yp).GetPosition();dst=(pcbnew.ToMM(d.x),pcbnew.ToMM(d.y));seg(b,n,pcbnew.F_Cu,endp,dst)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
