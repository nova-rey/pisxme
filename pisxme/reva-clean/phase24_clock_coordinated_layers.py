"""Disposable complete clock graph with layer-owned branch corridors."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent; BASE=R/'PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb'; OUT=R/'PHASE24_CLOCK_COORDINATED_LAYERS.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def P(f,n): return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def N(b,name):
 n=b.FindNet(name)
 if n is None: n=pcbnew.NETINFO_ITEM(b,name); n.SetNetCode(b.GetNetCount()+1); b.Add(n)
 return n
def pad(p,n,l):
 p.SetNet(n); p.SetNetCode(n.GetNetCode()); s=pcbnew.LSET(); s.AddLayer(l); p.SetLayerSet(s)
def T(b,n,a,z,l):
 if a==z: return
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); b.Add(t)
def path(b,n,pts,l):
 for a,z in zip(pts,pts[1:]): T(b,n,a,z,l)
def X(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(*q)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
MAP={'Y1':{'1':'XI','2':'VS','3':'XO','4':'VS'},'R23':{'1':'XI','2':'XO'},'C42':{'1':'XI','2':'VS'},'C43':{'1':'XO','2':'VS'}}
NET={'XI':'/STORAGE/BRIDGE_XI','XO':'/STORAGE/BRIDGE_XO','VS':'/STORAGE/BRIDGE_VSSOSC'}
LIB={'Y1':'Crystal_3225_4Pad','R23':'R_0402_1005Metric','C42':'C_0402_1005Metric','C43':'C_0402_1005Metric'}
def main():
 b=pcbnew.LoadBoard(str(BASE)); tracks=list(b.GetTracks()); zones=list(b.Zones()); fs=list(b.GetFootprints())
 for t in tracks: b.Remove(t)
 for z in zones: b.Remove(z)
 for f in fs:
  if f.GetReference()!='U7': b.Remove(f)
 u=b.FindFootprintByReference('U7'); u.SetPosition(V(100,100)); u.SetOrientationDegrees(0)
 ns={k:N(b,v) for k,v in NET.items()}; io=pcbnew.PCB_IO_KICAD_SEXPR(); parts={}
 for ref,pos in {'Y1':(100,115),'R23':(100,125),'C42':(94,125),'C43':(106,125)}.items():
  f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),LIB[ref]); f.SetReference(ref); f.SetPosition(V(*pos)); b.Add(f); parts[ref]=f
  for p in f.Pads(): pad(p,ns[MAP[ref][str(p.GetNumber())]],pcbnew.F_Cu if MAP[ref][str(p.GetNumber())]=='XO' else pcbnew.B_Cu)
 src={'XI':P(u,'52'),'VS':P(u,'53'),'XO':P(u,'54')}
 for k,p in src.items(): pad(p,ns[k],pcbnew.F_Cu)
 y={str(p.GetNumber()):xy(p) for p in parts['Y1'].Pads()}; r={str(p.GetNumber()):xy(p) for p in parts['R23'].Pads()}; c2={ref:{str(p.GetNumber()):xy(p) for p in parts[ref].Pads()} for ref in ('C42','C43')}
 # Separate source escapes; all ordinary vias are outside pads.
 path(b,ns['XI'],[xy(src['XI']),(97,108),(94,108)],pcbnew.F_Cu); X(b,ns['XI'],(94,108))
 path(b,ns['VS'],[xy(src['VS']),(97.5,109),(90,110)],pcbnew.F_Cu); X(b,ns['VS'],(90,110))
 path(b,ns['XO'],[xy(src['XO']),(98,109),(105,110)],pcbnew.F_Cu)
 # XI B.Cu upper-left bus and XO F.Cu right bus.
 path(b,ns['XI'],[(94,108),(94,112),(y['1'][0],112),y['1']],pcbnew.B_Cu)
 T(b,ns['XI'],(94,112),(94,122),pcbnew.B_Cu)
 path(b,ns['XO'],[(105,110),(105,125),(y['3'][0],125),y['3']],pcbnew.F_Cu)
 # VSSOSC B.Cu lower perimeter, with pad 2 and pad 4 approached on opposite sides.
 path(b,ns['VS'],[(90,110),(90,132),(103,132),(103,118),(y['2'][0],118),y['2']],pcbnew.B_Cu)
 path(b,ns['VS'],[y['2'],(97,115.85),(97,117.5),(103,117.5),(103,114.15),y['4']],pcbnew.B_Cu)
 # Passive branches terminate on their layer-owned buses.
 path(b,ns['XI'],[r['1'],(r['1'][0],122),(94,122)],pcbnew.B_Cu); path(b,ns['XI'],[c2['C42']['1'],(c2['C42']['1'][0],122),(94,122)],pcbnew.B_Cu)
 path(b,ns['XO'],[r['2'],(105,r['2'][1]),(105,125)],pcbnew.F_Cu); path(b,ns['XO'],[c2['C43']['1'],(105,c2['C43']['1'][1]),(105,125)],pcbnew.F_Cu)
 path(b,ns['VS'],[c2['C42']['2'],(c2['C42']['2'][0],135),(90,135),(90,132)],pcbnew.B_Cu); path(b,ns['VS'],[c2['C43']['2'],(c2['C43']['2'][0],135),(90,135),(90,132)],pcbnew.B_Cu)
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
