"""Apply the passing CM5IO Ethernet island to a disposable acreage board."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_CANDIDATE.kicad_pcb'
FIX=ROOT/'CM5IO_PISXME_ETHERNET_TRANSPLANT_FIXTURE.kicad_pcb'
OUT=ROOT/'ACREAGE_CM5IO_ETHERNET_PHASE17.kicad_pcb'
DX=5.0

def v(x,y): return pcbnew.VECTOR2I_MM(x,y)
def short(name): return str(name).rsplit('/',1)[-1]
def net(board,name):
    # The fixture's common-tap node is only a provisional disposable alias;
    # production EDAC CT1..CT4 remain untouched until a pin-accurate support
    # adaptation is authored.
    if short(name)=='ETH_CT_COMMON': name='ETH_CT1'
    for n in board.GetNetsByName().values():
        if short(n.GetNetname())==short(name): return n
    raise RuntimeError(f'missing board net: {name}')
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def copy_track(board,item,n):
    if isinstance(item,pcbnew.PCB_VIA):
        q=pcbnew.PCB_VIA(board); x,y=xy(item.GetPosition()); q.SetPosition(v(x+DX,y)); q.SetWidth(pcbnew.FromMM(.45)); q.SetDrill(pcbnew.FromMM(.20)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); board.Add(q); return
    q=pcbnew.PCB_TRACK(board); a=xy(item.GetStart()); z=xy(item.GetEnd()); q.SetStart(v(a[0]+DX,a[1])); q.SetEnd(v(z[0]+DX,z[1])); q.SetLayer(item.GetLayer()); q.SetWidth(item.GetWidth()); q.SetNet(n); board.Add(q)
def main():
    # KiCad's Python bindings keep one active BOARD context; loading a second
    # board can invalidate wrappers from the first. Snapshot the transplant
    # objects before loading the acreage board.
    fixture=pcbnew.LoadBoard(str(FIX))
    snapshots={}
    for ref,newref in (('U6','U6'),('U9','U9'),('J9','J_ETH_TAP'),('C1','C_ETH')):
        src=fixture.FindFootprintByReference(ref); assert src is not None, ref
        x,y=xy(src.GetPosition())
        f=pcbnew.FOOTPRINT(src)
        f.SetReference(newref)
        snapshots[newref]=(f,x,y)
    tracks=[]
    for item in fixture.GetTracks():
        name=short(item.GetNetname())
        if name.startswith(('CM5_GBE_TD','ETH_','GBE_')):
            tracks.append((pcbnew.PCB_VIA(item) if isinstance(item,pcbnew.PCB_VIA) else pcbnew.PCB_TRACK(item),name))
    board=pcbnew.LoadBoard(str(BASE))
    # Replace only Ethernet island shells in this disposable candidate.
    for ref in ('U6','U9','J2'):
        f=board.FindFootprintByReference(ref)
        if f: board.Remove(f)
    # Keep the acreage EDAC footprint and move it to the oracle island.  The
    # transplant fixture's copied J2 shell intentionally is not reused: its
    # temporary common-tap pin assignment is not the production EDAC mapping.
    j2=pcbnew.FOOTPRINT(pcbnew.PCB_IO_KICAD_SEXPR().FootprintLoad(str(ROOT/'PiSXMe_RevA_Clean.pretty'), 'EDAC_A70_112_331N126'))
    if j2 is None: raise RuntimeError('cannot load EDAC footprint')
    srcj2=fixture.FindFootprintByReference('J2'); x,y=xy(srcj2.GetPosition())
    j2.SetReference('J2'); j2.SetPosition(v(x+DX,y)); board.Add(j2)
    for newref,(f,x,y) in snapshots.items():
        f.SetPosition(v(x+DX,y)); board.Add(f)
        # Rebind copied pads to the acreage board's net objects.  KiCad's
        # footprint copy preserves the source-board net pointer, which is not
        # valid after insertion into a different board.
        for pad in f.Pads():
            pname=short(pad.GetNetname())
            if pname:
                pad.SetNet(net(board,pname))
    # Remove any previous Ethernet routing from the candidate only.
    for item in list(board.GetTracks()):
        if short(item.GetNetname()).startswith(('CM5_GBE_TD','ETH_','GBE_')): board.Remove(item)
    for item,name in tracks: copy_track(board,item,net(board,name))
    board.Save(str(OUT)); print('saved',OUT)
if __name__=='__main__': main()
