"""V42: farther-separated U7 SATA TX source vias and lanes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V41_SATA_TX_PAIR.kicad_pcb'; OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V42_SATA_TX_OUTER.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def pad(r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def seg(net,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(net);t.SetNetCode(net.GetNetCode());b.Add(t)
def via(net,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(net);v.SetNetCode(net.GetNetCode());b.Add(v)
spec=(('BRIDGE_SATA_TX_P','57','C30',(92.0,125.5),[(95.8,127.8),(95.8,125.5),(92.0,125.5)],[(92.0,125.5),(92.0,116.0),(103.0,116.0)]),('BRIDGE_SATA_TX_N','56','C31',(100.0,126.5),[(96.2,127.8),(96.2,126.5),(100.0,126.5)],[(100.0,126.5),(100.0,132.0),(103.0,132.0)]))
for name,pin,cap,vp,fp,bp in spec:
 n=b.FindNet('/STORAGE/'+name) or b.FindNet(name); assert n
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
 seg(n,fp[0],fp[1],F);seg(n,fp[1],fp[2],F);via(n,vp);seg(n,bp[0],bp[1],B);seg(n,bp[1],bp[2],B);via(n,bp[-1]);seg(n,bp[-1],xy(pad(cap,'2').GetPosition()),F)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
