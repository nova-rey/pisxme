"""V156: move only the CLKREQ_N connector launch outboard of REFCLK."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_1V1_OUTBOARD_HANDOFF_V154.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_MOVE_CLKREQ_J1_V156.kicad_pcb'
F=pcbnew.F_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return (round(p.x/1e6,3),round(p.y/1e6,3))
def tr(b,n,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F);q.SetWidth(pcbnew.FromMM(.20));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('CLKREQ_N')
 remove={((137.5,53.5),(137.5,70.275)),((137.5,70.275),(136.5,70.275)),((112.0,53.5),(137.5,53.5))}
 for x in list(b.GetTracks()):
  if x.GetNetname()=='CLKREQ_N' and type(x).__name__=='PCB_TRACK':
   pair=(xy(x.GetStart()),xy(x.GetEnd()))
   if pair in remove or pair[::-1] in remove:b.RemoveNative(x)
 tr(b,n,(112.0,53.5),(139.0,53.5));tr(b,n,(139.0,53.5),(139.0,70.275));tr(b,n,(139.0,70.275),(136.5,70.275))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
