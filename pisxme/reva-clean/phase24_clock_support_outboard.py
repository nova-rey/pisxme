"""Outboard/underside support-island discriminator for Phase 24."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_CLOCK_ASTAR_NEARWEST.kicad_pcb'; OUT=R/'PHASE24_CLOCK_SUPPORT_OUTBOARD.kicad_pcb'
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def P(f,n):return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def T(b,n,a,z):
 if a!=z:
  t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(pcbnew.B_Cu);t.SetWidth(pcbnew.FromMM(.1321));t.SetNet(n);b.Add(t)
def route(b,n,pts):
 for a,z in zip(pts,pts[1:]):T(b,n,a,z)
def main():
 b=pcbnew.LoadBoard(str(BASE));io=pcbnew.PCB_IO_KICAD_SEXPR();u=b.FindFootprintByReference('U7');y=b.FindFootprintByReference('Y1')
 ns={k:b.FindNet('/STORAGE/BRIDGE_'+v) for k,v in {'XI':'XI','XO':'XO','VS':'VSSOSC'}.items()}
 parts={}
 for ref,lib,pos in [('R23','R_0402_1005Metric',(90,155)),('C42','C_0402_1005Metric',(84,155)),('C43','C_0402_1005Metric',(96,155))]:
  f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),lib);f.SetReference(ref);f.SetPosition(V(*pos));b.Add(f);parts[ref]=f
 maps={'R23':{'1':'XI','2':'XO'},'C42':{'1':'XI','2':'VS'},'C43':{'1':'XO','2':'VS'}}
 for ref,f in parts.items():
  for p in f.Pads():
   n=ns[maps[ref][str(p.GetNumber())]];p.SetNet(n);p.SetNetCode(n.GetNetCode());ls=pcbnew.LSET();ls.AddLayer(pcbnew.B_Cu);p.SetLayerSet(ls)
 yp={str(p.GetNumber()):xy(p) for p in y.Pads()};rp={str(p.GetNumber()):xy(p) for p in parts['R23'].Pads()};cp={r:{str(p.GetNumber()):xy(p) for p in parts[r].Pads()} for r in ('C42','C43')}
 # Four isolated B.Cu lanes approach the already serialized Y1 pads from
 # the west/south acreage; this deliberately avoids the F.Cu USB3 fanout.
 route(b,ns['XI'],[rp['1'],(90,150),(102,150),(102,132),yp['1']]);route(b,ns['XI'],[cp['C42']['1'],(84,150),(102,150)])
 route(b,ns['XO'],[rp['2'],(90,148),(112,148),(112,132),yp['3']]);route(b,ns['XO'],[cp['C43']['1'],(96,148),(112,148)])
 route(b,ns['VS'],[cp['C42']['2'],(84,162),(80,162),(80,125),yp['2']]);route(b,ns['VS'],[cp['C43']['2'],(96,162),(100,162),(100,125),yp['4']])
 b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
