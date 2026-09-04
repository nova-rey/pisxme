"""Fresh coordinated storage island: exact CM5 escape, moved U7/J3, USB3+SATA."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb'; OUT=R/'ACREAGE_PHASE19_STORAGE_COORDINATED_FRESH.kicad_pcb'; W=pcbnew.FromMM(.13208)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def P(f,n): return next(p for p in list(f.Pads()) if str(p.GetNumber())==str(n))
def T(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);b.Add(t)
def X(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(V(*p));q.SetWidth(pcbnew.FromMM(.5));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);q.SetNet(n);b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U7');j=b.FindFootprintByReference('J3');src=b.FindFootprintByReference('J7')
 u.SetPosition(V(120,140));u.SetOrientationDegrees(180);j.SetPosition(V(145,125));j.SetOrientationDegrees(90)
 sp={str(p.GetNumber()):xy(p) for p in list(src.Pads())};up={str(p.GetNumber()):xy(p) for p in list(u.Pads())};jp={str(p.GetNumber()):xy(p) for p in list(j.Pads())};upad={str(p.GetNumber()):p for p in list(u.Pads())};jpad={str(p.GetNumber()):p for p in list(j.Pads())}
 for t in list(b.GetTracks()):
  if 'USB3' in t.GetNetname(): b.Remove(t)
 # Exact Phase 18 CM5 dogbones and B.Cu escapes to x=103/82, then new U7 landings.
 for name,spn,upn,first,second in (('CM5_USB3_RX_N','128','42',(72,103.9),(103,103)),('CM5_USB3_RX_P','130','43',(72,104.8),(103,105)),('CM5_USB3_TX_N','140','45',(72,108),(103,107))):
  n=b.FindNet('/CORE_CM5/'+name);s=sp[spn];d=up[upn];launch=(71.2,s[1]);T(b,n,s,launch,pcbnew.F_Cu);T(b,n,launch,first,pcbnew.F_Cu);X(b,n,first)
  if name == 'CM5_USB3_TX_N':
   T(b,n,first,(75,first[1]),pcbnew.B_Cu);X(b,n,(75,first[1]));T(b,n,(75,first[1]),second,pcbnew.F_Cu);X(b,n,second)
  else:
   T(b,n,first,(80,first[1]),pcbnew.B_Cu);T(b,n,(80,first[1]),(102,first[1]),pcbnew.B_Cu);T(b,n,(102,first[1]),second,pcbnew.B_Cu);X(b,n,second)
  if name.startswith('CM5_USB3_RX'):
   start={'CM5_USB3_RX_N':(80,103),'CM5_USB3_RX_P':(78,105)}[name]
   final={'CM5_USB3_RX_N':(112,138.5),'CM5_USB3_RX_P':(112,139.5)}[name]
   T(b,n,second,start,pcbnew.B_Cu);T(b,n,start,(start[0],130 if name.endswith('N') else 131),pcbnew.B_Cu);T(b,n,(start[0],130 if name.endswith('N') else 131),final,pcbnew.B_Cu);X(b,n,final);T(b,n,final,d,pcbnew.F_Cu)
  else:
   landing=((105,112),(115,112),(115,141.5))
   a=second
   for z in landing:T(b,n,a,z,pcbnew.F_Cu);a=z
   T(b,n,a,d,pcbnew.F_Cu)
 n=b.FindNet('/CORE_CM5/CM5_USB3_TX_P');s=sp['142'];d=up['46'];T(b,n,s,(71.2,106.7),pcbnew.F_Cu);T(b,n,(71.2,106.7),(71,109),pcbnew.F_Cu);X(b,n,(71,109));T(b,n,(71,109),(82,112),pcbnew.B_Cu);X(b,n,(82,112));T(b,n,(82,112),(82,150),pcbnew.B_Cu);T(b,n,(82,150),(114,150),pcbnew.B_Cu);X(b,n,(114,150));T(b,n,(114,150),d,pcbnew.F_Cu)
 # SATA V3 corridor on the same moved island.
 for name,un,jn,pts in (('BRIDGE_SATA_TX_P','57','1',[(120.5,130),(132,130),(132,134.25)]),('BRIDGE_SATA_TX_N','56','2',[(121,110),(150,110),(150,134)]),('BRIDGE_SATA_RX_P','60','3',[(119,120),(136,120),(136,133.75)]),('BRIDGE_SATA_RX_N','59','4',[(119.5,118),(144,118),(142,133.5)])):
  n=b.FindNet('/STORAGE/'+name);upad[un].SetNet(n);jpad[jn].SetNet(n);a=up[un]
  for i,z in enumerate(pts):
   T(b,n,a,z,pcbnew.F_Cu if name=='BRIDGE_SATA_TX_N' else (pcbnew.B_Cu if i else pcbnew.F_Cu));
   if name=='BRIDGE_SATA_TX_P' and i==0:X(b,n,z)
   if name in ('BRIDGE_SATA_RX_P','BRIDGE_SATA_RX_N') and i==0:X(b,n,z)
   a=z
  if name=='BRIDGE_SATA_TX_P': X(b,n,pts[-1]);T(b,n,pts[-1],jp[jn],pcbnew.F_Cu)
  elif name=='BRIDGE_SATA_TX_N': T(b,n,pts[-1],jp[jn],pcbnew.F_Cu)
  else: X(b,n,pts[-1]);T(b,n,pts[-1],jp[jn],pcbnew.F_Cu)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
