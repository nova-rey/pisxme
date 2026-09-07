"""V228: complete CLKREQ on the V227 coupled source-field basis."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_QFN_SIDEBAND_SPISO3_PERST_V227.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CLKREQ_R3_U113_J1_52_V228.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,l,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,x,y):
    v=pcbnew.PCB_VIA(b);v.SetPosition(p(x,y));v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
    b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('CLKREQ_N')
    add(b,n,F,(101.95,60.4),(102.4,61.0));via(b,n,102.4,61.0)
    add(b,n,B,(102.4,61.0),(102.4,68.4));add(b,n,B,(102.4,68.4),(137.5,68.4));via(b,n,137.5,68.4)
    add(b,n,F,(137.5,68.4),(137.5,70.28));add(b,n,F,(137.5,70.28),(136.5,70.28))
    add(b,n,F,(92.0,48.0),(92.0,42.0));via(b,n,92.0,42.0)
    add(b,n,B,(92.0,42.0),(80.0,42.0));add(b,n,B,(80.0,42.0),(80.0,68.4));add(b,n,B,(80.0,68.4),(102.4,68.4))
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
