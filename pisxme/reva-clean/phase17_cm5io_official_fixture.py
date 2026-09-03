"""Extract the official CM5IO Rev 2 Ethernet block as a disposable fixture."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "authority-inventory/cm5io-rev2/CM5IO.kicad_pcb"
OUT = ROOT / "CM5IO_ETHERNET_OFFICIAL_FIXTURE.kicad_pcb"

def main():
    board = pcbnew.LoadBoard(str(SRC))
    # Preserve the official board byte-for-byte at the PCB object level. This
    # is intentionally an exact disposable oracle copy: deleting thousands of
    # unrelated SWIG-owned tracks is not reliable in the KiCad 10 Flatpak ABI.
    board.Save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
