"""Phase 19 disposable candidate using reloaded U7/J3/clock endpoints.

This is deliberately an acreage experiment.  No inherited USB3/SATA/clock
copper is retained; the source CM5 pads, bridge, socket, split caps, and
40-MHz clock are regenerated as one coordinated island.
"""
from pathlib import Path
import os, re, pcbnew
R=Path(__file__).resolve().parent
ARGS={}
for _arg in __import__('sys').argv[1:]:
 if _arg.startswith('--') and '=' in _arg:
  _k,_v=_arg[2:].split('=',1); ARGS[_k]=_v
BASE=R/ARGS.get('P19_BASE',os.environ.get('P19_BASE','ACREAGE_CLOCK_CANDIDATE5.kicad_pcb'))
SYNC=R/'.phase19_open_island_sync.kicad_pcb'
OUT=R/'PHASE19_OPEN_ISLAND_LIVE.kicad_pcb'
PREP=ARGS.get('P19_PREP',os.environ.get('P19_PREP','0'))=='1'
SKIP_SATA=ARGS.get('P19_SKIP_SATA',os.environ.get('P19_SKIP_SATA','0'))=='1'
SKIP_CLOCK=ARGS.get('P19_SKIP_CLOCK',os.environ.get('P19_SKIP_CLOCK','0'))=='1'
SKIP_USB=ARGS.get('P19_SKIP_USB',os.environ.get('P19_SKIP_USB','0'))=='1'
CLOCK_ONLY=ARGS.get('P19_CLOCK_ONLY',os.environ.get('P19_CLOCK_ONLY','0'))=='1'
SATA270=ARGS.get('P19_SATA270',os.environ.get('P19_SATA270','0'))=='1'
USB_EAST=ARGS.get('P19_USB_EAST',os.environ.get('P19_USB_EAST','0'))=='1'
USB_TOP_EAST=ARGS.get('P19_USB_TOP_EAST',os.environ.get('P19_USB_TOP_EAST','0'))=='1'
USB_PAIR_SPLIT=ARGS.get('P19_USB_PAIR_SPLIT',os.environ.get('P19_USB_PAIR_SPLIT','0'))=='1'
USB_VERTICAL=ARGS.get('P19_USB_VERTICAL',os.environ.get('P19_USB_VERTICAL','0'))=='1'
W=pcbnew.FromMM(.200)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def pos(p): return (pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y))
def pad(f,n): return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def net(b,name):
 aliases={'/CORE_CM5/CM5_USB3_RX_N':'CM5_USB3_RX_N','/CORE_CM5/CM5_USB3_RX_P':'CM5_USB3_RX_P','/CORE_CM5/CM5_USB3_TX_N':'CM5_USB3_TX_N','/CORE_CM5/CM5_USB3_TX_P':'CM5_USB3_TX_P'}
 n=b.FindNet(name)
 if n is None and name in aliases: n=b.FindNet(aliases[name])
 if n is None:
  n=pcbnew.NETINFO_ITEM(b,name); n.SetNetCode(b.GetNetCount()+1); b.Add(n)
 return n
def seg(b,n,a,z,layer=pcbnew.F_Cu,width=W):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer); t.SetWidth(width); t.SetNet(n); b.Add(t)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)
def strip_old(b):
 for t in list(b.GetTracks()):
  n=t.GetNetname()
  if any(x in n for x in ('CM5_USB3','BRIDGE_SATA','SATA_M2','BRIDGE_XI','BRIDGE_XO','BRIDGE_VSSOSC','BRIDGE_3V3')):
   b.Remove(t)
def setpad(p,n): p.SetNet(n); p.SetNetCode(n.GetNetCode())
def main():
 if PREP:
  b=pcbnew.LoadBoard(str(BASE))
  u=b.FindFootprintByReference('U7'); j=b.FindFootprintByReference('J3')
  # Open region to the right of the PCIe/CM5 source corridors.
  u.SetPosition(V(280,105)); u.SetOrientationDegrees(270)
  j.SetPosition(V(200,140)); j.SetOrientationDegrees(270 if SATA270 else 90)
  old_mech=b.FindFootprintByReference('MECH_M2_2280')
  if old_mech is not None: b.Remove(old_mech)
  # This donor already carries clean C30-C33 clock-candidate objects.
  _caps={'C30':(240,110),'C31':(240,108),'C32':(240,114),'C33':(240,112)} if SATA270 else {'C30':(265,96),'C31':(265,100),'C32':(265,108),'C33':(265,112)}
  for ref,(x,y) in _caps.items():
   f=b.FindFootprintByReference(ref); f.SetPosition(V(x,y)); f.SetOrientationDegrees(0 if SATA270 else 180)
  for ref,xyv in {'Y1':(268,98),'R23':(272,98),'C42':(272,94),'C43':(276,98)}.items():
   f=b.FindFootprintByReference(ref)
   if f is None: raise RuntimeError('clock donor missing '+ref)
   f.SetPosition(V(*xyv)); f.SetOrientationDegrees(0)
  strip_old(b); b.Save(str(SYNC)); print(SYNC); return
 b=pcbnew.LoadBoard(str(SYNC))
 caps={ref:b.FindFootprintByReference(ref) for ref in ('C30','C31','C32','C33')}
 caps={ref:b.FindFootprintByReference(ref) for ref in ('C30','C31','C32','C33')}
 # All endpoints below are obtained only after native serialization reload.
 u=b.FindFootprintByReference('U7'); j=b.FindFootprintByReference('J3'); src=b.FindFootprintByReference('J7')
 U={str(p.GetNumber()):pos(p) for p in u.Pads()}; J={str(p.GetNumber()):pos(p) for p in j.Pads()}; S={str(p.GetNumber()):pos(p) for p in src.Pads()}
 N={}
 for name in ('/CORE_CM5/CM5_USB3_RX_N','/CORE_CM5/CM5_USB3_RX_P','/CORE_CM5/CM5_USB3_TX_N','/CORE_CM5/CM5_USB3_TX_P',
              '/STORAGE/BRIDGE_SATA_TX_P','/STORAGE/BRIDGE_SATA_TX_N','/STORAGE/BRIDGE_SATA_RX_P','/STORAGE/BRIDGE_SATA_RX_N',
              '/STORAGE/SATA_M2_TX_P','/STORAGE/SATA_M2_TX_N','/STORAGE/SATA_M2_RX_P','/STORAGE/SATA_M2_RX_N',
              '/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC'):
  N[name]=net(b,name)
 # USB3: source fanout drops to parallel B.Cu corridors below the PCIe bbox,
 # then climbs only in the open x>190 region and returns on F.Cu at U7.
 usb=(('CM5_USB3_RX_N','128','42',(78,90),(260,90)),('CM5_USB3_RX_P','130','43',(76,92),(265,92)),
      ('CM5_USB3_TX_N','140','45',(74,94),(270,94)),('CM5_USB3_TX_P','142','46',(72,96),(275,96))) if USB_EAST else (('CM5_USB3_RX_N','128','42',(78,114),(200,114)),('CM5_USB3_RX_P','130','43',(76,116),(204,116)),
      ('CM5_USB3_TX_N','140','45',(74,118),(208,118)),('CM5_USB3_TX_P','142','46',(72,120),(212,120)))
 for suffix,sp,up,start,far in usb:
  if SKIP_USB:
   continue
  n=N['/CORE_CM5/'+suffix]; s=S[sp]; d=U[up]
  setpad(pad(src,sp),n); setpad(pad(u,up),n)
  if USB_TOP_EAST:
   # Preserve the serialized CM5 source escape, then use four ordered
   # top-side B.Cu corridors and an outboard x>290 approach to U7.  This
   # keeps the USB3 graph outside the SATA island instead of changing the
   # source-side fanout as the rejected USB_EAST trial did.
   first={'CM5_USB3_RX_N':(78.0,103.9),'CM5_USB3_RX_P':(76.0,104.8),
          'CM5_USB3_TX_N':(74.0,108.0),'CM5_USB3_TX_P':(72.0,109.0)}[suffix]
   top={'CM5_USB3_RX_N':(86.0,80.0),'CM5_USB3_RX_P':(84.0,82.0),
        'CM5_USB3_TX_N':(82.0,84.0),'CM5_USB3_TX_P':(80.0,86.0)}[suffix]
   outx={'CM5_USB3_RX_N':295.0,'CM5_USB3_RX_P':296.0,
         'CM5_USB3_TX_N':297.0,'CM5_USB3_TX_P':298.0}[suffix]
   landing={'CM5_USB3_RX_N':(290.0,112.0),'CM5_USB3_RX_P':(291.0,114.5),
            'CM5_USB3_TX_N':(292.0,117.0),'CM5_USB3_TX_P':(293.0,119.5)}[suffix]
   launch=(71.2,s[1]); seg(b,n,s,launch); seg(b,n,launch,first); via(b,n,first)
   seg(b,n,first,top,pcbnew.B_Cu); seg(b,n,top,(outx,top[1]),pcbnew.B_Cu); seg(b,n,(outx,top[1]),(outx,landing[1]),pcbnew.B_Cu); seg(b,n,(outx,landing[1]),landing,pcbnew.B_Cu); via(b,n,landing)
   dog=(d[0],landing[1]-1.0); seg(b,n,landing,dog,pcbnew.F_Cu); seg(b,n,dog,d,pcbnew.F_Cu)
   continue
  if USB_PAIR_SPLIT:
   # Pair-preserving alternative: RX is one B.Cu pair and TX one F.Cu
   # pair.  The two pairs therefore cannot cross in the long corridor;
   # their U7 pad dogbones are kept in separate upper/lower launch bands.
   first={'CM5_USB3_RX_N':(72.0,103.9),'CM5_USB3_RX_P':(74.0,104.3),
          'CM5_USB3_TX_N':(78.0,106.3),'CM5_USB3_TX_P':(76.0,106.7)}[suffix]
   top={'CM5_USB3_RX_N':(72.0,82.0),'CM5_USB3_RX_P':(74.0,80.0),
        'CM5_USB3_TX_N':(78.0,86.0),'CM5_USB3_TX_P':(76.0,84.0)}[suffix]
   outx={'CM5_USB3_RX_N':295.0,'CM5_USB3_RX_P':296.0,
         'CM5_USB3_TX_N':297.0,'CM5_USB3_TX_P':298.0}[suffix]
   landing={'CM5_USB3_RX_N':(288.0,110.0),'CM5_USB3_RX_P':(289.0,112.0),
            'CM5_USB3_TX_N':(290.0,116.0),'CM5_USB3_TX_P':(291.0,118.0)}[suffix]
   launch=(71.2,s[1]); seg(b,n,s,launch); seg(b,n,launch,first)
   if suffix.startswith('CM5_USB3_RX_'):
    via(b,n,first); layer=pcbnew.B_Cu
   else:
    layer=pcbnew.F_Cu
   seg(b,n,first,(first[0],top[1]),layer); seg(b,n,(first[0],top[1]),(260.0,top[1]),layer)
   seg(b,n,(260.0,top[1]),(outx,top[1]),layer); seg(b,n,(outx,top[1]),(outx,landing[1]),layer); seg(b,n,(outx,landing[1]),landing,layer)
   if suffix.startswith('CM5_USB3_RX_'): via(b,n,landing)
   seg(b,n,landing,d,pcbnew.F_Cu)
   continue
  if USB_VERTICAL:
   # Pair-aware vertical-entry experiment: RX approaches the left side of
   # U7 from above on B.Cu, while TX approaches the right side from below
   # on F.Cu.  The long pair corridors are therefore disjoint from the
   # SATA island and from each other.
   first={'CM5_USB3_RX_N':(85.0,103.9),'CM5_USB3_RX_P':(88.0,104.3),
          'CM5_USB3_TX_N':(90.0,106.3),'CM5_USB3_TX_P':(93.0,106.7)}[suffix]
   lane_y={'CM5_USB3_RX_N':80.0,'CM5_USB3_RX_P':82.0,
           'CM5_USB3_TX_N':152.0,'CM5_USB3_TX_P':150.0}[suffix]
   outx={'CM5_USB3_RX_N':295.0,'CM5_USB3_RX_P':296.0,
         'CM5_USB3_TX_N':297.0,'CM5_USB3_TX_P':298.0}[suffix]
   landing={'CM5_USB3_RX_N':(285.0,104.0),'CM5_USB3_RX_P':(286.0,105.0),
            'CM5_USB3_TX_N':(287.0,115.0),'CM5_USB3_TX_P':(288.0,116.0)}[suffix]
   launch=(71.2,s[1]); seg(b,n,s,launch); seg(b,n,launch,first)
   is_rx=suffix.startswith('CM5_USB3_RX_')
   if is_rx: via(b,n,first)
   layer=pcbnew.B_Cu if is_rx else pcbnew.F_Cu
   seg(b,n,first,(first[0],lane_y),layer); seg(b,n,(first[0],lane_y),(outx,lane_y),layer)
   seg(b,n,(outx,lane_y),(outx,landing[1]),layer); seg(b,n,(outx,landing[1]),landing,layer)
   if is_rx: via(b,n,landing)
   seg(b,n,landing,d,pcbnew.F_Cu)
   continue
  seg(b,n,s,(start[0],s[1])); seg(b,n,(start[0],s[1]),start); via(b,n,start); seg(b,n,start,far,pcbnew.B_Cu)
  # The rotated U7 USB pads share a continuous bottom row.  Do not run a
  # same-layer horizontal track through that row; use a distinct B.Cu lane
  # and one ordinary via directly below each live destination pad.
  _i=['CM5_USB3_RX_N','CM5_USB3_RX_P','CM5_USB3_TX_N','CM5_USB3_TX_P'].index(suffix)
  landing=([(286.0,112.0),(287.5,114.5),(289.0,117.0),(290.5,119.5)][_i] if USB_EAST else [(276.0,112.0),(277.5,114.5),(280.0,117.0),(285.5,119.5)][_i])
  seg(b,n,far,landing,pcbnew.B_Cu); via(b,n,landing)
  dog=(d[0],landing[1]-1.0); seg(b,n,landing,dog,pcbnew.F_Cu); seg(b,n,dog,d,pcbnew.F_Cu)
 # SATA split capacitors.  Pair lanes are layer-separated after live pad
 # escapes; each transition is outside an SMD pad field.
 sata=(('BRIDGE_SATA_TX_P','57','1','C30',pcbnew.F_Cu,(224,96)),
       ('BRIDGE_SATA_TX_N','56','2','C31',pcbnew.B_Cu,(223,99)),
       ('BRIDGE_SATA_RX_P','60','3','C32',pcbnew.F_Cu,(216,103)),
       ('BRIDGE_SATA_RX_N','59','4','C33',pcbnew.B_Cu,(217,105)))
 for bn,upn,jn,cr,layer,esc in sata:
  if SKIP_SATA or CLOCK_ONLY:
   continue
  bridge=N['/STORAGE/'+bn]; socket=N['/STORAGE/'+bn.replace('BRIDGE_SATA_','SATA_M2_')]
  cp={str(p.GetNumber()):pos(p) for p in caps[cr].Pads()}; a=U[upn]; z=J[jn]
  setpad(pad(caps[cr],'1'),socket); setpad(pad(caps[cr],'2'),bridge); setpad(pad(j,jn),socket); setpad(pad(u,upn),bridge)
  if SATA270:
   # Never start a B.Cu segment directly on an SMD pad.  Use a short
   # F.Cu dogbone and an ordinary through-via outside the capacitor pad.
   cap_via = (cp['2'][0]+1.0, cp['2'][1])
   if bn in ('BRIDGE_SATA_TX_P','BRIDGE_SATA_RX_P'):
    if bn == 'BRIDGE_SATA_RX_P':
     e=(a[0]+3.0,a[1]); seg(b,bridge,a,e,pcbnew.F_Cu); via(b,bridge,e); seg(b,bridge,e,cap_via,pcbnew.B_Cu); via(b,bridge,cap_via); seg(b,bridge,cap_via,cp['2'],pcbnew.F_Cu)
    else:
     seg(b,bridge,a,cp['2'],pcbnew.F_Cu)
   else:
    if bn == 'BRIDGE_SATA_RX_N':
     seg(b,bridge,a,cp['2'],pcbnew.F_Cu)
    else:
     e=(a[0]-3.0,a[1]-1.0)
     seg(b,bridge,a,e,pcbnew.F_Cu); via(b,bridge,e); seg(b,bridge,e,cap_via,pcbnew.B_Cu); via(b,bridge,cap_via); seg(b,bridge,cap_via,cp['2'],pcbnew.F_Cu)
   # Keep each SATA pair on one signal layer.  The positive lane uses the
   # right-hand corridor and the negative lane the left-hand corridor; the
   # two pairs are assigned to opposite layers so the alternating M.2 pad
   # columns do not force a same-layer crossing.
   if bn == 'BRIDGE_SATA_TX_P':
    p=(235.0,110.0); seg(b,socket,cp['1'],p,pcbnew.F_Cu); seg(b,socket,p,(235.0,129.0),pcbnew.F_Cu); seg(b,socket,(235.0,129.0),(208.0,129.0),pcbnew.F_Cu); seg(b,socket,(208.0,129.0),(208.0,130.75),pcbnew.F_Cu); seg(b,socket,(208.0,130.75),z,pcbnew.F_Cu)
   elif bn == 'BRIDGE_SATA_TX_N':
    p=(190.0,108.0); seg(b,socket,cp['1'],p,pcbnew.F_Cu); seg(b,socket,p,(190.0,131.0),pcbnew.F_Cu); seg(b,socket,(190.0,131.0),z,pcbnew.F_Cu)
   elif bn == 'BRIDGE_SATA_RX_P':
    p=(238.5,cp['1'][1]); seg(b,socket,cp['1'],p,pcbnew.F_Cu); via(b,socket,p); m=(215.0,p[1]); seg(b,socket,p,m,pcbnew.B_Cu); q=(215.0,131.25); seg(b,socket,m,q,pcbnew.B_Cu); via(b,socket,q); seg(b,socket,q,z,pcbnew.F_Cu)
   else:
    p=(238.5,cp['1'][1]); seg(b,socket,cp['1'],p,pcbnew.F_Cu); via(b,socket,p); m=(210.0,p[1]); seg(b,socket,p,m,pcbnew.B_Cu); q=(210.0,132.5); seg(b,socket,m,q,pcbnew.B_Cu); r=(190.0,132.5); seg(b,socket,q,r,pcbnew.B_Cu); via(b,socket,r); seg(b,socket,r,(190.0,131.5),pcbnew.F_Cu); seg(b,socket,(190.0,131.5),z,pcbnew.F_Cu)
   continue
  if u.GetOrientationDegrees() == -90.0 and j.GetOrientationDegrees() == 90.0:
   # Rot270 U7 exposes SATA on a single west-facing row.  Use live pad
   # coordinates and a pair-per-layer monotonic launch to the left-column
   # M.2 pads; the two pairs never share a signal layer.
   if bn == 'BRIDGE_SATA_TX_P':
    e=(a[0]-3,a[1]); seg(b,bridge,a,e); seg(b,bridge,e,cp['2'])
   elif bn == 'BRIDGE_SATA_TX_N':
    e=(a[0]-2,a[1]-1.0); via(b,bridge,e); seg(b,bridge,a,e); seg(b,bridge,e,cp['2'],pcbnew.B_Cu)
   elif bn == 'BRIDGE_SATA_RX_P':
    e=(a[0]-5,a[1]+2.0); via(b,bridge,e); seg(b,bridge,a,e); seg(b,bridge,e,cp['2'],pcbnew.B_Cu)
   else:
    e=(a[0]-4,a[1]+4.0); via(b,bridge,e); seg(b,bridge,a,e); seg(b,bridge,e,cp['2'],pcbnew.B_Cu)
   # Legal horizontal M.2 orientation: independent live lanes approach the
   # rotated socket from four disjoint corridors around U7.
   if bn == 'BRIDGE_SATA_TX_P':
    q=(235.0,96.0); seg(b,socket,cp['1'],q,pcbnew.F_Cu); r=(215.0,96.0); seg(b,socket,q,r,pcbnew.F_Cu); seg(b,socket,r,(r[0],d[1]),pcbnew.F_Cu); seg(b,socket,(r[0],d[1]),d)
   elif bn == 'BRIDGE_SATA_TX_N':
    q=(235.0,100.0); seg(b,socket,cp['1'],q,pcbnew.F_Cu); via(b,socket,q); r=(210.0,100.0); seg(b,socket,q,r,pcbnew.B_Cu); via(b,socket,r); seg(b,socket,r,(r[0],d[1]+6),pcbnew.B_Cu); via(b,socket,(r[0],d[1]+6)); seg(b,socket,(r[0],d[1]+6),d)
   elif bn == 'BRIDGE_SATA_RX_P':
    q=(235.0,108.0); seg(b,socket,cp['1'],q,pcbnew.F_Cu); via(b,socket,q); r=(205.0,108.0); seg(b,socket,q,r,pcbnew.B_Cu); via(b,socket,r); seg(b,socket,r,(r[0],d[1]-5),pcbnew.B_Cu); via(b,socket,(r[0],d[1]-5)); seg(b,socket,(r[0],d[1]-5),d)
   else:
    q=(235.0,112.0); seg(b,socket,cp['1'],q,pcbnew.F_Cu); via(b,socket,q); r=(215.0,112.0); seg(b,socket,q,r,pcbnew.B_Cu); via(b,socket,r); seg(b,socket,r,(r[0],d[1]+10),pcbnew.B_Cu); via(b,socket,(r[0],d[1]+10)); seg(b,socket,(r[0],d[1]+10),d)
  elif layer==pcbnew.F_Cu:
   seg(b,bridge,a,(a[0]-2,a[1])); seg(b,bridge,(a[0]-2,a[1]),cp['2'])
   seg(b,socket,cp['1'],(230,cp['1'][1])); seg(b,socket,(230,cp['1'][1]),(230,z[1])); seg(b,socket,(230,z[1]),z)
  else:
   e=(a[0]-3,a[1]); via(b,bridge,e); seg(b,bridge,a,e,pcbnew.F_Cu); seg(b,bridge,e,cp['2'],pcbnew.B_Cu)
   e2=(232,cp['1'][1]); via(b,socket,e2); seg(b,socket,cp['1'],e2,pcbnew.F_Cu); seg(b,socket,e2,(232,z[1]),pcbnew.B_Cu); via(b,socket,(232,z[1])); seg(b,socket,(232,z[1]),z)
 # Clock net assignments and live endpoint routes.  VSSOSC is a private
 # return with ordinary through-vias beside the low-profile support parts.
 if SKIP_CLOCK:
  b.Save(str(OUT)); print(OUT); return
 maps={'Y1':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC','3':'/STORAGE/BRIDGE_XO','4':'/STORAGE/BRIDGE_VSSOSC'},
       'R23':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_XO'},'C42':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC'},'C43':{'1':'/STORAGE/BRIDGE_XO','2':'/STORAGE/BRIDGE_VSSOSC'}}
 for ref,m in maps.items():
  for p in b.FindFootprintByReference(ref).Pads(): setpad(p,N[m[str(p.GetNumber())]])
 for pn,nm in (('52','/STORAGE/BRIDGE_XI'),('53','/STORAGE/BRIDGE_VSSOSC'),('54','/STORAGE/BRIDGE_XO')): setpad(pad(u,pn),N[nm])
 Y={str(p.GetNumber()):pos(p) for p in b.FindFootprintByReference('Y1').Pads()}; R23={str(p.GetNumber()):pos(p) for p in b.FindFootprintByReference('R23').Pads()}; C42={str(p.GetNumber()):pos(p) for p in b.FindFootprintByReference('C42').Pads()}; C43={str(p.GetNumber()):pos(p) for p in b.FindFootprintByReference('C43').Pads()}
 xi,xo,vs=N['/STORAGE/BRIDGE_XI'],N['/STORAGE/BRIDGE_XO'],N['/STORAGE/BRIDGE_VSSOSC']
 # Live-endpoint clock topology: XI is a short F.Cu local star; XO is
 # isolated onto B.Cu through ordinary offset vias, so the two oscillator
 # nets cannot cross in the dense support-pad region.
 seg(b,xi,U['52'],(273.5,103.5)); seg(b,xi,(273.5,103.5),(271.5,103.5)); seg(b,xi,(271.5,103.5),R23['1'])
 seg(b,xi,Y['1'],(268.0,96.0)); seg(b,xi,(268.0,96.0),R23['1'])
 seg(b,xi,C42['1'],(271.5,96.0)); seg(b,xi,(271.5,96.0),R23['1'])
 for p,q in ((U['54'],(278.0,103.0)),(Y['3'],(269.5,100.5)),(R23['2'],(273.5,99.5)),(C43['1'],(275.5,96.5))):
  seg(b,xo,p,q); via(b,xo,q)
 for q in ((278.0,103.0),(269.5,100.5),(273.5,99.5),(275.5,96.5)):
  seg(b,xo,q,(q[0],90.0),pcbnew.B_Cu)
 seg(b,xo,(269.5,90.0),(278.0,90.0),pcbnew.B_Cu)
 # Return vias are deliberately offset from every SMD pad (no via-in-pad).
 for p,q in ((U['53'],(277.0,104.5)),(Y['2'],(264.0,100.0)),(Y['4'],(270.5,96.0)),(C42['2'],(274.5,92.5)),(C43['2'],(279.5,98.0))):
  seg(b,vs,p,q); via(b,vs,q)
 # Private oscillator return is joined on B.Cu outside the signal stubs.
 for q in ((277.0,104.5),(264.0,100.0),(270.5,96.0),(274.5,92.5),(279.5,98.0)):
  seg(b,vs,q,(q[0],106.0),pcbnew.B_Cu)
 seg(b,vs,(264.0,106.0),(279.5,106.0),pcbnew.B_Cu)
 # FREQSEL0/1 and VDDIO high on the local 3V3 net; local short fanout.
 v33=b.FindNet('/STORAGE/BRIDGE_3V3')
 for pn in ('24','30','31'): setpad(pad(u,pn),v33)
 seg(b,v33,U['24'],(287,106)); seg(b,v33,(287,106),U['30']); seg(b,v33,(287,106),U['31'])
 b.Save(str(OUT))
 # Remove only known donor duplicate net fields from U7 pads 5-12 in the
 # serialized footprint; this is the same deterministic cleanup used by the
 # coordinated authoring path.
 text=Path(OUT).read_text(); us=text.index('(footprint "TUSB9261IPVP_HTQFP64"'); ue=text.index('\n\t(footprint ',us+1); utext=text[us:ue]
 for pn in range(5,13):
  m=re.search(r'(?ms)(\n\t\t\(pad "'+str(pn)+r'".*?)(?=\n\t\t\(pad |\n\t\))',utext)
  if m: utext=utext[:m.start(1)]+re.sub(r'\n\t\t\t\(net "[^"]*"\)','',m.group(1))+utext[m.end(1):]
 Path(OUT).write_text(text[:us]+utext+text[ue:]); print(OUT)
if __name__=='__main__': main()
