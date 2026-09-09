"""V695: move the U1.20 3V3 descent outside the SPISI pad field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_C2_GND_U152_RSET_V693.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_3V3_LOAD_OUTER_V695.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
t(b,n,F,(101.95,72.4),(103.2,72.4));t(b,n,F,(103.2,72.4),(103.2,80.0));v(b,n,(103.2,80.0));t(b,n,B,(103.2,80.0),(120.4,80.0));v(b,n,(120.4,80.0));t(b,n,F,(120.4,80.0),(120.4,56.0));t(b,n,F,(120.4,56.0),(128.2,56.0));v(b,n,(128.2,56.0));t(b,n,F,(128.2,56.0),(128.2,58.0));v(b,n,(134.2,56.0));t(b,n,B,(128.2,56.0),(134.2,56.0));t(b,n,F,(134.2,56.0),(134.2,58.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
