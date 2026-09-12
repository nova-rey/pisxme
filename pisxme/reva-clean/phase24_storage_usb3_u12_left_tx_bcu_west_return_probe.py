#!/usr/bin/env python3
"""Third/final bounded TX strategy: west-side B.Cu return vias."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "PHASE24_STORAGE_MKEY_USB3_U12_LEFT_R80_MOVE_20260912.kicad_pcb"
OUT = ROOT / "PHASE24_STORAGE_MKEY_USB3_U12_LEFT_TX_BCU_WEST_RETURN_20260912.kicad_pcb"
TX = ("CM5_USB3_TX_N", "CM5_USB3_TX_P")

def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z,l=pcbnew.F_Cu):
    q=b.FindNet(n); t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l)
    t.SetWidth(pcbnew.FromMM(.13208)); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
def vi(b,n,p):
    q=b.FindNet(n); v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30))
    v.SetNet(q); v.SetNetCode(q.GetNetCode()); b.Add(v)

b=pcbnew.LoadBoard(str(BASE))
if b is None: raise SystemExit('cannot load base')
for x in list(b.GetTracks()):
    if isinstance(x,pcbnew.PCB_VIA) or x.GetNetname() not in TX: continue
    a,z=x.GetStart(),x.GetEnd(); ax,ay,zx,zy=map(pcbnew.ToMM,(a.x,a.y,z.x,z.y))
    if max(ay,zy)>120 and min(ax,zx)>140: b.RemoveNative(x)

# Pair remains coupled on B.Cu and returns west of the RX_P F.Cu trunk (x=147).
tr(b,'CM5_USB3_TX_N',(149,108),(149,124)); vi(b,'CM5_USB3_TX_N',(149,124))
tr(b,'CM5_USB3_TX_N',(149,124),(146.0,124),pcbnew.B_Cu)
tr(b,'CM5_USB3_TX_N',(146.0,124),(146.0,134.5),pcbnew.B_Cu); vi(b,'CM5_USB3_TX_N',(146.0,134.5))
tr(b,'CM5_USB3_TX_N',(146.0,134.5),(148.7,136.2))
tr(b,'CM5_USB3_TX_P',(151,112),(151,126)); vi(b,'CM5_USB3_TX_P',(151,126))
tr(b,'CM5_USB3_TX_P',(151,126),(146.6,126),pcbnew.B_Cu)
tr(b,'CM5_USB3_TX_P',(146.6,126),(146.6,133.8),pcbnew.B_Cu); vi(b,'CM5_USB3_TX_P',(146.6,133.8))
tr(b,'CM5_USB3_TX_P',(146.6,133.8),(148.3,135.8))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
