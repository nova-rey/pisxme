"""V378: lane-only RX pair regeneration around retained RSET/XTAL support."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_SUPPORT_XTALOUT_DIRECT_V372.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_LANE0_LANE_ONLY_V378.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b); x.SetPosition(P(*q)); x.SetWidth(pcbnew.FromMM(.60)); x.SetDrill(pcbnew.FromMM(.30)); x.SetLayerPair(F,B); x.SetNet(n); x.SetNetCode(n.GetNetCode()); b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE)); src=pcbnew.LoadBoard(str(BASE))
 for x in list(b.GetTracks()):
  if x.GetNetname()=='RTL_1V1': b.RemoveNative(x)
 for z in list(b.Zones()):
  if z.GetNetname()=='RTL_1V1': b.RemoveNative(z)
 for x in src.GetTracks():
  if x.GetNetname() in ('LANE0_TXP','LANE0_TXN'): b.Add(x.Duplicate())
 n=b.FindNet('LANE0_RXP'); s(b,n,F,(109.95,60.4),(110.6,60.4)); v(b,n,(110.6,60.4)); s(b,n,B,(110.6,60.4),(110.6,66.5)); s(b,n,B,(110.6,66.5),(132,66.5)); v(b,n,(132,66.5)); s(b,n,F,(132,66.5),(132,62.725)); s(b,n,F,(132,62.725),(134.25,62.725))
 n=b.FindNet('LANE0_RXN'); s(b,n,F,(109.95,60),(111.5,60)); v(b,n,(111.5,60)); s(b,n,B,(111.5,60),(111.5,66)); v(b,n,(111.5,66)); s(b,n,F,(111.5,66),(111.5,69)); v(b,n,(111.5,69)); s(b,n,B,(111.5,69),(135,69)); s(b,n,B,(135,69),(135,64.5)); v(b,n,(135,64.5)); s(b,n,F,(135,64.5),(133.75,64.5))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
