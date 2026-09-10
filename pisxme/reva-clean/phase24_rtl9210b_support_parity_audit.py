"""Native support-network parity audit for the accepted RTL9210B Path-B board.

The endpoint table is an assertion of expected support ownership. Connectivity
is obtained only from pcbnew's saved-board graph; this script never adds edges.
Boundary-only nets are reported explicitly instead of being treated as pass.
"""
from pathlib import Path
import json
import pcbnew

HERE = Path(__file__).resolve().parent
BOARD = HERE / "PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb"
REPORT = HERE / "PHASE24_RTL9210B_PATHB_SUPPORT_PARITY.json"

GROUPS = {
    "CLKREQ_N": [("U1", "13"), ("R3", "1"), ("J1", "52")],
    "PEDET": [("U1", "8"), ("R2", "1"), ("J1", "69")],
    "RSET": [("U1", "51"), ("R1", "1")],
    "XTAL_IN": [("U1", "53"), ("Y1", "1"), ("C1", "1")],
    "XTAL_OUT": [("U1", "54"), ("Y1", "2"), ("C2", "1")],
    "RTL_1V1": [("U1", n) for n in ("16", "25", "36", "40", "50", "55", "60", "63")] + [("C4", "1")],
    "RTL_3V3": [("U1", n) for n in ("20", "34", "39", "52")] + [("U2", "3"), ("U2", "8"), ("R2", "2"), ("R3", "2"), ("C3", "1")],
    "RTL_5V": [("U1", "17"), ("U1", "33"), ("C5", "1")],
    "SPICS": [("U1", "24"), ("U2", "1")],
    "SPISO": [("U1", "23"), ("U2", "2")],
    "SPISI": [("U1", "18"), ("U2", "5")],
    "SPICLK": [("U1", "19"), ("U2", "6")],
    "SPISO3": [("U1", "22"), ("U2", "7")],
}
BOUNDARY_ONLY = {"RESET_N": [("U1", "3")], "ISOLATEB": [("U1", "12")],
                 "PERST_N": [("U1", "14"), ("J1", "50")]}

def getpad(board, ref, number):
    fp = board.FindFootprintByReference(ref)
    assert fp, f"missing {ref}"
    pad = fp.FindPadByNumber(number)
    assert pad, f"missing {ref}.{number}"
    return pad

def connected(board, a, z):
    board.BuildConnectivity()
    return z in board.GetConnectivity().GetConnectedItems(a)

board = pcbnew.LoadBoard(str(BOARD))
results = {}
for net, endpoints in GROUPS.items():
    pads = [getpad(board, ref, number) for ref, number in endpoints]
    assert all(p.GetNetname() == net for p in pads), f"pad-net mismatch in {net}"
    links = [connected(board, pads[0], p) for p in pads[1:]]
    assert all(links), f"native support connectivity failed for {net}"
    results[net] = {"endpoints": endpoints, "pad_net_identity": "PASS",
                    "native_connectivity": "PASS"}

for net, endpoints in BOUNDARY_ONLY.items():
    pads = [getpad(board, ref, number) for ref, number in endpoints]
    assert all(p.GetNetname() == net for p in pads), f"pad-net mismatch in {net}"
    results[net] = {"endpoints": endpoints, "native_connectivity": "BOUNDARY_ONLY"}

report = {
    "board": BOARD.name,
    "native_graph_only": True,
    "closed_support_groups": results,
    "boundary_only_open_groups": sorted(BOUNDARY_ONLY),
    "regression_flags": {"RESET_N_missing_external_endpoint": True,
                          "ISOLATEB_missing_external_endpoint": True},
    "verdict": "PASS_WITH_EXPLICIT_OPEN_BOUNDARIES",
}
REPORT.write_text(json.dumps(report, indent=2) + "\n")
print("RTL9210B native support-network parity: PASS")
print(f"closed support groups: {len(GROUPS)}; boundary-only open groups: {len(BOUNDARY_ONLY)}")
print("OPEN boundary-only nets: RESET_N, ISOLATEB, PERST_N")
print(f"wrote {REPORT}")
