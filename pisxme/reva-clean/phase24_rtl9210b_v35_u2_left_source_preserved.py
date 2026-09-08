"""Source-preserving U2-left RTL9210B support-field experiment."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_RTL5V_PROBE_V4.kicad_pcb'; out=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_SOURCE_PRESERVED.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(p(*a));q.SetEnd(p(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(base));u1=b.FindFootprintByReference('U1');u2=b.FindFootprintByReference('U2');u2.SetPosition(u2.GetPosition()+p(-10,0))
for x in list(b.GetTracks()):
 if x.GetNetname() in {'SPISI','SPICLK','SPISO3','SPISO','SPICS'}: b.RemoveNative(x)
# Proven V35 source escapes, with only the B.Cu/destination legs changed.
spi=[('SPICS','24','1',(98.8,57.0),(98.8,57.0)),('SPISO','23','2',(101.0,58.5),(101.0,58.5)),('SPISO3','22','7',(100.2,60.0),(100.2,60.0)),('SPICLK','19','6',(102.0,64.0),(102.0,64.0)),('SPISI','18','5',(102.2,64.8),(102.2,64.8))]
for name,up,dp,source_v,_ in spi:
 n=b.FindNet(name); a=u1.FindPadByNumber(up).GetPosition(); z=u2.FindPadByNumber(dp).GetPosition(); A=(a.x/1e6,a.y/1e6); Z=(z.x/1e6,z.y/1e6); y=source_v[1]
 if name=='SPICS': s(b,n,F,A,(98.8,57.0))
 elif name=='SPISO': s(b,n,F,A,(99.2,58.5));s(b,n,F,(99.2,58.5),(101.0,58.5))
 elif name=='SPISO3': s(b,n,F,A,(99.6,60.0));s(b,n,F,(99.6,60.0),(100.2,60.0))
 elif name=='SPICLK': s(b,n,F,A,(100.8,65.0));s(b,n,F,(100.8,65.0),(102.0,64.0))
 else: s(b,n,F,A,(101.2,66.05));s(b,n,F,(101.2,66.05),(102.2,64.8))
 v(b,n,source_v);s(b,n,B,source_v,(Z[0],y));v(b,n,(Z[0],y));s(b,n,F,(Z[0],y),Z)
n=b.FindNet('RTL_1V1'); c4=b.FindFootprintByReference('C4');c4.SetPosition(c4.GetPosition()+p(-9.4,13.0))
paths=[(((94.05,67.20),(87.0,67.20)),), (((94.05,68.80),(88.0,68.80)),), (((94.05,72.80),(89.0,72.80)),), (((96.0,73.95),(96.0,77.5),(97.2,77.5)),), (((98.0,73.95),(98.0,84.0)),), (((99.2,73.95),(99.2,84.0)),)]
for path in paths:
 src=path[0][0]; points=path[0][1:]; prev=src
 for point in points: s(b,n,F,prev,point); prev=point
 esc=prev
 if esc[1] < 84: s(b,n,F,esc,(esc[0],84.0))
 v(b,n,(esc[0],84.0))
s(b,n,B,(87.0,84.0),(104.0,84.0));v(b,n,(104.0,84.0));s(b,n,F,(104.0,84.0),(104.0,82.0));s(b,n,F,(104.0,82.0),(104.0,82.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
