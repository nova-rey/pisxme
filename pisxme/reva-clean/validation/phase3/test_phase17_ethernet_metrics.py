"""Native KiCad metric checks for the disposable Phase 17 Ethernet route."""
import math
import sys
import pcbnew

board = pcbnew.LoadBoard(sys.argv[1])
pair_nets = [f"CM5_GBE_TD{i}_{p}" for i in range(4) for p in "PN"]
expected_pads = {
    "CM5_GBE_TD0_P": "1", "CM5_GBE_TD0_N": "2",
    "CM5_GBE_TD1_P": "3", "CM5_GBE_TD1_N": "6",
    "CM5_GBE_TD2_P": "7", "CM5_GBE_TD2_N": "8",
    "CM5_GBE_TD3_P": "9", "CM5_GBE_TD3_N": "10",
}
lengths = {}
for name in pair_nets:
    net = board.FindNet(name)
    assert net is not None, f"missing net {name}"
    tracks = [x for x in board.GetTracks()
              if x.GetNetCode() == net.GetNetCode()
              and isinstance(x, pcbnew.PCB_TRACK)]
    assert tracks, f"no route segments for {name}"
    assert all(x.GetLayer() == pcbnew.F_Cu for x in tracks), f"{name} not F.Cu-only"
    lengths[name] = sum(math.hypot(x.GetEnd().x - x.GetStart().x,
                                   x.GetEnd().y - x.GetStart().y) / 1e6
                        for x in tracks)

j2 = board.FindFootprintByReference("J2")
assert j2 is not None, "missing MagJack J2"
for name, pad_number in expected_pads.items():
    pad = j2.FindPadByNumber(pad_number)
    assert pad is not None and pad.GetNetname().split("/")[-1] == name, \
        f"J2 pad mapping mismatch for {name}"

for i in range(4):
    skew = abs(lengths[f"CM5_GBE_TD{i}_P"] - lengths[f"CM5_GBE_TD{i}_N"])
    assert skew <= 1.0, f"pair {i} skew {skew:.3f} mm exceeds bound"
    print(f"pair {i}: P={lengths[f'CM5_GBE_TD{i}_P']:.3f} mm "
          f"N={lengths[f'CM5_GBE_TD{i}_N']:.3f} mm skew={skew:.3f} mm")
print("Phase 17 Ethernet route metrics: PASS; F.Cu-only MDI, J2 mapping, <=1 mm pair skew")
