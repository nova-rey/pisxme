"""Disposable mapped B.Cu clock-island trial on the coordinated storage PCB."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'ACREAGE_PHASE19_CLOCK_COORDINATED3.kicad_pcb'; OUT=R/'PHASE19_COORDINATED_CLOCK_MAPPED_BCU.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def T(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); b.Add(t)
def X(b,n,p):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def main():
 b=pcbnew.LoadBoard(str(BASE)); keep={'U7','Y1','R23','C42','C43'}
 nets={n:b.FindNet(n) for n in ('/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC','/STORAGE/BRIDGE_3V3')}
 codes={n.GetNetCode() for n in nets.values()}
 for t in list(b.GetTracks()):
  if t.GetNetCode() in codes: b.Remove(t)
 # Mapped B.Cu window: outside the U7 body and the live F.Cu SATA launches.
 for ref,p in {'Y1':(122,118),'R23':(122,124),'C42':(116,124),'C43':(128,124)}.items():
  f=b.FindFootprintByReference(ref); f.SetLayer(pcbnew.B_Cu); f.SetPosition(V(*p)); f.SetOrientationDegrees(0)
  mp={'Y1':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC','3':'/STORAGE/BRIDGE_XO','4':'/STORAGE/BRIDGE_VSSOSC'},'R23':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_XO'},'C42':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC'},'C43':{'1':'/STORAGE/BRIDGE_XO','2':'/STORAGE/BRIDGE_VSSOSC'}}[ref]
  for q in f.Pads():
   n=nets[mp[str(q.GetNumber())]]; q.SetNet(n); q.SetNetCode(n.GetNetCode())
 u=b.FindFootprintByReference('U7')
 for pin,name in (('30','/STORAGE/BRIDGE_3V3'),('31','/STORAGE/BRIDGE_3V3'),('52','/STORAGE/BRIDGE_XI'),('53','/STORAGE/BRIDGE_VSSOSC'),('54','/STORAGE/BRIDGE_XO')):
  q=next(q for q in u.Pads() if str(q.GetNumber())==pin); q.SetNet(nets[name]); q.SetNetCode(nets[name].GetNetCode())
 xi,xo,vs,v33=(nets[n] for n in ('/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC','/STORAGE/BRIDGE_3V3'))
 # U7 top row exact pads: XI=(143,105.5), VSSOSC=(142.5,105.5), XO=(142,105.5).
 # Perpendicular-first F.Cu escape and separated vias outside the pad field.
 T(b,xi,(143,105.5),(143,101),pcbnew.F_Cu); T(b,xi,(143,101),(145,99),pcbnew.F_Cu); X(b,xi,(145,99))
 T(b,vs,(142.5,105.5),(142.5,100),pcbnew.F_Cu); T(b,vs,(142.5,100),(142.5,98.5),pcbnew.F_Cu); X(b,vs,(142.5,98.5))
 T(b,xo,(142,105.5),(142,101),pcbnew.F_Cu); T(b,xo,(142,101),(140,99),pcbnew.F_Cu); X(b,xo,(140,99))
 # B.Cu pair-free corridors: XI west, XO east, VSSOSC on a lower return bus.
 T(b,xi,(145,99),(145,116),pcbnew.B_Cu); T(b,xi,(145,116),(120.9,117.15),pcbnew.B_Cu)
 T(b,xi,(120.9,117.15),(121.5,124),pcbnew.B_Cu); T(b,xi,(120.9,117.15),(115.5,124),pcbnew.B_Cu)
 T(b,xo,(140,99),(140,115),pcbnew.B_Cu); T(b,xo,(140,115),(123.1,118.85),pcbnew.B_Cu)
 T(b,xo,(123.1,118.85),(122.5,124),pcbnew.B_Cu); T(b,xo,(123.1,118.85),(127.5,124),pcbnew.B_Cu)
 T(b,vs,(142.5,98.5),(142.5,130),pcbnew.B_Cu); T(b,vs,(114,130),(130,130),pcbnew.B_Cu)
 for p in ((120.9,120),(123.1,116),(116.5,124),(128.5,124)):
  T(b,vs,(p[0],130),p,pcbnew.B_Cu)
 # VSSOSC branches to Y1 pads 2/4 and the two capacitor return pads.
 f=b.FindFootprintByReference('Y1'); yp={str(q.GetNumber()):xy(q) for q in f.Pads()}
 T(b,vs,(120.9,120),yp['2'],pcbnew.B_Cu); T(b,vs,(123.1,116),yp['4'],pcbnew.B_Cu)
 f=b.FindFootprintByReference('C42'); cp={str(q.GetNumber()):xy(q) for q in f.Pads()}; T(b,vs,(116.5,124),cp['2'],pcbnew.B_Cu)
 f=b.FindFootprintByReference('C43'); cp={str(q.GetNumber()):xy(q) for q in f.Pads()}; T(b,vs,(128.5,124),cp['2'],pcbnew.B_Cu)
 # Both FREQSEL pins high; connect them around the adjacent top row.
 T(b,v33,(142.5,114.5),(142.5,117),pcbnew.F_Cu); T(b,v33,(142.5,117),(146,117),pcbnew.F_Cu); T(b,v33,(146,117),(146,114.5),pcbnew.F_Cu); T(b,v33,(146,114.5),(142,114.5),pcbnew.F_Cu)
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
