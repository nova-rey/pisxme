"""Fresh coordinated storage island: exact CM5 escape, moved U7/J3, USB3+SATA."""
from pathlib import Path
import os
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/os.environ.get('P19_BASE','ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb'); OUT=R/(os.environ.get('P19_OUT','ACREAGE_PHASE19_STORAGE_COORDINATED_FRESH.kicad_pcb')); W=pcbnew.FromMM(.13208)
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
 urot=int(os.environ.get('P19_U7_ROT','180'))
 # KiCad 10 refreshes transformed pad coordinates on serialization. Reload
 # after the placement edit so every generated route uses the saved geometry,
 # not stale pre-move pad positions.
 sync=R/'.phase19_storage_sync.kicad_pcb'; b.Save(str(sync)); b=pcbnew.LoadBoard(str(sync));u=b.FindFootprintByReference('U7');j=b.FindFootprintByReference('J3');src=b.FindFootprintByReference('J7')
 jrot=int(os.environ.get('P19_J3_ROT','90'))
 skip_sata=os.environ.get('P19_SKIP_SATA','0')=='1'
 # The live Phase 18 ancestor may already contain materialized C30-C33.
 # Normalize their presence before creating split nets, then serialize and
 # reload so no pre-netlist SWIG footprint proxy survives the mutation.
 io=pcbnew.PCB_IO_KICAD_SEXPR()
 # C30-C33 are not stable semantic identities in the inherited Phase 18
 # board (they may be unrelated regulator capacitors). Remove donor refs
 # before loading the four SATA coupling footprints.
 donor_caps={f.GetReference():f for f in b.GetFootprints() if f.GetReference() in ('C30','C31','C32','C33')}
 for ref in ('C30','C31','C32','C33'):
  if ref in donor_caps: b.Remove(donor_caps[ref])
 cap_xy={
  'C30':(130,132.0),'C31':(130,136.0),
  'C32':(134,132.0),'C33':(134,136.0),
 }
 for i,ref in enumerate(('C30','C31','C32','C33')):
  cap=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),'C_0402_1005Metric')
  if cap is None: raise RuntimeError('cannot load C_0402_1005Metric')
  cap.SetReference(ref); b.Add(cap)
  cap.SetPosition(V(*cap_xy[ref]))
 storage_nets={}
 for name in ('SATA_M2_TX_P','SATA_M2_TX_N','SATA_M2_RX_P','SATA_M2_RX_N'):
  full='/STORAGE/'+name
  storage_nets[full]=b.FindNet(full)
  if storage_nets[full] is None:
   storage_nets[full]=pcbnew.NETINFO_ITEM(b,full)
   storage_nets[full].SetNetCode(b.GetNetCount()+len(storage_nets))
   b.Add(storage_nets[full])
 # Keep the newly-created socket nets alive across the synchronization
 # save/reload by attaching them before serialization. KiCad drops sparse
 # net records that have no pad users yet.
 for name,un,jn,cref in (('BRIDGE_SATA_TX_P','57','1','C30'),('BRIDGE_SATA_TX_N','56','2','C31'),('BRIDGE_SATA_RX_P','60','3','C32'),('BRIDGE_SATA_RX_N','59','4','C33')):
  bridge=b.FindNet('/STORAGE/'+name); socket=storage_nets['/STORAGE/'+name.replace('BRIDGE_SATA_','SATA_M2_')]
  cf=b.FindFootprintByReference(cref); jf=b.FindFootprintByReference('J3')
  next(p for p in cf.Pads() if str(p.GetNumber())=='1').SetNetCode(socket.GetNetCode())
  next(p for p in cf.Pads() if str(p.GetNumber())=='2').SetNetCode(bridge.GetNetCode())
  next(p for p in jf.Pads() if str(p.GetNumber())==jn).SetNetCode(socket.GetNetCode())
 b.Save(sync); b=None; b=pcbnew.LoadBoard(str(sync));u=b.FindFootprintByReference('U7');j=b.FindFootprintByReference('J3');src=b.FindFootprintByReference('J7')
 storage_nets={'/STORAGE/'+name:b.FindNet('/STORAGE/'+name) for name in ('SATA_M2_TX_P','SATA_M2_TX_N','SATA_M2_RX_P','SATA_M2_RX_N')}
 sp={str(p.GetNumber()):xy(p) for p in list(src.Pads())};up={str(p.GetNumber()):xy(p) for p in list(u.Pads())};jp={str(p.GetNumber()):xy(p) for p in list(j.Pads())};upad={str(p.GetNumber()):p for p in list(u.Pads())};jpad={str(p.GetNumber()):p for p in list(j.Pads())}
 cap_pos={ref:{str(p.GetNumber()):xy(p) for p in list(b.FindFootprintByReference(ref).Pads())} for ref in ('C30','C31','C32','C33')}
 if not skip_sata:
  for name,un,jn,cref in (('BRIDGE_SATA_TX_P','57','1','C30'),('BRIDGE_SATA_TX_N','56','2','C31'),('BRIDGE_SATA_RX_P','60','3','C32'),('BRIDGE_SATA_RX_N','59','4','C33')):
   n=b.FindNet('/STORAGE/'+name); socket=storage_nets['/STORAGE/'+name.replace('BRIDGE_SATA_','SATA_M2_')]
   cap_pads=list(b.FindFootprintByReference(cref).Pads())
   # Set both object and serialized net code.  KiCad 10 can retain the
   # pointer transiently but emit a blank pad net for newly-created nets
   # unless the code is written explicitly.
   cp1pad=next(p for p in cap_pads if str(p.GetNumber())=='1'); cp1pad.SetNet(socket); cp1pad.SetNetCode(socket.GetNetCode())
   cp2pad=next(p for p in cap_pads if str(p.GetNumber())=='2'); cp2pad.SetNet(n); cp2pad.SetNetCode(n.GetNetCode())
   jpad[jn].SetNet(socket); jpad[jn].SetNetCode(socket.GetNetCode())
 for t in list(b.GetTracks()):
  # Moving the coherent storage island invalidates donor copper on both
  # high-speed buses. Remove only those routed nets; PCIe and unrelated
  # power/support copper remain inherited and untouched.
  if 'USB3' in t.GetNetname() or 'BRIDGE_SATA_' in t.GetNetname() or 'SATA_M2_' in t.GetNetname(): b.Remove(t)
 # Exact Phase 18 CM5 escape geometry, extended monotonically to the moved
 # U7 row. U7 is deliberately placed at y=110 so the four source orderings
 # and the 0.5 mm USB pad pitch remain ordered at the landing.
 for name,spn,upn,first,second in (('CM5_USB3_RX_N','128','42',(72,103.9),(103,103)),('CM5_USB3_RX_P','130','43',(72,104.8),(103,105)),('CM5_USB3_TX_N','140','45',(72,108),(103,107))):
  n=b.FindNet('/CORE_CM5/'+name);s=sp[spn];d=up[upn];launch=(71.2,s[1]);T(b,n,s,launch,pcbnew.F_Cu);T(b,n,launch,first,pcbnew.F_Cu);X(b,n,first)
  if name == 'CM5_USB3_TX_N':
   T(b,n,first,(82,108),pcbnew.B_Cu);X(b,n,(82,108));T(b,n,(82,108),(102,108),pcbnew.B_Cu);T(b,n,(102,108),second,pcbnew.B_Cu);X(b,n,second)
  else:
   T(b,n,first,second,pcbnew.B_Cu);X(b,n,second)
  landing={'CM5_USB3_RX_N':(115,112),'CM5_USB3_RX_P':(115,113),'CM5_USB3_TX_N':(115,114)}[name]
  T(b,n,second,landing,pcbnew.F_Cu); T(b,n,landing,d,pcbnew.F_Cu)
 n=b.FindNet('/CORE_CM5/CM5_USB3_TX_P');s=sp['142'];d=up['46'];T(b,n,s,(71.2,106.7),pcbnew.F_Cu);T(b,n,(71.2,106.7),(71,109),pcbnew.F_Cu);X(b,n,(71,109));T(b,n,(71,109),(82,112),pcbnew.B_Cu);X(b,n,(82,112));T(b,n,(82,112),(115,116),pcbnew.F_Cu);T(b,n,(115,116),d,pcbnew.F_Cu)
 if urot == 90:
  # Rotation-90 U7 has a horizontal USB pad row. Rebuild its landing from
  # the validated CM5 source escapes using isolated staged rails.
  for name,spn,upn,first,second,xrail in (('CM5_USB3_RX_N','128','42',(72,103.9),(103,103),100),('CM5_USB3_RX_P','130','43',(72,104.8),(103,105),102),('CM5_USB3_TX_N','140','45',(72,108),(103,107),104)):
   n=b.FindNet('/CORE_CM5/'+name);s=sp[spn];d=up[upn];launch=(71.2,s[1]);T(b,n,s,launch,pcbnew.F_Cu);T(b,n,launch,first,pcbnew.F_Cu);X(b,n,first)
   if name == 'CM5_USB3_TX_N': T(b,n,first,(82,108),pcbnew.B_Cu);X(b,n,(82,108));T(b,n,(82,108),(102,108),pcbnew.B_Cu);T(b,n,(102,108),second,pcbnew.B_Cu);X(b,n,second)
   else: T(b,n,first,second,pcbnew.B_Cu);X(b,n,second)
   T(b,n,second,(xrail,110),pcbnew.F_Cu);T(b,n,(xrail,110),(xrail,146),pcbnew.F_Cu);T(b,n,(xrail,146),d,pcbnew.F_Cu)
  n=b.FindNet('/CORE_CM5/CM5_USB3_TX_P');s=sp['142'];d=up['46'];T(b,n,s,(71.2,106.7),pcbnew.F_Cu);T(b,n,(71.2,106.7),(71,109),pcbnew.F_Cu);X(b,n,(71,109));T(b,n,(71,109),(82,112),pcbnew.B_Cu);X(b,n,(82,112));T(b,n,(82,112),(106,116),pcbnew.F_Cu);T(b,n,(106,116),(106,146),pcbnew.F_Cu);T(b,n,(106,146),d,pcbnew.F_Cu)
 # SATA corridor is derived from the actual moved pad coordinates.  The two
 # pairs use separate permitted layers and monotonic lanes; vias are outside
 # both SMD pad fields and each M.2 launch returns to F.Cu before the pad.
 if not skip_sata:
  for name,un,jn,cref,lane in (('BRIDGE_SATA_TX_P','57','1','C30',1),('BRIDGE_SATA_TX_N','56','2','C31',3),('BRIDGE_SATA_RX_P','60','3','C32',-3),('BRIDGE_SATA_RX_N','59','4','C33',-1)):
   cp=cap_pos[cref]; cp1=cp['1']; cp2=cp['2']
   n=b.FindNet('/STORAGE/'+name); socket=storage_nets['/STORAGE/'+name.replace('BRIDGE_SATA_','SATA_M2_')]
   s=up[un];d=jp[jn];a=cp2;z=cp1; x0,y0=s; x1,y1=d
   if jrot == 0:
    escape=(x0,y0-2) if name in ('BRIDGE_SATA_TX_P','BRIDGE_SATA_RX_P') else (x0,y0+2); layer=pcbnew.F_Cu if name in ('BRIDGE_SATA_TX_P','BRIDGE_SATA_TX_N') else pcbnew.B_Cu; T(b,n,s,escape,pcbnew.F_Cu); X(b,n,escape); T(b,n,escape,a,layer); X(b,n,a); T(b,n,a,cp2,pcbnew.F_Cu); T(b,socket,z,(z[0],d[1]),pcbnew.F_Cu); T(b,socket,(z[0],d[1]),d,pcbnew.F_Cu)
   else:
    # Co-located acreage island: escape each U7 pad to a distinct rail,
    # keep TX/RX pairs on separate permitted copper layers, then launch the
    # socket-side cap pads monotonically into the rotated J3 footprint.
    rails={'C30':(x0,128.0,pcbnew.F_Cu),'C31':(x0,142.0,pcbnew.B_Cu),
           'C32':(x0-2.0,126.0,pcbnew.F_Cu),'C33':(x0+2.0,144.0,pcbnew.B_Cu)}
    rx,ry,layer=rails[cref]; escape=(rx,ry)
    T(b,n,s,escape,pcbnew.F_Cu); X(b,n,escape); T(b,n,escape,a,layer); X(b,n,a)
    launch=(z[0]+(2.0 if jn in ('2','4') else -2.0),z[1])
    T(b,socket,z,launch,pcbnew.F_Cu); X(b,socket,launch); T(b,socket,launch,(launch[0],ry),layer); T(b,socket,(launch[0],ry),(d[0],ry),layer); T(b,socket,(d[0],ry),d,layer)
 # Do not rebuild the net table here: KiCad 10's BuildListOfNets() drops
 # intentionally sparse project-local socket-side nets before serialization.
 b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
