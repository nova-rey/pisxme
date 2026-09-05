"""Disposable open-shelf clock integration candidate on the V5 ancestor."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb'; OUT=R/'PHASE24_OPEN_SHELF_CLOCK.kicad_pcb'
NAMES={'/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC'}
MAP={'Y1':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC','3':'/STORAGE/BRIDGE_XO','4':'/STORAGE/BRIDGE_VSSOSC'},'R23':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_XO'},'C42':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC'},'C43':{'1':'/STORAGE/BRIDGE_XO','2':'/STORAGE/BRIDGE_VSSOSC'}}
LIB={'Y1':'Crystal_3225_4Pad','R23':'R_0402_1005Metric','C42':'C_0402_1005Metric','C43':'C_0402_1005Metric'}
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def P(f,n): return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def main():
 b=pcbnew.LoadBoard(str(BASE)); io=pcbnew.PCB_IO_KICAD_SEXPR(); nets={}
 for name in sorted(NAMES):
  n=b.FindNet(name)
  if n is None: n=pcbnew.NETINFO_ITEM(b,name); n.SetNetCode(b.GetNetCount()+1); b.Add(n)
  nets[name]=n
 for t in list(b.GetTracks()):
  if t.GetNetname() in NAMES: b.RemoveNative(t)
 u=b.FindFootprintByReference('U7'); u.SetOrientationDegrees(180)
 for num,name in {'52':'/STORAGE/BRIDGE_XI','53':'/STORAGE/BRIDGE_VSSOSC','54':'/STORAGE/BRIDGE_XO'}.items(): P(u,num).SetNet(nets[name]); P(u,num).SetNetCode(nets[name].GetNetCode())
 fs={}
 for ref,pos in {'Y1':(210,140),'R23':(210,153),'C42':(204,153),'C43':(216,153)}.items():
  f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),LIB[ref]); f.SetReference(ref); f.SetPosition(V(*pos)); b.Add(f); fs[ref]=f
  for p in f.Pads(): p.SetNet(nets[MAP[ref][str(p.GetNumber())]]); p.SetNetCode(nets[MAP[ref][str(p.GetNumber())]].GetNetCode()); p.SetLayer(pcbnew.B_Cu)
 def S(name,a,z,l=pcbnew.F_Cu,w=.1321):
  t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(nets[name]); b.Add(t)
 def X(name,p):
  v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(nets[name]); b.Add(v)
 # Derive the rot180 clock endpoints from the serialized footprint rather
 # than relying on historical absolute coordinates. Escape below the J3
 # body before going outboard.
 XI,VS,XO=('/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_VSSOSC','/STORAGE/BRIDGE_XO')
 xi0,vs0,xo0=(xy(P(u,n)) for n in ('52','53','54'))
 # Use the proven asymmetric rot180 escape before entering three separated
 # shelf lanes. All endpoints are derived from the serialized U7/Y1 pads.
 S(XI,xi0,(123.5,134.5)); S(XI,(123.5,134.5),(126.5,134.5)); X(XI,(126.5,134.5)); S(XI,(126.5,134.5),(126.5,145),pcbnew.B_Cu); S(XI,(126.5,145),(210,145),pcbnew.B_Cu); S(XI,(210,145),(210,138.9),pcbnew.B_Cu); S(XI,(210,138.9),xy(P(fs['Y1'],'1')),pcbnew.B_Cu)
 S(VS,vs0,(vs0[0],133)); X(VS,(vs0[0],133)); S(VS,(vs0[0],133),(122.5,147),pcbnew.B_Cu); S(VS,(122.5,147),(209,147),pcbnew.B_Cu); S(VS,(209,147),(209,138.9),pcbnew.B_Cu); S(VS,(209,138.9),xy(P(fs['Y1'],'2')),pcbnew.B_Cu)
 S(XO,xo0,(121,134)); S(XO,(121,134),(113,134)); X(XO,(113,134)); S(XO,(113,134),(113,149),pcbnew.B_Cu); S(XO,(113,149),(208,149),pcbnew.B_Cu); S(XO,(208,149),(208,141.1),pcbnew.B_Cu); S(XO,(208,141.1),xy(P(fs['Y1'],'3')),pcbnew.B_Cu)
 # Source-to-Y1 discriminator ends here; passive fanout is reintroduced only
 # after this launch has passed native DRC.
 b.Save(str(OUT)); print(OUT); return
 # Common VSSOSC exits the crystal on the opposite side and returns to C42/C43.
 S(VS,xy(P(fs['Y1'],'2')),(207,140),pcbnew.B_Cu); X(VS,(207,140)); S(VS,(207,140),xy(P(fs['Y1'],'4')),pcbnew.F_Cu)
 # Local passive fanout uses distinct B.Cu lanes and offset vias at SMD pads.
 for ref,num,p in [('R23','1',(209.5,153)),('C42','1',(203.5,153)),('R23','2',(210.5,153)),('C43','1',(215.5,153))]:
  name=MAP[ref][num]; q=xy(P(fs[ref],num)); X(name,p); S(name,q,p,pcbnew.F_Cu)
 S(XI,(210,145),(209.5,153),pcbnew.B_Cu); S(XI,(210,145),(203.5,153),pcbnew.B_Cu)
 S(XO,(208,149),(210.5,153),pcbnew.B_Cu); S(XO,(208,149),(215.5,153),pcbnew.B_Cu)
 # Ground-side oscillator returns use explicit offset vias.
 for ref,num,p in [('C42','2',(204.5,153)),('C43','2',(216.5,153))]:
  X(VS,p); S(VS,xy(P(fs[ref],num)),p,pcbnew.F_Cu)
 S(VS,(207,140),(204.5,153),pcbnew.B_Cu); S(VS,(207,140),(216.5,153),pcbnew.B_Cu)
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
