"""V1519: XTAL_OUT source hop west of the rehomed U1.55 branch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U155_REHOME_V1517.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTALOUT_SOURCEHOP_V1519.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('XTAL_OUT'); assert n; F,B=pcbnew.F_Cu,pcbnew.B_Cu
def tr(a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(*xy)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
tr((94.05,67.6),(93.4,67.6),F); tr((93.4,67.6),(92.4,67.4),F); via((92.4,67.4)); tr((92.4,67.4),(88.8,67.4),B); via((88.8,67.4)); tr((88.8,67.4),(87.2,67.4),F); via((87.2,67.4)); tr((87.2,67.4),(86.0,55.0),B); tr((86.0,55.0),(89.0,55.0),B); via((89.0,55.0)); tr((89.0,55.0),(89.4,59.0),F); tr((89.4,59.0),(90.5,60.5),F); tr((90.5,60.5),(91.0,62.0),F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
