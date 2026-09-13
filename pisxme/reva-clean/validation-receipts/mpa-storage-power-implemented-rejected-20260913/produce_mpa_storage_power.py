from pathlib import Path
import pcbnew

R = Path('/workspace/project/pisxme/reva-clean')
BASE = R / 'PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb'
OUT = R / 'PHASE24_MPA_STORAGE_POWER_IMPLEMENTED_CANDIDATE.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(0.20)
WF = pcbnew.FromMM(0.10)

def V(x,y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p):
    q=p.GetPosition(); return pcbnew.ToMM(q.x), pcbnew.ToMM(q.y)
def fp(r):
    f=b.FindFootprintByReference(r)
    if f is None: raise RuntimeError('missing '+r)
    return f
def pad(r,n):
    p=fp(r).FindPadByNumber(str(n))
    if p is None: raise RuntimeError(f'missing {r}.{n}')
    return p
def net(name):
    n=b.FindNet(name)
    if n is None: raise RuntimeError('missing net '+name)
    return n
def seg(n,a,z,layer,width=W):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(width); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def path(n,pts,layer,width=W):
    for a,z in zip(pts,pts[1:]): seg(n,a,z,layer,width)
def via(n,p,width=0.35,drill=0.15):
    v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(width)); v.SetDrill(pcbnew.FromMM(drill)); v.SetLayerPair(F,B)
    v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
def pxy(r,n): return xy(pad(r,n))

b=pcbnew.LoadBoard(str(BASE))
if b is None: raise SystemExit('cannot load base')

# Binding MPA placement. No other footprint is moved.
for ref,(x,y,rot) in {
 'U13':(180,135,180), 'C30':(103.5,116,180), 'C32':(103.5,120,180),
 'C33':(103.5,128,180), 'C31':(103.5,132,180), 'F2':(18,145,None), 'D2':(35,145,None)
}.items():
    f=fp(ref); f.SetPosition(V(x,y));
    if rot is not None: f.SetOrientationDegrees(rot)

# Four U7-to-coupling-capacitor branches. U7 pad-field launches are 0.10 mm
# F.Cu; transitions occur outside the pad field and each cap is approached via
# a separate B.Cu lane and a local F.Cu landing.
for name,up,cap,src,dst in [
 ('BRIDGE_SATA_TX_P','57','C30',(95.8,129.3),(102.0,116.0)),
 ('BRIDGE_SATA_TX_N','56','C31',(96.2,129.8),(102.0,132.0)),
 ('BRIDGE_SATA_RX_P','60','C32',(94.6,130.3),(102.0,120.0)),
 ('BRIDGE_SATA_RX_N','59','C33',(95.0,130.8),(102.0,128.0)),
]:
    n=net(name); p=pxy('U7',up); q=pxy(cap,'2')
    seg(n,p,src,F,WF); via(n,src)
    # separated local lanes around the relocated capacitor column
    if name.endswith('TX_P'): pts=[src,(100.0,129.3),(100.0,116.0),dst]
    elif name.endswith('TX_N'): pts=[src,(101.0,129.8),(101.0,136.0),(102.0,132.0)]
    elif name.endswith('RX_P'): pts=[src,(99.0,130.3),(99.0,120.0),dst]
    else: pts=[src,(98.0,130.8),(98.0,128.0),dst]
    path(n,pts,B,W); via(n,dst); seg(n,dst,q,F,WF)

# Capacitor-to-U13 Port-B. TX is carried on separated upper F.Cu channels;
# RX is carried on separated lower B.Cu channels below U11/U12.
portb=[
 ('TUSB_SATA_TXP','C30','38',(104.0,113.0),(176.0,113.0)),
 ('TUSB_SATA_TXN','C31','37',(104.0,115.0),(176.0,115.0)),
 ('TUSB_SATA_RXP','C32','36',(104.0,145.0),(176.0,145.0)),
 ('TUSB_SATA_RXN','C33','35',(104.0,147.0),(176.0,147.0)),
]
for name,cap,up,sv,ev in portb:
    n=net(name); src=pxy(cap,'1'); dst=pxy('U13',up)
    # local cap landing and U13 horizontal fine escape
    seg(n,src,(104.0,sv[1]),F,WF); via(n,sv)
    path(n,[sv,(120.0,sv[1]),(160.0,sv[1]),ev],F if 'TX' in name else B,W)
    via(n,ev); seg(n,ev,dst,F,WF)

# U13 Port-A to J3 ordered corridors. J3 contacts are through pads and are
# approached on B.Cu after the U13 local F.Cu escape.
port_a=[
 ('M2_SATA_A_P_PCIE_TXP0','2','49',(184.0,145.0),(207.0,155.0)),
 ('M2_SATA_A_N_PCIE_TXN0','3','47',(184.0,147.0),(207.0,156.0)),
 ('M2_SATA_B_P_PCIE_RXN0','6','41',(184.0,153.0),(207.0,157.0)),
 ('M2_SATA_B_N_PCIE_RXP0','7','43',(184.0,155.0),(207.0,158.0)),
]
for name,up,jp,sv,ev in port_a:
    n=net(name); src=pxy('U13',up); dst=pxy('J3',jp)
    seg(n,src,sv,F,WF); via(n,sv)
    path(n,[sv,(195.0,sv[1]),(203.0,ev[1]),ev],B,W)
    # J3 is approached through a via outside its keepout, then landed on F.Cu.
    j3v=(208.0,dst[1]); via(n,j3v); seg(n,ev,j3v,B,W); seg(n,j3v,dst,F,WF)

# STORAGE_SEL has one shared B.Cu corridor with a branch via at U13.9 and a
# lower/east handoff to U14.4. AUTO_PEDET follows the same east/lower intent.
n=net('STORAGE_SEL')
u12=pxy('U12','9'); u13=pxy('U13','9'); u14=pxy('U14','4')
seg(n,u12,(161.0,135.0),F,WF); via(n,(161.0,145.0)); seg(n,(161.0,135.0),(161.0,145.0),F,WF)
via(n,(184.0,145.0)); seg(n,(161.0,145.0),(184.0,145.0),B,W); seg(n,(184.0,145.0),u13,F,WF)
path(n,[(184.0,145.0),(203.0,145.0),(207.0,150.95)],B,W); via(n,(207.0,150.95)); seg(n,(207.0,150.95),u14,F,WF)
n=net('AUTO_PEDET'); src=pxy('U14','2'); dst=pxy('J3','69')
seg(n,src,(207.0,149.0),F,WF); via(n,(207.0,149.0)); path(n,[(207.0,149.0),(214.0,149.0),(218.0,155.0),(224.0,155.0)],B,W); via(n,(224.0,155.0)); seg(n,(224.0,155.0),dst,F,WF)

# Branch-B input: J6 to relocated F2 input field on the outer-left corridor;
# all four F2 input pads are then joined locally. Fused output uses a separate
# west-side corridor to Q2/U2 and the relocated D2.
n=net('12V_IN_B'); j6=pxy('J6','1'); f21=pxy('F2','1'); u23=pxy('U2','3'); c42=pxy('C4','2')
via(n,(7.0,60.0)); seg(n,j6,(7.0,60.0),F,W); path(n,[(7.0,60.0),(6.0,100.0),(6.0,140.0),(11.6,143.75)],B,W); seg(n,(11.6,143.75),f21,B,W)
for a in [('F2','1'),('F2','2'),('F2','3'),('F2','4')]:
    if a[1]!='1': seg(n,pxy('F2',a[1]),f21,F,W)
via(n,(16.5,100.0)); path(n,[(11.6,143.75),(16.5,135.0),(16.5,100.0)],B,W); seg(n,(16.5,100.0),u23,B,W)
seg(n,u23,(15.8,96.0),F,W); seg(n,(15.8,96.0),c42,F,W)

n=net('FUSED_12V_B'); f25=pxy('F2','5'); q21=pxy('Q2','1'); u26=pxy('U2','6'); d21=pxy('D2','1')
for num in ['6','7','8']: seg(n,pxy('F2',num),f25,F,W)
seg(n,f25,d21,F,W)
via(n,(27.0,140.0)); seg(n,f25,(27.0,140.0),F,W); path(n,[(27.0,140.0),(27.0,103.0),(7.46,103.0),(7.46,108.0)],B,W); seg(n,(7.46,108.0),q21,B,W)
via(n,(24.0,101.0)); path(n,[(7.46,108.0),(24.0,108.0),(24.0,101.0)],B,W); seg(n,(24.0,101.0),u26,B,W)

b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
