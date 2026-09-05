"""Clock integration trial on the rotation-aware SATA ancestor."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE19_COORDINATED_U7ROT270_SATAFIX.kicad_pcb'; OUT=R/'PHASE19_COORDINATED_U7ROT270_SATAFIX_CLOCK_WEST.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def T(b,n,a,z,l=pcbnew.F_Cu):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); b.Add(t)
def X(b,n,p):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(BASE)); names=('/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC','/STORAGE/BRIDGE_3V3'); nets={n:b.FindNet(n) for n in names}
 for n in names:
  if nets[n] is None: nets[n]=pcbnew.NETINFO_ITEM(b,n); nets[n].SetNetCode(b.GetNetCount()+1); b.Add(nets[n])
 u=b.FindFootprintByReference('U7'); codes={n.GetNetCode() for n in nets.values()}
 for t in list(b.GetTracks()):
  if t.GetNetCode() in codes: b.Remove(t)
 io=pcbnew.PCB_IO_KICAD_SEXPR()
 for ref,lib in [('Y1','Crystal_3225_4Pad'),('R23','R_0402_1005Metric'),('C42','C_0402_1005Metric'),('C43','C_0402_1005Metric')]:
  if b.FindFootprintByReference(ref) is None:
   f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),lib); f.SetReference(ref); b.Add(f)
 pos={'Y1':(105,145),'R23':(105,155),'C42':(99,155),'C43':(111,155)}
 mp={'Y1':{'1':names[0],'2':names[2],'3':names[1],'4':names[2]},'R23':{'1':names[0],'2':names[1]},'C42':{'1':names[0],'2':names[2]},'C43':{'1':names[1],'2':names[2]}}
 for ref,p in pos.items():
  f=b.FindFootprintByReference(ref); f.SetPosition(V(*p)); f.SetOrientationDegrees(0)
  for q in f.Pads(): q.SetNet(nets[mp[ref][str(q.GetNumber())]]); q.SetNetCode(nets[mp[ref][str(q.GetNumber())]].GetNetCode())
 for pin,n in [('52',names[0]),('53',names[2]),('54',names[1]),('30',names[3]),('31',names[3])]:
  q=next(q for q in u.Pads() if str(q.GetNumber())==pin); q.SetNet(nets[n]); q.SetNetCode(nets[n].GetNetCode())
 xi,xo,vs,v33=(nets[n] for n in names)
 # U7 rot270 exact row: XI 135.5,127; VSSOSC 135.5,127.5; XO 135.5,128.
 T(b,xi,(135.5,127),(130,127)); T(b,xi,(130,127),(130,140)); T(b,xi,(130,140),(103.9,144.15))
 T(b,xo,(135.5,128),(129,128)); T(b,xo,(129,128),(129,146)); T(b,xo,(129,146),(106.1,145.85))
 T(b,vs,(135.5,127.5),(128,127.5)); T(b,vs,(128,127.5),(128,165)); T(b,vs,(128,165),(103.9,145.85))
 # Short local branches are kept on their own side of the crystal body.
 T(b,xi,(103.9,144.15),(104.5,155)); T(b,xi,(103.9,144.15),(98.5,155)); T(b,xi,(103.9,144.15),(104.5,155))
 T(b,xo,(106.1,145.85),(105.5,155)); T(b,xo,(106.1,145.85),(111.5,155)); T(b,vs,(103.9,145.85),(106.1,144.15)); T(b,vs,(103.9,145.85),(99.5,155)); T(b,vs,(103.9,145.85),(112.5,155))
 T(b,v33,(137.5,123),(137.5,120)); T(b,v33,(137.5,120),(140,120)); T(b,v33,(140,120),(140,123))
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
