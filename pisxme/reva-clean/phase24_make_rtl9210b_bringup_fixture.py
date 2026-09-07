#!/usr/bin/env python3
"""Make an isolated RTL9210B-CG bring-up PCB fixture.

This is deliberately not production CAD.  It captures the verified controller
and M-key pin ownership plus the complete support-net boundary needed for a
future virgin-chip experiment.  High-speed routing is intentionally left for
the follow-up SI author; no guessed copper is promoted by this generator.
"""
from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
FP = HERE / "authority-inventory/rtl9210b/RTL9210B-CG_QUALIFICATION.kicad_mod"
OUT = HERE / "PHASE24_RTL9210B_BRINGUP_FIXTURE.kicad_pcb"

NETS = [
    "GND", "RTL_5V", "RTL_3V3", "RTL_1V1", "SSD_3V3", "PEDET",
    "USB_TXP0", "USB_TXN0", "USB_RXP0", "USB_RXN0", "USB_DP", "USB_DM",
    "LANE0_TXP", "LANE0_TXN", "LANE0_RXP", "LANE0_RXN", "REFCLK_P",
    "REFCLK_N", "PERST_N", "CLKREQ_N", "SPICS", "SPICLK", "SPISI",
    "SPISO", "SPISO2", "SPISO3", "RSET", "XTAL_IN", "XTAL_OUT",
    "ISOLATEB", "DEVSLP", "UART_TX", "UART_RX", "JTAG_TMS", "JTAG_TDI",
    "JTAG_TCK", "JTAG_TDO",
]
NET = {name: i + 1 for i, name in enumerate(NETS)}

RTL_NET = {
    "3": "RESET_N",  # created below as an alias net for the fixture boundary
    "5": "JTAG_TCK", "6": "JTAG_TDI", "8": "PEDET", "9": "JTAG_TDO",
    "12": "ISOLATEB", "13": "CLKREQ_N", "14": "PERST_N",
    "16": "RTL_1V1", "17": "RTL_5V", "18": "SPISI", "19": "SPICLK",
    "20": "RTL_3V3", "21": "SPISO2", "22": "SPISO3", "23": "SPISO",
    "24": "SPICS", "25": "RTL_1V1", "26": "DEVSLP", "33": "RTL_5V",
    "34": "RTL_3V3", "36": "RTL_1V1", "37": "USB_DP", "38": "USB_DM",
    "39": "RTL_3V3", "40": "RTL_1V1", "41": "USB_TXP0", "42": "USB_TXN0",
    "45": "GND", "46": "USB_RXP0", "47": "USB_RXN0", "50": "RTL_1V1",
    "51": "RSET", "52": "RTL_3V3", "53": "XTAL_IN", "54": "XTAL_OUT",
    "55": "RTL_1V1", "60": "RTL_1V1", "61": "REFCLK_P", "62": "REFCLK_N",
    "63": "RTL_1V1", "64": "LANE0_RXP", "65": "LANE0_RXN", "66": "GND",
    "67": "LANE0_TXN", "68": "LANE0_TXP", "69": "GND",
}
NETS.insert(1, "RESET_N")
NET = {name: i + 1 for i, name in enumerate(NETS)}


def pad_line(number: str, x: float, y: float, sx: float, sy: float,
             net_name: str | None, shape: str = "oval") -> str:
    net = 0 if not net_name else NET[net_name]
    name = "" if not net_name else net_name
    return (f'    (pad "{number}" smd {shape} (at {x:.3f} {y:.3f}) '
            f'(size {sx:.3f} {sy:.3f}) (layers "F.Cu" "F.Paste" "F.Mask") '
            f'(net {net} "{name}"))')


def generic(ref: str, value: str, x: float, y: float,
            pads: list[tuple[str, str | None]], size=(1.0, 0.8)) -> str:
    sx, sy = size
    lines = [
        f'  (footprint "BRINGUP_{value}" (layer "F.Cu")',
        f'    (property "Reference" "{ref}" (at {x:.3f} {y - 1.5:.3f} 0) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))',
        f'    (property "Value" "{value}" (at {x:.3f} {y + 1.5:.3f} 0) (layer "F.Fab") hide (effects (font (size 0.7 0.7))))',
        '    (attr smd)',
    ]
    for i, (pad, net_name) in enumerate(pads):
        # Keep the disposable support pads physically separated.  This is a
        # fixture boundary, not a compact production footprint.
        pitch = max(1.2, sx + 0.4)
        px = x + (i - (len(pads) - 1) / 2) * pitch
        lines.append(pad_line(pad, px, y, sx, sy, net_name, "rect"))
    lines.append('  )')
    return '\n'.join(lines)


def main() -> None:
    source = FP.read_text(errors="replace")
    pad_re = re.compile(r'\(pad (\d+) smd (?:oval|rect).*?\(at ([^ )]+) ([^ )]+) ([^ )]+)\).*?\(size ([^ )]+) ([^ )]+)\)', re.S)
    rtl_pads: list[str] = []
    for m in pad_re.finditer(source):
        number, x, y, rot, sx, sy = m.groups()
        net_name = RTL_NET.get(number)
        if number == "69":
            rtl_pads.append(pad_line(number, 80, 62, 4.8, 4.8, "GND", "rect"))
        else:
            rtl_pads.append(pad_line(number, 80 + float(x), 62 + float(y), float(sx), float(sy), net_name))
    if len(rtl_pads) != 69:
        raise SystemExit(f"expected 69 RTL pads, got {len(rtl_pads)}")

    m2_pads = {
        41: (133.75, 62.725, "LANE0_RXN"), 43: (134.25, 62.725, "LANE0_RXP"),
        47: (135.25, 62.725, "LANE0_TXN"), 49: (135.75, 62.725, "LANE0_TXP"),
        50: (136.00, 70.275, "PERST_N"), 52: (136.50, 70.275, "CLKREQ_N"),
        53: (136.75, 62.725, "REFCLK_N"), 55: (137.25, 62.725, "REFCLK_P"),
        69: (140.75, 62.725, "PEDET"),
        2: (114.75, 62.725, "SSD_3V3"), 4: (115.25, 62.725, "SSD_3V3"),
        6: (115.75, 62.725, "SSD_3V3"), 8: (116.25, 62.725, "SSD_3V3"),
    }
    m2_lines = [
        '  (footprint "BRINGUP_M2_MKEY" (layer "F.Cu")',
        '    (property "Reference" "J1" (at 127 59 0) (layer "F.SilkS") (effects (font (size 0.9 0.9) (thickness 0.12))))',
        '    (property "Value" "M.2 Socket 3 M-key 2280" (at 127 75 0) (layer "F.Fab") hide (effects (font (size 0.7 0.7))))',
        '    (attr smd)',
    ]
    for number, (x, y, net_name) in m2_pads.items():
        m2_lines.append(pad_line(str(number), x, y, 0.30, 1.55, net_name, "rect"))
    m2_lines.append('  )')

    footprints = [
        '\n'.join(['  (footprint "RTL9210B-CG_QUALIFICATION" (layer "F.Cu")',
                   '    (property "Reference" "U1" (at 80 52 0) (layer "F.SilkS") (effects (font (size 0.9 0.9) (thickness 0.12))))',
                   '    (property "Value" "RTL9210B-CG" (at 80 72 0) (layer "F.Fab") hide (effects (font (size 0.7 0.7))))',
                   '    (attr smd)', *rtl_pads, '  )']),
        '\n'.join(m2_lines),
        generic("Y1", "XTAL_25MHz", 88, 48, [("1", "XTAL_IN"), ("2", "XTAL_OUT")], (1.0, 0.8)),
        generic("C1", "16pF_XTAL_IN", 91, 48, [("1", "XTAL_IN"), ("2", "GND")], (0.8, 0.8)),
        generic("C2", "16pF_XTAL_OUT", 94, 48, [("1", "XTAL_OUT"), ("2", "GND")], (0.8, 0.8)),
        generic("R1", "12k_RSET", 97, 48, [("1", "RSET"), ("2", "GND")], (0.8, 0.8)),
        generic("U2", "W25Q128_SPI_FLASH", 104, 48, [("1", "SPICS"), ("2", "SPISO"), ("3", "RTL_3V3"), ("4", "GND"), ("5", "SPISI"), ("6", "SPICLK"), ("7", "SPISO3"), ("8", "RTL_3V3")], (0.65, 0.65)),
        generic("C3", "RTL_3V3_DEC", 109, 48, [("1", "RTL_3V3"), ("2", "GND")], (0.8, 0.8)),
        generic("C4", "RTL_1V1_DEC", 112, 48, [("1", "RTL_1V1"), ("2", "GND")], (0.8, 0.8)),
        generic("C5", "RTL_5V_DEC", 115, 48, [("1", "RTL_5V"), ("2", "GND")], (0.8, 0.8)),
        generic("R2", "PEDET_PULLUP", 118, 48, [("1", "PEDET"), ("2", "RTL_3V3")], (0.8, 0.8)),
        generic("R3", "CLKREQ_PULLUP", 121, 48, [("1", "CLKREQ_N"), ("2", "RTL_3V3")], (0.8, 0.8)),
        generic("TP1", "SPI_PROGRAM_CS", 88, 78, [("1", "SPICS")], (1.2, 1.2)),
        generic("TP2", "SPI_PROGRAM_CLK", 92, 78, [("1", "SPICLK")], (1.2, 1.2)),
        generic("TP3", "SPI_PROGRAM_SI", 96, 78, [("1", "SPISI")], (1.2, 1.2)),
        generic("TP4", "SPI_PROGRAM_SO", 100, 78, [("1", "SPISO")], (1.2, 1.2)),
        generic("TP5", "GND_TEST", 104, 78, [("1", "GND")], (1.2, 1.2)),
        generic("TP6", "RESET_TEST", 108, 78, [("1", "RESET_N")], (1.2, 1.2)),
        generic("TP7", "UART_TX_TEST", 112, 78, [("1", "UART_TX")], (1.2, 1.2)),
        generic("TP8", "UART_RX_TEST", 116, 78, [("1", "UART_RX")], (1.2, 1.2)),
    ]
    layers = '(layers (0 "F.Cu" signal) (2 "B.Cu" signal) (4 "In1.Cu" power "In1.GND") (6 "In2.Cu" power "In2.PWR") (8 "In3.Cu" power "In3.PROTECTED_12V") (10 "In4.Cu" power "In4.GND") (5 "F.SilkS" user "f.silkscreen") (7 "B.SilkS" user "b.silkscreen") (25 "Edge.Cuts" user))'
    net_lines = '\n'.join(f'  (net {NET[n]} "{n}")' for n in NETS)
    outline = '\n'.join([
        '  (gr_rect (start 65 40) (end 145 85) (stroke (width 0.2) (type default)) (fill none) (layer "Edge.Cuts"))',
        '  (gr_text "RTL9210B PATH-B BRING-UP — NON-PRODUCTION" (at 105 82) (layer "F.SilkS") (effects (font (size 1 1) (thickness 0.15))))',
    ])
    OUT.write_text(
        '(kicad_pcb\n  (version 20260206) (generator pcbnew)\n'
        '  (general (thickness 1.6))\n  (paper "A4")\n  ' + layers + '\n'
        '  (setup (pad_to_mask_clearance 0))\n' + net_lines + '\n' +
        '\n'.join(footprints) + '\n' + outline + '\n)\n'
    )
    print(OUT)


if __name__ == "__main__":
    main()
