"""Build a disposable Path-A SATA route through U13's real selector ports."""
from pathlib import Path
import os
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/os.environ.get('PISXME_SELECTOR_BASE','PHASE24_STORAGE_SELECTOR_AUTHORITY_PLACEMENT_20260906.kicad_pcb')
OUT=ROOT/os.environ.get('PISXME_SELECTOR_OUT','PHASE24_STORAGE_SATA_SELECTOR_CORRIDOR_20260906.kicad_pcb')
F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=pcbnew.FromMM(0.20)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def pos(p):
 q=p.GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def net(b,n):
 for x in (n,'/STORAGE/'+n):
  q=b.FindNet(x)
  if q:return q
 raise RuntimeError('missing net '+n)
def seg(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def path(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):seg(b,n,a,z,l)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(V(*p));q.SetWidth(pcbnew.FromMM(.5));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def pinpos(b,r,n): return pos(pad(b,r,n))

b=pcbnew.LoadBoard(str(BASE))
if os.environ.get('PISXME_SELECTOR_MINIMAL')=='1':
 keep={'U7','U13','J3','C30','C31','C32','C33'}
 for t in list(b.GetTracks()): b.RemoveNative(t)
 for z in list(b.Zones()): b.RemoveNative(z)
 for f in list(b.GetFootprints()):
  if f.GetReference() not in keep: b.RemoveNative(f)
all_sata=('BRIDGE_SATA_','TUSB_SATA_','M2_SATA_')
for t in list(b.GetTracks()):
 if any(x in t.GetNetname() for x in all_sata): b.RemoveNative(t)
caps={'TXP':('C30','BRIDGE_SATA_TX_P','TUSB_SATA_TXP','38'),
      'TXN':('C31','BRIDGE_SATA_TX_N','TUSB_SATA_TXN','37'),
      'RXP':('C32','BRIDGE_SATA_RX_P','TUSB_SATA_RXP','36'),
      'RXN':('C33','BRIDGE_SATA_RX_N','TUSB_SATA_RXN','35')}

# Keep the coupling row ordered and source all coordinates from native pads.
for r,(x,y) in {'C30':(103.5,116),'C31':(103.5,132),'C32':(103.5,120),'C33':(103.5,128)}.items():
 f=b.FindFootprintByReference(r);f.SetPosition(V(x,y));f.SetOrientationDegrees(180)

# U7's four SATA pads are a 0.4-mm-pitch edge row.  Escape each pad with a
# short outward F.Cu dogbone before the ordinary through-via; no via is put in
# the pad and no escape crosses a neighboring U7 pad.
u7paths={
 'TXP':([(95.8,127.8),(95.8,128.7),(96.5,129.4)],(96.5,129.4),(99,116)),
 'TXN':([(96.2,127.8),(96.2,128.7),(97.1,129.4)],(97.1,129.4),(98,132)),
 'RXP':([(94.6,127.8),(94.6,128.7),(93.7,129.4)],(93.7,129.4),(97,120)),
 'RXN':([(95.0,127.8),(95.0,128.7),(94.3,130.0)],(94.3,130.0),(96,128)),}
for k,(r,bridge,sata,upin) in caps.items():
 dog,src_via,turn=u7paths[k]
 n=net(b,bridge); cap2=pinpos(b,r,'2')
 path(b,n,dog,F); via(b,n,src_via); path(b,n,[src_via,turn,cap2],B); via(b,n,cap2)

# Capacitor pad 1 to U13 Port B. Each path changes layer away from the pads.
bpaths={
 'TXP':(F,[(103.5,116),(110,116),(110,142)],(177.5,142)),
 'TXN':(B,[(103.5,132),(112,132),(112,140)],(177.5,140)),
 'RXP':(F,[(103.5,120),(108,120),(108,154)],(177.5,154)),
 'RXN':(B,[(103.5,128),(114,128),(114,156)],(177.5,156)),}
for k,(r,bridge,sata,upin) in caps.items():
 n=net(b,sata);l,pts,vp=bpaths[k];pts=[pinpos(b,r,'1')]+pts[1:]
 pts=pts+[vp]
 if l==B:
  via(b,n,pts[0]);path(b,n,pts,B);via(b,n,vp)
 else:
  path(b,n,pts,F);via(b,n,vp)
 path(b,n,[vp,pinpos(b,'U13',upin)],F)

# U13 Port A to M-key lane-0 contacts. RX is a monotonic F.Cu pair; TX is
# deliberately kept on B.Cu until connector-side dogbones to avoid a pad-field
# crossing in this first selector-inclusive fixture.
apaths={
 'TXP':('2','49',B,[(178.5,147.2),(185,147.2),(205,138),(217,138),(222.75,157.5)]),
 'TXN':('3','47',B,[(178.5,147.6),(186,147.6),(204,136),(216,136),(222.25,157.5)]),
 'RXN':('6','41',F,[(178.5,148.8),(190,150),(205,152),(220.75,159.725)]),
 'RXP':('7','43',F,[(178.5,149.2),(190,151),(206,153),(221.25,159.725)]),}
for k,(up,jp,l,pts) in apaths.items():
 n=net(b, {'TXP':'M2_SATA_A_P_PCIE_TXP0','TXN':'M2_SATA_A_N_PCIE_TXN0','RXN':'M2_SATA_B_P_PCIE_RXN0','RXP':'M2_SATA_B_N_PCIE_RXP0'}[k])
 if l==B:
  via(b,n,pts[0]);path(b,n,pts,B);via(b,n,pts[-1]);path(b,n,[pts[-1],pinpos(b,'J3',jp)],F)
 else:path(b,n,[pinpos(b,'U13',up)]+pts[1:],F)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
