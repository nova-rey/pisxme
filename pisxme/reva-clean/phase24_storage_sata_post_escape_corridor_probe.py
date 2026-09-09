"""Disposable SATA probe: preserve U7 native dogbones, alter post-escape lanes."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_VCCK_LOCAL_V1.kicad_pcb'; OUT=R/'PHASE24_STORAGE_SATA_POST_ESCAPE_V1.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu
def V(x,y): return pcbnew.VECTOR2I(int(round(x*1e6)),int(round(y*1e6)))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def pos(b,r,n): return xy(pad(b,r,n).GetPosition())
def N(b,s):
 n=b.FindNet(s) or b.FindNet('/STORAGE/'+s)
 if not n: raise RuntimeError(s)
 return n
def seg(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.2));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def path(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):seg(b,n,a,z,l)
def via(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE))
for t in list(b.GetTracks()):
 if 'BRIDGE_SATA_' in t.GetNetname(): b.RemoveNative(t)
ch={
 'BRIDGE_SATA_RX_P':('U7','60','C32',(93.7,129.4),(103.0,120.0),[(94.6,127.8),(94.6,128.7),(93.7,129.4)],[(97.0,120.0),(103.0,120.0)]),
 'BRIDGE_SATA_RX_N':('U7','59','C33',(94.3,130.0),(103.0,128.0),[(95.0,127.8),(95.0,129.0),(94.3,130.0)],[(96.0,128.0),(103.0,128.0)]),
 'BRIDGE_SATA_TX_P':('U7','57','C30',(96.5,129.4),(103.0,116.0),[(95.8,127.8),(95.8,128.7),(96.5,129.4)],[(101.0,129.4),(101.0,114.0),(103.0,114.0),(103.0,116.0)]),
 'BRIDGE_SATA_TX_N':('U7','56','C31',(97.1,129.4),(103.0,132.0),[(96.2,127.8),(96.2,128.7),(97.1,129.4)],[(102.0,129.4),(102.0,134.0),(103.0,134.0),(103.0,132.0)]),
}
for name,(sr,sn,cr,sv,cv,escape,corr) in ch.items():
 n=N(b,name); path(b,n,escape,F); via(b,n,sv); path(b,n,[sv]+corr,B); via(b,n,cv); path(b,n,[cv,pos(b,cr,'2')],F)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
