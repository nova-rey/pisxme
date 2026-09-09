"""V694: close U1.20, C3, and U2 RTL_3V3 load endpoints."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_C2_GND_U152_RSET_V693.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_3V3_LOAD_V694.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_3V3')
# U1.20 lower/right escape to a dedicated B.Cu load collector.
t(b,n,F,(101.95,72.4),(102.5,72.4));t(b,n,F,(102.5,72.4),(102.5,80.0));v(b,n,(102.5,80.0));t(b,n,B,(102.5,80.0),(120.4,80.0));v(b,n,(120.4,80.0));t(b,n,F,(120.4,80.0),(120.4,51.0))
# C3.1 to U2.3/8 through a clear y=56 escape above the U2 pad row.
t(b,n,F,(120.4,51.0),(120.4,56.0));t(b,n,F,(120.4,56.0),(128.2,56.0));v(b,n,(128.2,56.0));t(b,n,F,(128.2,56.0),(128.2,58.0));v(b,n,(134.2,56.0));t(b,n,B,(128.2,56.0),(134.2,56.0));t(b,n,F,(134.2,56.0),(134.2,58.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
