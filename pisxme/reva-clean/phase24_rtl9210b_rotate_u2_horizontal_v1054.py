"""V1054: add the local GND return for the rotated U2 pad 4."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ROTATE_U2_HORIZONTAL_V1053.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ROTATE_U2_HORIZONTAL_V1054.kicad_pcb'; F=pcbnew.F_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('GND'); q=pcbnew.PCB_TRACK(b); q.SetStart(P(115,76.4)); q.SetEnd(P(115,77.4)); q.SetLayer(F); q.SetWidth(pcbnew.FromMM(.2)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
v=pcbnew.PCB_VIA(b); v.SetPosition(P(115,77.4)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
