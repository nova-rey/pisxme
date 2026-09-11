"""Saved-board authority/parity census for the isolated RTL9210B Path-B candidate.

All connectivity claims come from KiCad's native connectivity graph built from
the saved pads, tracks, vias, and zones. The tables below are assertions only;
they never add graph edges.
"""
from pathlib import Path
import json
import sys
import pcbnew

HERE = Path(__file__).resolve().parent
BOARD = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb"
if not BOARD.is_absolute():
    BOARD = HERE / BOARD
REPORT = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "PHASE24_RTL9210B_PATHB_CENSUS.json"
if not REPORT.is_absolute():
    REPORT = HERE / REPORT

U1_PADS = {
    "REFCLK_P": "61", "REFCLK_N": "62",
    "LANE0_RXP": "64", "LANE0_RXN": "65",
    "LANE0_TXN": "67", "LANE0_TXP": "68",
}
J1_PADS = {
    "REFCLK_P": "55", "REFCLK_N": "53",
    "LANE0_RXP": "43", "LANE0_RXN": "41",
    "LANE0_TXN": "47", "LANE0_TXP": "49",
}
REQUIRED_U1_NETS = {
    "RESET_N": "3", "PEDET": "8", "ISOLATEB": "12",
    "CLKREQ_N": "13", "PERST_N": "14", "RSET": "51",
    "XTAL_IN": "53", "XTAL_OUT": "54", "RTL_1V1": "16",
    "RTL_5V": "17", "RTL_3V3": "20", "GND": "45",
}

def pad(board, ref, number):
    fp = board.FindFootprintByReference(ref)
    assert fp, f"missing footprint {ref}"
    result = fp.FindPadByNumber(number)
    assert result, f"missing {ref}.{number}"
    return result

def native_join(board, a, z):
    board.BuildConnectivity()
    return z in board.GetConnectivity().GetConnectedItems(a)

def remove_one_signal_track(board, net_name):
    board.BuildConnectivity()
    tracks = [x for x in board.GetTracks()
              if isinstance(x, pcbnew.PCB_TRACK) and x.GetNetname() == net_name]
    assert tracks, f"no removable track for {net_name}"
    board.RemoveNative(tracks[0])

board = pcbnew.LoadBoard(str(BOARD))
assert board.FindFootprintByReference("U1")
assert board.FindFootprintByReference("J1")
assert "PiSXMe:" not in BOARD.read_text(errors="replace")

pad_net_assertions = {}
for net_name, number in U1_PADS.items():
    actual = pad(board, "U1", number).GetNetname()
    assert actual == net_name, f"U1.{number}: expected {net_name}, got {actual}"
    jactual = pad(board, "J1", J1_PADS[net_name]).GetNetname()
    assert jactual == net_name, f"J1.{J1_PADS[net_name]}: expected {net_name}, got {jactual}"
    pad_net_assertions[f"U1.{number}"] = actual
    pad_net_assertions[f"J1.{J1_PADS[net_name]}"] = jactual

for net_name, number in REQUIRED_U1_NETS.items():
    actual = pad(board, "U1", number).GetNetname()
    assert actual == net_name, f"U1.{number}: expected {net_name}, got {actual}"
    pad_net_assertions[f"U1.{number}"] = actual

for net_name in U1_PADS:
    assert native_join(board, pad(board, "U1", U1_PADS[net_name]),
                       pad(board, "J1", J1_PADS[net_name])), net_name

negative_controls = {}
for net_name in U1_PADS:
    negative = pcbnew.LoadBoard(str(BOARD))
    remove_one_signal_track(negative, net_name)
    still_joined = native_join(negative, pad(negative, "U1", U1_PADS[net_name]),
                               pad(negative, "J1", J1_PADS[net_name]))
    assert not still_joined, f"negative control did not fail for {net_name}"
    negative_controls[net_name] = "PASS"

net_names = sorted(str(name) for name in board.GetNetsByName() if str(name))
report = {
    "board": BOARD.name,
    "native_graph": True,
    "legacy_namespace_absent": True,
    "u1_pad_net_assertions": pad_net_assertions,
    "six_net_endpoint_connectivity": "PASS",
    "six_trace_removal_negative_controls": negative_controls,
    "net_count": len(net_names),
    "nets": net_names,
}
REPORT.write_text(json.dumps(report, indent=2) + "\n")
print("RTL9210B Path-B saved-board authority/parity census PASS")
print(f"native six-net endpoint connectivity PASS; {len(negative_controls)} negative controls PASS")
print(f"wrote {REPORT}")
