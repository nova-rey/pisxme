"""V36: disposable F.Cu local-rail-zone probe from the V35 support island."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_LOCAL_RAIL_ZONES_V36.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def zone(board,net,pts):
 z=pcbnew.ZONE(board);z.SetLayer(pcbnew.F_Cu);z.SetNet(net);z.SetNetCode(net.GetNetCode());z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL)
 poly=pcbnew.VECTOR_VECTOR2I()
 for x,y in pts:poly.append(P(x,y))
 z.AddPolygon(poly);board.Add(z)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 zone(b,b.FindNet('RTL_3V3'),[(83.8,78),(91.5,78),(91.5,73),(93,73),(93,64),(101.5,64),(101.5,67),(111,67),(111,71),(101,71),(101,75),(95.5,75),(95.5,78),(91.5,78),(91.5,82),(83.8,82)])
 zone(b,b.FindNet('RTL_5V'),[(94,64),(97.5,64),(97.5,65),(103,65),(103,67),(118,67),(118,71),(101,71),(101,69),(94,69)])
 zone(b,b.FindNet('RTL_1V1'),[(97,64),(100,64),(100,67),(115,67),(115,71),(101,71),(101,75),(100,75),(100,76),(95,76),(95,74),(92,74),(92,67),(97,67)])
 b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
