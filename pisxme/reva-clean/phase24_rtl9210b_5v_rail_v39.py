"""V39: explicit RTL_5V route against corrected native C5 pads."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CORRECT_RAIL_CAPS_V38.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_5V_RAIL_V39.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_5V')
 t(b,n,F,(95.2,66.05),(95.2,63.0));v(b,n,(95.2,63.0));t(b,n,B,(95.2,63.0),(102.5,63.0));t(b,n,B,(102.5,63.0),(102.5,59.0));t(b,n,B,(102.5,59.0),(116.0,59.0));t(b,n,B,(116.0,59.0),(116.0,68.0));v(b,n,(116.0,68.0));t(b,n,F,(116.0,68.0),(116.4,69.0))
 t(b,n,F,(101.95,66.8),(103.0,66.8));v(b,n,(103.0,66.8));t(b,n,B,(103.0,66.8),(102.5,66.8));t(b,n,B,(102.5,66.8),(102.5,63.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
