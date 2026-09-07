"""Saved-board native audit for the moved RTL9210B local support routes."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
PCB = ROOT / "PHASE24_RTL9210B_SUPPORT_RELOCATION_ROUTE_V2.kicad_pcb"
EXPECTED = {
    "XTAL_IN": {("U1", "53"), ("Y1", "1"), ("C1", "1")},
    "XTAL_OUT": {("U1", "54"), ("Y1", "2"), ("C2", "1")},
    "RSET": {("U1", "51"), ("R1", "1")},
    "RTL_1V1": {("U1", n) for n in ("16", "36", "40", "50", "55", "60", "63")} | {("C4", "1")},
}

def pad(board, ref, number):
    fp = next((x for x in board.GetFootprints()
               if str(x.GetReference()) == ref), None)
    if fp is None: raise AssertionError(f"missing footprint {ref}")
    result = fp.FindPadByNumber(number)
    if result is None: raise AssertionError(f"missing pad {ref}.{number}")
    return result

def component_keys(board, anchor):
    board.BuildConnectivity()
    result = {(anchor.GetParentFootprint().GetReference(), anchor.GetNumber())}
    result.update((x.GetParentFootprint().GetReference(), x.GetNumber())
                  for x in board.GetConnectivity().GetConnectedItems(anchor)
                  if isinstance(x, pcbnew.PAD))
    return result

def audit(board):
    for net, expected in EXPECTED.items():
        got = component_keys(board, pad(board, *next(iter(expected))))
        missing = expected - got
        if missing: raise AssertionError(f"{net}: missing {sorted(missing)}")
        print(f"PASS native {net}: {len(expected)} endpoints")

if __name__ == "__main__":
    audit(pcbnew.LoadBoard(str(PCB)))
