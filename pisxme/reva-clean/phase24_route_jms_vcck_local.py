#!/usr/bin/env python3
"""Route the U11 JMS_VCCK pad to its native C82 decoupler endpoint."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_MKEY_USB3_EAST_SUPPORT_V6_U14_REPAIR_20260912.kicad_pcb'
OUT=R/'PHASE24_STORAGE_MKEY_USB3_VCCK_LOCAL_20260912.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('JMS_VCCK')
def tr(a,z,l=pcbnew.F_Cu):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
# U11 left-edge exit, then a B.Cu vertical transition before approaching C82.
tr((136.35,132.4),(133.0,132.4)); v=pcbnew.PCB_VIA(b); v.SetPosition(V(133.0,132.4)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v); tr((133.0,132.4),(133.0,116.0),pcbnew.B_Cu); v=pcbnew.PCB_VIA(b); v.SetPosition(V(133.0,116.0)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v); tr((133.0,116.0),(133.5,114.5))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
