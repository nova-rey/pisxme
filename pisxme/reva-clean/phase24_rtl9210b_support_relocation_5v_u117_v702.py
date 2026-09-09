"""V702: shorten and angle the U1.17 escape past the nearby 1V1 via."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_OVERPASS_FINAL_V699.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_U117_V702.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_5V')
tr(b,n,F,(101.20,73.95),(101.20,74.50));tr(b,n,F,(101.20,74.50),(102.20,76.20));vi(b,n,(102.20,76.20))
tr(b,n,B,(102.20,76.20),(104.50,76.20));vi(b,n,(104.50,76.20))
tr(b,n,F,(104.50,76.20),(104.50,50.00));tr(b,n,F,(104.50,50.00),(106.00,50.00))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
