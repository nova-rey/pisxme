"""Native RTL_5V endpoint audit and trace-removal negative control."""
import sys
import pcbnew

GROUP = [('U1', '17'), ('U1', '33'), ('C5', '1')]

def pads(board):
    return {(f.GetReference(), p.GetNumber()): p for f in board.GetFootprints() for p in f.Pads()}

def connected(board):
    board.BuildConnectivity(); ps = pads(board); root = ps[GROUP[0]]
    items = board.GetConnectivity().GetConnectedItems(root)
    return all(ps[key] in items for key in GROUP[1:])

def main(path):
    board = pcbnew.LoadBoard(path)
    if not connected(board):
        raise AssertionError('RTL_5V endpoint group is disconnected')
    trial = pcbnew.LoadBoard(path)
    victim = next((x for x in trial.GetTracks() if x.GetNetname() == 'RTL_5V'), None)
    if victim is None:
        raise AssertionError('no RTL_5V trace available for negative control')
    trial.RemoveNative(victim)
    if connected(trial):
        raise AssertionError('trace-removal negative control unexpectedly passed')
    print('RTL_5V: PASS U1.17/U1.33/C5.1; trace-removal negative control: PASS')

if __name__ == '__main__':
    main(sys.argv[1])
