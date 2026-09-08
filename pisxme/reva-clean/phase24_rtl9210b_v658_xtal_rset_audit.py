"""Native saved-board audit for V658 XTAL/RSET, with trace-removal control."""
from pathlib import Path
import sys
import pcbnew

TARGET={"XTAL_IN":(("U1","53"),("Y1","1"),("C1","1")),"XTAL_OUT":(("U1","54"),("Y1","2"),("C2","1")),"RSET":(("U1","51"),("R1","1"))}
def pad(b,r,n):
    f=b.FindFootprintByReference(r); assert f is not None, r
    p=f.FindPadByNumber(n); assert p is not None, f'{r}.{n}'; return p
def key(x): return (str(x.GetParentFootprint().GetReference()),str(x.GetNumber()))
def audit(b):
    b.BuildConnectivity(); c=b.GetConnectivity()
    for net,ends in TARGET.items():
        got={key(x) for x in c.GetConnectedItems(pad(b,*ends[0])) if isinstance(x,pcbnew.PAD)}|{ends[0]}
        assert not (set(ends)-got), f'{net} missing {sorted(set(ends)-got)}'
def main(path):
    b=pcbnew.LoadBoard(str(path)); audit(b)
    bad=pcbnew.LoadBoard(str(path)); bad.BuildConnectivity(); victim=next((x for x in bad.GetTracks() if x.GetNetname()=='XTAL_OUT' and isinstance(x,pcbnew.PCB_TRACK)),None)
    assert victim is not None; bad.RemoveNative(victim)
    try: audit(bad)
    except AssertionError: print('PASS V658 native XTAL_IN/XTAL_OUT/RSET audit and negative control'); return
    raise AssertionError('negative control unexpectedly passed')
if __name__=='__main__': main(Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('PHASE24_RTL9210B_XTAL_RSET_COHERENT_PROBE.kicad_pcb'))
