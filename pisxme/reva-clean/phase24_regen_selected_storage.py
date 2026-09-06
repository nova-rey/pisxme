"""Regenerate selected-macro USB3/SATA corridors from native pad positions.

This disposable trial leaves clock/support routing for a separate pass. All
endpoints are resolved from the saved board; no expected graph is injected.
"""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
BASE = Path(os.environ.get('PISXME_STORAGE_BASE', str(R / 'PHASE24_SELECTED_MACRO_PLACEMENT.kicad_pcb')))
OUT = Path(os.environ.get('PISXME_STORAGE_OUT', str(R / 'PHASE24_SELECTED_MACRO_STORAGE_REGEN.kicad_pcb')))
F, B = pcbnew.F_Cu, pcbnew.B_Cu
W = pcbnew.FromMM(.15)

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def pos(board, ref, number):
    p = board.FindFootprintByReference(ref).FindPadByNumber(str(number))
    if p is None: raise RuntimeError(f'missing {ref}.{number}')
    q = p.GetPosition(); return pcbnew.ToMM(q.x), pcbnew.ToMM(q.y)
def track(board, net, points, layer):
    for a, z in zip(points, points[1:]):
        if a == z: continue
        t = pcbnew.PCB_TRACK(board); t.SetStart(V(*a)); t.SetEnd(V(*z))
        t.SetLayer(layer); t.SetWidth(W); t.SetNet(net); board.Add(t)
def via(board, net, point):
    q = pcbnew.PCB_VIA(board); q.SetPosition(V(*point)); q.SetWidth(pcbnew.FromMM(.5))
    q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(F, B); q.SetNet(net); board.Add(q)

b = pcbnew.LoadBoard(str(BASE))

# CM5 USB3 to U7. These corridors use the actual J7/U7 pad centers and keep
# the four conductors separated on F.Cu over In1.
usb = {
    'CM5_USB3_RX_N': ('128', '42', [(70.04,103.90),(78.0,114.0),(86.0,120.0)]),
    'CM5_USB3_RX_P': ('130', '43', [(70.04,104.30),(78.5,114.5),(86.5,120.5)]),
    'CM5_USB3_TX_N': ('140', '45', [(70.04,106.30),(79.5,116.0),(87.0,122.0)]),
    'CM5_USB3_TX_P': ('142', '46', [(70.04,106.70),(80.0,116.5),(87.5,122.5)]),
}
for name, (j7pad, u7pad, middle) in usb.items():
    net = b.FindNet('/CORE_CM5/' + name)
    track(b, net, [pos(b,'J7',j7pad)] + middle + [pos(b,'U7',u7pad)], F)

# SATA bridge-to-socket routes include the four required AC-coupling
# capacitors. Bridge-side copper uses the BRIDGE_SATA_* net and M.2-side
# copper uses the SATA_M2_* net; they are intentionally not shorted.
sata = {
    'TX_P': ('57','C30','2','1','1',(99.0,116.0),(105.0,116.0),(132.725,133.25)),
    'TX_N': ('56','C31','2','1','2',(100.0,132.0),(105.0,132.0),(140.275,133.0)),
    'RX_P': ('60','C32','2','1','3',(98.0,120.0),(106.0,120.0),(132.725,132.75)),
    'RX_N': ('59','C33','2','1','4',(101.0,128.0),(107.0,128.0),(140.275,132.5)),
}
for suffix, (u7pad, cap, cap_bridge, cap_m2, j3pad, v0, lane, finish) in sata.items():
    bridge = b.FindNet('/STORAGE/BRIDGE_SATA_' + suffix)
    m2 = b.FindNet('/STORAGE/SATA_M2_' + suffix)
    start = pos(b,'U7',u7pad)
    cap_b = pos(b,cap,cap_bridge); cap_m = pos(b,cap,cap_m2)
    finish = pos(b,'J3',j3pad)
    track(b, bridge, [start, v0, cap_b], F)
    track(b, m2, [cap_m, lane], F); via(b, m2, lane)
    # The long post-cap corridors are separated by their launch lanes.
    end_via = (finish[0]-2.0, finish[1])
    track(b, m2, [lane, end_via], B); via(b, m2, end_via)
    track(b, m2, [end_via, finish], F)

b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
