"""Disposable rot180 U7 clock source-escape discriminator."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb'; OUT=R/'PHASE24_ROT180_SOURCE_ESCAPE.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def main():
 b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U7'); u.SetOrientationDegrees(180)
 names={'52':'/STORAGE/BRIDGE_XI','53':'/STORAGE/BRIDGE_VSSOSC','54':'/STORAGE/BRIDGE_XO'}; ns={}
 for name in names.values():
  n=b.FindNet(name)
  if n is None: n=pcbnew.NETINFO_ITEM(b,name); n.SetNetCode(b.GetNetCount()+1); b.Add(n)
  ns[name]=n
 for t in list(b.GetTracks()): b.RemoveNative(t)
 for num,name in names.items():
  p=next(p for p in u.Pads() if str(p.GetNumber())==num); p.SetNet(ns[name]); p.SetNetCode(ns[name].GetNetCode())
 def S(name,a,z,l=pcbnew.F_Cu):
  t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.1321)); t.SetNet(ns[name]); b.Add(t)
 def X(name,p):
  v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(ns[name]); b.Add(v)
 pads={n:(pcbnew.ToMM(next(p for p in u.Pads() if str(p.GetNumber())==n).GetPosition().x),pcbnew.ToMM(next(p for p in u.Pads() if str(p.GetNumber())==n).GetPosition().y)) for n in names}
 # Escape perpendicular/away from the actual top-edge row, with separated
 # exits: XI right, VSSOSC upward, XO left.
 XI,VS,XO=(names[x] for x in ('52','53','54'))
 S(XI,pads['52'],(123.5,134.5)); S(XI,(123.5,134.5),(126.5,134.5)); X(XI,(126.5,134.5)); S(XI,(126.5,134.5),(126.5,150),pcbnew.B_Cu)
 S(VS,pads['53'],(pads['53'][0],133)); X(VS,(pads['53'][0],133)); S(VS,(pads['53'][0],133),(122.5,150),pcbnew.B_Cu)
 S(XO,pads['54'],(121,134)); S(XO,(121,134),(113,134)); X(XO,(113,134)); S(XO,(113,134),(113,150),pcbnew.B_Cu)
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
