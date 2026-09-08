"""Native endpoint/open inventory for the current RTL9210B disposable board."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BOARD = H / 'PHASE24_RTL9210B_ORIENTATION180_3V3_C3_JOIN_PROBE.kicad_pcb'
OUT = H / 'PHASE24_RTL9210B_SUPPORT_OPEN_INVENTORY.txt'

b = pcbnew.LoadBoard(str(BOARD))
b.BuildConnectivity()
q = {(f.GetReference(), str(p.GetNumber())): p
     for f in b.GetFootprints() for p in f.Pads() if p.GetNetCode()}
lines = [f'BOARD {BOARD.name}']
for name in ('PEDET', 'CLKREQ_N', 'PERST_N', 'RTL_3V3', 'SPISI', 'SPICLK', 'SPISO3',
             'SPISO', 'SPICS', 'RSET', 'XTAL_IN', 'XTAL_OUT', 'REFCLK_P',
             'REFCLK_N', 'LANE0_RXP', 'LANE0_RXN', 'LANE0_TXP', 'LANE0_TXN',
             'SSD_3V3'):
    n = b.FindNet(name)
    pads = [(ref, num) for (ref, num), p in q.items()
            if p.GetNetCode() == n.GetNetCode()]
    if not pads:
        continue
    component = b.GetConnectivity().GetConnectedItems(q[pads[0]])
    joined = sum(q[item] in component for item in pads)
    lines.append(f'{name}: pads={len(pads)} joined_from_first={joined} endpoints={pads}')
OUT.write_text('\n'.join(lines) + '\n')
print(OUT)
