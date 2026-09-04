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
 u.SetPosition(V(float(os.environ.get('P19_U7_X','140')),float(os.environ.get('P19_U7_Y','110'))));u.SetOrientationDegrees(int(os.environ.get('P19_U7_ROT','180')));j.SetPosition(V(float(os.environ.get('P19_J3_X','180')),float(os.environ.get('P19_J3_Y','95'))));j.SetOrientationDegrees(int(os.environ.get('P19_J3_ROT','90')))
 # KiCad 10 refreshes transformed pad coordinates on serialization. Reload
 # after the placement edit so every generated route uses the saved geometry,
 # not stale pre-move pad positions.
 sync=R/'.phase19_storage_sync.kicad_pcb'; b.Save(str(sync)); b=pcbnew.LoadBoard(str(sync));u=b.FindFootprintByReference('U7');j=b.FindFootprintByReference('J3');src=b.FindFootprintByReference('J7')
 sp={str(p.GetNumber()):xy(p) for p in list(src.Pads())};up={str(p.GetNumber()):xy(p) for p in list(u.Pads())};jp={str(p.GetNumber()):xy(p) for p in list(j.Pads())};upad={str(p.GetNumber()):p for p in list(u.Pads())};jpad={str(p.GetNumber()):p for p in list(j.Pads())}
 for t in list(b.GetTracks()):
  if 'USB3' in t.GetNetname(): b.Remove(t)
 # Exact Phase 18 CM5 escape geometry, extended monotonically to the moved
 # U7 row. U7 is deliberately placed at y=110 so the four source orderings
 # and the 0.5 mm USB pad pitch remain ordered at the landing.
 for name,spn,upn,first,second in (('CM5_USB3_RX_N','128','42',(72,103.9),(103,103)),('CM5_USB3_RX_P','130','43',(72,104.8),(103,105)),('CM5_USB3_TX_N','140','45',(72,108),(103,107))):
  n=b.FindNet('/CORE_CM5/'+name);s=sp[spn];d=up[upn];launch=(71.2,s[1]);T(b,n,s,launch,pcbnew.F_Cu);T(b,n,launch,first,pcbnew.F_Cu);X(b,n,first)
  if name == 'CM5_USB3_TX_N':
   T(b,n,first,(82,108),pcbnew.B_Cu);X(b,n,(82,108));T(b,n,(82,108),(102,108),pcbnew.B_Cu);T(b,n,(102,108),second,pcbnew.B_Cu);X(b,n,second)
  else:
   T(b,n,first,(103,first[1]),pcbnew.B_Cu);X(b,n,(103,first[1]));T(b,n,(103,first[1]),second,pcbnew.B_Cu);X(b,n,second)
  xrail={'CM5_USB3_RX_N':128,'CM5_USB3_RX_P':129,'CM5_USB3_TX_N':130}[name]; mid=(125,second[1]); rail=(xrail,second[1]); landing=(xrail,d[1]); T(b,n,second,mid,pcbnew.B_Cu); X(b,n,mid); T(b,n,mid,rail,pcbnew.F_Cu); X(b,n,rail); T(b,n,rail,landing,pcbnew.B_Cu); X(b,n,landing); T(b,n,landing,d,pcbnew.F_Cu)
 n=b.FindNet('/CORE_CM5/CM5_USB3_TX_P');s=sp['142'];d=up['46'];T(b,n,s,(71.2,106.7),pcbnew.F_Cu);T(b,n,(71.2,106.7),(71,109),pcbnew.F_Cu);X(b,n,(71,109));T(b,n,(71,109),(82,112),pcbnew.B_Cu);X(b,n,(82,112));T(b,n,(82,112),(125,112),pcbnew.B_Cu);X(b,n,(125,112));T(b,n,(125,112),(131,112),pcbnew.F_Cu);X(b,n,(131,112));T(b,n,(131,112),(131,d[1]),pcbnew.B_Cu);X(b,n,(131,d[1]));T(b,n,(131,d[1]),d,pcbnew.F_Cu)
 # SATA corridor is derived from the actual moved pad coordinates.  The two
 # pairs use separate permitted layers and monotonic lanes; vias are outside
 # both SMD pad fields and each M.2 launch returns to F.Cu before the pad.
 for name,un,jn,lane,layer in (('BRIDGE_SATA_TX_P','57','1',1,pcbnew.B_Cu),('BRIDGE_SATA_TX_N','56','2',-1,pcbnew.B_Cu),('BRIDGE_SATA_RX_P','60','3',-3,pcbnew.B_Cu),('BRIDGE_SATA_RX_N','59','4',-5,pcbnew.B_Cu)):
  n=b.FindNet('/STORAGE/'+name);upad[un].SetNet(n);jpad[jn].SetNet(n)
  s=up[un];d=jp[jn]; x0,y0=s; x1,y1=d
  escape=(x0-3,y0+lane) if x0 < 140 else (x0+3,y0+lane)
  xrail={'BRIDGE_SATA_RX_N':128,'BRIDGE_SATA_RX_P':129,'BRIDGE_SATA_TX_N':130,'BRIDGE_SATA_TX_P':131}.get(name,130)
  mid=(125,escape[1]); rail=(xrail,escape[1]); landing=(xrail,d[1])
  T(b,n,s,escape,pcbnew.F_Cu); X(b,n,escape); T(b,n,escape,mid,pcbnew.B_Cu); X(b,n,mid); T(b,n,mid,rail,pcbnew.F_Cu); X(b,n,rail); T(b,n,rail,landing,pcbnew.B_Cu); X(b,n,landing); T(b,n,landing,d,pcbnew.F_Cu)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
