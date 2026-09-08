"""V381: exact V328 lane plus a reallocated RTL_3V3 U1.52 escape.

XTAL_OUT remains temporarily removed so this test isolates the lane/3V3
channel interaction.  The 3V3 path is still derived from the saved native
support board and joins its existing power trunk through an ordinary via.
"""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_XTALOUT_DIRECT_V372.kicad_pcb'
SRC=H/'PHASE24_RTL9210B_LANE0_ROUTE_V328.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_LANE0_REALLOCATE_3V3_V381.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def near(q,x,y): return abs(q[0]-x)<.002 and abs(q[1]-y)<.002
def main():
 b=pcbnew.LoadBoard(str(BASE)); src=pcbnew.LoadBoard(str(SRC))
 for x in list(b.GetTracks()):
  if x.GetNetname()=='RTL_1V1' or x.GetNetname()=='XTAL_OUT': b.RemoveNative(x)
 for z in list(b.Zones()):
  if z.GetNetname()=='RTL_1V1': b.RemoveNative(z)
 # Remove only the old U1.52-to-power-trunk escape; retain the rest of the
 # native 3V3 support network and its verified power-plane connection.
 for x in list(b.GetTracks()):
  if x.GetNetname()!='RTL_3V3': continue
  a=(x.GetStart().x/1e6,x.GetStart().y/1e6); z=(x.GetEnd().x/1e6,x.GetEnd().y/1e6)
  if (near(a,109.95,65.2) or near(z,109.95,65.2) or near(a,112,65.2) or near(z,112,65.2)):
   b.RemoveNative(x)
 for x in src.GetTracks():
  if x.GetNetname() in ('LANE0_TXP','LANE0_TXN'): b.Add(x.Duplicate())
 n=b.FindNet('LANE0_RXP'); seg(b,n,F,(109.95,60.4),(110.6,60.4)); seg(b,n,F,(110.6,60.4),(110.6,66.5)); via(b,n,(110.6,66.5)); seg(b,n,B,(110.6,66.5),(132,66.5)); via(b,n,(132,66.5)); seg(b,n,F,(132,66.5),(134.25,66.5)); seg(b,n,F,(134.25,66.5),(134.25,62.725))
 n=b.FindNet('LANE0_RXN'); seg(b,n,F,(109.95,60),(111.5,60)); seg(b,n,F,(111.5,60),(111.5,64.5)); via(b,n,(111.5,64.5)); seg(b,n,B,(111.5,64.5),(132,64.5)); via(b,n,(132,64.5)); seg(b,n,F,(132,64.5),(133.75,64.5)); seg(b,n,F,(133.75,64.5),(133.75,62.725))
 n=b.FindNet('RTL_3V3'); seg(b,n,F,(109.95,65.2),(108,65.2)); seg(b,n,F,(108,65.2),(108,67)); via(b,n,(108,67)); seg(b,n,B,(108,67),(104.4,68.5))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
