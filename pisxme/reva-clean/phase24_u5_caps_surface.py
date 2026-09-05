"""Surface-only U5 C44-C47 discriminator; avoids unnecessary ground vias."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb'; OUT=R/'PHASE24_U5_CAPS_SURFACE.kicad_pcb'
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def P(f,n):return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def T(b,n,a,z):
 if a!=z:
  t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(pcbnew.F_Cu);t.SetWidth(pcbnew.FromMM(.2));t.SetNet(n);b.Add(t)
def main():
 b=pcbnew.LoadBoard(str(BASE));io=pcbnew.PCB_IO_KICAD_SEXPR();rail=b.FindNet('/REGULATORS/BRIDGE_1V1');gnd=b.FindNet('POWER_GND');u5=b.FindFootprintByReference('U5')
 for t in list(b.GetTracks()):
  if t.GetNetCode()==rail.GetNetCode():b.RemoveNative(t)
 fs={}
 for ref,pos in {'C44':(250,130),'C45':(256,130),'C46':(250,136),'C47':(256,136)}.items():
  f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),'C_1210_3225Metric');f.SetReference(ref);f.SetPosition(V(*pos));b.Add(f);fs[ref]=f;P(f,'1').SetNet(rail);P(f,'1').SetNetCode(rail.GetNetCode());P(f,'2').SetNet(gnd);P(f,'2').SetNetCode(gnd.GetNetCode())
 # Coherent F.Cu rail from U5's existing 1V1 launch to each capacitor.
 src=(237.25,106.25);T(b,rail,src,(247,106.25));T(b,rail,(247,106.25),(247,138));
 for ref,f in fs.items():
  q=xy(P(f,'1'));T(b,rail,(247,q[1]),q)
 # Ground is intentionally left to the existing filled POWER_GND zones;
 # there are no added vias or plane-layer signals in this discriminator.
 b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
