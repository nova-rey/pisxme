"""V899: move XTAL_IN transition beyond the SPICS B.Cu corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V885_SUPPORT_GND_RETURN_V888.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V888_RESTORE_3V3_XTALIN_BCU_V899.kicad_pcb'
F=pcbnew.F_Cu;B=pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(x,y));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));p=b.FindNet('RTL_3V3')
tr(b,p,[(94.8,73.95),(94.8,76.0),(93.0,76.0)],F)
n=b.FindNet('XTAL_IN');tr(b,n,[(95.2,73.95),(95.2,74.8),(101.5,74.8),(101.5,76.0)],F);via(b,n,101.5,76.0)
tr(b,n,[(101.5,76.0),(101.5,55.0),(86.0,55.0)],B);via(b,n,86.0,55.0);tr(b,n,[(86.0,55.0),(88.0,59.0),(88.0,62.0)],F)
tr(b,b.FindNet('XTAL_OUT'),[(95.6,73.95),(95.6,74.6),(96.8,75.8),(96.8,77.0),(84.0,77.0),(84.0,54.0),(90.2,54.0),(90.2,59.0),(89.4,59.0),(91.0,62.0)],F)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
