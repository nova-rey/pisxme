"""Native PCB mapping gate for the corrected Ethernet netlist."""
from pathlib import Path
import os
import pcbnew

BOARD = Path(os.environ.get("PISXME_BOARD", Path(__file__).resolve().parents[2] / "pisxme" / "reva-clean" / "ACREAGE_PCIE_PHASE16.kicad_pcb"))
EXPECTED = {
    # TI TPD4EUSB30DQAR flow-through authority: 1/10 and 2/9 are
    # channels 1/2, 3/8 are GND, and 4/7 and 5/6 are channels 3/4.
    "U6": {"1": "CM5_GBE_TD0_P", "2": "CM5_GBE_TD0_N", "3": "ETH_GND", "4": "CM5_GBE_TD1_N", "5": "CM5_GBE_TD1_P", "6": "CM5_GBE_TD1_P", "7": "CM5_GBE_TD1_N", "8": "ETH_GND", "9": "CM5_GBE_TD0_N", "10": "CM5_GBE_TD0_P"},
    "U9": {"1": "CM5_GBE_TD2_P", "2": "CM5_GBE_TD2_N", "3": "ETH_GND", "4": "CM5_GBE_TD3_N", "5": "CM5_GBE_TD3_P", "6": "CM5_GBE_TD3_P", "7": "CM5_GBE_TD3_N", "8": "ETH_GND", "9": "CM5_GBE_TD2_N", "10": "CM5_GBE_TD2_P"},
    # EDAC physical MDI/tap/LED pads are direct; logical shield pins 17/18
    # terminate on the two numbered 1.60 mm shield lands 19/20.
    "J2": {
        "1": "CM5_GBE_TD0_P", "2": "CM5_GBE_TD0_N",
        "3": "CM5_GBE_TD1_P", "6": "CM5_GBE_TD1_N",
        "7": "CM5_GBE_TD2_P", "8": "CM5_GBE_TD2_N",
        "9": "CM5_GBE_TD3_P", "10": "CM5_GBE_TD3_N",
        "11": "ETH_CT1", "12": "ETH_CT2", "13": "ETH_CT3", "14": "ETH_CT4",
        "15": "GBE_LED_Y_A", "16": "GBE_LED_Y_K",
        "17": "GBE_LED_G_A", "18": "GBE_LED_G_K",
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
