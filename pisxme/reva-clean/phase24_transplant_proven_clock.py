"""Transform the proven rot90 clock fixture into the V5 rot180 acreage."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent; BASE=R/'PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb'; ORACLE=R/'PHASE24_STORAGE_ROT90_PROBE.kicad_pcb'; OUT=R/'PHASE24_PROVEN_CLOCK_ROT180_ACREAGE.kicad_pcb'
NAMES={'/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC'}
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def T(p):
 x,y=p; return (120.0+(y-140.0),140.0-(x-120.0))
def main():
 b=pcbnew.LoadBoard(str(BASE)); o=pcbnew.LoadBoard(str(ORACLE)); io=pcbnew.PCB_IO_KICAD_SEXPR()
 nets={n:b.FindNet(n) for n in NAMES}
 for name,n in list(nets.items()):
  if n is None:
   n=pcbnew.NETINFO_ITEM(b,name); n.SetNetCode(b.GetNetCount()+1); b.Add(n); nets[name]=n
 for t in list(b.GetTracks()):
  if t.GetNetname() in NAMES: b.RemoveNative(t)
 u=b.FindFootprintByReference('U7'); u.SetOrientationDegrees(180)
 for num,name in {'52':'/STORAGE/BRIDGE_XI','53':'/STORAGE/BRIDGE_VSSOSC','54':'/STORAGE/BRIDGE_XO'}.items():
  p=next(p for p in u.Pads() if str(p.GetNumber())==num); p.SetNet(nets[name]); p.SetNetCode(nets[name].GetNetCode())
 libs={'Y1':'Crystal_3225_4Pad','R23':'R_0402_1005Metric','C42':'C_0402_1005Metric','C43':'C_0402_1005Metric'}
 maps={'Y1':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC','3':'/STORAGE/BRIDGE_XO','4':'/STORAGE/BRIDGE_VSSOSC'},'R23':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_XO'},'C42':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC'},'C43':{'1':'/STORAGE/BRIDGE_XO','2':'/STORAGE/BRIDGE_VSSOSC'}}
 for ref,lib in libs.items():
  src=o.FindFootprintByReference(ref); f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),lib); f.SetReference(ref); f.SetPosition(V(*T(xy(src)))); f.SetOrientationDegrees((src.GetOrientationDegrees()+90)%360); b.Add(f)
  for p in f.Pads(): p.SetNet(nets[maps[ref][str(p.GetNumber())]]); p.SetNetCode(nets[maps[ref][str(p.GetNumber())]].GetNetCode())
 for item in o.GetTracks():
  if item.GetNetname() not in NAMES: continue
  n=nets[item.GetNetname()]
  if isinstance(item,pcbnew.PCB_VIA):
   v=pcbnew.PCB_VIA(b); v.SetPosition(V(*T(xy(item)))); v.SetWidth(item.GetWidth()); v.SetDrill(item.GetDrill()); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
  else:
   t=pcbnew.PCB_TRACK(b); t.SetStart(V(*T((pcbnew.ToMM(item.GetStart().x),pcbnew.ToMM(item.GetStart().y))))); t.SetEnd(V(*T((pcbnew.ToMM(item.GetEnd().x),pcbnew.ToMM(item.GetEnd().y))))); t.SetLayer(item.GetLayer()); t.SetWidth(item.GetWidth()); t.SetNet(n); b.Add(t)
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
