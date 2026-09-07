"""Native saved-board audit for the isolated RTL_1V1 QFN fanout."""
from pathlib import Path
import pcbnew
PCB=Path("PHASE24_RTL9210B_1V1_PADFIELD_ISOLATION_V1.kicad_pcb")
def fp(b,r): return next(f for f in b.GetFootprints() if f.GetReference()==r)
def main():
 b=pcbnew.LoadBoard(str(PCB));b.BuildConnectivity();c=b.GetConnectivity();u=fp(b,"U1")
 root=u.FindPadByNumber("16")
 got={(x.GetParentFootprint().GetReference(),x.GetNumber()) for x in c.GetConnectedItems(root) if isinstance(x,pcbnew.PAD)}
 expected={("U1",n) for n in ("16","25","36","40","50","55","60","63")}|{("C4","1")}
 missing=expected-got
 if missing: raise SystemExit(f"FAIL missing RTL_1V1 endpoints: {sorted(missing)}")
 print("PASS native isolated RTL_1V1 padfield fanout: U1 pads 16/25/36/40/50/55/60/63 and C4.1")
if __name__=="__main__": main()
