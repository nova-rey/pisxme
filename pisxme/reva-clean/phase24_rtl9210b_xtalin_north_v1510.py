"""V1510: XTAL_IN north corridor, separated from PCIe lower shelves."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RSET_WEST_V1508.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTALIN_NORTH_V1510.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('XTAL_IN'); assert n; F,B=pcbnew.F_Cu,pcbnew.B_Cu
def tr(a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(*xy)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
tr((94.05,67.2),(93.4,67.4),F); tr((93.4,67.4),(91.5,67.4),F); via((91.5,67.4)); tr((91.5,67.4),(91.5,66.0),B); tr((91.5,66.0),(86.0,66.0),B); tr((86.0,66.0),(86.0,55.0),B); tr((86.0,55.0),(88.0,55.0),B); via((88.0,55.0)); tr((88.0,55.0),(88.0,62.0),F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
