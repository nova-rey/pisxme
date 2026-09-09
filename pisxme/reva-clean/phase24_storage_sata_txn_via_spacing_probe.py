"""Disposable minimal SATA probe: move only the TXN source transition."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_VCCK_LOCAL_V1.kicad_pcb'; OUT=R/'PHASE24_STORAGE_SATA_TXN_VIA_SPACING_V1.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu
def V(x,y): return pcbnew.VECTOR2I(int(round(x*1e6)),int(round(y*1e6)))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def P(r,n): return xy(b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition())
def N(s):
 n=b.FindNet(s) or b.FindNet('/STORAGE/'+s)
 if not n: raise RuntimeError(s)
 return n
def seg(n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.2));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def path(n,pts,l):
 for a,z in zip(pts,pts[1:]):seg(n,a,z,l)
def via(n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE))
for t in list(b.GetTracks()):
 if 'BRIDGE_SATA_' in t.GetNetname(): b.RemoveNative(t)
spec={
 'BRIDGE_SATA_RX_P':('U7','60','C32',(93.7,129.4),[(97,120),(103,120)]),
 'BRIDGE_SATA_RX_N':('U7','59','C33',(94.3,130.0),[(96,128),(103,128)]),
 'BRIDGE_SATA_TX_P':('U7','57','C30',(96.5,129.4),[(99,116),(103,116)]),
 'BRIDGE_SATA_TX_N':('U7','56','C31',(97.8,130.6),[(98,132),(103,132)]),}
esc={'BRIDGE_SATA_RX_P':[(94.6,127.8),(94.6,128.7),(93.7,129.4)],'BRIDGE_SATA_RX_N':[(95,127.8),(95,129),(94.3,130)],'BRIDGE_SATA_TX_P':[(95.8,127.8),(95.8,128.7),(96.5,129.4)],'BRIDGE_SATA_TX_N':[(96.2,127.8),(96.2,129.1),(97.8,130.6)]}
for name,(r,p,c,sv,corr) in spec.items():
 n=N(name); path(n,esc[name],F); via(n,sv); path(n,[sv]+corr,B); via(n,(103, {'BRIDGE_SATA_RX_P':120,'BRIDGE_SATA_RX_N':128,'BRIDGE_SATA_TX_P':116,'BRIDGE_SATA_TX_N':132}[name])); path(n,[(103, {'BRIDGE_SATA_RX_P':120,'BRIDGE_SATA_RX_N':128,'BRIDGE_SATA_TX_P':116,'BRIDGE_SATA_TX_N':132}[name]),P(c,'2')],F)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.BuildListOfNets();b.Save(str(OUT));print(OUT)
