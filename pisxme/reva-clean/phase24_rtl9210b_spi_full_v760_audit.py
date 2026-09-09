"""Native saved-board audit and negative controls for V760's five SPI nets."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
PCB = H / 'PHASE24_RTL9210B_SPI_QFN_SOURCE_FANOUT_FULL_SPI_V760.kicad_pcb'
TARGET = {
    'SPISI': ('U1.18', 'U2.5'), 'SPICLK': ('U1.19', 'U2.6'),
    'SPISO3': ('U1.22', 'U2.7'), 'SPISO': ('U1.23', 'U2.2'),
    'SPICS': ('U1.24', 'U2.1'),
}

def key(p):
    return f'{p.GetParentFootprint().GetReference()}.{p.GetNumber()}'

def pad_map(board):
    return {key(p): p for f in board.GetFootprints() for p in f.Pads()}

def connected_pad_keys(board, pad):
    board.BuildConnectivity()
    return {key(x) for x in board.GetConnectivity().GetConnectedItems(pad)
            if type(x).__name__ in ('PAD', 'PCB_PAD')} | {key(pad)}

def assert_endpoints(board):
    pads = pad_map(board)
    for net, ends in TARGET.items():
        for endpoint in ends:
            assert endpoint in pads, f'missing endpoint {endpoint}'
            assert str(pads[endpoint].GetNetname()) == net, (
                f'{endpoint}: expected {net}, got {pads[endpoint].GetNetname()}')
        reached = connected_pad_keys(board, pads[ends[0]])
        assert set(ends) <= reached, f'{net} disconnected: {sorted(reached)}'
        print(f'{net}: PASS {ends[0]} <-> {ends[1]}')

def negative_control(path, net):
    board = pcbnew.LoadBoard(str(path)); pads = pad_map(board)
    source, dest = TARGET[net]
    board.BuildConnectivity()
    source_pad = pads[source]
    candidates = [x for x in board.GetConnectivity().GetConnectedItems(source_pad)
                  if type(x).__name__ == 'PCB_TRACK' and x.GetNetname() == net]
    assert candidates, f'{net}: no source-connected track for negative control'
    for candidate in candidates:
        trial = pcbnew.LoadBoard(str(path))
        victim = next((x for x in trial.GetTracks()
                       if type(x).__name__ == 'PCB_TRACK'
                       and x.GetNetname() == net
                       and x.GetStart() == candidate.GetStart()
                       and x.GetEnd() == candidate.GetEnd()), None)
        if victim is None:
            continue
        trial.RemoveNative(victim); trial.BuildConnectivity()
        trial_pads = pad_map(trial)
        if dest not in connected_pad_keys(trial, trial_pads[source]):
            print(f'{net}: PASS source-track negative control')
            return
    raise AssertionError(f'{net}: every tested trace removal still connected')

board = pcbnew.LoadBoard(str(PCB))
assert_endpoints(board)
for net in TARGET:
    negative_control(PCB, net)
print('V760 five-net SPI native connectivity and negative controls: PASS')
