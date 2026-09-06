"""Disposable U7 SATA bridge-side escape to the authoritative capacitors."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_STORAGE_ISLAND_COHERENT_USB3_REPAIRED.kicad_pcb';OUT=R/'PHASE24_STORAGE_ISLAND_COHERENT_USB3_SATA_BRIDGE_ESCAPE.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.13208)
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):
 p=p.GetPosition() if hasattr(p,'GetPosition') else p;return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def P(b,r,n):return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def T(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);b.Add(t)
def X(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.50));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);b.Add(v)
b=pcbnew.LoadBoard(str(BASE)); jobs=(('TX_P','57','C30','2'),('TX_N','56','C31','2'),('RX_P','60','C32','2'),('RX_N','59','C33','2'))
for t in list(b.GetTracks()):
 if any(t.GetNetname()=='/STORAGE/BRIDGE_SATA_'+k for k,_,_,_ in jobs):b.Remove(t)
routes={'TX_P':(('/STORAGE/BRIDGE_SATA_TX_P',[(110.5,100.5),(110.5,98),(116.5,98),(116.5,97),(117.5,97)],F),),
 'TX_N':(('/STORAGE/BRIDGE_SATA_TX_N',[(111,100.5),(112,102),(112,112),(116.5,112),(116.5,113),(117.5,113)],B),),
 'RX_P':(('/STORAGE/BRIDGE_SATA_RX_P',[(109,100.5),(107,98),(122.5,98),(122.5,97),(123.5,97)],B),),
 'RX_N':(('/STORAGE/BRIDGE_SATA_RX_N',[(109.5,100.5),(108,103),(108,112),(122.5,112),(122.5,113),(123.5,113)],B),)}
for k,jp,cap,cp in jobs:
 n=b.FindNet(routes[k][0][0]); pts=routes[k][0][1]; layer=routes[k][0][2]; src=xy(P(b,'U7',jp)); dst=xy(P(b,cap,cp));
 T(b,n,src,pts[0],F)
 if layer==F:
  for a,z in zip(pts,pts[1:]):T(b,n,a,z,F)
 else:
  T(b,n,pts[0],pts[1],F);X(b,n,pts[1])
  for a,z in zip(pts[1:],pts[2:-1]):T(b,n,a,z,B)
  X(b,n,pts[-2]);T(b,n,pts[-2],dst,F)
 if layer==F:T(b,n,pts[-1],dst,F)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
