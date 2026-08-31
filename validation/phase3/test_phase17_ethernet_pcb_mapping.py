"""Native PCB mapping gate for the corrected Ethernet netlist."""
from pathlib import Path
import os
import pcbnew

BOARD = Path(os.environ.get("PISXME_BOARD", Path(__file__).resolve().parents[2] / "pisxme" / "reva-clean" / "ACREAGE_PCIE_PHASE16.kicad_pcb"))
EXPECTED = {
    "U6": {"1": "CM5_GBE_TD0_P", "2": "CM5_GBE_TD0_N", "3": "CM5_GBE_TD1_P", "4": "CM5_GBE_TD1_N", "5": "ETH_POWER", "6": "ETH_GND"},
    "U9": {"1": "CM5_GBE_TD2_P", "2": "CM5_GBE_TD2_N", "3": "CM5_GBE_TD3_P", "4": "CM5_GBE_TD3_N", "5": "ETH_POWER", "6": "ETH_GND"},
    # Logical Ethernet symbol pins 1..18 land on EDAC physical pads 18..1.
    "J2": {
        "18": "CM5_GBE_TD0_P", "17": "CM5_GBE_TD0_N",
        "16": "CM5_GBE_TD1_P", "15": "CM5_GBE_TD1_N",
        "14": "CM5_GBE_TD2_P", "13": "CM5_GBE_TD2_N",
        "12": "CM5_GBE_TD3_P", "11": "CM5_GBE_TD3_N",
        "10": "ETH_CT1", "9": "ETH_CT2", "8": "ETH_CT3", "7": "ETH_CT4",
        "6": "GBE_LED_Y_A", "5": "GBE_LED_Y_K",
        "4": "GBE_LED_G_A", "3": "GBE_LED_G_K",
        "2": "GBE_SHIELD", "1": "GBE_SHIELD",
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
