"""Join the proven J7 launch boundary to the official CM5IO island."""
from pathlib import Path
import os
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'CM5IO_J7_LAUNCH_FIXTURE.kicad_pcb'
ISLAND=ROOT/'CM5IO_PISXME_ETHERNET_TRANSPLANT_FIXTURE.kicad_pcb'
OUT=ROOT/'CM5IO_J7_CM5IO_BOUNDARY_FIXTURE.kicad_pcb'
ISLAND_DX=90.0 if os.environ.get('PISXME_ISLAND_RIGHT')=='1' else 0.0
MDI=tuple(f'CM5_GBE_TD{i}_{p}' for i in range(4) for p in 'PN')

def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def net(b,name):
    n=b.FindNet(name)
    if n is None: n=pcbnew.NETINFO_ITEM(b,name); b.Add(n)
    return n
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def track(b,n,pts,layer=pcbnew.F_Cu):
    for a,z in zip(pts,pts[1:]):
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
        t.SetWidth(pcbnew.FromMM(.127)); t.SetNet(n); b.Add(t)
def via(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30))
    q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)
def edge(b,a,z):
    s=pcbnew.PCB_SHAPE(b); s.SetShape(pcbnew.SHAPE_T_SEGMENT); s.SetLayer(pcbnew.Edge_Cuts)
    s.SetStart(V(*a)); s.SetEnd(V(*z)); s.SetWidth(pcbnew.FromMM(.05)); b.Add(s)

def main():
    b=pcbnew.LoadBoard(str(BASE)); src=pcbnew.LoadBoard(str(ISLAND))
    names=set(MDI)|{'ETH_GND','ETH_CT_COMMON','GBE_SHIELD','GBE_LED_Y_A','GBE_LED_Y_K','GBE_LED_G_A','GBE_LED_G_K'}
    nets={n:net(b,n) for n in names}
    # Copy the official island footprints with their already-authoritative
    # positions/orientations, rebinding pads by net name into this board.
    for ref in ('U9','U6','J2','J9','C1'):
        f0=src.FindFootprintByReference(ref); f=pcbnew.FOOTPRINT(f0); f.SetPosition(V(xy(f0.GetPosition())[0]+ISLAND_DX,xy(f0.GetPosition())[1])); b.Add(f)
        for p in f.Pads():
            name=str(p.GetNetname()).rsplit('/',1)[-1]
            if name in nets: p.SetNet(nets[name])
    # Retain all official MDI island segments whose endpoints are outside the
    # omitted CM5 source legs.  The exact J7 launch fixture supplies those.
    for t0 in src.GetTracks():
        name=str(t0.GetNetname()).rsplit('/',1)[-1]
        if name not in MDI: continue
        a,z=xy(t0.GetStart()),xy(t0.GetEnd()); a=(a[0]+ISLAND_DX,a[1]); z=(z[0]+ISLAND_DX,z[1])
        if max(a[1],z[1]) >= 70: continue
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(t0.GetLayer())
        t.SetWidth(t0.GetWidth()); t.SetNet(nets[name]); b.Add(t)
    # Copy the island support/return copper, excluding the MDI routes.
    for t0 in src.GetTracks():
        name=str(t0.GetNetname()).rsplit('/',1)[-1]
        if name in MDI or name not in nets: continue
        a,z=xy(t0.GetStart()),xy(t0.GetEnd()); a=(a[0]+ISLAND_DX,a[1]); z=(z[0]+ISLAND_DX,z[1])
        if not (0 <= a[0] <= 100 and 35 <= a[1] <= 75 and 0 <= z[0] <= 100 and 35 <= z[1] <= 75): continue
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(t0.GetLayer())
        t.SetWidth(t0.GetWidth()); t.SetNet(nets[name]); b.Add(t)
    # Official CM5IO-derived ESD source-side landing points in this island.
    land={'CM5_GBE_TD3_P':(26.204119+ISLAND_DX,59.210),'CM5_GBE_TD3_N':(26.361524+ISLAND_DX,59.590),
          'CM5_GBE_TD2_N':(27.021298+ISLAND_DX,60.110),'CM5_GBE_TD2_P':(27.178701+ISLAND_DX,60.490),
          'CM5_GBE_TD1_P':(32.660000+ISLAND_DX,58.871297),'CM5_GBE_TD1_N':(33.039999+ISLAND_DX,59.028702),
          'CM5_GBE_TD0_N':(34.160000+ISLAND_DX,58.571298),'CM5_GBE_TD0_P':(34.539999+ISLAND_DX,58.728702)}
    boundary={3:(10,90),4:(90,90),5:(8,92),6:(92,92),9:(6,94),10:(94,94),11:(4,96),12:(96,96)}
    names_by_pad={3:'CM5_GBE_TD3_P',4:'CM5_GBE_TD1_P',5:'CM5_GBE_TD3_N',6:'CM5_GBE_TD1_N',
                  9:'CM5_GBE_TD2_N',10:'CM5_GBE_TD0_N',11:'CM5_GBE_TD2_P',12:'CM5_GBE_TD0_P'}
    bridge_outer=os.environ.get('PISXME_BRIDGE_OUTER')=='1'
    bridge_round=os.environ.get('PISXME_BRIDGE_ROUND')=='1'
    if bridge_round:
        # Pair-specific round-the-envelope bridge.  TD3 stays on B.Cu over
        # the top-left perimeter, TD2 uses F.Cu over the bottom-left, TD1
        # uses F.Cu on the separated right approach, and TD0 uses B.Cu on
        # the bottom-right.  This keeps same-layer corridors disjoint while
        # preserving the exact official ESD landing coordinates.
        paths={
          'CM5_GBE_TD3_P':([(10,90),(0,90),(0,50),(110,50),(113,50),(113,57.5),land['CM5_GBE_TD3_P']],pcbnew.B_Cu),
          'CM5_GBE_TD3_N':([(8,92),(-1,92),(-1,51),(111,51),(114,51),(114,58.5),land['CM5_GBE_TD3_N']],pcbnew.B_Cu),
          'CM5_GBE_TD2_N':([(6,94),(-2,94),(-2,135),(112,135),(112,62),land['CM5_GBE_TD2_N']],pcbnew.F_Cu),
          'CM5_GBE_TD2_P':([(4,96),(-3,96),(-3,136),(113,136),(113,63),land['CM5_GBE_TD2_P']],pcbnew.F_Cu),
          'CM5_GBE_TD1_P':([(90,90),(103,90),(103,45),(120,45),(120,57),land['CM5_GBE_TD1_P']],pcbnew.F_Cu),
          'CM5_GBE_TD1_N':([(92,92),(92,140),(124,140),(124,62),land['CM5_GBE_TD1_N']],pcbnew.F_Cu),
          'CM5_GBE_TD0_N':([(94,94),(94,138),(125,138),(125,61),(125,61),land['CM5_GBE_TD0_N']],pcbnew.B_Cu),
          'CM5_GBE_TD0_P':([(96,96),(96,139),(126,139),(126,62),(126,62),land['CM5_GBE_TD0_P']],pcbnew.B_Cu)}
        for name,(pts,layer) in paths.items():
            n=nets[name]; end=pts[-1]
            if layer==pcbnew.F_Cu:
                track(b,n,pts,pcbnew.F_Cu)
            else:
                rv=pts[-2]; track(b,n,pts[:-2]+[rv],pcbnew.B_Cu); via(b,n,rv); track(b,n,[rv,end],pcbnew.F_Cu)
        b.Save(str(OUT)); print('saved',OUT); return
    if bridge_outer:
        # Each pair owns one signal layer for the bridge.  Through-hole
        # boundary pads permit the layer choice without a source via; return
        # vias are staggered well beyond the pair-clearance requirement.
        rv={'CM5_GBE_TD3_P':(23.0,58.0),'CM5_GBE_TD3_N':(23.0,60.0),
            'CM5_GBE_TD2_N':(24.0,59.0),'CM5_GBE_TD2_P':(24.0,61.0),
            'CM5_GBE_TD1_P':(30.0,57.8),'CM5_GBE_TD1_N':(30.0,59.8),
            'CM5_GBE_TD0_N':(32.0,58.8),'CM5_GBE_TD0_P':(32.0,60.8)}
        layer={'CM5_GBE_TD3_P':pcbnew.F_Cu,'CM5_GBE_TD3_N':pcbnew.F_Cu,
               'CM5_GBE_TD2_N':pcbnew.B_Cu,'CM5_GBE_TD2_P':pcbnew.B_Cu,
               'CM5_GBE_TD1_P':pcbnew.F_Cu,'CM5_GBE_TD1_N':pcbnew.F_Cu,
               'CM5_GBE_TD0_N':pcbnew.B_Cu,'CM5_GBE_TD0_P':pcbnew.B_Cu}
        lane={'CM5_GBE_TD3_P':50.0,'CM5_GBE_TD3_N':51.0,'CM5_GBE_TD2_N':52.0,'CM5_GBE_TD2_P':53.0,
              'CM5_GBE_TD1_P':54.0,'CM5_GBE_TD1_N':55.0,'CM5_GBE_TD0_N':56.0,'CM5_GBE_TD0_P':57.0}
        for number,name in names_by_pad.items():
            start=boundary[number]; end=land[name]; n=nets[name]; xedge=1.0 if start[0]<50 else 101.0
            p=rv[name]
            track(b,n,[start,(xedge,start[1]),(xedge,lane[name]),(p[0],lane[name]),p],layer[name])
            via(b,n,p); track(b,n,[p,end],pcbnew.F_Cu)
        b.Save(str(OUT)); print('saved',OUT); return
    # Each group has a monotonic independent F.Cu approach. TD0 uses B.Cu
    # for the group-order correction, with widely separated return vias.
    for number,name in names_by_pad.items():
        n=nets[name]; start=boundary[number]; end=land[name]
        if number in (10,12):
            sv=(start[0]-4,start[1]+(number-11)*1.0)
            rv=(end[0]-3.0,end[1]+(2.0 if number==10 else -2.0))
            track(b,n,[start,sv],pcbnew.B_Cu); track(b,n,[sv,(45,80),(rv[0],rv[1])],pcbnew.B_Cu)
            via(b,n,rv); track(b,n,[rv,end],pcbnew.F_Cu)
        else:
            lane_y=72.0+(number%10)*0.8
            track(b,n,[start,(start[0]-4 if start[0]<50 else start[0]+4,start[1]),
                       (20 if start[0]<50 else 45,lane_y),end],pcbnew.F_Cu)
    # Expand the disposable outline to contain both the launch and island.
    for d in list(b.GetDrawings()):
        if d.GetLayer()==pcbnew.Edge_Cuts: b.Remove(d)
    x1=190 if ISLAND_DX else 100
    for a,z in (((2,35),(x1,35)),((x1,35),(x1,145)),((x1,145),(2,145)),((2,145),(2,35))): edge(b,a,z)
    b.Save(str(OUT)); print('saved',OUT)
if __name__=='__main__': main()
