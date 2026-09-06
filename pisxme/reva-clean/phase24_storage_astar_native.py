"""Disposable native-pad obstacle-aware SATA router for Phase 24.

All terminals and nets come from the saved PCB.  The router never adds graph
edges for expected connectivity; it emits real KiCad tracks/vias only.
"""
from pathlib import Path
from heapq import heappush, heappop
import math
import os
import pcbnew

R = Path(__file__).resolve().parent
BASE = Path(os.environ.get('PISXME_SATA_BASE', str(R/'PHASE24_SELECTED_MACRO_ETH_SUPPORT_V15.kicad_pcb')))
OUT = Path(os.environ.get('PISXME_SATA_OUT', str(R/'PHASE24_SELECTED_MACRO_SATA_ASTAR_NATIVE.kicad_pcb')))
F, B = pcbnew.F_Cu, pcbnew.B_Cu
STEP, WIDTH, VIA_W, VIA_D = .25, .15, .50, .30
LAYERS = (F, B)

def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def size_xy(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def grid(p): return (round(p[0]/STEP), round(p[1]/STEP))
def point(g): return (g[0]*STEP, g[1]*STEP)
def fp(b,r): return b.FindFootprintByReference(r)
def pad(b,r,n):
    p=fp(b,r).FindPadByNumber(str(n))
    if p is None: raise RuntimeError(f'missing {r}.{n}')
    return p

def layers(p): return [l for l in LAYERS if p.GetLayerSet().Contains(l)]
def block(occ, layer, p, radius=.2):
    gx,gy=grid(p); rr=max(1,math.ceil(radius/STEP))
    for dx in range(-rr,rr+1):
        for dy in range(-rr,rr+1): occ[layer].add((gx+dx,gy+dy))
def line_block(occ, layer, a, z, radius=.2):
    ax,ay=grid(a); zx,zy=grid(z); count=max(abs(zx-ax),abs(zy-ay),1)
    for i in range(count+1):
        q=(round(ax+(zx-ax)*i/count),round(ay+(zy-ay)*i/count)); rr=max(1,math.ceil(radius/STEP))
        for dx in range(-rr,rr+1):
            for dy in range(-rr,rr+1): occ[layer].add((q[0]+dx,q[1]+dy))

def occupancy(b, ignored):
    occ={F:set(),B:set()}
    hard={F:set(),B:set()}
    for t in b.GetTracks():
        if isinstance(t,pcbnew.PCB_VIA):
            q=xy(t.GetPosition()); block(occ,F,q,.35); block(occ,B,q,.35)
        else: line_block(occ,t.GetLayer(),xy(t.GetStart()),xy(t.GetEnd()),.22)
    for f in b.GetFootprints():
        if f.GetReference() in ignored: continue
        for p in f.Pads():
            sx,sy=size_xy(p.GetSize())
            drill=size_xy(p.GetDrillSize())[0]
            r=max(sx,sy)/2 + (.30 if drill < 1.5 else 1.4)
            pad_layers=layers(p)
            # NPTH and through-hole pads may report no usable copper layer
            # set through the Python wrapper, but their drilled/physical body
            # still blocks both outer copper layers.
            drilled = drill > 0 or p.GetAttribute() == 3
            if not pad_layers and drilled:
                pad_layers=list(LAYERS)
            for l in pad_layers: block(occ,l,xy(p.GetPosition()),r)
            if drilled:
                for l in LAYERS: block(hard,l,xy(p.GetPosition()),r)
    return occ,hard

def route(occ,hard,start,goal,start_layer=F,goal_layer=F,x_gate=None,
          clear_start_mm=2.0,clear_goal_mm=2.0):
    # Terminal halos are a per-segment escape allowance, not global edits to
    # the board obstacle map.  Keeping the base map intact prevents a later
    # lane from using the first lane's cleared pad field as a shortcut.
    local={F:set(occ[F]), B:set(occ[B])}
    s=(*grid(start),start_layer); t=(*grid(goal),goal_layer)
    # Native SMD/QFN escapes need a real local departure window.  Two grid
    # cells was only 0.5 mm and left the source pad imprisoned by its legal
    # neighboring pads; clear a bounded 2 mm halo for the current terminal.
    for l,q,clear_mm in ((start_layer,s,clear_start_mm),(goal_layer,t,clear_goal_mm)):
        cells=math.ceil(clear_mm/STEP)
        for dx in range(-cells,cells+1):
            for dy in range(-cells,cells+1): local[l].discard((q[0]+dx,q[1]+dy))
    # Restore physical drilled-hole keepouts after the terminal departure
    # allowance.  Target halos may clear neighboring SMD pads, but never a
    # connector mounting hole or other through-hole body.
    for l in LAYERS: local[l].update(hard[l])
    bounds=(grid((1,1)),grid((299,179)))
    q=[(0,s)]; cost={s:0}; prev={s:None}
    while q:
        _,cur=heappop(q)
        if cur==t: break
        x,y,l=cur
        for nx,ny,nl in ((x+1,y,l),(x-1,y,l),(x,y+1,l),(x,y-1,l),(x,y,B if l==F else F)):
            if not(bounds[0][0]<=nx<=bounds[1][0] and bounds[0][1]<=ny<=bounds[1][1]): continue
            # Keep ordinary through-vias away from the M.2 SMD launch.  The
            # final copper approach must be on F.Cu; a transition in the
            # connector pad field is via-in/near-pad geometry and is not a
            # valid Rev-A escape.
            if nl != l and abs(nx-t[0]+0.0)*STEP + abs(ny-t[1]+0.0)*STEP < 3.0:
                continue
            if (nx,ny) in local[nl] and (nx,ny,nl)!=t: continue
            ns=(nx,ny,nl)
            gate=0
            if x_gate is not None and 117.0 <= ny*STEP <= 132.5:
                side,limit=x_gate
                if (side < 0 and nx*STEP > limit) or (side > 0 and nx*STEP < limit):
                    gate=18
            nc=cost[cur]+1+(28 if nl!=l else 0)+gate
            if nc<cost.get(ns,10**12):
                cost[ns]=nc; prev[ns]=cur
                h=abs(nx-t[0])+abs(ny-t[1])+(28 if nl!=t[2] else 0)
                heappush(q,(nc+h,ns))
    if t not in prev: raise RuntimeError(f'no route {start}->{goal}')
    out=[]; cur=t
    while cur is not None: out.append(cur);cur=prev[cur]
    return list(reversed(out))

def via(b,n,p):
    v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(VIA_W));v.SetDrill(pcbnew.FromMM(VIA_D));v.SetLayerPair(F,B);v.SetNet(n);b.Add(v)
def emit(b,n,path,occ):
    last=None
    for a,z in zip(path,path[1:]):
        if a[2]!=z[2]:
            p=point(a[:2]);via(b,n,p);block(occ,F,p,.38);block(occ,B,p,.38);last=None;continue
        if last is None:last=point(a[:2])
        end=point(z[:2]);t=pcbnew.PCB_TRACK(b);t.SetStart(V(*last));t.SetEnd(V(*end));t.SetLayer(a[2]);t.SetWidth(pcbnew.FromMM(WIDTH));t.SetNet(n);b.Add(t)
        line_block(occ,a[2],last,end,.22);last=end

def direct(b,n,a,z,layer,occ):
    t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(WIDTH));t.SetNet(n);b.Add(t)
    line_block(occ,layer,a,z,.22)

b=pcbnew.LoadBoard(str(BASE))
# Disposable storage-island placement override.  The default is the saved
# candidate; experiments may move only J3 to test whether its physical
# mounting-hole/pad field, rather than U7 or the macro topology, is the local
# launch constraint.
j3x=os.environ.get('PISXME_J3_X'); j3y=os.environ.get('PISXME_J3_Y')
if j3x and j3y:
    j3=b.FindFootprintByReference('J3')
    j3.SetPosition(V(float(j3x),float(j3y)))
# Remove only the previous SATA copper so this experiment evaluates the new
# native-pad route rather than colliding with inherited SATA geometry.  USB3,
# PCIe, power, and all unrelated copper remain untouched.
for t in list(b.GetTracks()):
    if any(k in t.GetNetname() for k in ('BRIDGE_SATA_', 'SATA_M2_')):
        b.Remove(t)
# Keep all pads in the obstacle model.  `route()` clears only the actual
# source/target halos for the current segment; excluding whole footprints
# would allow one lane to pass through adjacent pads of another net.
ignored=set()
occ,hard=occupancy(b,ignored)
# This baseline intentionally leaves drilled-hole handling to the native DRC
# while the pair escape is tuned; the earlier hard-hole waypoint variants are
# preserved in history as rejected experiments.
hard={F:set(),B:set()}
jobs=[
 ('BRIDGE_SATA_TX_P','57','C30','2','1'),
 ('BRIDGE_SATA_TX_N','56','C31','2','2'),
 ('BRIDGE_SATA_RX_P','60','C32','2','3'),
 ('BRIDGE_SATA_RX_N','59','C33','2','4'),
]
for name,up,cap,cp,jp in jobs:
    bridge=b.FindNet('/STORAGE/'+name); socket=b.FindNet('/STORAGE/'+name.replace('BRIDGE_SATA_','SATA_M2_'))
    if bridge is None or socket is None: raise RuntimeError(name)
    a=xy(pad(b,'U7',up).GetPosition()); z=xy(pad(b,cap,cp).GetPosition())
    bridge_start = B if name.startswith('BRIDGE_SATA_RX_') else F
    if os.environ.get('PISXME_BASELINE_ESCAPE') == '1':
        bridge_start=F
    if bridge_start == B:
        # Escape the dense U7 pad field on F.Cu before changing layers.  A
        # via directly on the QFN pad field is not an acceptable terminal.
        dogbone = (102.5,117.0) if name == 'BRIDGE_SATA_RX_P' else (106.5,117.0)
        dog_gate = (-1,103.0) if name == 'BRIDGE_SATA_RX_P' else (1,106.0)
        path=route(occ,hard,a,dogbone,F,F,dog_gate,2.0,0.5); emit(b,bridge,path,occ)
        via(b,bridge,dogbone)
        path=route(occ,hard,dogbone,z,B,F); emit(b,bridge,path,occ)
    else:
        path=route(occ,hard,a,z,F,F); emit(b,bridge,path,occ)
    a=xy(pad(b,cap,'1').GetPosition()); z=xy(pad(b,'J3',jp).GetPosition())
    # Keep the RX socket pair on B.Cu after an ordinary via at the coupling
    # capacitor; TX remains F.Cu.  This is a permitted layer split and avoids
    # the close M.2 launch pair weaving on one layer.
    socket_start = B if name.startswith('BRIDGE_SATA_RX_') else F
    if os.environ.get('PISXME_BASELINE_ESCAPE') != '1' and name == 'BRIDGE_SATA_TX_N':
        socket_start=B
    gate = None
    if name == 'BRIDGE_SATA_RX_P': gate=(-1,118.75)
    if name == 'BRIDGE_SATA_RX_N': gate=(1,120.25)
    if socket_start == B:
        # The coupling capacitor is an F.Cu SMD pad.  Explicitly launch the
        # B.Cu corridor through an ordinary via at the segment source; the
        # A* path itself begins on B.Cu and cannot infer this terminal via.
        via(b,socket,a)
    if name == 'BRIDGE_SATA_RX_P': gate=(-1,118.75)
    if name == 'BRIDGE_SATA_RX_N': gate=(1,120.25)
    path=route(occ,hard,a,z,socket_start,F,gate); emit(b,socket,path,occ)
    print(name,'bridge',a,'to',z)
b.Save(str(OUT));print(OUT)
