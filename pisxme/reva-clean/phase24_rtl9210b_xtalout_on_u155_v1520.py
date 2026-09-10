"""V1520: remove obsolete R1 GND collector before XTAL_OUT launch."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U155_REHOME_V1517.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_XTALOUT_ON_U155_V1520.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('XTAL_OUT'); g=b.FindNet('GND'); assert n and g; F,B=pcbnew.F_Cu,pcbnew.B_Cu
for q in list(b.GetTracks()):
 if q.GetNetname()=='GND':
  a=(q.GetStart()[0]/1e6,q.GetStart()[1]/1e6); z=(q.GetEnd()[0]/1e6,q.GetEnd()[1]/1e6)
  if {a,z}=={(89.2,65.0),(89.2,67.0)}: b.RemoveNative(q)
for q in list(b.GetTracks()):
 if type(q).__name__=='PCB_VIA' and q.GetNetname()=='GND' and abs(q.GetPosition()[0]/1e6-89.2)<.01 and abs(q.GetPosition()[1]/1e6-67.0)<.01: b.RemoveNative(q)
def tr(a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(*xy)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
tr((94.05,67.6),(93.4,67.6),F); tr((93.4,67.6),(91.0,67.8),F); via((91.0,67.8)); tr((91.0,67.8),(88.8,67.8),B); via((88.8,67.8)); tr((88.8,67.8),(87.2,67.8),F); via((87.2,67.8)); tr((87.2,67.8),(86.0,55.0),B); tr((86.0,55.0),(89.0,55.0),B); via((89.0,55.0)); tr((89.0,55.0),(89.4,59.0),F); tr((89.4,59.0),(90.5,60.5),F); tr((90.5,60.5),(91.0,62.0),F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
