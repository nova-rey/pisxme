"""Saved-board native RSET endpoint audit with a serialized negative control."""
from pathlib import Path
import pcbnew

PCB=Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V11_NATIVE_RSET.kicad_pcb")
def pad(b, ref, num):
    return next(f.FindPadByNumber(num) for f in b.GetFootprints() if f.GetReference()==ref)
def connected(b, a, ref, num):
    b.BuildConnectivity(); c=b.GetConnectivity(); want=pad(b,ref,num)
    return want in c.GetConnectedItems(a)
def main():
    b=pcbnew.LoadBoard(str(PCB)); a=pad(b,"U1","51")
    if not connected(b,a,"R1","1"): raise SystemExit("FAIL U1.51/R1.1 disconnected")
    # Remove the sole donor endpoint segment at R1.1 in a disposable in-memory copy.
    removed=False
    r1=pad(b,"R1","1").GetPosition()
    for item in list(b.GetTracks()):
        if item.GetNetname()=="RSET" and (item.GetStart()==r1 or item.GetEnd()==r1):
            b.Remove(item); removed=True
    if not removed: raise SystemExit("FAIL negative-control setup found no RSET endpoint")
    if connected(b,a,"R1","1"): raise SystemExit("FAIL negative control did not disconnect RSET")
    print("PASS native RSET endpoints; negative control fails as required")
if __name__=="__main__": main()
