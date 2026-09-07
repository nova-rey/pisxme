"""Native saved-board connectivity and negative-control audit for V184."""
from pathlib import Path
import tempfile
import pcbnew

HERE = Path(__file__).resolve().parent
PCB = HERE / "PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V184.kicad_pcb"
EXPECT = {
    "XTAL_IN": {("U1", "53"), ("Y1", "1"), ("C1", "1")},
    "XTAL_OUT": {("U1", "54"), ("Y1", "2"), ("C2", "1")},
    "RSET": {("U1", "51"), ("R1", "1")},
    "REFCLK_P": {("U1", "61"), ("J1", "55")},
    "REFCLK_N": {("U1", "62"), ("J1", "53")},
}


def key(item):
    return (item.GetParentFootprint().GetReference(), item.GetNumber())


def connected(board, ref, number):
    board.BuildConnectivity()
    pad = board.FindFootprintByReference(ref).FindPadByNumber(number)
    return {key(item) for item in board.GetConnectivity().GetConnectedItems(pad)
            if type(item).__name__ == "PAD"}


def assert_net(board, name):
    expected = EXPECT[name]
    root = next(iter(expected))
    assert expected <= connected(board, *root), (name, expected, connected(board, *root))


def main():
    board = pcbnew.LoadBoard(str(PCB))
    for name in EXPECT:
        assert_net(board, name)

    # Each negative control removes one necessary routed item from a disposable
    # saved copy; the audit must reject the resulting disconnected net.
    for name in ("XTAL_IN", "XTAL_OUT", "RSET", "REFCLK_P", "REFCLK_N"):
        bad = pcbnew.LoadBoard(str(PCB))
        victim = next(item for item in bad.GetTracks()
                      if type(item).__name__ == "PCB_TRACK" and item.GetNetname() == name)
        bad.RemoveNative(victim)
        with tempfile.NamedTemporaryFile(suffix=".kicad_pcb") as handle:
            bad.Save(handle.name)
            broken = pcbnew.LoadBoard(handle.name)
            try:
                assert_net(broken, name)
            except AssertionError:
                continue
            raise AssertionError(f"negative control unexpectedly passed for {name}")
    print("V184 native support connectivity PASS; five trace-removal negative controls PASS")


if __name__ == "__main__":
    main()
