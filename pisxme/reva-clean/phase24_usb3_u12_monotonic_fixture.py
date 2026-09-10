"""Disposable J7-to-U12 USB3 monotonic escape discriminator.

This deliberately avoids grid search in the dense J7 field. RX and TX pairs
use separate permitted copper layers after explicit, pad-aware F.Cu dogbones;
the only retained footprints are the native CM5 connector and U12.
"""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / 'PHASE24_STORAGE_COPPER_SCRUBBED_V116.kicad_pcb'
OUT = R / 'PHASE24_USB3_U12_MONOTONIC_FIXTURE.kicad_pcb'
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.13208)


def V(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def pad(board, ref, number):
    item = board.FindFootprintByReference(ref).FindPadByNumber(str(number))
    if item is None:
        raise RuntimeError(f'missing {ref}.{number}')
    return item.GetPosition()


def seg(board, net, a, z, layer):
    if a == z:
        return
    item = pcbnew.PCB_TRACK(board)
    item.SetStart(a); item.SetEnd(z); item.SetLayer(layer)
    item.SetWidth(W); item.SetNet(net); board.Add(item)


def via(board, net, p):
    item = pcbnew.PCB_VIA(board)
    item.SetPosition(p); item.SetWidth(pcbnew.FromMM(.50))
    item.SetDrill(pcbnew.FromMM(.30)); item.SetLayerPair(F, B)
    item.SetNet(net); board.Add(item)


b = pcbnew.LoadBoard(str(BASE))
for item in list(b.GetFootprints()):
    if item.GetReference() not in ('J7', 'U12'):
        b.RemoveNative(item)
for item in list(b.GetTracks()):
    b.RemoveNative(item)
for zone in list(b.Zones()):
    b.RemoveNative(zone)

jobs = {
    'CM5_USB3_RX_N': ('128', '16', V(72.0, 103.9), V(148.0, 139.0), B),
    'CM5_USB3_RX_P': ('130', '15', V(74.5, 104.8), V(148.0, 138.0), B),
    'CM5_USB3_TX_N': ('140', '12', V(79.0, 107.5), V(148.0, 134.0), F),
    'CM5_USB3_TX_P': ('142', '11', V(80.0, 109.0), V(148.0, 133.0), F),
}
for name, (jp, up, source_escape, target_escape, layer) in jobs.items():
    net = b.FindNet('/CORE_CM5/' + name) or b.FindNet(name)
    if net is None:
        raise RuntimeError(f'missing native net {name}')
    source = pad(b, 'J7', jp); target = pad(b, 'U12', up)
    # First dogbone is outside the J7 pad column; no via-in-pad.
    seg(b, net, source, source_escape, F)
    via(b, net, source_escape)
    seg(b, net, source_escape, target_escape, layer)
    via(b, net, target_escape)
    seg(b, net, target_escape, target, F)

b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
