"""Fresh coordinated storage island: exact CM5 escape, moved U7/J3, USB3+SATA."""
from pathlib import Path
import os
import sys
import pcbnew
# KiCad's Flatpak launcher does not consistently preserve host-side environment
# overrides.  Accept the same P19_* names as explicit --NAME=value arguments
# so every disposable candidate is reproducible inside the native tool.
for _arg in sys.argv[1:]:
 if _arg.startswith('--') and '=' in _arg:
  _key, _value = _arg[2:].split('=', 1)
  os.environ[_key.replace('-', '_')] = _value
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
 ux=float(os.environ.get('P19_U7_X','140')); uy=float(os.environ.get('P19_U7_Y','110'))
 # Carry the authoritative oscillator island with the moved bridge only when
 # explicitly requested.  The selected macro already contains a native
 # clock/support placement; silently translating it into the SATA pad field
 # creates a false route obstruction and violates coherent-island authority.
 if os.environ.get('P19_KEEP_CLOCK','0') != '1':
  for ref,dx,dy in (('Y1',8.0,-5.0),('R23',8.0,0.0),('C42',8.0,5.0),('C43',12.0,5.0)):
   f=b.FindFootprintByReference(ref)
   if f is not None: f.SetPosition(V(ux+dx,uy+dy))
 b.Save(str(sync)); b=pcbnew.LoadBoard(str(sync));u=b.FindFootprintByReference('U7');j=b.FindFootprintByReference('J3');src=b.FindFootprintByReference('J7')
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
 ux=float(os.environ.get('P19_U7_X','120'))
 cap_xy={
  'C30':(ux+10.0,uy-8.0),'C31':(ux+10.0,uy-4.0),
  # Separate RX capacitors vertically so the TX socket launch cannot pass
  # through the opposite pair's bridge-side pad field.
  'C32':(ux+14.0,uy-12.0),'C33':(ux+14.0,uy),
 }
 if os.environ.get('P19_SATA_V3','0') == '1':
  # Reuse the proven V3 monotonic corridor, but materialize the required
  # split coupling capacitors in-line instead of overlaying them afterward.
  cap_xy={'C30':(127.0,130.0),'C31':(135.0,110.0),
          'C32':(127.0,120.0),'C33':(127.0,118.0)}
 if urot == 270 and jrot == 90 and os.environ.get('P19_SATA_ROT270','0') == '1':
  # Rotation-aware bridge-side capacitor island.  The older V3 branch was
  # authored for U7 rotation 180 and placed these capacitors into the new
  # clock/SATA pad field when reused at rotation 270.
  cap_xy={'C30':(ux+10.0,uy-8.0),'C31':(ux+10.0,uy-4.0),
          'C32':(ux+10.0,uy-12.0),'C33':(ux+10.0,uy)}
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
  # TX_P remains on B.Cu through this point in the validated lower corridor;
  # it does not need a return via at `second`.  The other three branches
  # transition there in at least one coordinated experiment.
  if name != 'CM5_USB3_TX_P': X(b,n,second)
  landing=(110.0,d[1])
  if os.environ.get('P19_USB_REPATH','0') == '1':
   # Coordinated V3 repath: keep the RX_N return left of the F.Cu pair
   # field, move RX_P to B.Cu before the lower landing, and move TX_N to a
   # B.Cu vertical below the frozen PCIe trunk.  The four branches are
   # intentionally authored together so a local fix cannot create a pair
   # crossing in another branch.
   if name == 'CM5_USB3_RX_N':
    T(b,n,second,(90.0,second[1]),pcbnew.F_Cu); T(b,n,(90.0,second[1]),(90.0,d[1]),pcbnew.F_Cu); T(b,n,(90.0,d[1]),d,pcbnew.F_Cu)
   elif name == 'CM5_USB3_RX_P':
    vx=float(os.environ.get('P19_RXP_FX','102.0')); v=(vx,130.0); q=(113.0,130.0); r=(113.0,d[1]); T(b,n,second,(vx,second[1]),pcbnew.F_Cu); T(b,n,(vx,second[1]),v,pcbnew.F_Cu); X(b,n,v); T(b,n,v,q,pcbnew.B_Cu); T(b,n,q,r,pcbnew.B_Cu); X(b,n,r); T(b,n,r,d,pcbnew.F_Cu)
   elif name == 'CM5_USB3_TX_N':
    v=(115.0,107.0); q=(115.0,130.0); r=(115.0,d[1]); T(b,n,second,v,pcbnew.F_Cu); T(b,n,v,q,pcbnew.F_Cu); X(b,n,q); T(b,n,q,r,pcbnew.B_Cu); X(b,n,r); T(b,n,r,d,pcbnew.F_Cu)
   else:
    T(b,n,second,landing,pcbnew.B_Cu); X(b,n,landing); T(b,n,landing,d,pcbnew.F_Cu)
  elif name == 'CM5_USB3_RX_N' and os.environ.get('P19_RXN_DIRECT','0') == '1':
   # For the synchronized V3 placement, the serialized RX_N pad is reached
   # directly from the existing source-corridor via.  This is the narrow
   # crossing repair identified by the independent PCB review; it avoids the
   # former x=95 vertical detour and does not touch PCIe copper.
   v=(d[0]-2.5,d[1]); T(b,n,second,v,pcbnew.B_Cu); X(b,n,v); T(b,n,v,d,pcbnew.F_Cu)
  elif name == 'CM5_USB3_RX_P' and os.environ.get('P19_RXP_B','0') == '1':
   # Complementary pad-field escape experiment: remain on B.Cu from the
   # existing source via and return beside the serialized RX_P pad.
   v=(d[0]-2.5,d[1]); T(b,n,second,v,pcbnew.B_Cu); X(b,n,v); T(b,n,v,d,pcbnew.F_Cu)
  elif name == 'CM5_USB3_RX_P' and os.environ.get('P19_RXP_STAGGER','0') == '1':
   # Leave the source fanout on F.Cu, then use a short B.Cu final escape to
   # separate the two adjacent U7 RX pads without entering the PCIe trunk.
   v=(d[0]-2.5,130.0); q=(d[0]-2.5,d[1]); T(b,n,second,v,pcbnew.F_Cu); X(b,n,v); T(b,n,v,q,pcbnew.B_Cu); X(b,n,q); T(b,n,q,d,pcbnew.F_Cu)
  elif os.environ.get('P19_USB_DIRECT_FINAL','0') == '1' and d[0] <= second[0]+3.0:
   # When U7 is returned to the validated Phase-18 neighborhood, its USB
   # pads are west of the extension corridor.  Preserve the native ancestor's
   # short direct landings instead of routing east and doubling back through
   # the adjacent pad field.
   T(b,n,second,d,pcbnew.F_Cu)
  elif name == 'CM5_USB3_RX_N' and os.environ.get('P19_RXN_FX'):
   # Alternate F.Cu return column for the synchronized storage placement.
   # This keeps RX_N off the PCIe B.Cu trunk while routing around TX_N.
   fx=float(os.environ.get('P19_RXN_FX'))
   T(b,n,second,(fx,second[1]),pcbnew.F_Cu); T(b,n,(fx,second[1]),(fx,d[1]),pcbnew.F_Cu); T(b,n,(fx,d[1]),d,pcbnew.F_Cu)
  elif name == 'CM5_USB3_RX_N':
   # Transition back to F.Cu at the right edge of the source corridor, then
   # descend left of the frozen B.Cu PCIe trunk. TX_P remains on B.Cu below,
   # so this vertical landing cannot cross its F.Cu diagonal.
   landing=(95.0,d[1]); T(b,n,second,(95.0,second[1]),pcbnew.F_Cu); T(b,n,(95.0,second[1]),landing,pcbnew.F_Cu); T(b,n,landing,d,pcbnew.F_Cu)
  elif name == 'CM5_USB3_TX_P':
   # Keep the lower TX_P corridor on B.Cu and return at a single via outside
   # the moved-U7 pad field.
   if os.environ.get('P19_USB_DIRECT_FINAL','0') == '1':
    T(b,n,second,(98.0,second[1]),pcbnew.F_Cu); T(b,n,(98.0,second[1]),(98.0,d[1]),pcbnew.F_Cu); T(b,n,(98.0,d[1]),d,pcbnew.F_Cu)
   else:
    T(b,n,second,landing,pcbnew.B_Cu); X(b,n,landing); T(b,n,landing,d,pcbnew.F_Cu)
  elif name == 'CM5_USB3_TX_N' and os.environ.get('P19_TXN_B','0') == '1':
   # Optional layer-separated final dogleg for placement experiments.  The
   # source corridor is already on B.Cu at `second`; remain on B.Cu until a
   # clearance-safe landing west of the U7 pad row, then return to F.Cu.
   bx=float(os.environ.get('P19_TXN_BX','110.0'))
   T(b,n,second,(bx,second[1]),pcbnew.B_Cu)
   T(b,n,(bx,second[1]),(bx,d[1]),pcbnew.B_Cu)
   landing=(bx,d[1]); X(b,n,landing); T(b,n,landing,d,pcbnew.F_Cu)
  elif name == 'CM5_USB3_TX_N' and os.environ.get('P19_TXN_FDOG','0') == '1':
   # F.Cu dogleg variant: move the final vertical leg east of the RX_N
   # horizontal landing so the two same-layer segments are monotonic.
   fx=float(os.environ.get('P19_TXN_FX','120.0'))
   T(b,n,second,(fx,second[1]),pcbnew.F_Cu)
   T(b,n,(fx,second[1]),(fx,d[1]),pcbnew.F_Cu)
   T(b,n,(fx,d[1]),d,pcbnew.F_Cu)
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
   if urot == 270 and jrot == 90 and os.environ.get('P19_SATA_ROT270','0') == '1':
    # U7 rotation-270: clock escapes west, SATA bridge pads escape east.
    # Keep the four bridge-side legs in distinct local lanes and launch the
    # socket-side nets monotonically toward the rotated J3 pad columns.
    if name == 'BRIDGE_SATA_TX_P':
     e=(s[0]+6.0,s[1]); T(b,n,s,e,pcbnew.F_Cu); T(b,n,e,a,pcbnew.F_Cu)
     q=(z[0]+8.0,z[1]); T(b,socket,z,q,pcbnew.F_Cu); T(b,socket,q,d,pcbnew.F_Cu)
    elif name == 'BRIDGE_SATA_TX_N':
     e=(s[0]+6.0,s[1]); T(b,n,s,e,pcbnew.F_Cu); X(b,n,e); T(b,n,e,a,pcbnew.B_Cu)
     q=(z[0]+8.0,z[1]); T(b,socket,z,q,pcbnew.B_Cu); T(b,socket,q,d,pcbnew.B_Cu)
    elif name == 'BRIDGE_SATA_RX_P':
     e=(s[0]+6.0,s[1]); T(b,n,s,e,pcbnew.F_Cu); T(b,n,e,a,pcbnew.F_Cu)
     q=(z[0]+8.0,z[1]); T(b,socket,z,q,pcbnew.F_Cu); T(b,socket,q,d,pcbnew.F_Cu)
    else:
     e=(s[0]+6.0,s[1]); T(b,n,s,e,pcbnew.F_Cu); X(b,n,e); T(b,n,e,a,pcbnew.B_Cu)
     q=(z[0]+8.0,z[1]); T(b,socket,z,q,pcbnew.B_Cu); T(b,socket,q,d,pcbnew.B_Cu)
   elif os.environ.get('P19_SATA_NORTH','0') == '1' and jrot == 90 and urot == 180:
    # Native north escape for the selected U7 rotation.  The SATA pads occupy
    # the upper edge of this saved footprint; leave that edge first, then use
    # separated F.Cu/B.Cu lanes.  Every B.Cu transition is outside both the
    # U7 and 0402 pad fields.
    north_lane={'BRIDGE_SATA_TX_P':101.0,'BRIDGE_SATA_TX_N':99.5,
                'BRIDGE_SATA_RX_P':109.0,'BRIDGE_SATA_RX_N':110.5}[name]
    north_y={'BRIDGE_SATA_TX_P':117.5,'BRIDGE_SATA_TX_N':116.5,
             'BRIDGE_SATA_RX_P':118.5,'BRIDGE_SATA_RX_N':115.5}[name]
    e=(north_lane,north_y); layer=pcbnew.F_Cu if name.startswith('BRIDGE_SATA_TX_') else pcbnew.B_Cu
    T(b,n,s,(s[0],north_y),pcbnew.F_Cu); T(b,n,(s[0],north_y),e,pcbnew.F_Cu)
    if layer == pcbnew.B_Cu:
     X(b,n,e); bridge_v=(a[0],a[1]-1.0); T(b,n,e,bridge_v,pcbnew.B_Cu); X(b,n,bridge_v); T(b,n,bridge_v,a,pcbnew.F_Cu)
    else:
     T(b,n,e,a,pcbnew.F_Cu)
    # Socket-side legs use distinct monotonic upper/lower lanes and return to
    # F.Cu before the M.2 pads.
    socket_v=(z[0]+(2.0 if jn in ('1','3') else -2.0), z[1]-4.0)
    T(b,socket,z,socket_v,pcbnew.F_Cu); X(b,socket,socket_v)
    socket_lane=(socket_v[0], d[1]-4.0 if jn in ('1','3') else d[1]+4.0)
    T(b,socket,socket_v,socket_lane,pcbnew.B_Cu); X(b,socket,socket_lane); T(b,socket,socket_lane,d,pcbnew.F_Cu)
   elif os.environ.get('P19_SATA_V3','0') == '1' and jrot == 90:
    # V3 routes: TX_P uses the lower B.Cu corridor, TX_N the upper F.Cu
    # corridor, and the RX pair use separated B.Cu lanes.  Each cap is
    # traversed from pad 2 to pad 1 with a short F.Cu link; no via is placed
    # on an SMD pad.
    if name == 'BRIDGE_SATA_TX_P':
     e=(s[0],133.0); v=(a[0]-0.5,130.0); T(b,n,s,e,pcbnew.F_Cu); X(b,n,e); T(b,n,e,v,pcbnew.B_Cu); X(b,n,v); T(b,n,v,a,pcbnew.F_Cu)
     e=(137.0,130.0); q=(138.0,134.25); T(b,socket,z,e,pcbnew.F_Cu); X(b,socket,e); T(b,socket,e,q,pcbnew.B_Cu); X(b,socket,q); T(b,socket,q,d,pcbnew.F_Cu)
    elif name == 'BRIDGE_SATA_TX_N':
     T(b,n,s,(121.0,110.0),pcbnew.F_Cu); T(b,n,(121.0,110.0),a,pcbnew.F_Cu); e=(150.0,134.0); q=(148.5,134.0); T(b,socket,z,(150.0,110.0),pcbnew.F_Cu); T(b,socket,(150.0,110.0),e,pcbnew.F_Cu); X(b,socket,e); T(b,socket,e,q,pcbnew.B_Cu); X(b,socket,q); T(b,socket,q,d,pcbnew.F_Cu)
    elif name == 'BRIDGE_SATA_RX_P':
     e=(119.0,120.0); v=(a[0]-0.5,120.0); T(b,n,s,e,pcbnew.F_Cu); X(b,n,e); T(b,n,e,v,pcbnew.B_Cu); X(b,n,v); T(b,n,v,a,pcbnew.F_Cu)
     q=(136.0,120.0); r=(136.0,133.75); T(b,socket,z,q,pcbnew.F_Cu); X(b,socket,q); T(b,socket,q,r,pcbnew.B_Cu); X(b,socket,r); T(b,socket,r,d,pcbnew.F_Cu)
    else:
     e=(119.5,118.0); v=(a[0]-0.5,118.0); T(b,n,s,e,pcbnew.F_Cu); X(b,n,e); T(b,n,e,v,pcbnew.B_Cu); X(b,n,v); T(b,n,v,a,pcbnew.F_Cu)
     e=(128.5,118.0); q=(144.0,118.0); r=(144.0,133.5); T(b,socket,z,e,pcbnew.F_Cu); X(b,socket,e); T(b,socket,e,q,pcbnew.B_Cu); T(b,socket,q,r,pcbnew.B_Cu); X(b,socket,r); T(b,socket,r,d,pcbnew.F_Cu)
   elif jrot == 0 and os.environ.get('P19_SATA_ORTHO','0') == '1':
    # Explicit monotonic rot-0 M.2 launch for the Phase-18 U7 neighborhood.
    # TX remains on F.Cu; RX crosses to B.Cu beside (never in) the 0402 pads,
    # then returns with ordinary through-vias before the connector pads.
    if name == 'BRIDGE_SATA_TX_P':
     T(b,n,s,(s[0],97.0),pcbnew.F_Cu); T(b,n,(s[0],97.0),a,pcbnew.F_Cu)
    elif name == 'BRIDGE_SATA_TX_N':
     T(b,n,s,(s[0],101.0),pcbnew.F_Cu); T(b,n,(s[0],101.0),a,pcbnew.F_Cu)
    elif name == 'BRIDGE_SATA_RX_P':
     e=(s[0],93.0); v=(a[0]-0.5,93.0); T(b,n,s,e,pcbnew.F_Cu); X(b,n,e); T(b,n,e,v,pcbnew.B_Cu); X(b,n,v); T(b,n,v,a,pcbnew.F_Cu)
    else:
     e=(s[0],105.0); v=(a[0]-0.5,105.0); T(b,n,s,e,pcbnew.F_Cu); X(b,n,e); T(b,n,e,v,pcbnew.B_Cu); X(b,n,v); T(b,n,v,a,pcbnew.F_Cu)
    if name == 'BRIDGE_SATA_TX_P':
     q=(130.0,97.0); T(b,socket,z,q,pcbnew.F_Cu); T(b,socket,q,d,pcbnew.F_Cu)
    elif name == 'BRIDGE_SATA_TX_N':
     q=(130.0,101.0); T(b,socket,z,q,pcbnew.F_Cu); T(b,socket,q,d,pcbnew.F_Cu)
    elif name == 'BRIDGE_SATA_RX_P':
     e=(126.0,93.0); v=(126.0,93.0); q=(138.0,104.725); T(b,socket,z,e,pcbnew.F_Cu); X(b,socket,e); T(b,socket,e,q,pcbnew.B_Cu); X(b,socket,q); T(b,socket,q,d,pcbnew.F_Cu)
    else:
     e=(126.0,105.0); q=(138.0,112.275); T(b,socket,z,e,pcbnew.F_Cu); X(b,socket,e); T(b,socket,e,q,pcbnew.B_Cu); X(b,socket,q); T(b,socket,q,d,pcbnew.F_Cu)
   elif jrot == 0:
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
 # Refill the inherited reference planes after adding all ordinary through
 # vias.  Native DRC otherwise evaluates stale zone geometry as a collision
 # at every new F.Cu/B.Cu transition.
 # Keep the SWIG zone container alive while native KiCad fills it.  Passing
 # the temporary generator expression directly can segfault in KiCad 10's
 # Flatpak after a footprint rotation/materialization sequence.
 if os.environ.get('P19_FILL_ZONES', '0') == '1':
  _zones = list(b.Zones())
  _filler = pcbnew.ZONE_FILLER(b)
  _filler.Fill(_zones)
 b.Save(str(OUT))
 # Preserve every serialized U7 pad/net assignment.  Earlier generations
 # removed pads 5-12 indiscriminately under the assumption that they were
 # stale donor fields; on the selected native footprint pads 6/7/9 are real
 # USB3/SATA functions.  Connectivity is authoritative from the saved
 # footprint, so no broad text surgery is permitted here.
 print(OUT)
if __name__=='__main__':main()
