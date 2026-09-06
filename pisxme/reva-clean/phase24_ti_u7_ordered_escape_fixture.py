#!/usr/bin/env python3
"""Disposable ordered USB3/SATA escape for the authoritative TI U7 field."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_TI_STORAGE_ISOLATED_HS.kicad_pcb'
OUT=R/'PHASE24_TI_STORAGE_ORDERED_ESCAPE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=pcbnew.FromMM(.15)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def P(b,r,n): return FPS[r].FindPadByNumber(str(n))
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def net(b,n):
    q=b.FindNet(n)
    if q is None: raise RuntimeError(f'missing net {n}')
    return q
def tr(b,n,a,z,l):
    if a==z:return
    q=pcbnew.PCB_TRACK(b);q.SetStart(V(*a));q.SetEnd(V(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);b.Add(q)
def via(b,n,p):
    q=pcbnew.PCB_VIA(b);q.SetPosition(V(*p));q.SetWidth(pcbnew.FromMM(.5));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);b.Add(q)
def path(b,n,pts,l):
    for a,z in zip(pts,pts[1:]):tr(b,n,a,z,l)

b=pcbnew.LoadBoard(str(BASE))
FPS={f.GetReference():f for f in b.GetFootprints()}
POS={(r,str(p.GetNumber())):(pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y))
     for r,f in FPS.items() for p in f.Pads()}
# Normalize only the authoritative four CM5 source pads; this fixture never
# creates a net from expected connectivity.
for name,jp,_ in [('CM5_USB3_RX_N','128','42'),('CM5_USB3_RX_P','130','43'),('CM5_USB3_TX_N','140','45'),('CM5_USB3_TX_P','142','46')]:
    P(b,'J7',jp).SetNet(net(b,name))
# Ordered coupling-capacitor row: RX_P, RX_N, TX_P, TX_N.  Pad 2 is the
# bridge side because these native footprints are oriented 180 degrees.
row={'RX_P':('C32',124.),'RX_N':('C33',128.),'TX_P':('C30',132.),'TX_N':('C31',136.)}
for ref,x in row.values(): FPS[ref].SetPosition(V(x,150.))
# Keep low-speed oscillator/decoupling support physically present but outside
# the high-speed escape corridors.  This represents a later placement choice
# (including underside placement), not a component or net substitution.
for ref in ('Y1','R23','C42','C43','C16','C17','C19'):
    if ref in FPS:
        p=FPS[ref].GetPosition(); FPS[ref].SetPosition(V(p.x/1e6+75.,p.y/1e6+25.))
for ref,_x in row.values():
    for p in FPS[ref].Pads():
        POS[(ref,str(p.GetNumber()))]=xy(p)
for t in list(b.GetTracks()): b.RemoveNative(t)

# CM5 source -> U7.  Each source pad gets an F.Cu dogbone and an ordinary
# through-via, then a dedicated B.Cu lane; each U7 arrival is a separate F.Cu
# dogbone outside the 8.5 mm TI land pattern.
usb=[('RX_N','128','42',103.9,100.),('RX_P','130','43',104.3,102.),
     ('TX_N','140','45',106.3,104.),('TX_P','142','46',106.7,106.)]
for k,jp,up,sy,ly in usb:
    n=net(b,'CM5_USB3_'+k);src=POS[('J7',jp)];dst=POS[('U7',up)]
    sv=(74.,ly); ev={'RX_N':(112.,dst[1]),'RX_P':(113.,dst[1]),
                     'TX_N':(114.,dst[1]),'TX_P':(115.,dst[1])}[k]
    path(b,n,[src,(72.,src[1]),sv],F);via(b,n,sv);path(b,n,[sv,ev],B);via(b,n,ev);path(b,n,[ev,dst],F)

# U7 SATA bottom row -> coupling capacitors, preserving physical pair order.
# RX uses B.Cu and TX uses F.Cu after ordinary dogbone transitions.  The via
# positions are deliberately separated from the 0.4 mm-pitch pad row.
bridge_via={'RX_P':(114.,145.5),'RX_N':(116.,146.5),
            'TX_P':(118.,147.5),'TX_N':(120.,148.5)}
for k,(ref,x) in row.items():
    up={'RX_P':'60','RX_N':'59','TX_P':'57','TX_N':'56'}[k]
    n=net(b,'/STORAGE/BRIDGE_SATA_'+k);src=POS[('U7',up)];dst=POS[(ref,'2')]
    vp=bridge_via[k]; layer=B if k.startswith('RX_') else F
    path(b,n,[src,(src[0],vp[1]),vp],F);via(b,n,vp)
    if layer == B:
        ep=(dst[0]-1.5,dst[1]); path(b,n,[vp,(ep[0],vp[1]),ep],B);via(b,n,ep);path(b,n,[ep,dst],F)
    else:
        path(b,n,[vp,(dst[0],vp[1]),dst],F)

# Capacitor output -> J3.  Use two monotonic F.Cu groups, with the left and
# right M.2 launches kept in their native pair order.
socket={
 'RX_P':('C32','1','J3','3',[(124.5,150.),(124.5,156.),(130.,156.),(138.,137.)]),
 'TX_P':('C30','1','J3','1',[(132.5,150.),(132.5,158.),(136.,158.),(139.,138.)]),
 'RX_N':('C33','1','J3','4',[(128.5,150.),(130.5,150.),(144.,156.),(146.,136.)]),
 'TX_N':('C31','1','J3','2',[(136.5,150.),(138.5,150.),(145.,158.),(146.,138.)]),
}
for k,(cr,cp,jr,jp,pts) in socket.items():
    n=net(b,'/STORAGE/SATA_M2_'+k);dst=POS[(jr,jp)]
    if k.endswith('_N'):
        # Pad 1 is F.Cu SMD: dogbone to an ordinary via, B.Cu corridor,
        # then an ordinary via outside the M.2 pad field.
        start=pts[0]; sv=(start[0]+1.5,start[1]); ev=pts[-1]
        path(b,n,[start,sv],F);via(b,n,sv);path(b,n,[sv,ev],B);via(b,n,ev);path(b,n,[ev,dst],F)
    else:
        path(b,n,pts[:-1]+[dst],F)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
