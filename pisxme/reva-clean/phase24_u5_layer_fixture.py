"""Disposable U5/C44-C47 layer-owned source/return topology fixture."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb';OUT=R/'PHASE24_U5_LAYER_FIXTURE.kicad_pcb'
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def P(f,n):return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def T(b,n,a,z,l):
 if a!=z:
  t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.2));t.SetNet(n);b.Add(t)
def X(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*q));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(BASE));io=pcbnew.PCB_IO_KICAD_SEXPR();u=b.FindFootprintByReference('U5');r=b.FindFootprintByReference('R20')
 for t in list(b.GetTracks()):b.RemoveNative(t)
 for z in list(b.Zones()):b.RemoveNative(z)
 rail=b.FindNet('/REGULATORS/BRIDGE_1V1');gnd=b.FindNet('POWER_GND');fs={}
 for ref,pos in {'C44':(250,128),'C45':(258,128),'C46':(250,138),'C47':(258,138)}.items():
  f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),'C_1210_3225Metric');f.SetReference(ref);f.SetPosition(V(*pos));f.SetOrientationDegrees(90);b.Add(f);fs[ref]=f
  P(f,'1').SetNet(rail);P(f,'1').SetNetCode(rail.GetNetCode());P(f,'2').SetNet(gnd);P(f,'2').SetNetCode(gnd.GetNetCode())
 p9=P(u,'9');p2=P(r,'2');p9.SetNet(rail);p9.SetNetCode(rail.GetNetCode());p2.SetNet(gnd);p2.SetNetCode(gnd.GetNetCode())
 X(b,rail,(239,110));T(b,rail,xy(p9),(239,110),pcbnew.F_Cu);T(b,rail,(239,110),(264,110),pcbnew.B_Cu);T(b,rail,(264,110),(264,136.65),pcbnew.B_Cu)
 X(b,gnd,(247,114));T(b,gnd,xy(p2),(247,114),pcbnew.F_Cu);T(b,gnd,(247,114),(244,114),pcbnew.B_Cu);T(b,gnd,(244,114),(244,139.35),pcbnew.B_Cu)
 for f in fs.values():
  p1,p2=xy(P(f,'1')),xy(P(f,'2'));T(b,rail,(264,p1[1]),p1,pcbnew.B_Cu);T(b,gnd,(244,p2[1]),p2,pcbnew.B_Cu)
 b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
