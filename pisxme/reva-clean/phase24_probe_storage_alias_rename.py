"""Disposable probe: normalize co-located STORAGE NC aliases by name.

Only exact STORAGE local-label records at the known duplicate coordinates are
renamed.  This is a probe, not a production promotion path; native ERC and
semantic netlist comparison decide whether the hypothesis is safe.
"""
from pathlib import Path
import argparse
import re

NAMES = {
    "NC_62": "JMS_CC1_NC", "NC_61": "JMS_CC2_NC", "NC_59": "JMS_GPIO10_NC",
    "NC_58": "JMS_GPIO11_NC", "NC_57": "JMS_GPIO12_NC", "NC_52": "JMS_XAVDDH",
    "NC_20": "JMS_AVDDL", "NC_19": "JMS_AVDD33", "NC_15": "JMS_RESET_N",
    "NC_14": "JMS_GPIO9_NC", "NC_13": "JMS_GPIO8_NC", "NC_10": "JMS_VBUS_SENSE",
    "NC_9": "JMS_GPIO5_NC", "NC_8": "JMS_GPIO4_NC", "NC_7": "JMS_SPI_CS_N_DNP",
    "NC_6": "JMS_VCCO", "NC_5": "JMS_SPI_SI_DNP", "NC_4": "JMS_SPI_SCK_DNP",
    "NC_3": "JMS_SPI_SO_DNP", "NC_2": "JMS_VCCK", "NC_1": "JMS_VDDREG_5V",
}

def end(text, start):
    depth = 0; quoted = escaped = False
    for i in range(start, len(text)):
        c = text[i]
        if quoted and escaped: escaped = False
        elif quoted and c == "\\": escaped = True
        elif c == '"': quoted = not quoted
        elif not quoted and c == '(': depth += 1
        elif not quoted and c == ')':
            depth -= 1
            if depth == 0: return i + 1
    raise ValueError("unbalanced label")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output", type=Path)
    a = ap.parse_args()
    text = a.input.read_text()
    edits = []
    pos = 0
    while True:
        m = re.search(r'\(label "([^"]+)"', text[pos:])
        if not m: break
        start = pos + m.start(); finish = end(text, start)
        name = m.group(1)
        record = text[start:finish]
        if name in NAMES and "(at 70 " in record:
            replacement = record.replace(f'(label "{name}"',
                                         f'(label "{NAMES[name]}"', 1)
            edits.append((start, finish, replacement))
        pos = finish
    for start, finish, replacement in reversed(edits):
        text = text[:start] + replacement + text[finish:]
    a.output.write_text(text)
    print(f"renamed={len(edits)} output={a.output}")

if __name__ == "__main__":
    main()
