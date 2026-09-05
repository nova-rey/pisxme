"""Disposable outboard clock-island placement and native-pad route trial."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_U7_3V3_CURRENT_LOCAL.kicad_pcb'; OUT=R/'PHASE24_CLOCK_ISLAND_OUTBOARD.kicad_pcb'
V=lambda x,y:pcbnew.VECTOR2I_MM(float(x),float(y))
N={'XI':'/STORAGE/BRIDGE_XI','XO':'/STORAGE/BRIDGE_XO','VS':'/STORAGE/BRIDGE_VSSOSC'}
MAP={'Y1':{'1':'XI','2':'VS','3':'XO','4':'VS'},'R23':{'1':'XI','2':'XO'},'C42':{'1':'XI','2':'VS'},'C43':{'1':'XO','2':'VS'}}
def main():
 b=pcbnew.LoadBoard(str(BASE)); nets={k:b.FindNet(v) for k,v in N.items()}
 # Coherent outboard island, selected from open acreage above/right of U7.
 for ref,pos in {'Y1':(130,105),'R23':(130,112),'C42':(124,112),'C43':(136,112)}.items():
  f=b.FindFootprintByReference(ref); f.SetPosition(V(*pos)); f.SetOrientationDegrees(0)
  s=pcbnew.LSET(); s.AddLayer(pcbnew.F_Cu); s.AddLayer(pcbnew.F_Mask); s.AddLayer(pcbnew.F_Paste)
  for p in f.Pads():
   p.SetLayerSet(s); p.SetNet(nets[MAP[ref][str(p.GetNumber())]]); p.SetNetCode(nets[MAP[ref][str(p.GetNumber())]].GetNetCode())
 u=b.FindFootprintByReference('U7')
 for num,k in [('52','XI'),('53','VS'),('54','XO')]:
  p=next(p for p in u.Pads() if p.GetNumber()==num);p.SetNet(nets[k]);p.SetNetCode(nets[k].GetNetCode())
 def P(ref,num):
  f=b.FindFootprintByReference(ref);return next(p for p in f.Pads() if p.GetNumber()==num).GetPosition()
 def T(k,a,z):
  q=pcbnew.PCB_TRACK(b);q.SetLayer(pcbnew.F_Cu);q.SetNet(nets[k]);q.SetWidth(pcbnew.FromMM(.20));q.SetStart(a);q.SetEnd(z);b.Add(q)
 def xy(p):return p.x/1e6,p.y/1e6
 # Explicit separated F.Cu buses; each endpoint is queried after transforms.
 xi=P('U7','52'); xo=P('U7','54'); vs=P('U7','53')
 xic=P('C42','1'); xir=P('R23','1'); xiy=P('Y1','1')
 xoc=P('C43','1'); xor=P('R23','2'); xoy=P('Y1','3')
 vsc=P('C42','2'); vsy2=P('Y1','2'); vsy4=P('Y1','4'); vsc3=P('C43','2')
 # XI left lane, XO right lane, VSSOSC lower perimeter lane.
 T('XI',xi,V(123,112)); T('XI',V(123,112),xic); T('XI',xic,xir); T('XI',xir,V(129.5,108)); T('XI',V(129.5,108),xiy)
 T('XO',xo,V(122,110)); T('XO',V(122,110),xor); T('XO',xor,xoc); T('XO',xor,V(131.1,110)); T('XO',V(131.1,110),xoy)
 T('VS',vs,V(122.5,116)); T('VS',V(122.5,116),V(136.5,116)); T('VS',V(124.5,116),vsc); T('VS',V(136.5,116),vsc3); T('VS',V(128.9,116),vsy2); T('VS',V(131.1,116),vsy4)
 pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
if __name__=='__main__':main()
