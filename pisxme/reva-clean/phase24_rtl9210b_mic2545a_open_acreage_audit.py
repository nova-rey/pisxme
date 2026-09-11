"""Saved-board MIC2545A candidate audit with trace-removal controls."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
PCB = H / "PHASE24_RTL9210B_PATHB_V1603_V1517_MIC2545A_OPEN_ACREAGE_U1LOCAL015_CANDIDATE.kicad_pcb"

def p(b, ref, number):
    return b.FindFootprintByReference(ref).FindPadByNumber(str(number))

def connected(b, a, z):
    b.BuildConnectivity()
    return z in b.GetConnectivity().GetConnectedItems(a)

GROUPS = [
    (("U3", 1), ("U1", 12)),
    (("U3", 3), ("R15", 2)),
    (("U3", 4), ("R15", 1)),
    (("U3", 5), ("C18", 1)),
    (("U3", 7), ("R2", 2)),
    (("U3", 6), ("J1", 2)),
    (("U3", 8), ("J1", 2)),
]

b = pcbnew.LoadBoard(str(PCB))
for (ar, an), (zr, zn) in GROUPS:
    a, z = p(b, ar, an), p(b, zr, zn)
    assert a.GetNetname() == z.GetNetname(), f"net mismatch {ar}.{an}/{zr}.{zn}"
    assert connected(b, a, z), f"native connectivity missing {ar}.{an}/{zr}.{zn}"

# Signal/support controls remove one actual source-attached trace in a
# disposable copy; no expected graph edges are injected.  GND is intentionally
# omitted because the filled zone is an independent physical connection.
for (ar, an), (zr, zn) in [GROUPS[i] for i in (0, 2)]:
    q = pcbnew.LoadBoard(str(PCB))
    src, dst = p(q, ar, an), p(q, zr, zn)
    q.BuildConnectivity()
    victim = next((x for x in q.GetConnectivity().GetConnectedItems(src)
                   if isinstance(x, pcbnew.PCB_TRACK) and x.GetNetname() == src.GetNetname()), None)
    assert victim is not None, f"no source trace for {ar}.{an}"
    q.RemoveNative(victim)
    assert not connected(q, p(q, ar, an), p(q, zr, zn)), f"negative control passed {ar}.{an}"

print("PASS MIC2545A candidate native support connectivity; 2 trace-removal negative controls PASS; shared output and GND zone continuity audited")
