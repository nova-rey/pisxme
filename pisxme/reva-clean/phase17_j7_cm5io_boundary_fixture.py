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
    # Optional BCM54210PE-supported pair/polarity permutation experiment.  It
    # changes only the disposable fixture's physical launch assignment; the
    # source and connector remain electrically identified by their nets.
    pair_swap=os.environ.get('PISXME_BRIDGE_SWAP')=='1'
    island_map={n:n for n in MDI}
    if pair_swap:
        island_map.update({
          'CM5_GBE_TD3_P':'CM5_GBE_TD3_N','CM5_GBE_TD3_N':'CM5_GBE_TD3_P',
          'CM5_GBE_TD2_N':'CM5_GBE_TD2_P','CM5_GBE_TD2_P':'CM5_GBE_TD2_N',
          'CM5_GBE_TD1_P':'CM5_GBE_TD0_N','CM5_GBE_TD1_N':'CM5_GBE_TD0_P',
          'CM5_GBE_TD0_N':'CM5_GBE_TD1_P','CM5_GBE_TD0_P':'CM5_GBE_TD1_N'})
    # Copy the official island footprints with their already-authoritative
    # positions/orientations, rebinding pads by net name into this board.
    for ref in ('U9','U6','J2','J9','C1'):
        f0=src.FindFootprintByReference(ref); f=pcbnew.FOOTPRINT(f0); f.SetPosition(V(xy(f0.GetPosition())[0]+ISLAND_DX,xy(f0.GetPosition())[1])); b.Add(f)
        for p in f.Pads():
            name=str(p.GetNetname()).rsplit('/',1)[-1]
            if name in nets: p.SetNet(nets[island_map.get(name,name)])
    # Retain all official MDI island segments whose endpoints are outside the
    # omitted CM5 source legs.  The exact J7 launch fixture supplies those.
    for t0 in src.GetTracks():
        name=str(t0.GetNetname()).rsplit('/',1)[-1]
        if name not in MDI: continue
        a,z=xy(t0.GetStart()),xy(t0.GetEnd()); a=(a[0]+ISLAND_DX,a[1]); z=(z[0]+ISLAND_DX,z[1])
        # Retain the official island-side graph, including its source handoff
        # segments.  The transplant's omitted CM5 source legs are the
        # segments whose original x range reaches back below 59 mm.
        if min(a[0],z[0]) < 59.0: continue
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(t0.GetLayer())
        t.SetWidth(t0.GetWidth()); t.SetNet(nets[island_map.get(name,name)]); b.Add(t)
    # Copy the island support/return copper, excluding the MDI routes.
    for t0 in src.GetTracks():
        name=str(t0.GetNetname()).rsplit('/',1)[-1]
        if name in MDI or name not in nets: continue
        a,z=xy(t0.GetStart()),xy(t0.GetEnd()); a=(a[0]+ISLAND_DX,a[1]); z=(z[0]+ISLAND_DX,z[1])
        if not (0 <= a[0] <= 100 and 35 <= a[1] <= 75 and 0 <= z[0] <= 100 and 35 <= z[1] <= 75): continue
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(t0.GetLayer())
        t.SetWidth(t0.GetWidth()); t.SetNet(nets[name]); b.Add(t)
    # Official CM5IO-derived ESD source-side landing points in this island.
    physical_land={'CM5_GBE_TD3_P':(59.4213+ISLAND_DX,67.210),'CM5_GBE_TD3_N':(59.5787+ISLAND_DX,67.590),
          'CM5_GBE_TD2_N':(59.8213+ISLAND_DX,68.110),'CM5_GBE_TD2_P':(59.9787+ISLAND_DX,68.490),
          'CM5_GBE_TD1_P':(60.3213+ISLAND_DX,69.010),'CM5_GBE_TD1_N':(60.4787+ISLAND_DX,69.390),
          'CM5_GBE_TD0_N':(60.8213+ISLAND_DX,69.910),'CM5_GBE_TD0_P':(60.9787+ISLAND_DX,70.290)}
    land={name:physical_land[island_map[name]] for name in MDI}
    boundary={3:(10,90),4:(90,90),5:(8,92),6:(92,92),9:(6,94),10:(94,94),11:(4,96),12:(96,96)}
    names_by_pad={3:'CM5_GBE_TD3_P',4:'CM5_GBE_TD1_P',5:'CM5_GBE_TD3_N',6:'CM5_GBE_TD1_N',
                  9:'CM5_GBE_TD2_N',10:'CM5_GBE_TD0_N',11:'CM5_GBE_TD2_P',12:'CM5_GBE_TD0_P'}
    bridge_outer=os.environ.get('PISXME_BRIDGE_OUTER')=='1'
    bridge_round=os.environ.get('PISXME_BRIDGE_ROUND')=='1'
    bridge_swap=os.environ.get('PISXME_BRIDGE_SWAP')=='1'
    if bridge_swap:
        # Pair-preserving monotonic corridors.  TD1 enters the physical TD0
        # landing and TD0 enters the physical TD1 landing; P/N polarity is
        # unchanged.  The left group uses four top lanes; the swapped right
        # group uses four independent upper-right lanes.
        paths={
          'CM5_GBE_TD3_P':([(10,90),(10,93),(7,93),(7,40.5),(149.579,40.5),land['CM5_GBE_TD3_P']],pcbnew.B_Cu),
          'CM5_GBE_TD3_N':([(8,92),(8,41.4),(149.421,41.4),land['CM5_GBE_TD3_N']],pcbnew.B_Cu),
          'CM5_GBE_TD2_N':([(6,94),(6,42.0),(149.979,42.0),land['CM5_GBE_TD2_N']],pcbnew.B_Cu),
          'CM5_GBE_TD2_P':([(4,96),(4,97),(3,97),(3,42.5),(149.821,42.5),land['CM5_GBE_TD2_P']],pcbnew.B_Cu),
          'CM5_GBE_TD1_P':([(90,90),(160,70),(160,35),(150.821,35),land['CM5_GBE_TD1_P']],pcbnew.B_Cu),
          'CM5_GBE_TD1_N':([(92,92),(161,70),(161,35.6),(150.979,35.6),land['CM5_GBE_TD1_N']],pcbnew.B_Cu),
          'CM5_GBE_TD0_N':([(94,94),(162,70),(162,37),(150.321,37),land['CM5_GBE_TD0_N']],pcbnew.B_Cu),
          'CM5_GBE_TD0_P':([(96,96),(163,70),(163,37.6),(150.479,37.6),land['CM5_GBE_TD0_P']],pcbnew.B_Cu)}
        for name,(pts,layer) in paths.items():
            track(b,nets[name],pts,layer)
        # Transition the right-side F.Cu source launch at the boundary, then
        # use B.Cu for every long bridge corridor.  At the remote island the
        # through-via lands directly on the retained official F.Cu handoff.
        for number,name in names_by_pad.items():
            if number in (4,6,10,12): via(b,nets[name],boundary[number])
        for name in paths: via(b,nets[name],land[name])
        # Expand the disposable outline before saving this branch.
        for d in list(b.GetDrawings()):
            if d.GetLayer()==pcbnew.Edge_Cuts: b.Remove(d)
        for a,z in (((2,35),(190,35)),((190,35),(190,145)),((190,145),(2,145)),((2,145),(2,35))): edge(b,a,z)
        b.Save(str(OUT)); print('saved',OUT); return
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
