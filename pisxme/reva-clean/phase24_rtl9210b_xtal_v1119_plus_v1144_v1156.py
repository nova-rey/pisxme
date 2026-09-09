"""V1156: combine known-clean V1119 XTAL_IN with V1144 XTAL_OUT."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_QFN_GND_ATTACH_V1123.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_XTAL_V1119_PLUS_V1144_V1156.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,c,l,ps):
    for a,z in zip(ps,ps[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNetCode(c); b.Add(q)
def via(b,c,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.6)); q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(F,B); q.SetNetCode(c); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); ni=b.FindNet('XTAL_IN').GetNetCode(); no=b.FindNet('XTAL_OUT').GetNetCode()
tr(b,ni,F,[(94.05,67.2),(93.5,67.2),(93.0,67.5),(91.5,68.6)])
via(b,ni,(91.5,68.6)); tr(b,ni,B,[(91.5,68.6),(91.5,75.0),(85.5,75.0),(85.5,62.0)])
via(b,ni,(85.5,62.0)); tr(b,ni,F,[(85.5,62.0),(88.0,62.0),(88.0,59.0)])
tr(b,no,F,[(94.05,67.6),(93.4,67.6),(91.5,67.6)])
via(b,no,(91.5,67.6)); tr(b,no,B,[(91.5,67.6),(88.0,68.0),(88.0,58.0)])
via(b,no,(88.0,58.0)); tr(b,no,F,[(88.0,58.0),(89.4,58.0),(89.4,59.0),(90.5,59.0),(90.5,60.5),(91.0,62.0)])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
