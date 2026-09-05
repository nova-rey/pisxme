"""Add the authoritative TUSB9261 clock network to the rot270 storage trial."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'PHASE19_COORDINATED_U7ROT270_FULL.kicad_pcb'
OUT = R / 'PHASE19_COORDINATED_U7ROT270_CLOCK.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def T(b,n,a,z,l=pcbnew.F_Cu):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); b.Add(t)
def X(b,n,p):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 names=('/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC','/STORAGE/BRIDGE_3V3')
 nets={n:b.FindNet(n) for n in names}
 for name in names:
  if nets[name] is None:
   nets[name]=pcbnew.NETINFO_ITEM(b,name); nets[name].SetNetCode(b.GetNetCount()+1); b.Add(nets[name])
 u=b.FindFootprintByReference('U7')
 codes={n.GetNetCode() for n in nets.values()}
 for t in list(b.GetTracks()):
  if t.GetNetCode() in codes: b.Remove(t)
 io=pcbnew.PCB_IO_KICAD_SEXPR()
 for ref,lib in [('Y1','Crystal_3225_4Pad'),('R23','R_0402_1005Metric'),('C42','C_0402_1005Metric'),('C43','C_0402_1005Metric')]:
  if b.FindFootprintByReference(ref) is None:
   f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),lib); f.SetReference(ref); b.Add(f)
 positions={'Y1':(250,150),'R23':(270,149),'C42':(250,170),'C43':(270,170)}
 maps={'Y1':{'1':names[0],'2':names[2],'3':names[1],'4':names[2]},'R23':{'1':names[0],'2':names[1]},'C42':{'1':names[0],'2':names[2]},'C43':{'1':names[1],'2':names[2]}}
 for ref,pos in positions.items():
  f=b.FindFootprintByReference(ref); f.SetPosition(V(*pos)); f.SetOrientationDegrees(0)
  for p in f.Pads():
   n=nets[maps[ref][str(p.GetNumber())]]; p.SetNet(n); p.SetNetCode(n.GetNetCode())
 for pin,name in [('30',names[3]),('31',names[3]),('52',names[0]),('53',names[2]),('54',names[1])]:
  p=next(p for p in u.Pads() if str(p.GetNumber())==pin); p.SetNet(nets[name]); p.SetNetCode(nets[name].GetNetCode())
 xi,xo,vs,v33=(nets[n] for n in names)
 # Rot270 live pad row: XI=(135.5,127), VSSOSC=(135.5,127.5), XO=(135.5,128).
 # Escape west, perpendicular to the vertical row, before any layer change.
 T(b,xi,(135.5,127),(131,127)); T(b,xi,(131,127),(125,127)); X(b,xi,(125,127)); T(b,xi,(125,127),(210,127),pcbnew.B_Cu); T(b,xi,(210,127),(210,142),pcbnew.B_Cu)
 T(b,xo,(135.5,128),(131,128)); T(b,xo,(131,128),(123,128)); X(b,xo,(123,128)); T(b,xo,(123,128),(220,128),pcbnew.B_Cu); T(b,xo,(220,128),(220,145),pcbnew.B_Cu)
 T(b,vs,(135.5,127.5),(131,127.5)); T(b,vs,(131,127.5),(121,127.5)); X(b,vs,(121,127.5)); T(b,vs,(121,127.5),(230,127.5),pcbnew.B_Cu); T(b,vs,(230,127.5),(230,175),pcbnew.B_Cu)
 # Convert each support endpoint with an ordinary via; long nets stay on B.Cu.
 xi_v=[(247.5,147.5),(269.5,146.5),(247.5,168.0)]
 xo_v=[(253.5,152.5),(272.5,147.5),(272.5,168.0)]
 vs_v=[(247.5,153.5),(253.5,147.5),(252.5,172.5),(272.5,172.5)]
 for p in xi_v+xo_v+vs_v: X(b,xi if p in xi_v else xo if p in xo_v else vs,p)
 for p in xi_v: T(b,xi,(210,142),p,pcbnew.B_Cu)
 for p in xo_v: T(b,xo,(220,145),p,pcbnew.B_Cu)
 for p in vs_v: T(b,vs,(230,175),p,pcbnew.B_Cu)
 # Short F.Cu dogbones from the support vias to the exact SMD pads.
 pads={ref:{str(p.GetNumber()):(pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)) for p in b.FindFootprintByReference(ref).Pads()} for ref in positions}
 for n,p,q in [(xi,xi_v[0],pads['Y1']['1']),(xi,xi_v[1],pads['R23']['1']),(xi,xi_v[2],pads['C42']['1']), (xo,xo_v[0],pads['Y1']['3']),(xo,xo_v[1],pads['R23']['2']),(xo,xo_v[2],pads['C43']['1'])]: T(b,n,p,q)
 for p,q in [(vs_v[0],pads['Y1']['2']),(vs_v[1],pads['Y1']['4']),(vs_v[2],pads['C42']['2']),(vs_v[3],pads['C43']['2'])]: T(b,vs,p,q)
 # FREQSEL0/FREQSEL1 high in the authoritative 40 MHz mode.
 T(b,v33,(137.5,123),(137.5,120)); T(b,v33,(137.5,120),(140,120)); T(b,v33,(140,120),(140,123))
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
