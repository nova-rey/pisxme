"""Ground-aware U5 island with separated source-side rail lanes."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb';OUT=R/'PHASE24_U5_CAPS_GROUND_AWARE_V2.kicad_pcb'
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def P(f,n):return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def T(b,n,a,z):
 if a!=z:
  t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(pcbnew.F_Cu);t.SetWidth(pcbnew.FromMM(.2));t.SetNet(n);b.Add(t)
def main():
 b=pcbnew.LoadBoard(str(BASE));io=pcbnew.PCB_IO_KICAD_SEXPR();rail=b.FindNet('/REGULATORS/BRIDGE_1V1');gnd=b.FindNet('POWER_GND');fs={}
 for ref,pos in {'C44':(250,128),'C45':(258,128),'C46':(250,138),'C47':(258,138)}.items():
  f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),'C_1210_3225Metric');f.SetReference(ref);f.SetPosition(V(*pos));f.SetOrientationDegrees(90);b.Add(f);fs[ref]=f;P(f,'1').SetNet(rail);P(f,'1').SetNetCode(rail.GetNetCode());P(f,'2').SetNet(gnd);P(f,'2').SetNetCode(gnd.GetNetCode())
 # Existing 1V1 node at U5's validated rail endpoint; side-separated trunks
 # keep the return path out of every capacitor rail branch.
 T(b,rail,(237.25,107),(235,107));T(b,rail,(235,107),(235,120));T(b,rail,(235,120),(264,120));T(b,rail,(264,120),(264,136.65))
 T(b,gnd,(246.5,118),(246.5,119));T(b,gnd,(246.5,119),(244,119));T(b,gnd,(244,119),(244,139.35))
 for f in fs.values():
  p1,p2=xy(P(f,'1')),xy(P(f,'2'));T(b,rail,(264,p1[1]),p1);T(b,gnd,(244,p2[1]),p2)
 b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
