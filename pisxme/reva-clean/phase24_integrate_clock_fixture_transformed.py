"""Try the proven clock fixture topology in the U7=120,140 rotated frame."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb'; ORACLE=R/'PHASE24_CLOCK_COORDINATED_LAYERS.kicad_pcb'; OUT=R/'PHASE24_U5_CLOCK_FIXTURE_TRANSFORMED.kicad_pcb'
NAMES={'/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC'}
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(p): return (220-pcbnew.ToMM(p.x),240-pcbnew.ToMM(p.y))
def main():
 b=pcbnew.LoadBoard(str(BASE));o=pcbnew.LoadBoard(str(ORACLE)); nets={n:b.FindNet(n) for n in NAMES}
 for n in nets.values():
  if n is None: raise RuntimeError('missing clock net')
 pos={'Y1':(120,125),'R23':(120,115),'C42':(126,115),'C43':(114,115)}
 for ref,(x,y) in pos.items():
  f=b.FindFootprintByReference(ref); f.SetPosition(V(x,y)); f.SetOrientationDegrees(180)
  # The transformed fixture and existing authoritative footprints share pad maps.
  for p in f.Pads():
   n=nets[{'Y1':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC','3':'/STORAGE/BRIDGE_XO','4':'/STORAGE/BRIDGE_VSSOSC'},'R23':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_XO'},'C42':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC'},'C43':{'1':'/STORAGE/BRIDGE_XO','2':'/STORAGE/BRIDGE_VSSOSC'}}[ref][str(p.GetNumber())]];p.SetNet(n);p.SetNetCode(n.GetNetCode())
 u=b.FindFootprintByReference('U7');
 for num,name in [('52','/STORAGE/BRIDGE_XI'),('53','/STORAGE/BRIDGE_VSSOSC'),('54','/STORAGE/BRIDGE_XO')]:
  p=next(p for p in u.Pads() if str(p.GetNumber())==num);n=nets[name];p.SetNet(n);p.SetNetCode(n.GetNetCode())
 for item in o.GetTracks():
  if item.GetNetname() not in NAMES: continue
  n=nets[item.GetNetname()]
  if isinstance(item,pcbnew.PCB_VIA):
   v=pcbnew.PCB_VIA(b);v.SetPosition(V(*tr(item.GetPosition())));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(item.GetDrill());v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);b.Add(v)
  else:
   t=pcbnew.PCB_TRACK(b);t.SetStart(V(*tr(item.GetStart())));t.SetEnd(V(*tr(item.GetEnd())));t.SetLayer(item.GetLayer());t.SetWidth(item.GetWidth());t.SetNet(n);b.Add(t)
 pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
