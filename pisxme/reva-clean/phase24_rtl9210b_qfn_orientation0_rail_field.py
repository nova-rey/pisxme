"""Native 0-degree RTL9210B rail source-field allocation probe."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H/'PHASE24_RTL9210B_QFN_ORIENTATION0_PROBE.kicad_pcb'
OUT = H/'PHASE24_RTL9210B_QFN_ORIENTATION0_RAIL_FIELD.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
    t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
    v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(BASE))
n3=b.FindNet('RTL_3V3'); n1=b.FindNet('RTL_1V1')
# Perimeter-aware top/left escapes from the transformed native pad centers.
# 3V3 source group: U1.39 and U1.52, then separated B.Cu corridors to U2.
seg(b,n3,F,(99.6,66.05),(100.35,65.25)); via(b,n3,(100.35,65.25))
seg(b,n3,B,(100.35,65.25),(100.35,63.5)); seg(b,n3,B,(100.35,63.5),(80.2,63.5)); via(b,n3,(80.2,63.5)); seg(b,n3,F,(80.2,63.5),(80.2,80.0))
seg(b,n3,F,(94.05,66.8),(93.15,66.0)); via(b,n3,(93.15,66.0)); seg(b,n3,B,(93.15,66.0),(91.5,66.0)); seg(b,n3,B,(91.5,66.0),(91.5,63.5))
# 1V1 source group: two outward escapes join a separate lower B.Cu bus.
for src,esc in [((100.8,66.05),(101.65,65.25)),((99.2,66.05),(98.35,65.25)),((95.2,66.05),(94.35,65.25)),((94.05,68.0),(92.55,68.8)),((94.05,70.0),(92.0,70.8)),((94.05,71.2),(91.5,72.0))]:
    seg(b,n1,F,src,esc); via(b,n1,esc); seg(b,n1,B,esc,(esc[0],84.5));
seg(b,n1,B,(91.5,84.5),(104.0,84.5)); via(b,n1,(104.0,84.5)); seg(b,n1,F,(104.0,84.5),(104.0,82.0))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
