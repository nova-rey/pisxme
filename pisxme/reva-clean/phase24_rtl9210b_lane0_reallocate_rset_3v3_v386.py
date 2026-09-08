"""V386: widen the support channel by moving the RSET return below 3V3."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_XTALOUT_DIRECT_V372.kicad_pcb'; SRC=H/'PHASE24_RTL9210B_LANE0_ROUTE_V328.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_LANE0_REALLOCATE_RSET_3V3_V387.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def xy(p): return (p.x/1e6,p.y/1e6)
def near(q, refs): return any(abs(q[0]-x)<.002 and abs(q[1]-y)<.002 for x,y in refs)
def main():
 b=pcbnew.LoadBoard(str(BASE)); src=pcbnew.LoadBoard(str(SRC))
 for x in list(b.GetTracks()):
  if x.GetNetname() in ('RTL_1V1','XTAL_OUT','RSET'): b.RemoveNative(x)
  elif x.GetNetname()=='RTL_3V3' and (near(xy(x.GetStart()),((109.95,65.2),(112,65.2))) or near(xy(x.GetEnd()),((109.95,65.2),(112,65.2)))): b.RemoveNative(x)
 for z in list(b.Zones()):
  if z.GetNetname()=='RTL_1V1': b.RemoveNative(z)
 for x in src.GetTracks():
  if x.GetNetname() in ('LANE0_TXP','LANE0_TXN'): b.Add(x.Duplicate())
 n=b.FindNet('LANE0_RXP'); seg(b,n,F,(109.95,60.4),(110.6,60.4)); seg(b,n,F,(110.6,60.4),(110.6,66.5)); via(b,n,(110.6,66.5)); seg(b,n,B,(110.6,66.5),(132,66.5)); via(b,n,(132,66.5)); seg(b,n,F,(132,66.5),(134.25,66.5)); seg(b,n,F,(134.25,66.5),(134.25,62.725))
 n=b.FindNet('LANE0_RXN'); seg(b,n,F,(109.95,60),(111.5,60)); seg(b,n,F,(111.5,60),(111.5,64.5)); via(b,n,(111.5,64.5)); seg(b,n,B,(111.5,64.5),(132,64.5)); via(b,n,(132,64.5)); seg(b,n,F,(132,64.5),(133.75,64.5)); seg(b,n,F,(133.75,64.5),(133.75,62.725))
 n=b.FindNet('RTL_3V3'); seg(b,n,F,(109.95,65.2),(109.8,65.2)); seg(b,n,F,(109.8,65.2),(109.8,66.8)); via(b,n,(109.8,66.8)); seg(b,n,B,(109.8,66.8),(109.8,68.5)); seg(b,n,B,(109.8,68.5),(112,68.5)); via(b,n,(112,68.5)); seg(b,n,pcbnew.In2_Cu,(112,68.5),(104.4,68.5))
 n=b.FindNet('RSET'); seg(b,n,F,(109.2,65.95),(109.2,67.5)); seg(b,n,F,(109.2,67.5),(108.5,67.5)); via(b,n,(108.5,67.5)); seg(b,n,B,(108.5,67.5),(101.4,67.5)); via(b,n,(101.4,67.5)); seg(b,n,F,(101.4,67.5),(101.4,71.0))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
