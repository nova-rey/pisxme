"""V911: full support geometry with only inherited SPI copper scrubbed."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V885_SUPPORT_GND_RETURN_V888.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V888_FULL_SUPPORT_SPI_SCRUB_V911.kicad_pcb'
F=pcbnew.F_Cu;B=pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(x,y));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
for x in list(b.GetTracks()):
 if x.GetNetname() in ('SPICS','SPICLK','SPISO','SPISO3','SPISI') or (x.GetNetname()=='RTL_3V3' and any(92<=p.x/1e6<=95.5 and 73<=p.y/1e6<=77.5 for p in (x.GetStart(),x.GetEnd()))): b.RemoveNative(x)
p=b.FindNet('RTL_3V3');tr(b,p,[(94.8,73.95),(94.8,76.0),(93.0,76.0)],F);via(b,p,93.0,76.0)
n=b.FindNet('XTAL_IN');tr(b,n,[(95.2,73.95),(95.2,76.5),(100.0,76.5)],F);via(b,n,100.0,76.5);tr(b,n,[(100.0,76.5),(100.0,55.0),(86.0,55.0)],B);via(b,n,86.0,55.0);tr(b,n,[(86.0,55.0),(88.0,59.0),(88.0,62.0)],F)
n=b.FindNet('XTAL_OUT');tr(b,n,[(95.6,73.95),(95.6,77.0),(96.0,77.0)],F);via(b,n,96.0,77.0);tr(b,n,[(96.0,77.0),(82.0,77.0),(82.0,54.0),(90.2,54.0)],B);via(b,n,90.2,54.0);tr(b,n,[(90.2,54.0),(89.4,59.0),(91.0,62.0)],F)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
