"""Audit that TPSM63606 switch-node default pins have no external copper."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parents[2]
BOARD = ROOT / "ACREAGE_U5_VOUT_PHASE15.kicad_pcb"


def main() -> None:
    board = pcbnew.LoadBoard(str(BOARD))
    expected = {
        "/REGULATORS/SW_CM5_5V": "U3",
        "/REGULATORS/CBOOT_CM5_5V": "U3",
        "/REGULATORS/RBOOT_CM5_5V": "U3",
        "/REGULATORS/SW_BRIDGE_3V3": "U4",
        "/REGULATORS/CBOOT_BRIDGE_3V3": "U4",
        "/REGULATORS/RBOOT_BRIDGE_3V3": "U4",
        "/REGULATORS/SW_BRIDGE_1V1": "U5",
        "/REGULATORS/CBOOT_BRIDGE_1V1": "U5",
        "/REGULATORS/RBOOT_BRIDGE_1V1": "U5",
    }
    for net_name, regulator in expected.items():
        net = next(n for n in board.GetNetsByName().values()
                   if n.GetNetname() == net_name)
        tracks = [x for x in board.GetTracks() if x.GetNet() == net]
        assert not tracks, f"external copper on {net_name}"
        pads = [(f.GetReference(), str(p.GetNumber()))
                for f in board.GetFootprints() for p in f.Pads()
                if p.GetNet() == net]
        assert not pads or (len(pads) == 1 and pads[0][0] == regulator), (net_name, pads)
    print("Phase 15 switch containment audit: PASS; no external SW/CBOOT/RBOOT copper")


if __name__ == "__main__":
    main()
