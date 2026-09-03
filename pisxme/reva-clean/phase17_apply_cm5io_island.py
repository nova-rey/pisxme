"""Apply the passing CM5IO Ethernet island to a disposable acreage board."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=Path(__import__('os').environ.get('PISXME_BASE', ROOT/'ACREAGE_CANDIDATE.kicad_pcb'))
FIX=ROOT/'CM5IO_PISXME_ETHERNET_TRANSPLANT_FIXTURE.kicad_pcb'
OUT=Path(__import__('os').environ.get('PISXME_OUT', ROOT/'ACREAGE_CM5IO_ETHERNET_PHASE17.kicad_pcb'))
DX=5.0

def v(x,y): return pcbnew.VECTOR2I_MM(x,y)
def short(name): return str(name).rsplit('/',1)[-1]
def net(board,name):
    # The fixture's common-tap node is only a provisional disposable alias;
    # production EDAC CT1..CT4 remain untouched until a pin-accurate support
    # adaptation is authored.
    if short(name)=='ETH_CT_COMMON': name='ETH_CT1'
    for candidate in (str(name), short(name), '/ETHERNET/'+short(name)):
        n=board.FindNet(candidate)
        if n is not None: return n
    raise RuntimeError(f'missing board net: {name}')
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def copy_track(board,item,n):
    if isinstance(item,pcbnew.PCB_VIA):
            q=pcbnew.PCB_VIA(board); x,y=xy(item.GetPosition()); q.SetPosition(v(x+DX,y)); q.SetWidth(pcbnew.FromMM(.45)); q.SetDrill(pcbnew.FromMM(.20)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNetCode(n.GetNetCode()); board.Add(q); return
    q=pcbnew.PCB_TRACK(board); a=xy(item.GetStart()); z=xy(item.GetEnd()); q.SetStart(v(a[0]+DX,a[1])); q.SetEnd(v(z[0]+DX,z[1])); q.SetLayer(item.GetLayer()); q.SetWidth(item.GetWidth()); q.SetNetCode(n.GetNetCode()); board.Add(q)
def main():
    # KiCad's Python bindings keep one active BOARD context; loading a second
    # board can invalidate wrappers from the first. Snapshot the transplant
    # objects before loading the acreage board.
    fixture=pcbnew.LoadBoard(str(FIX))
    snapshots={}
    for ref,newref in (('U6','U6'),('U9','U9'),('J2','J2'),('J9','J_ETH_TAP'),('C1','C_ETH')):
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
    for newref,(f,x,y) in snapshots.items():
        f.SetPosition(v(x+DX,y)); board.Add(f)
        # Rebind copied pads to the acreage board's net objects.  KiCad's
        # footprint copy preserves the source-board net pointer, which is not
        # valid after insertion into a different board.
        for pad in f.Pads():
            pname=short(pad.GetNetname())
            if newref=='J2':
                pname={1:'CM5_GBE_TD0_P',2:'CM5_GBE_TD0_N',3:'CM5_GBE_TD1_P',6:'CM5_GBE_TD1_N',
                       7:'CM5_GBE_TD2_P',8:'CM5_GBE_TD2_N',9:'CM5_GBE_TD3_P',10:'CM5_GBE_TD3_N',
                       11:'ETH_CT1',12:'ETH_CT2',13:'ETH_CT3',14:'ETH_CT4',15:'GBE_LED_Y_A',
                       16:'GBE_LED_Y_K',17:'GBE_LED_G_A',18:'GBE_LED_G_K',19:'GBE_SHIELD',20:'GBE_SHIELD'}.get(int(str(pad.GetNumber()) or 0),'')
            if pname:
                pad.SetNetCode(net(board,pname).GetNetCode())
    # Remove any previous Ethernet routing from the candidate only.
    for item in list(board.GetTracks()):
        if short(item.GetNetname()).startswith(('CM5_GBE_TD','ETH_','GBE_')): board.Remove(item)
    for item,name in tracks: copy_track(board,item,net(board,name))
    board.Save(str(OUT)); print('saved',OUT)
if __name__=='__main__': main()
