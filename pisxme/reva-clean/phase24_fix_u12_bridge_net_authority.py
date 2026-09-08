#!/usr/bin/env python3
"""Migrate the integrated U12 symbol to the reviewed bridge-side USB nets."""
from pathlib import Path
from phase3_scaffold import balanced

ROOT = Path(__file__).resolve().parent
SCHEMATIC = ROOT / "STORAGE.kicad_sch"

PIN_NETS = {
    # U12 RX pins are the direct bridge receive side in this implementation;
    # only the bridge TX pins have the explicit AC-coupling capacitor nets.
    "22": "USB_RXN1", "23": "USB_RXP1",
    "24": "JMS_USB3_TXN", "25": "JMS_USB3_TXP",
}

def main():
    text = SCHEMATIC.read_text()
    marker = '(symbol "PiSXMeRevAClean:HD3SS6126_RUA0042A"'
    start = text.index(marker)
    end = start + len(balanced(text, start))
    block = text[start:end]
    for pin, net in PIN_NETS.items():
        number = block.index(f'(number "{pin}"')
        pin_start = block.rfind('(pin passive line', 0, number)
        name = block.index('(name "', pin_start)
        value = name + len('(name "')
        close = block.index('"', value)
        block = block[:value] + net + block[close:]
        if block[value:value + len(net)] != net:
            raise SystemExit(f"could not migrate U12 pin {pin}")
    SCHEMATIC.write_text(text[:start] + block + text[end:])
    print("migrated U12 pins 22-25 to bridge-side USB3 net authority")

if __name__ == "__main__":
    main()
