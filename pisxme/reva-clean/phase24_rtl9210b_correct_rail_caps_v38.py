"""V38: replace malformed disposable rail-cap footprints with local SMD CAD."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CORRECT_RAIL_CAPS_V38.kicad_pcb'
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def main():
 b=pcbnew.LoadBoard(str(BASE));io=pcbnew.PCB_IO_KICAD_SEXPR()
 specs=[('C3','RTL_3V3',(111.2,69.0)),('C4','RTL_1V1',(114.2,69.0)),('C5','RTL_5V',(117.2,69.0))]
 for ref,netname,pos in specs:
  old=b.FindFootprintByReference(ref);b.RemoveNative(old)
  f=io.FootprintLoad(str(HERE/'PiSXMe_RevA_Clean.pretty'),'C_0603_1608Metric')
  f.SetReference(ref);f.SetPosition(P(*pos));b.Add(f)
  net=b.FindNet(netname);g=b.FindNet('GND')
  for p in f.Pads():
   n=net if p.GetNumber()=='1' else g;p.SetNet(n);p.SetNetCode(n.GetNetCode())
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
