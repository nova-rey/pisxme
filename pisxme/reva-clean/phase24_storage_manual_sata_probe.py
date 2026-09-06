"""Disposable SATA continuation for the native manual USB3 probe."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_LOCAL_J3_EDGE_MANUAL_MONOTONIC.kicad_pcb'
OUT=R/'PHASE24_STORAGE_LOCAL_J3_EDGE_MANUAL_USB3_SATA_V2.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.15)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def n(b,s):
    q=b.FindNet(s)
    if q is None: raise RuntimeError(s)
    return q
def pad(b,r,k): return b.FindFootprintByReference(r).FindPadByNumber(str(k))
def tr(b,net,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(F);t.SetWidth(W);t.SetNet(net);b.Add(t)
def emit(b,net,pts):
    for a,z in zip(pts,pts[1:]): tr(b,net,a,z)
b=pcbnew.LoadBoard(str(BASE))
jobs=[
 ('TX_P','57','C30','2','1',[(90.5,115.5),(90.5,113.5),(100,113.5),(105.5,118)],[(120,120),(134,130)]),
 ('TX_N','56','C31','2','2',[(91.0,115.5),(91.0,112.5),(102,112.5),(113.5,118)],[(121,121),(142,131)]),
 ('RX_P','60','C32','2','3',[(89.0,115.5),(88.0,117.0),(98,130),(105.5,132)],[(120,132),(137,133.75)]),
 ('RX_N','59','C33','2','4',[(89.5,115.5),(88.5,118.0),(100,131),(113.5,132)],[(122,134),(145,133.5)]),
]
for suffix,up,cap,cp,jp,lane,socketlane in jobs:
    bridge=n(b,'/STORAGE/BRIDGE_SATA_'+suffix); socket=n(b,'/STORAGE/SATA_M2_'+suffix)
    a=xy(pad(b,'U7',up).GetPosition()); z=xy(pad(b,cap,cp).GetPosition()); emit(b,bridge,[a]+lane[1:])
    a=xy(pad(b,cap,'1').GetPosition()); z=xy(pad(b,'J3',jp).GetPosition()); emit(b,socket,[a]+socketlane+[z])
    print(suffix,a,z)
b.Save(str(OUT));print(OUT)
