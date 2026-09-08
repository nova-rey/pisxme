"""V399: clear the remaining RSET/XTAL_OUT local envelopes with standard vias."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_XTALIN_VIA_REPOSITIONED_V397.kicad_pcb'; out=H/'PHASE24_RTL9210B_LOCAL_CLEARANCE_V399.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def xy(p): return (p.x/1e6,p.y/1e6)
def near(q,refs): return any(abs(q[0]-x)<.002 and abs(q[1]-y)<.002 for x,y in refs)
b=pcbnew.LoadBoard(str(src))
for x in list(b.GetTracks()):
 if x.GetNetname() in ('RSET','XTAL_OUT'): b.RemoveNative(x)
 n=x.GetNetname()
 if n=='RTL_3V3' and (near(xy(x.GetStart()),((109.95,65.2),(112,65.2))) or near(xy(x.GetEnd()),((109.95,65.2),(112,65.2)))): b.RemoveNative(x)
n=b.FindNet('RTL_3V3'); seg(b,n,F,(109.95,65.2),(109.8,65.2)); seg(b,n,F,(109.8,65.2),(109.8,66.8)); via(b,n,(109.8,66.8)); seg(b,n,B,(109.8,66.8),(109.8,68.5)); seg(b,n,B,(109.8,68.5),(112,68.5)); via(b,n,(112,68.5)); seg(b,n,pcbnew.In2_Cu,(112,68.5),(104.4,68.5))
n=b.FindNet('RSET'); seg(b,n,F,(109.2,65.95),(109.2,67.5)); seg(b,n,F,(109.2,67.5),(108.5,67.5)); via(b,n,(108.5,67.5)); seg(b,n,B,(108.5,67.5),(101.4,68.5)); via(b,n,(101.4,68.5)); seg(b,n,F,(101.4,68.5),(101.4,71.0))
n=b.FindNet('XTAL_OUT'); seg(b,n,F,(109.95,64.4),(109.2,64.4)); seg(b,n,F,(109.2,64.4),(108.5,63.5)); seg(b,n,F,(108.5,63.5),(108.5,61.5)); via(b,n,(108.5,61.5)); seg(b,n,B,(108.5,61.5),(108.5,46.0)); seg(b,n,B,(108.5,46.0),(116.7,46.0)); via(b,n,(116.7,46.0)); seg(b,n,F,(116.7,46.0),(116.7,49.0)); seg(b,n,F,(116.7,49.0),(118.0,49.0)); via(b,n,(118.0,49.0)); seg(b,n,B,(118.0,49.0),(120.4,49.0)); seg(b,n,B,(120.4,49.0),(120.4,53.0)); via(b,n,(120.4,53.0))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
