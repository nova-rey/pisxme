"""V1052: move local SPI flash outboard and test the U1.20/U2.3 rail."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_ORIENTATION0_QFN_RAILS_V1048.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_MOVE_U2_SUPPLY_V1052.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); u2=b.FindFootprintByReference('U2'); u2.SetPosition(u2.GetPosition()+pcbnew.VECTOR2I_MM(10,0)); n=b.FindNet('RTL_3V3')
# U1.20 escapes past the source row, then the moved flash receives the rail
# on its lower supply pad (new U2.3 at x=115,y=77.6).
add(b,n,[(101.95,72.4),(104.5,72.4)],F); via(b,n,(104.5,72.4)); add(b,n,[(104.5,72.4),(114.5,72.4),(114.5,77.6)],B); via(b,n,(114.5,77.6)); add(b,n,[(114.5,77.6),(115,77.6)],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
