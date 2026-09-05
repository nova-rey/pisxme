"""Add the complete coordinated clock-support island to the acreage clock oracle."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CLOCK_ASTAR_NEARWEST.kicad_pcb'
OUT=R/'PHASE24_CLOCK_SUPPORT_TRANSPLANT.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def pad(f,n): return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def T(b,n,a,z,l,w=.1321):
 if a==z:return
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); b.Add(t)
def path(b,n,pts,l):
 for a,z in zip(pts,pts[1:]): T(b,n,a,z,l)
def main():
 b=pcbnew.LoadBoard(str(BASE)); io=pcbnew.PCB_IO_KICAD_SEXPR()
 u=b.FindFootprintByReference('U7'); y=b.FindFootprintByReference('Y1')
 ns={k:b.FindNet('/STORAGE/BRIDGE_'+v) for k,v in {'XI':'XI','XO':'XO','VS':'VSSOSC'}.items()}
 parts={}
 # Keep the validated Y1/source oracle and place the support parts in a
 # coherent south island; all pad layers match their net-owned clock buses.
 for ref,lib,pos in [('R23','R_0402_1005Metric',(108,140)),('C42','C_0402_1005Metric',(102,140)),('C43','C_0402_1005Metric',(114,140))]:
  f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),lib); f.SetReference(ref); f.SetPosition(V(*pos)); b.Add(f); parts[ref]=f
 maps={'R23':{'1':'XI','2':'XO'},'C42':{'1':'XI','2':'VS'},'C43':{'1':'XO','2':'VS'}}
 for ref,f in parts.items():
  for p in f.Pads():
   n=ns[maps[ref][str(p.GetNumber())]]; p.SetNet(n); p.SetNetCode(n.GetNetCode()); ls=pcbnew.LSET(); ls.AddLayer(pcbnew.F_Cu if maps[ref][str(p.GetNumber())]=='XO' else pcbnew.B_Cu); p.SetLayerSet(ls)
 yp={str(p.GetNumber()):xy(p) for p in y.Pads()}; rp={str(p.GetNumber()):xy(p) for p in parts['R23'].Pads()}; c={r:{str(p.GetNumber()):xy(p) for p in parts[r].Pads()} for r in ('C42','C43')}
 # Layer-owned buses mirror the passing disposable graph.  They terminate
 # at serialized Y1 pads and do not enter the U7 pad field.
 path(b,ns['XI'],[rp['1'],(108,137),(103,137),(103,132),yp['1']],pcbnew.B_Cu)
 path(b,ns['XI'],[c['C42']['1'],(102,136),(103,136),(103,132)],pcbnew.B_Cu)
 path(b,ns['XO'],[rp['2'],(108,143),(115,143),(115,132),yp['3']],pcbnew.F_Cu)
 path(b,ns['XO'],[c['C43']['1'],(114,143),(115,143)],pcbnew.F_Cu)
 path(b,ns['VS'],[c['C42']['2'],(102,145),(100,145),(100,134),yp['2']],pcbnew.B_Cu)
 path(b,ns['VS'],[c['C43']['2'],(114,145),(116,145),(116,134),yp['4']],pcbnew.B_Cu)
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__':main()
