"""V67: co-author XOUT with a rehomed JMS_XAVDDH transition."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V54_STORAGE_GND_SOLID.kicad_pcb'
OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V67_CLOCK_PAIR_REHOME.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
def route(name,ps,l):
 n=b.FindNet(name); assert n
 for a,z in zip(ps,ps[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(name,p):
 n=b.FindNet(name); assert n
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
for name in ('XOUT','JMS_XAVDDH'):
 n=b.FindNet(name); assert n
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
route('XOUT',[(137.8,131.4),(139.5,129.2)],F); via('XOUT',(139.5,129.2)); route('XOUT',[(139.5,129.2),(132,129.2),(146.5,112)],B); via('XOUT',(146.5,112)); route('XOUT',[(146.5,112),(148.9,115.85)],F)
route('JMS_XAVDDH',[(138.2,131.4),(138.2,130.4),(140.5,130.4),(140.5,128.5)],F); via('JMS_XAVDDH',(140.5,128.5)); route('JMS_XAVDDH',[(140.5,128.5),(149,121.5)],B); via('JMS_XAVDDH',(149,121.5)); route('JMS_XAVDDH',[(149,121.5),(149.5,120)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
