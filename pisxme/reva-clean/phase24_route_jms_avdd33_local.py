#!/usr/bin/env python3
"""Route U11 JMS_AVDD33 to its native C80 decoupler endpoint."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_MKEY_USB3_VCCK_LOCAL_20260912.kicad_pcb'
OUT=R/'PHASE24_STORAGE_MKEY_USB3_AVDD33_LOCAL_20260912.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('JMS_AVDD33')
def tr(a,z,l=pcbnew.F_Cu,w=.20):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(p):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
tr((142.2,138.6),(142.2,140.0),pcbnew.F_Cu,.15); tr((142.2,140.0),(148.0,140.0),pcbnew.F_Cu,.15); via((148.0,140.0)); tr((148.0,140.0),(148.0,112.5),pcbnew.B_Cu); via((148.0,112.5)); tr((148.0,112.5),(126.5,112.5)); tr((126.5,112.5),(126.5,114.5))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
