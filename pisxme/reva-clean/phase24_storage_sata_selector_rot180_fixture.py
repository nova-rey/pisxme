"""Disposable SATA selector fixture with U13 rotated for physical signal flow.

This experiment keeps the corrected source nets and changes only the local
U13 orientation/route.  Port B faces the bridge/capacitor row; Port A faces
the M-key socket.  It is not production PCB authority until native DRC and
pair checks pass.
"""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'PHASE24_STORAGE_SELECTOR_AUTHORITY_PLACEMENT_20260907.kicad_pcb'
OUT=ROOT/'PHASE24_STORAGE_SATA_SELECTOR_ROT180_20260907.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=pcbnew.FromMM(.20)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):
 q=p.GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def net(b,n):
 for x in (n,'/STORAGE/'+n):
  q=b.FindNet(x)
  if q:return q
 raise RuntimeError(n)
def track(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def path(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):track(b,n,a,z,l)
def via(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)

b=pcbnew.LoadBoard(str(BASE))
keep={'U7','U13','J3','C30','C31','C32','C33'}
for t in list(b.GetTracks()):b.RemoveNative(t)
for z in list(b.Zones()):b.RemoveNative(z)
for f in list(b.GetFootprints()):
 if f.GetReference() not in keep:b.RemoveNative(f)
u13=b.FindFootprintByReference('U13');u13.SetOrientationDegrees(180)
# Match the reversed Port-B pad order after the 180-degree turn.
for r,(x,y) in {'C30':(104,132),'C31':(104,128),'C32':(104,120),'C33':(104,116)}.items():
 f=b.FindFootprintByReference(r);f.SetPosition(V(x,y));f.SetOrientationDegrees(180)

# U7 edge escape: short F.Cu dogbones, then ordinary vias and separated B.Cu
# corridors.  The capacitor endpoints are obtained after their transforms.
esc={
 'TXP':('57','C30',(95.8,128.7),(96.5,129.4)),
 'TXN':('56','C31',(96.2,128.7),(97.1,129.4)),
 'RXP':('60','C32',(94.6,128.7),(93.7,129.4)),
 'RXN':('59','C33',(95.0,128.7),(94.3,130.0)),}
for k,(pin,cap,dog,sv) in esc.items():
 bridge={'TXP':'BRIDGE_SATA_TX_P','TXN':'BRIDGE_SATA_TX_N','RXP':'BRIDGE_SATA_RX_P','RXN':'BRIDGE_SATA_RX_N'}[k]
 n=net(b,bridge);src=xy(pad(b,'U7',pin));dst=xy(pad(b,cap,'2'))
 path(b,n,[src,dog,sv],F);via(b,n,sv);path(b,n,[sv,(100,sv[1]),dst],B);via(b,n,dst)

# Port-B path.  The reordered capacitor row and rotated U13 now have the same
# physical order, so these monotonic B.Cu corridors do not need to weave.
portb={'TXP':('C30','38',(160,153.2),(176,153.2)),
       'TXN':('C31','37',(162,152.8),(176,152.8)),
       'RXP':('C32','36',(164,152.4),(176,152.4)),
       'RXN':('C33','35',(166,152.0),(176,152.0))}
for k,(cap,upin,turn,vp) in portb.items():
 sata={'TXP':'TUSB_SATA_TXP','TXN':'TUSB_SATA_TXN','RXP':'TUSB_SATA_RXP','RXN':'TUSB_SATA_RXN'}[k]
 n=net(b,sata);src=xy(pad(b,cap,'1'));dst=xy(pad(b,'U13',upin))
 via(b,n,src);path(b,n,[src,(120,turn[1]),turn,vp],B);via(b,n,vp);path(b,n,[vp,dst],F)

# Port-A launch.  TX uses B.Cu and RX uses F.Cu with separate outside-package
# target vias; all final dogbones are sourced from native J3 pad positions.
launch={'TXP':('2','49',B,(188,146)),
        'TXN':('3','47',B,(190,144)),
        'RXN':('6','41',F,(194,158)),
        'RXP':('7','43',F,(196,156))}
names={'TXP':'M2_SATA_A_P_PCIE_TXP0','TXN':'M2_SATA_A_N_PCIE_TXN0',
       'RXN':'M2_SATA_B_P_PCIE_RXN0','RXP':'M2_SATA_B_N_PCIE_RXP0'}
for k,(up,jp,l,turn) in launch.items():
 n=net(b,names[k]);src=xy(pad(b,'U13',up));dst=xy(pad(b,'J3',jp))
 if l==B:
  sv=(185,turn[1]);path(b,n,[src,(183,src[1]),sv],F);via(b,n,sv);via(b,n,turn);path(b,n,[sv,turn],B);via(b,n,turn);path(b,n,[turn,dst],F)
 else:path(b,n,[src,turn,dst],F)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
