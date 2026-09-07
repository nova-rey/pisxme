"""V91: move the U1.60 transition outside the QFN bottom pad field."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_QFN_ESCAPE_JLC_V86.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_U160_FAR_RIGHT_JLC_V91.kicad_pcb'
F=pcbnew.F_Cu;B=pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z,w=.15):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def vi(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1');d=b.GetDesignSettings();d.m_TrackMinWidth=pcbnew.FromMM(.13208);d.m_MinClearance=pcbnew.FromMM(.15);nc=d.m_NetSettings.GetDefaultNetclass();nc.SetTrackWidth(pcbnew.FromMM(.13208));nc.SetClearance(pcbnew.FromMM(.15));d.m_NetSettings.SetDefaultNetclass(nc);d.m_NetSettings.RecomputeEffectiveNetclasses()
 tr(b,n,F,(98.0,73.95),(98.0,74.8));tr(b,n,F,(98.0,74.8),(99.6,74.8));tr(b,n,F,(99.6,74.8),(99.6,75.8));vi(b,n,(99.6,75.8));tr(b,n,B,(99.6,75.8),(110.0,75.8));tr(b,n,B,(110.0,75.8),(110.0,69.5))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
