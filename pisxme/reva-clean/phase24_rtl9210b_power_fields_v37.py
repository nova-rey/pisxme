"""V37: explicit F.Cu pad-to-via access and shaped B.Cu power fields."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_POWER_FIELDS_V37.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;TW=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,a,z,w=TW):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(w);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def z(b,n,pts):
 q=pcbnew.ZONE(b);q.SetLayer(B);q.SetNet(n);q.SetNetCode(n.GetNetCode());q.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL)
 p=pcbnew.VECTOR_VECTOR2I();[p.append(P(*xy)) for xy in pts];q.AddPolygon(p);b.Add(q)
def access(b,net,items):
 for pad,via_xy in items:
  t(b,net,pad,via_xy);v(b,net,via_xy)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 n=b.FindNet('RTL_3V3');access(b,n,[((94.8,66.05),(94.8,65.0)),((94.05,68.4),(93.2,68.4)),((94.8,73.95),(94.8,75.0)),((84.2,80),(84.2,81)),((90.2,80),(90.2,81)),((90.2,56),(89.5,56)),((93.2,56),(94.0,56)),((110.4,69),(110.4,68))]);z(b,n,[(82,54),(112,54),(112,72),(102,72),(102,76),(92,76),(92,74),(90,74),(90,83),(82,83)])
 n=b.FindNet('RTL_5V');access(b,n,[((95.2,66.05),(95.2,64.5)),((101.95,66.8),(103.0,66.8)),((116.4,69),(116.4,68))]);z(b,n,[(93,63),(119,63),(119,72),(101,72),(101,69),(93,69)])
 n=b.FindNet('RTL_1V1');access(b,n,[((98.4,66.05),(98.4,64.8)),((94.05,67.2),(93.2,67.2)),((94.05,68.8),(93.2,68.8)),((94.05,72.8),(93.2,72.8)),((96,73.95),(96,75)),((98,73.95),(98,75)),((99.2,73.95),(99.2,75)),((101.95,67.2),(103.0,67.2)),((113.4,69),(113.4,68))]);z(b,n,[(92,63),(116,63),(116,72),(102,72),(102,76),(92,76)])
 b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
