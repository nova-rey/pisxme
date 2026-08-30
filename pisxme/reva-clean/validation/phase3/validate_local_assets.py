"""Validate the two currently extracted clean-library assets.

This is deliberately a small structural check: it proves the CM5 symbol's
numeric pin set equals the donor-derived CM5 carrier footprint's numeric pad
set. It does not claim schematic-to-PCB connectivity or mechanical fit.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SYMBOL = ROOT / "PiSXMe_RevA_Clean.kicad_sym"
FOOTPRINT = ROOT / "PiSXMe_RevA_Clean.pretty" / "PiSXMeRevAClean_Raspberry_Pi_5_Compute_Module.kicad_mod"


def main() -> None:
    symbols = SYMBOL.read_text()
    start = symbols.index('(symbol "PiSXMeRevAClean:ComputeModule5-CM5"')
    end = symbols.index('(symbol "PiSXMeRevAClean:MagJack-A70-112-331N126"', start)
    pin_numbers = set(re.findall(r'\(number "([0-9]+)"', symbols[start:end]))
    pads = FOOTPRINT.read_text()
    pad_numbers = set(re.findall(r'\(pad "([0-9]+)"', pads))
    if pin_numbers != pad_numbers:
        raise SystemExit(
            f"CM5 pin/pad mismatch: symbol-only={sorted(pin_numbers - pad_numbers)} "
            f"footprint-only={sorted(pad_numbers - pin_numbers)}"
        )
    print(f"CM5 symbol pins={len(pin_numbers)} footprint pads={len(pad_numbers)} parity=PASS")


if __name__ == "__main__":
    main()

