"""Disposable U5-local materialization of schematic-authoritative C44-C47."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb'
OUT=R/'PHASE24_U5_CAPS_ISLAND.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def pad(f,n): return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def net(b,name):
 n=b.FindNet(name)
 if n is None:
  n=pcbnew.NETINFO_ITEM(b,name); n.SetNetCode(b.GetNetCount()+1); b.Add(n)
 return n
def track(b,n,a,z,l=pcbnew.B_Cu,w=.2):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); b.Add(t)
def via(b,n,p):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(BASE)); io=pcbnew.PCB_IO_KICAD_SEXPR(); rail=net(b,'/REGULATORS/BRIDGE_1V1'); gnd=net(b,'POWER_GND'); u5=b.FindFootprintByReference('U5')
 # This candidate regenerates the affected bridge-1V1 corridor, so remove
 # only the old rail copper before authoring the new route.
 for t in list(b.GetTracks()):
  if t.GetNetCode()==rail.GetNetCode(): b.RemoveNative(t)
 positions={'C44':(250,130),'C45':(256,130),'C46':(250,136),'C47':(256,136)}; fs={}
 for ref,pos in positions.items():
  f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),'C_1210_3225Metric'); f.SetReference(ref); f.SetPosition(V(*pos)); f.SetLayer(pcbnew.B_Cu); b.Add(f); fs[ref]=f
  pad(f,'1').SetNet(rail); pad(f,'1').SetNetCode(rail.GetNetCode()); pad(f,'2').SetNet(gnd); pad(f,'2').SetNetCode(gnd.GetNetCode())
 # Use U5 pad 9 as the shortest bridge-1V1 source; fan out on B.Cu.
 source=(237.25,107.0); via(b,rail,(239,120)); track(b,rail,source,(239,120),pcbnew.F_Cu)
 rail_targets=[]
 for ref,f in fs.items():
  p1=xy(pad(f,'1')); q=(p1[0],p1[1]-1.0); via(b,rail,q); track(b,rail,p1,q,pcbnew.F_Cu); rail_targets.append((ref,q))
 for ref,q in rail_targets:
  track(b,rail,(239,120),q,pcbnew.B_Cu)
 # Each capacitor gets an offset GND via; the existing In4 POWER_GND zone
 # supplies the common return after refill.
 for f in fs.values():
  p2=xy(pad(f,'2')); q=(p2[0]+.8,p2[1]+.8); via(b,gnd,q); track(b,gnd,p2,q,pcbnew.F_Cu)
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
