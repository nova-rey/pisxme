#!/usr/bin/env python3
"""Route the JMS583 reset support tree on the current storage candidate."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_MKEY_USB3_VCCO_REHOME_20260912.kicad_pcb'
OUT=R/'PHASE24_STORAGE_MKEY_USB3_RESET_LOCAL_20260912.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('JMS_RESET_N')
def tr(a,z,l=pcbnew.F_Cu,w=.20):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(p):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
# Leave the U11 left-edge row, then use a dedicated B.Cu low-speed channel.
tr((136.35,137.6),(135.2,137.6),w=.15); tr((135.2,137.6),(135.2,139.6),w=.15); via((135.2,139.6)); tr((135.2,139.6),(128.0,139.6),pcbnew.B_Cu); via((128.0,139.6)); tr((128.0,139.6),(128.0,116.0),w=.15); tr((128.0,116.0),(126.5,116.0),w=.15); tr((126.5,116.0),(126.5,117.0),w=.15); tr((126.5,116.0),(123.0,116.0),w=.15); tr((123.0,116.0),(123.0,117.0))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
