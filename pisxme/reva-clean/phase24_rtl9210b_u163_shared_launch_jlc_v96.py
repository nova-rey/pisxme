"""V96: join U1.63 RTL_1V1 to the promoted U1.60 F.Cu launch."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_U160_XTAL_ABOVE_JLC_V95.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_U163_SHARED_LAUNCH_JLC_V96.kicad_pcb'
F=pcbnew.F_Cu;B=pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z,w=.15):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(w));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('RTL_1V1');d=b.GetDesignSettings();d.m_TrackMinWidth=pcbnew.FromMM(.13208);d.m_MinClearance=pcbnew.FromMM(.15);nc=d.m_NetSettings.GetDefaultNetclass();nc.SetTrackWidth(pcbnew.FromMM(.13208));nc.SetClearance(pcbnew.FromMM(.15));d.m_NetSettings.SetDefaultNetclass(nc);d.m_NetSettings.RecomputeEffectiveNetclasses()
 tr(b,n,F,(99.2,73.95),(99.2,74.8));
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
