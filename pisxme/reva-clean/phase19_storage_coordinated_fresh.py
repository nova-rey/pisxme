"""Fresh coordinated storage island: exact CM5 escape, moved U7/J3, USB3+SATA."""
from pathlib import Path
import os
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb'; OUT=R/(os.environ.get('P19_OUT','ACREAGE_PHASE19_STORAGE_COORDINATED_FRESH.kicad_pcb')); W=pcbnew.FromMM(.13208)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def P(f,n): return next(p for p in list(f.Pads()) if str(p.GetNumber())==str(n))
def T(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);b.Add(t)
def X(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(V(*p));q.SetWidth(pcbnew.FromMM(.5));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);q.SetNet(n);b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U7');j=b.FindFootprintByReference('J3');src=b.FindFootprintByReference('J7')
 u.SetPosition(V(float(os.environ.get('P19_U7_X','120')),float(os.environ.get('P19_U7_Y','140'))));u.SetOrientationDegrees(int(os.environ.get('P19_U7_ROT','180')));j.SetPosition(V(float(os.environ.get('P19_J3_X','145')),float(os.environ.get('P19_J3_Y','125'))));j.SetOrientationDegrees(int(os.environ.get('P19_J3_ROT','90')))
 sp={str(p.GetNumber()):xy(p) for p in list(src.Pads())};up={str(p.GetNumber()):xy(p) for p in list(u.Pads())};jp={str(p.GetNumber()):xy(p) for p in list(j.Pads())};upad={str(p.GetNumber()):p for p in list(u.Pads())};jpad={str(p.GetNumber()):p for p in list(j.Pads())}
 for t in list(b.GetTracks()):
  if 'USB3' in t.GetNetname(): b.Remove(t)
 # Exact Phase 18 CM5 dogbones and B.Cu escapes to x=103/82, then new U7 landings.
 for name,spn,upn,first,second in (('CM5_USB3_RX_N','128','42',(72,103.9),(103,103)),('CM5_USB3_RX_P','130','43',(72,104.8),(103,105)),('CM5_USB3_TX_N','140','45',(72,108),(103,107))):
  n=b.FindNet('/CORE_CM5/'+name);s=sp[spn];d=up[upn];launch=(71.2,s[1]);T(b,n,s,launch,pcbnew.F_Cu);T(b,n,launch,first,pcbnew.F_Cu);X(b,n,first)
  # Preserve the validated source-side escapes, then use ordered horizontal
  # B.Cu lanes to a common landing rail. This is placement-independent and
  # avoids the old candidate's hard-coded downward detour.
  if name == 'CM5_USB3_TX_N':
   T(b,n,first,(75,first[1]),pcbnew.B_Cu);X(b,n,(75,first[1]));T(b,n,(75,first[1]),second,pcbnew.B_Cu);X(b,n,second)
  else:
   T(b,n,first,(80,first[1]),pcbnew.B_Cu);T(b,n,(80,first[1]),(102,first[1]),pcbnew.B_Cu);T(b,n,(102,first[1]),second,pcbnew.B_Cu);X(b,n,second)
  rail=(125, second[1]); X(b,n,rail); T(b,n,second,rail,pcbnew.B_Cu); T(b,n,rail,d,pcbnew.F_Cu)
 n=b.FindNet('/CORE_CM5/CM5_USB3_TX_P');s=sp['142'];d=up['46'];T(b,n,s,(71.2,106.7),pcbnew.F_Cu);T(b,n,(71.2,106.7),(71,109),pcbnew.F_Cu);X(b,n,(71,109));T(b,n,(71,109),(82,112),pcbnew.B_Cu);X(b,n,(82,112));T(b,n,(82,112),(125,112),pcbnew.B_Cu);X(b,n,(125,112));T(b,n,(125,112),d,pcbnew.F_Cu)
 # SATA corridor is derived from the actual moved pad coordinates.  The two
 # pairs use separate permitted layers and monotonic lanes; vias are outside
 # both SMD pad fields and each M.2 launch returns to F.Cu before the pad.
 for name,un,jn,lane,layer in (('BRIDGE_SATA_TX_P','57','1',5,pcbnew.F_Cu),('BRIDGE_SATA_TX_N','56','2',7,pcbnew.B_Cu),('BRIDGE_SATA_RX_P','60','3',-3,pcbnew.F_Cu),('BRIDGE_SATA_RX_N','59','4',-5,pcbnew.B_Cu)):
  n=b.FindNet('/STORAGE/'+name);upad[un].SetNet(n);jpad[jn].SetNet(n)
  s=up[un];d=jp[jn]; x0,y0=s; x1,y1=d; turn=(x0+10,y0+lane); end=(x1-4,y1+lane)
  T(b,n,s,turn,pcbnew.F_Cu); X(b,n,turn); T(b,n,turn,end,layer); X(b,n,end); T(b,n,end,d,pcbnew.F_Cu)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
