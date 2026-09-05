"""Integrate the reviewed U5 bulk-cap island with real pad-to-via launches."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_NO_LEGACY_CT_ALIASES.kicad_pcb';OUT=R/'PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb'
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def P(f,n):return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def T(b,n,a,z,l):
 if a!=z:
  t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.2));t.SetNet(n);b.Add(t)
def X(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*q));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(BASE));rail=b.FindNet('/REGULATORS/BRIDGE_1V1');gnd=b.FindNet('POWER_GND');u5=b.FindFootprintByReference('U5');r20=b.FindFootprintByReference('R20')
 caps={}
 for ref,pos in {'C44':(250,128),'C45':(258,128),'C46':(250,138),'C47':(258,138)}.items():
  f=b.FindFootprintByReference(ref)
  if f is None: raise RuntimeError(f'missing {ref} in integrated baseline')
  f.SetPosition(V(*pos));f.SetOrientationDegrees(90);caps[ref]=f
  for p,n in ((P(f,'1'),rail),(P(f,'2'),gnd)):p.SetNet(n);p.SetNetCode(n.GetNetCode())
 p9=P(u5,'9');p9.SetNet(rail);p9.SetNetCode(rail.GetNetCode());p2=P(r20,'2');p2.SetNet(gnd);p2.SetNetCode(gnd.GetNetCode())
 # Offset dogbones, all ordinary through-vias outside the 1210 pads.
 rail_v={'C44':(251.2,129.35),'C45':(259.2,129.35),'C46':(251.2,139.35),'C47':(259.2,139.35)}
 gnd_v={'C44':(248.8,126.65),'C45':(256.8,126.65),'C46':(248.8,136.65),'C47':(256.8,136.65)}
 X(b,rail,(239,110));T(b,rail,xy(p9),(239,110),pcbnew.F_Cu);T(b,rail,(239,110),(239,116),pcbnew.B_Cu);T(b,rail,(239,116),(264,116),pcbnew.B_Cu);T(b,rail,(264,116),(264,139.35),pcbnew.B_Cu)
 X(b,gnd,(247,114));T(b,gnd,xy(p2),(247,114),pcbnew.F_Cu);T(b,gnd,(247,114),(268,114),pcbnew.B_Cu);T(b,gnd,(268,114),(268,145),pcbnew.B_Cu);T(b,gnd,(268,145),(248.8,145),pcbnew.B_Cu);T(b,gnd,(248.8,145),(248.8,126.65),pcbnew.B_Cu);T(b,gnd,(248.8,126.65),(256.8,126.65),pcbnew.B_Cu);T(b,gnd,(248.8,145),(248.8,136.65),pcbnew.B_Cu);T(b,gnd,(248.8,136.65),(256.8,136.65),pcbnew.B_Cu)
 for ref,f in caps.items():
  a=xy(P(f,'1'));q=rail_v[ref];X(b,rail,q);T(b,rail,a,q,pcbnew.F_Cu);T(b,rail,(264,a[1]),q,pcbnew.B_Cu)
  a=xy(P(f,'2'));q=gnd_v[ref];X(b,gnd,q);T(b,gnd,a,q,pcbnew.F_Cu)
 pcbnew.ZONE_FILLER(b).Fill(b.Zones())
 b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
