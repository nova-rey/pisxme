"""Disposable Phase-24 test: move the existing Ethernet island west and
regenerate only its CM5IO-derived copper.  No footprint or pad graph is
synthetically copied; the destination board's native footprints remain the
authority.  Support-net completion is intentionally a later neighborhood
step if this placement clears the high-speed corridor.
"""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CM5_GROUND_RIGHT_SAME_ROWS.kicad_pcb'
FIX=R/'CM5IO_DIRECT_J7_ETHERNET_FIXTURE.kicad_pcb'
OUT=R/'PHASE24_MACRO_ETH_WEST_MDI_REGEN.kicad_pcb'
DX,DY=-62.5,92.0
PREFIX=('CM5_GBE_TD','ETH_','GBE_')
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def moved(p):
    x,y=mm(p)
    return V(x+DX,y+DY) if x>60.0 else p
def dest_net(b,name):
    short=str(name).rsplit('/',1)[-1]
    if short=='ETH_GND': short='POWER_GND'
    n=b.FindNet(short)
    if n is None:
        n=pcbnew.NETINFO_ITEM(b,short); b.Add(n)
    return n.GetNetCode()
s=pcbnew.LoadBoard(str(FIX))
source_tracks=[]
for item in list(s.GetTracks()):
    name=str(item.GetNetname()).rsplit('/',1)[-1]
    if not name.startswith(PREFIX): continue
    if isinstance(item,pcbnew.PCB_VIA):
        q=item.GetPosition(); source_tracks.append(('via',(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)),name,item.GetWidth(pcbnew.F_Cu),item.GetDrill()))
    else:
        a,z=item.GetStart(),item.GetEnd(); source_tracks.append(('track',(pcbnew.ToMM(a.x),pcbnew.ToMM(a.y)),(pcbnew.ToMM(z.x),pcbnew.ToMM(z.y)),name,item.GetLayer(),item.GetWidth()))
del s
b=pcbnew.LoadBoard(str(BASE))
# Resolve destination net codes while the board is in its native loaded state;
# some KiCad-10 SWIG operations return opaque wrappers after footprint edits.
NETCODES={}
for name in set(x[2] if x[0]=='via' else x[3] for x in source_tracks):
    short=name.rsplit('/',1)[-1]
    if short=='ETH_GND': short='POWER_GND'
    n=b.FindNet(short)
    if n is None:
        n=pcbnew.NETINFO_ITEM(b,short); b.Add(n)
    NETCODES[name]=n.GetNetCode()
MDICODES={NETCODES.get(f'CM5_GBE_TD{i}_{p}') for i in range(4) for p in 'PN'}
for ref in ('J2','U6','U9'):
    f=b.FindFootprintByReference(ref)
    if f is None: raise RuntimeError(ref)
    q=f.GetPosition(); f.SetPosition(V(q.x/1e6+DX,q.y/1e6+DY))
for item in list(b.GetTracks()):
    if str(item.GetNetname()).rsplit('/',1)[-1].startswith(PREFIX): b.Remove(item)
records=[]
for item in source_tracks:
    if item[0]=='via':
        _,p,name,w,d=item; records.append(('via',moved(V(*p)),NETCODES[name],w,d))
    else:
        _,a,z,name,l,w=item; records.append(('track',moved(V(*a)),moved(V(*z)),NETCODES[name],l,w))
for rec in records:
    if rec[0]=='via':
        _,p,n,w,d=rec; q=pcbnew.PCB_VIA(b); q.SetPosition(p); q.SetWidth(max(w,pcbnew.FromMM(.50))); q.SetDrill(d); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNetCode(n); b.Add(q)
    else:
        _,a,z,n,l,w=rec
        if a==z: continue
        q=pcbnew.PCB_TRACK(b); q.SetStart(a); q.SetEnd(z); q.SetLayer(l); q.SetWidth(pcbnew.FromMM(.13208) if n in MDICODES else w); q.SetNetCode(n); b.Add(q)
# Zone refill is deliberately deferred to native kicad-cli for this
# disposable placement trial; the SWIG zone filler is unstable after a large
# cross-board transplant in KiCad 10.0.5.
b.Save(str(OUT)); print(OUT)
