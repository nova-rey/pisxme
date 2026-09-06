"""Regenerate U7 clock support in a measured open region."""
from pathlib import Path
from heapq import heappush, heappop
import math
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'PHASE24_SELECTED_MACRO_SWAP_STORAGE_SATA_PAIR_CORRIDOR_V26_AUTH_SKEW.kicad_pcb'
OUT = R / 'PHASE24_SELECTED_MACRO_STORAGE_V26_CLOCK_REGENERATED_COMMON.kicad_pcb'
STEP = .25
NETS = {'XI':'/STORAGE/BRIDGE_XI','XO':'/STORAGE/BRIDGE_XO','VS':'/STORAGE/BRIDGE_VSSOSC'}
MAP = {'Y1':{'1':'XI','2':'VS','3':'XO','4':'VS'}, 'R23':{'1':'XI','2':'XO'},
       'C42':{'1':'XI','2':'VS'}, 'C43':{'1':'XO','2':'VS'}}

def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def cell(q): return round(q[0]/STEP), round(q[1]/STEP)
def pxy(c): return c[0]*STEP, c[1]*STEP

b = pcbnew.LoadBoard(str(BASE))
u = b.FindFootprintByReference('U7')
nets = {k:b.FindNet(v) for k,v in NETS.items()}
for item in list(b.GetTracks()):
    if item.GetNetname() in NETS.values(): b.RemoveNative(item)
positions = {'Y1':(112,145), 'R23':(112,165), 'C42':(102,165), 'C43':(122,165)}
for ref, pos in positions.items():
    f = b.FindFootprintByReference(ref); f.SetPosition(V(*pos)); f.SetOrientationDegrees(0)
    for p in f.Pads():
        k = MAP[ref][str(p.GetNumber())]
        p.SetNet(nets[k]); p.SetNetCode(nets[k].GetNetCode())
        ls = pcbnew.LSET(); ls.AddLayer(pcbnew.B_Cu); p.SetLayerSet(ls)

def blocked(netcode):
    out = set()
    def mark(a,z):
        x,y=xy(a); X,Y=xy(z)
        for i in range(math.floor(min(x,X)/STEP)-1, math.ceil(max(x,X)/STEP)+2):
            for j in range(math.floor(min(y,Y)/STEP)-1, math.ceil(max(y,Y)/STEP)+2): out.add((i,j))
    for t in b.GetTracks():
        if t.GetLayer()==pcbnew.B_Cu and t.GetNetCode()!=netcode: mark(t.GetStart(),t.GetEnd())
    for f in b.GetFootprints():
        for p in f.Pads():
            if p.GetNetCode()==netcode or not p.GetLayerSet().Contains(pcbnew.B_Cu): continue
            q=xy(p.GetPosition()); sx=pcbnew.ToMM(p.GetSize().x); sy=pcbnew.ToMM(p.GetSize().y)
            mark(V(q[0]-sx/2-.2,q[1]-sy/2-.2),V(q[0]+sx/2+.2,q[1]+sy/2+.2))
    return out

def route(start, goal, occ, reserved):
    s=cell(start); g=cell(goal); q=[(0,s)]; prev={s:None}; cost={s:0}
    while q:
        _, z=heappop(q)
        if z==g: break
        for v in ((z[0]+1,z[1]),(z[0]-1,z[1]),(z[0],z[1]+1),(z[0],z[1]-1)):
            if not (65/STEP<=v[0]<=140/STEP and 110/STEP<=v[1]<=190/STEP): continue
            if v!=g and (v in occ or v in reserved): continue
            c=cost[z]+1
            if c<cost.get(v,10**9): cost[v]=c; prev[v]=z; heappush(q,(c+abs(v[0]-g[0])+abs(v[1]-g[1]),v))
    if g not in prev: raise RuntimeError(f'no path {start}->{goal}')
    path=[]; z=g
    while z is not None: path.append(z); z=prev[z]
    return list(reversed(path))

reserved=set()
for number, key in [('52','XI'),('54','XO'),('53','VS')]:
    p=next(p for p in u.Pads() if p.GetNumber()==number); net=nets[key]
    start=xy(p.GetPosition()); via=(start[0]+({'52':.75,'54':-.25,'53':.25}[number]),start[1]+1.0)
    targets=[]
    for f in b.GetFootprints():
        if f.GetReference() not in MAP: continue
        for pad in f.Pads():
            if pad.GetNetname()==NETS[key]: targets.append(xy(pad.GetPosition()))
    # Reach the shared crystal first, then fan out to the more distant
    # passives.  This keeps the high-value pad-field escape short and avoids
    # reserving a branch through the neighboring crystal pad.
    targets.sort(key=lambda q: (q[1], q[0]))
    current=via
    v=pcbnew.PCB_VIA(b); v.SetPosition(V(*via)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(net); b.Add(v)
    dog=pcbnew.PCB_TRACK(b); dog.SetStart(p.GetPosition()); dog.SetEnd(V(*via)); dog.SetLayer(pcbnew.F_Cu); dog.SetWidth(pcbnew.FromMM(.15)); dog.SetNet(net); b.Add(dog)
    for target in targets:
        # Candidate search permits the native DRC to arbitrate exact
        # sub-grid spacing; the reservation set is retained for diagnostics
        # but is not treated as a synthetic electrical obstacle.
        path=route(current,target,blocked(net.GetNetCode()),set())
        for a,z in zip(path,path[1:]):
            t=pcbnew.PCB_TRACK(b); t.SetStart(V(*pxy(a))); t.SetEnd(V(*pxy(z))); t.SetLayer(pcbnew.B_Cu); t.SetWidth(pcbnew.FromMM(.15)); t.SetNet(net); b.Add(t); reserved.add(z)
        current=target
        print(key, target, len(path))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
