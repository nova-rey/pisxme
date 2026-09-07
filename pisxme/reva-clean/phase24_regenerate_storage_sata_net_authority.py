"""Regenerate the four Path-A SATA socket-side pad nets from STORAGE authority.

This is a disposable derivation step, not a production PCB-only repair.  The
mapping is the reviewed source contract in STORAGE.kicad_sch and is checked
against the native M-key contact nets before any pad assignment is made.
"""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
BASE = Path(os.environ.get("PISXME_STORAGE_NET_BASE",
                          str(R / "PHASE24_DUAL_MODE_STORAGE_SUPPORT_ROUTED.kicad_pcb")))
OUT = Path(os.environ.get("PISXME_STORAGE_NET_OUT",
                         str(R / "PHASE24_STORAGE_SATA_NET_AUTHORITY_REGEN_20260906.kicad_pcb")))

FAMILY = {
    "C30.1": ("TUSB_SATA_TXP", "U13.38"),
    "C31.1": ("TUSB_SATA_TXN", "U13.37"),
    "C32.1": ("TUSB_SATA_RXP", "U13.36"),
    "C33.1": ("TUSB_SATA_RXN", "U13.35"),
}

def pkey(p):
    return f"{p.GetParentFootprint().GetReference()}.{p.GetNumber()}"

b = pcbnew.LoadBoard(str(BASE))
if b is None:
    raise RuntimeError(f"cannot load {BASE}")
pads = {pkey(p): p for f in b.GetFootprints() for p in f.Pads()}

for source, (net_name, socket_key) in FAMILY.items():
    if source not in pads or socket_key not in pads:
        raise RuntimeError(f"missing authority endpoint {source} or {socket_key}")
    socket_net = pads[socket_key].GetNetname()
    if socket_net not in (net_name, "/STORAGE/" + net_name) and not socket_net.endswith("/" + net_name):
        raise RuntimeError(f"selector-side authority mismatch {socket_key}: {socket_net} != {net_name}")
    net = b.FindNet(net_name) or b.FindNet("/STORAGE/" + net_name)
    if net is None:
        raise RuntimeError(f"missing native net object {net_name}")
    pads[source].SetNet(net)
    pads[source].SetNetCode(net.GetNetCode())

b.BuildListOfNets()
b.Save(str(OUT))
print(OUT)
