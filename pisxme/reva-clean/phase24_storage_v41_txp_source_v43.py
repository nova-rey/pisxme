"""V43: translate only the U7 SATA TX_P source transition leftward."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V41_SATA_TX_PAIR.kicad_pcb'
OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V43_TXP_SOURCE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def pad(r,p): return b.FindFootprintByReference(r).FindPadByNumber(str(p))
def seg(n,a,z,l):
    t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(n,p):
    v=pcbnew.PCB_VIA(b);v.SetPosition(P(*p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
n=b.FindNet('/STORAGE/BRIDGE_SATA_TX_P') or b.FindNet('BRIDGE_SATA_TX_P');assert n
for t in list(b.GetTracks()):
    if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
start=xy(pad('U7','57').GetPosition()); cap=xy(pad('C30','2').GetPosition()); vp=(92.5,125.5)
for a,z in zip([start,(95.8,127.8),(95.8,125.5),vp],[(95.8,127.8),(95.8,125.5),vp]): seg(n,a,z,F)
via(n,vp);seg(n,vp,(92.5,116.0),B);seg(n,(92.5,116.0),cap,B)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
