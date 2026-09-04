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
 uy=float(os.environ.get('P19_U7_Y','110'))
 cap_xy={
  'C30':(130,uy-8.0),'C31':(130,uy-4.0),
  # Separate RX capacitors vertically so the TX socket launch cannot pass
  # through the opposite pair's bridge-side pad field.
  'C32':(134,uy-12.0),'C33':(134,uy),
 }
 for i,ref in enumerate(('C30','C31','C32','C33')):
  cap=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),'C_0402_1005Metric')
  if cap is None: raise RuntimeError('cannot load C_0402_1005Metric')
  cap.SetReference(ref); cap.SetOrientationDegrees(180); b.Add(cap)
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
 # Preserve the validated CM5 source escapes from Phase 18 and extend only
 # their final landing to the serialized moved-U7 pad row. The final
 # horizontal dogbone approaches each QFN pad from the west, avoiding the
 # neighboring pad field; TX polarity/order is handled by the established
 # two-corridor source escape.
 usb_rows=(('CM5_USB3_RX_N','128','42',(72.0,103.9),(103.0,103.0)),
           ('CM5_USB3_RX_P','130','43',(72.0,104.8),(103.0,105.0)),
           ('CM5_USB3_TX_N','140','45',(72.0,108.0),(103.0,107.0)),
           ('CM5_USB3_TX_P','142','46',(71.0,109.0),(82.0,112.0)))
 for name,spn,upn,first,second in usb_rows:
  n=b.FindNet('/CORE_CM5/'+name); s=sp[spn]; d=up[upn]
  launch=(71.2,s[1])
  T(b,n,s,launch,pcbnew.F_Cu)
  T(b,n,launch,first,pcbnew.F_Cu); X(b,n,first)
  if name == 'CM5_USB3_TX_N':
   T(b,n,first,(80.0,108.0),pcbnew.B_Cu); T(b,n,(80.0,108.0),(102.0,108.0),pcbnew.B_Cu)
   T(b,n,(102.0,108.0),second,pcbnew.B_Cu)
  elif name == 'CM5_USB3_TX_P':
   T(b,n,first,(82.0,112.0),pcbnew.B_Cu)
  else:
   T(b,n,first,second,pcbnew.B_Cu)
  X(b,n,second)
  landing=(110.0,d[1])
  if name == 'CM5_USB3_RX_N':
   # Transition back to F.Cu at the right edge of the source corridor, then
   # descend left of the frozen B.Cu PCIe trunk. TX_P remains on B.Cu below,
   # so this vertical landing cannot cross its F.Cu diagonal.
   landing=(95.0,d[1]); T(b,n,second,(95.0,second[1]),pcbnew.F_Cu); T(b,n,(95.0,second[1]),landing,pcbnew.F_Cu); T(b,n,landing,d,pcbnew.F_Cu)
  elif name == 'CM5_USB3_TX_P':
   # Keep the lower TX_P corridor on B.Cu and return at a single via outside
   # the moved-U7 pad field.
   T(b,n,second,landing,pcbnew.B_Cu); X(b,n,landing); T(b,n,landing,d,pcbnew.F_Cu)
  else:
   T(b,n,second,landing,pcbnew.F_Cu); T(b,n,landing,d,pcbnew.F_Cu)
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
    # Co-located acreage island: TX bridge escapes remain on F.Cu and RX
    # bridge escapes use B.Cu, so the four adjacent U7 pads never weave on a
    # common layer. Socket-side RX launches similarly use a separated B.Cu
    # corridor before short final returns to the J3 pads.
    if name == 'BRIDGE_SATA_TX_P':
     escape=(x0-2.5,132.0); T(b,n,s,escape,pcbnew.F_Cu); T(b,n,escape,(a[0],132.0),pcbnew.F_Cu); T(b,n,(a[0],132.0),a,pcbnew.F_Cu)
    elif name == 'BRIDGE_SATA_TX_N':
     escape=(x0+2.0,136.0); T(b,n,s,escape,pcbnew.F_Cu); T(b,n,escape,(a[0],136.0),pcbnew.F_Cu); T(b,n,(a[0],136.0),a,pcbnew.F_Cu)
    elif name == 'BRIDGE_SATA_RX_P':
     escape=(x0-3.0,138.0); T(b,n,s,escape,pcbnew.F_Cu); X(b,n,escape); T(b,n,escape,(a[0]-2.0,126.0),pcbnew.B_Cu); X(b,n,(a[0]-2.0,126.0)); T(b,n,(a[0]-2.0,126.0),a,pcbnew.F_Cu)
    else:
     escape=(x0-3.0,144.0); T(b,n,s,escape,pcbnew.F_Cu); X(b,n,escape); T(b,n,escape,(a[0]-2.0,146.0),pcbnew.B_Cu); X(b,n,(a[0]-2.0,146.0)); T(b,n,(a[0]-2.0,146.0),a,pcbnew.F_Cu)
    if name.startswith('BRIDGE_SATA_TX_'):
     launch=(z[0]+(6.0 if jn=='2' else 2.0), z[1])
     T(b,socket,z,launch,pcbnew.F_Cu); T(b,socket,launch,d,pcbnew.F_Cu)
    elif name == 'BRIDGE_SATA_RX_P':
     via1=(z[0],130.0); via2=(d[0]+2.7,d[1]); T(b,socket,z,via1,pcbnew.F_Cu); X(b,socket,via1); T(b,socket,via1,via2,pcbnew.B_Cu); X(b,socket,via2); T(b,socket,via2,d,pcbnew.F_Cu)
    else:
     via1=(z[0],138.0); via2=(d[0]+2.7,d[1]); T(b,socket,z,via1,pcbnew.F_Cu); X(b,socket,via1); T(b,socket,via1,via2,pcbnew.B_Cu); X(b,socket,via2); T(b,socket,via2,d,pcbnew.F_Cu)
 # Do not rebuild the net table here: KiCad 10's BuildListOfNets() drops
 # intentionally sparse project-local socket-side nets before serialization.
 b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
