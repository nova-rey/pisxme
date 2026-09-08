"""V567: RTL_5V pad escapes with B.Cu perimeter bypass; disposable trial."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V562.kicad_pcb'
out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V567_RTL5V_BYPASS.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,a,z,l):
    t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def v(b,n,q):
    x=pcbnew.PCB_VIA(b); x.SetPosition(P(*q)); x.SetWidth(pcbnew.FromMM(.60)); x.SetDrill(pcbnew.FromMM(.30)); x.SetLayerPair(F,B); x.SetNet(n); x.SetNetCode(n.GetNetCode()); b.Add(x)
b=pcbnew.LoadBoard(str(base)); n=b.FindNet('RTL_5V')
c5=next(x for x in b.Footprints() if x.GetReference()=='C5'); c5.SetPosition(P(96,55.5))
# Pad 33 and pad 17 each leave on F.Cu; vias are outside the QFN pad field.
s(b,n,(102.05,64.8),(101.5,64.8),F); s(b,n,(101.5,64.8),(101.2,64.2),F); v(b,n,(101.2,64.2))
s(b,n,(102.8,58.05),(101.2,58.05),F); v(b,n,(101.2,58.05))
# Join the two source branches on B.Cu, then bypass the 1V1 field at the perimeter.
s(b,n,(101.2,64.2),(101.2,58.05),B)
s(b,n,(101.2,58.05),(101.2,54.5),B); s(b,n,(101.2,54.5),(95.2,54.5),B); s(b,n,(95.2,54.5),(95.2,54.8),B); v(b,n,(95.2,54.8)); s(b,n,(95.2,54.8),(95.2,55.5),F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
