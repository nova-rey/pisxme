"""Native PCB mapping gate for the corrected Ethernet netlist."""
from pathlib import Path
import os
import pcbnew

BOARD = Path(os.environ.get("PISXME_BOARD", Path(__file__).resolve().parents[2] / "pisxme" / "reva-clean" / "ACREAGE_PCIE_PHASE16.kicad_pcb"))
EXPECTED = {
    # TI TPD4E004DRYR pin authority: IO1/IO2 = 1/2, GND = 3,
    # IO3/IO4 = 4/5, VCC = 6.
    "U6": {"1": "CM5_GBE_TD0_P", "2": "CM5_GBE_TD0_N", "3": "ETH_GND", "4": "CM5_GBE_TD1_P", "5": "CM5_GBE_TD1_N", "6": "ETH_POWER"},
    "U9": {"1": "CM5_GBE_TD2_P", "2": "CM5_GBE_TD2_N", "3": "ETH_GND", "4": "CM5_GBE_TD3_P", "5": "CM5_GBE_TD3_N", "6": "ETH_POWER"},
    # EDAC physical MDI/tap/LED pads are direct; logical shield pins 17/18
    # terminate on the two numbered 1.60 mm shield lands 19/20.
    "J2": {
        "1": "CM5_GBE_TD0_P", "2": "CM5_GBE_TD0_N",
        "3": "CM5_GBE_TD1_P", "4": "CM5_GBE_TD1_N",
        "5": "CM5_GBE_TD2_P", "6": "CM5_GBE_TD2_N",
        "7": "CM5_GBE_TD3_P", "8": "CM5_GBE_TD3_N",
        "9": "ETH_CT1", "10": "ETH_CT2", "11": "ETH_CT3", "12": "ETH_CT4",
        "13": "GBE_LED_Y_A", "14": "GBE_LED_Y_K",
        "15": "GBE_LED_G_A", "16": "GBE_LED_G_K",
        "19": "GBE_SHIELD", "20": "GBE_SHIELD",
    },
}


def main():
    board = pcbnew.LoadBoard(str(BOARD))
    for ref, expected in EXPECTED.items():
        fp = board.FindFootprintByReference(ref)
        assert fp is not None, ref
        actual = {str(p.GetNumber()): p.GetNetname().removeprefix("/ETHERNET/") for p in fp.Pads() if str(p.GetNumber()) in expected}
        assert actual == expected, (ref, actual)
    print("phase17 Ethernet PCB pin mapping: PASS; ESD/MagJack pin authority preserved")


if __name__ == "__main__":
    main()
