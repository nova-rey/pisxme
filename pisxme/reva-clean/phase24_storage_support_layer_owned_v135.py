"""V135: package-aware mixed-layer USB3 support escape.

This disposable experiment keeps the validated V127 CM5/U12 escape and
authors the U11 capacitor and U12 bridge-side support from real pads.  The
four dense support corridors leave the QFN fields on F.Cu, cross the open
storage acreage on B.Cu, and return outside the U12 right pad column.
"""
from pathlib import Path
import sys
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'PHASE24_STORAGE_USB3_R80_RELOCATED_V127.kicad_pcb'
OUT = R / 'PHASE24_STORAGE_SUPPORT_LAYER_OWNED_V135.kicad_pcb'
if len(sys.argv) > 1: BASE = R / sys.argv[1]
if len(sys.argv) > 2: OUT = R / sys.argv[2]
TARGET_STAGGER = len(sys.argv) > 3 and sys.argv[3] == 'local_target_stagger'
RX_FCU = len(sys.argv) > 3 and sys.argv[3] == 'local_target_rx_fcu'
RX_FAR = len(sys.argv) > 3 and sys.argv[3] == 'local_target_rx_far'
CAP_CLEAR = len(sys.argv) > 3 and sys.argv[3] == 'integrated_cap_clear'
RX_FAR = RX_FAR or CAP_CLEAR
LOCAL_ONLY = len(sys.argv) > 3 and sys.argv[3] in {'local', 'local_rot180', 'local_target_stagger', 'local_target_rx_fcu', 'local_target_rx_far'}
ROTATE_U12 = len(sys.argv) > 3 and sys.argv[3] == 'local_rot180'
ROTATE_U12_90 = len(sys.argv) > 3 and sys.argv[3] == 'local_rot90'
LOCAL_ONLY = LOCAL_ONLY or ROTATE_U12_90
LOCAL_ONLY = LOCAL_ONLY or (len(sys.argv) > 4 and sys.argv[4] == 'local')
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.13208)

def V(x, y): return pcbnew.VECTOR2I_MM(float(x), float(y))
def xy(p):
    p = p.GetPosition() if hasattr(p, 'GetPosition') else p
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def pad(b, ref, number): return b.FindFootprintByReference(ref).FindPadByNumber(str(number))
def leaf(n): return n.rsplit('/', 1)[-1]

def net(b, name):
    return b.FindNet(name) or b.FindNet('/STORAGE/' + name)

def seg(b, n, a, z, layer):
    if a == z: return
    q = pcbnew.PCB_TRACK(b); q.SetStart(V(*a)); q.SetEnd(V(*z)); q.SetLayer(layer)
    q.SetWidth(W); q.SetNet(n); b.Add(q)

def via(b, n, p):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F, B); q.SetNet(n); b.Add(q)

b = pcbnew.LoadBoard(str(BASE))
owned = {'USB_TXP1','USB_TXN1','JMS_USB3_TXP','JMS_USB3_TXN','USB_RXP1','USB_RXN1'}
if ROTATE_U12:
    b.FindFootprintByReference('U12').SetOrientationDegrees(180)
elif ROTATE_U12_90:
    b.FindFootprintByReference('U12').SetOrientationDegrees(90)
if LOCAL_ONLY:
    for t in list(b.GetTracks()): b.RemoveNative(t)
    for z in list(b.Zones()): b.RemoveNative(z)
    for f in list(b.GetFootprints()):
        if f.GetReference() not in {'U11','U12','C86','C87'}: b.RemoveNative(f)
for t in list(b.GetTracks()):
    if leaf(t.GetNetname()) in owned: b.RemoveNative(t)

# Put the series capacitors immediately below their actual U11 TX pads.  The
# 90-degree orientation makes each pad's two terminals vertical and keeps the
# source-to-cap legs monotonic in the open south escape.
cap_positions = {'C86': (146.0, 155.0), 'C87': (146.0, 165.0)} if CAP_CLEAR else {'C86': (146.0, 160.0), 'C87': (146.0, 165.0)}
for ref, pos in cap_positions.items():
    f = b.FindFootprintByReference(ref)
    if f is None: raise RuntimeError('missing ' + ref)
    f.SetPosition(V(*pos)); f.SetOrientationDegrees(0)
    if LOCAL_ONLY:
        # The disposable support fixture is judged with native DRC.  Its
        # moved capacitor reference silk lands on the tiny pad aperture;
        # remove only that fixture-local graphic, leaving the library and
        # production footprint untouched.
        for g in list(f.GraphicalItems()):
            if g.GetLayer() == pcbnew.F_SilkS:
                f.RemoveNative(g)

# U11 TX pads -> AC caps -> B.Cu corridors -> U12 bridge TX pads.
for name, upad, cap, target, corridor, target_x in (
    ('USB_TXP1','21','C86.1','25',(148.0,160.0),145.0 if ROTATE_U12 else (155.0 if ROTATE_U12_90 else 155.0)),
    ('USB_TXN1','22','C87.1','24',(148.0,165.0),147.0 if ROTATE_U12 else (158.5 if ROTATE_U12_90 else 160.0)),
):
    n = net(b, name); bridge_n = net(b, 'JMS_USB3_TXP' if name == 'USB_TXP1' else 'JMS_USB3_TXN')
    c_ref, c_num = cap.split('.')
    src = xy(pad(b,'U11',upad)); c1 = xy(pad(b,c_ref,c_num)); c2 = xy(pad(b,c_ref,'2'))
    dst = xy(pad(b,'U12',target)); cv = corridor
    target_y = (133.0 if name == 'USB_TXP1' else 132.6) if ROTATE_U12 else ((132.0 if name == 'USB_TXP1' else 131.0) if ROTATE_U12_90 else (137.0 if name == 'USB_TXP1' else 137.4))
    tv = ((163.0, 134.5) if name == 'USB_TXP1' else (164.0, 135.5)) if (TARGET_STAGGER or RX_FAR) else (target_x, target_y)
    if TARGET_STAGGER or RX_FAR:
        cv = ((154.0 if name == 'USB_TXP1' else 155.0), c1[1]) if CAP_CLEAR else ((149.0 if name == 'USB_TXP1' else 151.0), c1[1])
    source_via = (142.0, 139.6) if name == 'USB_TXP1' else (141.0, 141.0)
    source_lane = (143.0, 140.0) if name == 'USB_TXP1' else (139.0, 141.0)
    if name == 'USB_TXP1':
        seg(b,n,src,(141.4,139.6),F); seg(b,n,(141.4,139.6),source_via,F)
    else:
        seg(b,n,src,source_via,F)
    via(b,n,source_via)
    seg(b,n,source_via,source_lane,B)
    cap_via = (145.0, c1[1])
    seg(b,n,source_lane,(source_lane[0],c1[1]),B)
    seg(b,n,(source_lane[0],c1[1]),cap_via,B); via(b,n,cap_via)
    seg(b,n,cap_via,c1,F)
    seg(b,bridge_n,c2,cv,F); via(b,bridge_n,cv)
    lane_x = {'USB_TXP1':143.0, 'USB_TXN1':142.0}[name] if ROTATE_U12 else ({'USB_TXP1':152.0, 'USB_TXN1':153.0}[name])
    approach_y = {'USB_TXP1':132.5, 'USB_TXN1':132.1}[name] if ROTATE_U12 else ({'USB_TXP1':136.5, 'USB_TXN1':136.9}[name])
    if TARGET_STAGGER or RX_FAR:
        seg(b,bridge_n,cv,(cv[0],tv[1]),B)
        seg(b,bridge_n,(cv[0],tv[1]),tv,B)
    else:
        seg(b,bridge_n,cv,(lane_x,cv[1]),B)
        seg(b,bridge_n,(lane_x,cv[1]),(lane_x,approach_y),B)
        seg(b,bridge_n,(lane_x,approach_y),(tv[0],approach_y),B)
        seg(b,bridge_n,(tv[0],approach_y),tv,B)
    via(b,bridge_n,tv)
    if TARGET_STAGGER or RX_FAR:
        shoulder = (162.0, dst[1])
        seg(b,bridge_n,dst,shoulder,F)
        seg(b,bridge_n,shoulder,tv,F)
    else:
        seg(b,bridge_n,tv,dst,F)

# U11 RX pads -> B.Cu corridors -> U12's bridge RX pads.  Their y corridors
# are below the TX capacitor launches and their return vias are farther
# outboard than the TX returns, avoiding the U12 pad-field funnel.
for name, upad, target, source_via, target_via in (
    ('USB_RXP1','26','23',((132.0,170.0) if TARGET_STAGGER else (142.0,170.0)),(151.0 if ROTATE_U12 else (160.0 if TARGET_STAGGER else (161.0 if ROTATE_U12_90 else 155.0)),139.2 if TARGET_STAGGER else (132.2 if ROTATE_U12 else (132.0 if ROTATE_U12_90 else 137.8)))),
    ('USB_RXN1','27','22',((128.0,175.0) if TARGET_STAGGER else (136.0,175.0)),(161.0 if TARGET_STAGGER else (149.0 if ROTATE_U12 else (163.5 if ROTATE_U12_90 else 161.0)),140.2 if TARGET_STAGGER else (131.8 if ROTATE_U12 else (131.0 if ROTATE_U12_90 else 138.2)))),
):
    n = net(b,name); src = xy(pad(b,'U11',upad)); dst = xy(pad(b,'U12',target))
    if RX_FCU:
        # Both RX endpoints are native F.Cu pads. Keep the pair on F.Cu and
        # use monotonic shoulders; this deliberately removes the otherwise
        # impossible six-via QFN target-field requirement.
        shoulder = (148.0, dst[1])
        seg(b,n,src,(145.0,src[1]),F)
        seg(b,n,(145.0,src[1]),shoulder,F)
        seg(b,n,shoulder,dst,F)
        continue
    if CAP_CLEAR:
        sv = (150.0, 142.0) if name == 'USB_RXP1' else (151.0, 144.0)
    else:
        sv = source_via
    tv = ((170.0, 140.0) if name == 'USB_RXP1' else (171.0, 141.0)) if RX_FAR else (((160.0, 138.8) if name == 'USB_RXP1' else (161.0, 139.8)) if TARGET_STAGGER else target_via)
    if CAP_CLEAR:
        if name == 'USB_RXN1':
            # The south transition leaves the dense U11 side row before the
            # B.Cu corridor; keep the pad-to-via ownership explicit.
            seg(b,n,src,(src[0],sv[1]),F)
            seg(b,n,(src[0],sv[1]),sv,F)
        else:
            y = sv[1]
            seg(b,n,src,(src[0],y),F); seg(b,n,(src[0],y),sv,F)
    else:
        seg(b,n,src,(src[0],sv[1]),F); seg(b,n,(src[0],sv[1]),sv,F)
    via(b,n,sv)
    lane_x = 141.0 if name == 'USB_RXP1' else 140.0 if ROTATE_U12 else (154.0 if name == 'USB_RXP1' else 155.0)
    approach_y = 131.7 if name == 'USB_RXP1' else 131.3 if ROTATE_U12 else (137.3 if name == 'USB_RXP1' else 138.0)
    if CAP_CLEAR:
        low = 173.0 if name == 'USB_RXP1' else 178.0
        # Keep RXN's far column to the right of the RXP column.  A one-mm
        # parallel shelf offset is not sufficient here because the final
        # target dogbones still enter the same native clearance envelope;
        # the separated column makes the topology non-intersecting.
        far = 170.0 if name == 'USB_RXP1' else 180.0
        if name == 'USB_RXN1':
            # Keep RXN entirely north of the PERST shelf: the source via
            # rises to an outboard B.Cu lane, then approaches the target from
            # the east.  This avoids both the RXP lower shelf and CM5_PERST.
            bypass_y = 128.0
            bypass_x = 165.0
            # Jog east before rising past the nearby CM5 USB3 RX-N via.
            handoff_x = 152.5
            handoff_y = 140.0
            seg(b,n,sv,(sv[0],handoff_y),B)
            seg(b,n,(sv[0],handoff_y),(handoff_x,handoff_y),B)
            seg(b,n,(handoff_x,handoff_y),(handoff_x,bypass_y),B)
            seg(b,n,(handoff_x,bypass_y),(bypass_x,bypass_y),B)
            seg(b,n,(bypass_x,bypass_y),(bypass_x,tv[1]),B)
            seg(b,n,(bypass_x,tv[1]),tv,B)
        else:
            seg(b,n,sv,(sv[0],low),B)
            seg(b,n,(sv[0],low),(far,low),B)
        if name == 'USB_RXP1':
            seg(b,n,(far,low),tv,B)
    elif RX_FAR:
        seg(b,n,sv,(170.0 if name == 'USB_RXP1' else 171.0,sv[1]),B)
        seg(b,n,(170.0 if name == 'USB_RXP1' else 171.0,sv[1]),tv,B)
    elif TARGET_STAGGER or RX_FAR:
        seg(b,n,sv,(sv[0],tv[1]),B)
        seg(b,n,(sv[0],tv[1]),tv,B)
    else:
        seg(b,n,sv,(lane_x,sv[1]),B)
        seg(b,n,(lane_x,sv[1]),(lane_x,approach_y),B)
        seg(b,n,(lane_x,approach_y),(tv[0],approach_y),B)
        seg(b,n,(tv[0],approach_y),tv,B)
    via(b,n,tv)
    if RX_FAR:
        shoulder = (159.0, dst[1])
        seg(b,n,dst,shoulder,F)
        seg(b,n,shoulder,tv,F)
    elif TARGET_STAGGER:
        shoulder = (159.0, dst[1])
        seg(b,n,dst,shoulder,F)
        seg(b,n,shoulder,tv,F)
    else:
        seg(b,n,tv,dst,F)

# Keep the validated V123-style single-ended PERST duck.  Its original
# F.Cu y=150 trunk is exactly where the outboard support island now lives.
perst = b.FindNet('/CORE_CM5/CM5_PERST') or b.FindNet('CM5_PERST')
if not CAP_CLEAR:
    for t in list(b.GetTracks()):
        if leaf(t.GetNetname()) != 'CM5_PERST' or t.GetLayer() != F: continue
        a, z = xy(t.GetStart()), xy(t.GetEnd())
        if {round(a[0],2), round(z[0],2)} == {64.0,152.54} and abs(a[1]-150) < .02 and abs(z[1]-150) < .02:
            b.RemoveNative(t)
            seg(b,perst,(64,150),(64,147),F); via(b,perst,(64,147))
            seg(b,perst,(64,147),(152.54,147),B); via(b,perst,(152.54,147))
            seg(b,perst,(152.54,147),(152.54,150),F)
            break

b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.BuildConnectivity()
b.Save(str(OUT)); print(OUT)
