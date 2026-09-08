"""V3 disposable V35 co-allocation: move U2 left, regenerate SPI, add 1V1."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_RTL5V_PROBE_V4.kicad_pcb'; out=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_REROUTE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(p(*a));q.SetEnd(p(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(base)); u2=b.FindFootprintByReference('U2'); u2.SetPosition(u2.GetPosition()+p(-10,0))
for x in list(b.GetTracks()):
 if x.GetNetname() in {'SPISI','SPICLK','SPISO3','SPISO','SPICS'}: b.RemoveNative(x)
for name,up,dp,y in [('SPICS','24','1',57.0),('SPISO','23','2',58.5),('SPISO3','22','7',60.0),('SPICLK','19','6',64.0),('SPISI','18','5',64.8)]:
 n=b.FindNet(name); a=u1=b.FindFootprintByReference('U1').FindPadByNumber(up).GetPosition(); z=u2.FindPadByNumber(dp).GetPosition(); A=(a.x/1e6,a.y/1e6); Z=(z.x/1e6,z.y/1e6)
 s(b,n,F,A,(A[0],y));v(b,n,(A[0],y));s(b,n,B,(A[0],y),(Z[0],y));v(b,n,(Z[0],y));s(b,n,F,(Z[0],y),Z)
n=b.FindNet('RTL_1V1'); c4=b.FindFootprintByReference('C4'); c4.SetPosition(c4.GetPosition()+p(-9.4,13.0))
for src,esc in [((94.05,67.20),(87.0,67.20)),((94.05,68.80),(88.0,68.80)),((94.05,72.80),(89.0,72.80)),((96.0,73.95),(96.0,84.0)),((98.0,73.95),(98.0,84.0)),((99.2,73.95),(99.2,84.0))]:
 s(b,n,F,src,esc); v(b,n,esc if esc[1]==84.0 else esc)
 if esc[1] != 84.0: s(b,n,F,esc,(esc[0],84.0));v(b,n,(esc[0],84.0))
s(b,n,B,(87.0,84.0),(104.0,84.0));v(b,n,(104.0,84.0));s(b,n,F,(104.0,84.0),(104.0,82.0));s(b,n,F,(104.0,82.0),(104.0,82.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
