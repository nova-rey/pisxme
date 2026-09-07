"""V122: move the PEDET bottom return clear of C2 XTAL_OUT."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_PEDET_J1_V116.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_PEDET_R2_RIGHT_RETURN_V122.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.15));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('PEDET')
 tr(b,n,F,(89.0,56.0),(80.0,56.0));via(b,n,(80.0,56.0));tr(b,n,B,(80.0,56.0),(80.0,83.0));tr(b,n,B,(80.0,83.0),(114.0,83.0));via(b,n,(114.0,83.0));tr(b,n,F,(114.0,83.0),(114.0,71.5));tr(b,n,F,(114.0,71.5),(104.0,71.5));tr(b,n,F,(104.0,71.5),(104.0,70.4))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
