"""Outboard U5 capacitor placement discriminator on F.Cu."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb';OUT=R/'PHASE24_U5_CAPS_OUTBOARD.kicad_pcb'
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def P(f,n):return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def T(b,n,a,z):
 if a!=z:
  t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(pcbnew.F_Cu);t.SetWidth(pcbnew.FromMM(.2));t.SetNet(n);b.Add(t)
def main():
 b=pcbnew.LoadBoard(str(BASE));io=pcbnew.PCB_IO_KICAD_SEXPR();rail=b.FindNet('/REGULATORS/BRIDGE_1V1');gnd=b.FindNet('POWER_GND')
 for t in list(b.GetTracks()):
  if t.GetNetCode()==rail.GetNetCode():b.RemoveNative(t)
 fs={}
 for ref,pos in {'C44':(260,145),'C45':(266,145),'C46':(260,151),'C47':(266,151)}.items():
  f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),'C_1210_3225Metric');f.SetReference(ref);f.SetPosition(V(*pos));b.Add(f);fs[ref]=f
  P(f,'1').SetNet(rail);P(f,'1').SetNetCode(rail.GetNetCode());P(f,'2').SetNet(gnd);P(f,'2').SetNetCode(gnd.GetNetCode())
 src=(237.25,106.25);T(b,rail,src,(258,106.25));T(b,rail,(258,106.25),(258,153))
 for f in fs.values():
  q=xy(P(f,'1'));T(b,rail,(258,q[1]),q)
 b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
