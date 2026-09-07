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
 'TXP':(B,[(104,116),(140,108),(184,108),(184,145.8)],(184,145.8)),
 'TXN':(B,[(104,132),(140,104),(185,104),(185,145.2)],(185,145.2)),
 'RXP':(B,[(104,120),(140,156),(184,156),(184,154)],(184,154)),
 'RXN':(B,[(104,128),(140,160),(185,160),(185,155)],(185,155)),}
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
 'TXP':('2','49',B,[(178.5,147.2),(177.3,146.2),(176.2,145.6),(196,130),(220,130),(220,157)]),
 'TXN':('3','47',F,[(178.5,147.6),(177.3,148.8),(176.2,149.8),(196,134),(218,134),(218,157)]),
 'RXN':('6','41',B,[(178.5,148.8),(177.3,150.2),(176.2,151.0),(196,162),(216,162),(216,157)]),
 'RXP':('7','43',F,[(178.5,149.2),(177.3,150.8),(176.2,152.0),(196,158),(214,157)]),}
for k,(up,jp,l,pts) in apaths.items():
 n=net(b, {'TXP':'M2_SATA_A_P_PCIE_TXP0','TXN':'M2_SATA_A_N_PCIE_TXN0','RXN':'M2_SATA_B_P_PCIE_RXN0','RXP':'M2_SATA_B_N_PCIE_RXP0'}[k])
 if l==B:
  path(b,n,pts[:3],F);via(b,n,pts[2]);path(b,n,pts[2:],B);via(b,n,pts[-1]);path(b,n,[pts[-1],pinpos(b,'J3',jp)],F)
 else:path(b,n,[pinpos(b,'U13',up)]+pts[1:]+[pinpos(b,'J3',jp)],F)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
