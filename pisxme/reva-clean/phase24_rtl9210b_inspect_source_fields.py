"""Print native pad/track facts for RTL9210B source-field comparison."""
import collections
import sys
import pcbnew

for filename in sys.argv[1:]:
    board = pcbnew.LoadBoard(filename)
    print("\n" + filename)
    for ref in ("U1", "U2", "Y1", "C1", "C2", "R1", "R2", "R3", "C3", "C4", "C5"):
        fp = board.FindFootprintByReference(ref)
        if fp:
            print(ref, round(fp.GetPosition().x / 1e6, 3), round(fp.GetPosition().y / 1e6, 3), fp.GetOrientation() / 10)
    print("tracks", collections.Counter(track.GetNetname() for track in board.GetTracks()))
    for name in ("RTL_5V", "RTL_3V3", "RTL_1V1", "SPISI", "SPICLK", "SPISO3", "SPISO", "SPICS", "XTAL_IN", "XTAL_OUT", "RSET", "PEDET", "CLKREQ_N", "PERST_N", "REFCLK_P", "REFCLK_N"):
        if not board.FindNet(name):
            continue
        pads = []
        for fp in board.GetFootprints():
            for pad in fp.Pads():
                if pad.GetNetname() == name:
                    pads.append(f"{fp.GetReference()}.{pad.GetNumber()}@{pad.GetPosition().x/1e6:.2f},{pad.GetPosition().y/1e6:.2f}")
        print(name, "pads=", " ".join(pads), "tracks=", sum(t.GetNetname() == name for t in board.GetTracks()))
