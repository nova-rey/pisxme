"""V1028: disposable GND-zone stitching-via discriminator."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_U140_3V3_GND_CONTACT_V1027.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_GND_ZONE_STITCH_PROBE_V1028.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('GND'); q=pcbnew.PCB_VIA(b); q.SetPosition(P(70.0,45.0)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q); b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
