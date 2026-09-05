"""Transplant the proven rotated-U7 clock copper onto the Phase24 candidate."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb'
ORACLE=R/'PHASE19_PASS_CLOCK_ROT180_S20.kicad_pcb'
OUT=R/'PHASE24_U5_CLOCK_INTEGRATED.kicad_pcb'
NAMES={'/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC'}
POS={'Y1':(140,125,180),'R23':(140,115,180),'C42':(146,115,180),'C43':(134,115,180)}
NETS={'Y1':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC','3':'/STORAGE/BRIDGE_XO','4':'/STORAGE/BRIDGE_VSSOSC'},
      'R23':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_XO'},
      'C42':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC'},
      'C43':{'1':'/STORAGE/BRIDGE_XO','2':'/STORAGE/BRIDGE_VSSOSC'}}
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def main():
 b=pcbnew.LoadBoard(str(BASE)); o=pcbnew.LoadBoard(str(ORACLE))
 nets={n:b.FindNet(n) for n in NAMES}
 if any(v is None for v in nets.values()): raise RuntimeError('clock net missing from integrated board')
 # The refs already exist in the authoritative candidate; move them as a block.
 for ref,(x,y,rot) in POS.items():
  f=b.FindFootprintByReference(ref)
  if f is None: raise RuntimeError(f'missing {ref}')
  f.SetPosition(V(x,y)); f.SetOrientationDegrees(rot)
  for p in f.Pads():
   n=nets[NETS[ref][str(p.GetNumber())]]; p.SetNet(n); p.SetNetCode(n.GetNetCode())
 u=b.FindFootprintByReference('U7')
 for num,name in [('52','/STORAGE/BRIDGE_XI'),('53','/STORAGE/BRIDGE_VSSOSC'),('54','/STORAGE/BRIDGE_XO')]:
  p=next(p for p in u.Pads() if str(p.GetNumber())==num); n=nets[name]; p.SetNet(n); p.SetNetCode(n.GetNetCode())
 # Copy only oracle copper belonging to the clock nets; its U7 and support
 # coordinates are already the same rotated-U7 coordinate frame.
 for item in o.GetTracks():
  if item.GetNetname() not in NAMES: continue
  n=nets[item.GetNetname()]
  if isinstance(item,pcbnew.PCB_VIA):
   v=pcbnew.PCB_VIA(b); v.SetPosition(item.GetPosition()); v.SetWidth(pcbnew.FromMM(0.5)); v.SetDrill(item.GetDrill()); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
  else:
   t=pcbnew.PCB_TRACK(b); t.SetStart(item.GetStart()); t.SetEnd(item.GetEnd()); t.SetLayer(item.GetLayer()); t.SetWidth(item.GetWidth()); t.SetNet(n); b.Add(t)
 pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
