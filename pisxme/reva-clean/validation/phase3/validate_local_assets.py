"""Validate the two currently extracted clean-library assets.

This is deliberately a small structural check: it proves the selected
electrical pin sets equal their local footprint pad sets. It does not claim
schematic-to-PCB connectivity or mechanical fit.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SYMBOL = ROOT / "PiSXMe_RevA_Clean.kicad_sym"
FOOTPRINT = ROOT / "PiSXMe_RevA_Clean.pretty" / "PiSXMeRevAClean_Raspberry_Pi_5_Compute_Module.kicad_mod"
MAG_SYMBOL_NAME = 'PiSXMeRevAClean:MagJack-A70-112-331N126'
MAG_FOOTPRINT = ROOT / "PiSXMe_RevA_Clean.pretty" / "EDAC_A70_112_331N126.kicad_mod"


def symbol_block(symbols: str, name: str, next_name: str | None = None) -> str:
    start = symbols.index(f'(symbol "{name}"')
    end = symbols.index(f'(symbol "{next_name}"', start) if next_name else symbols.rindex('\n)')
    return symbols[start:end]


def numbered_pads(path: Path) -> set[str]:
    return set(re.findall(r'\(pad "([0-9]+)"', path.read_text()))


def main() -> None:
    symbols = SYMBOL.read_text()
    cm5 = symbol_block(
        symbols,
        'PiSXMeRevAClean:ComputeModule5-CM5',
        MAG_SYMBOL_NAME,
    )
    pin_numbers = set(re.findall(r'\(number "([0-9]+)"', cm5))
    pad_numbers = numbered_pads(FOOTPRINT)
    if pin_numbers != pad_numbers:
        raise SystemExit(
            f"CM5 pin/pad mismatch: symbol-only={sorted(pin_numbers - pad_numbers)} "
            f"footprint-only={sorted(pad_numbers - pin_numbers)}"
        )
    print(f"CM5 symbol pins={len(pin_numbers)} footprint pads={len(pad_numbers)} parity=PASS")

    mag = symbol_block(
        symbols,
        MAG_SYMBOL_NAME,
        None,
    )
    mag_pins = set(re.findall(r'\(number "([0-9]+)"', mag))
    mag_pads = numbered_pads(MAG_FOOTPRINT)
    if mag_pins != mag_pads:
        raise SystemExit(
            f"EDAC pin/pad mismatch: symbol-only={sorted(mag_pins - mag_pads)} "
            f"footprint-only={sorted(mag_pads - mag_pins)}"
        )
    assert not {'19', '20'} & mag_pins
    print(f"EDAC A70-112-331N126 pins={len(mag_pins)} pads={len(mag_pads)} parity=PASS; shield=mechanical-NPTH")


if __name__ == "__main__":
    main()
