#!/usr/bin/env python3
"""Native KiCad connectivity audit for the U7 oscillator support group."""
from pathlib import Path
import sys
import pcbnew

GROUPS = {
    'XI': {'Y1.1', 'R23.1', 'C42.1'},
    'XO': {'Y1.3', 'R23.2', 'C43.1'},
    'VSSOSC': {'Y1.2', 'Y1.4', 'C42.2', 'C43.2'},
}

def token(pad):
    return f'{pad.GetParentFootprint().GetReference()}.{pad.GetNumber()}'

board = pcbnew.LoadBoard(sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).with_name('PHASE24_SELECTED_MACRO_STORAGE_V26_CLOCK_V2_SOUTH40.kicad_pcb')))
board.BuildConnectivity(); graph = board.GetConnectivity()
for name, expected in GROUPS.items():
    ref, number = next(iter(expected)).split('.')
    pad = next(p for p in board.FindFootprintByReference(ref).Pads() if p.GetNumber() == number)
    actual = {token(x) for x in graph.GetConnectedItems(pad) if type(x).__name__ == 'PAD'}
    missing = expected - actual
    if missing: raise SystemExit(f'FAIL {name}: missing {sorted(missing)}')
    print(f'PASS {name}: {len(expected)} native pad endpoints connected')
print('PASS: native U7 clock connectivity')
