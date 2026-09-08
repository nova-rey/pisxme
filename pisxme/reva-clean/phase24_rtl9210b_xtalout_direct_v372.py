"""V372: direct U1 XTAL_OUT F.Cu escape to outboard riser."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V368.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_SUPPORT_XTALOUT_DIRECT_V372.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b); x.SetPosition(P(*q)); x.SetWidth(pcbnew.FromMM(.60)); x.SetDrill(pcbnew.FromMM(.30)); x.SetLayerPair(F,B); x.SetNet(n); x.SetNetCode(n.GetNetCode()); b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('XTAL_OUT')
 for x in list(b.GetTracks()):
  if x.GetNetname()=='XTAL_OUT': b.RemoveNative(x)
 s(b,n,F,(109.95,64.4),(117.5,64.4)); v(b,n,(117.5,64.4)); s(b,n,B,(117.5,64.4),(117.5,49)); v(b,n,(117.5,49)); s(b,n,F,(117.5,49),(116.7,49))
 s(b,n,F,(120.4,53),(120.4,50)); v(b,n,(120.4,50)); s(b,n,B,(120.4,50),(117.5,50)); s(b,n,B,(117.5,50),(117.5,49))
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
