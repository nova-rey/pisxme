"""V52: normalize resistor frames and use a verified pad-side B.Cu collector."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_U1_52_HANDOFF_V49.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_3V3_RAIL_JOIN_V52.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def normalize(f,anchor):
 coords={p.GetNumber():p.GetPosition() for p in f.Pads()}; f.SetPosition(P(*anchor))
 for p in f.Pads(): p.SetPosition(coords[p.GetNumber()])
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3')
 for ref,anchor in [('R2',(89.6,56.0)),('R3',(92.6,56.0))]: normalize(b.FindFootprintByReference(ref),anchor)
 # Pad 2 is the right-hand RTL_3V3 pad on both native resistor footprints.
 tr(b,n,F,(90.2,56.0),(91.2,56.0));tr(b,n,F,(91.2,56.0),(91.2,54.0));vi(b,n,(91.2,54.0))
 tr(b,n,F,(93.2,56.0),(94.2,56.0));tr(b,n,F,(94.2,56.0),(94.2,54.0));vi(b,n,(94.2,54.0))
 tr(b,n,B,(91.2,54.0),(94.2,54.0));tr(b,n,B,(94.2,54.0),(102.5,54.0));tr(b,n,B,(102.5,54.0),(102.5,60.8));tr(b,n,B,(102.5,60.8),(100.4,60.8))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
