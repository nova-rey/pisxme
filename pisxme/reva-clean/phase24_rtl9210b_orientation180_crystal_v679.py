"""V679: close the local 25 MHz crystal and load-capacitor field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_RSET_LOWER_CHANNEL_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_CRYSTAL_V679.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); ni=b.FindNet('XTAL_IN'); no=b.FindNet('XTAL_OUT')
# Keep the two crystal nets on separate monotonic corridors with short cap joins.
t(b,ni,(101.95,72.8),(104.0,72.8));t(b,ni,(104.0,72.8),(108.3,75.8))
t(b,ni,(108.3,75.8),(109.6,77.0));t(b,ni,(109.6,77.0),(109.6,78.0))
t(b,no,(101.95,72.4),(104.0,71.5));t(b,no,(104.0,71.5),(109.7,75.8))
t(b,no,(109.7,75.8),(111.4,77.0));t(b,no,(111.4,77.0),(111.4,78.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
