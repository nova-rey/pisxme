"""Native saved-connectivity audit for the best V169 REFCLK topology."""
from pathlib import Path
import tempfile
import pcbnew

HERE = Path(__file__).resolve().parent
PCB = HERE / 'PHASE24_RTL9210B_REFCLK_SUPPORT_V169.kicad_pcb'
EXPECTED_P = {('U1','61'), ('J1','55')}
EXPECTED_N = {('U1','62'), ('J1','53')}

def key(item):
    fp = item.GetParentFootprint()
    return (fp.GetReference(), item.GetNumber()) if fp else None
def reached(board, ref, number):
    board.BuildConnectivity()
    pad = board.FindFootprintByReference(ref).FindPadByNumber(number)
    return {key(x) for x in board.GetConnectivity().GetConnectedItems(pad)
            if type(x).__name__ == 'PAD'}
def main():
    board = pcbnew.LoadBoard(str(PCB))
    for ref, number in (('U1','61'), ('U1','62')):
        got = reached(board, ref, number)
        expected = EXPECTED_P if number == '61' else EXPECTED_N
        assert expected <= got, (ref, number, sorted(got))
    broken = pcbnew.LoadBoard(str(PCB))
    victim = next(x for x in broken.GetTracks()
                   if type(x).__name__ == 'PCB_TRACK' and x.GetNetname() == 'REFCLK_P')
    broken.RemoveNative(victim)
    with tempfile.NamedTemporaryFile(suffix='.kicad_pcb') as f:
        broken.Save(f.name)
        check = pcbnew.LoadBoard(f.name)
        assert not (EXPECTED_P <= reached(check, 'U1', '61'))
    print('V169 native REFCLK connectivity PASS; trace-removal negative control PASS')
if __name__ == '__main__': main()
