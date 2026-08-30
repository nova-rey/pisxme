"""Generate the native Phase 3 hierarchy shell from the proven KiCad fixture.

The fixture is used only as a parser-valid embedded-symbol template. All
production connectivity remains native KiCad and all placement/routing data is
discarded. This script is deterministic and is removed or superseded once
real Phase 3 symbols/sheets are authored.
"""

from pathlib import Path
from uuid import UUID

ROOT = Path(__file__).resolve().parent
TEMPLATE = Path(__file__).resolve().parents[2] / "work" / "skidl_spike" / "golden_hierarchy.kicad_sch"
ROOT_UUID = str(UUID(int=0x30000000000000000000000000000000))
SHEETS = (
    "CORE_CM5", "V100_PCIE", "V100_POWER", "POWER_INPUT", "REGULATORS",
    "ETHERNET", "STORAGE", "SERVICE", "COOLING", "DEBUG",
)
PORTS = {
    "CORE_CM5": ("CM5_PCIE", "CM5_USB3", "CM5_GBE", "SERVICE_USB2", "CM5_POWER"),
    "V100_PCIE": ("CM5_PCIE", "V100_PCIE", "V100_REFCLK", "V100_PERST"),
    "V100_POWER": ("V100_POWER_12V", "V100_GND", "V100_THERMAL"),
    "POWER_INPUT": ("12V_IN_A", "12V_IN_B", "12V_PROTECTED", "POWER_PG_FAULT"),
    "REGULATORS": ("12V_PROTECTED", "CM5_5V", "STORAGE_3V3", "BRIDGE_1V1_3V3"),
    "ETHERNET": ("CM5_GBE", "GBE_LED", "GBE_SHIELD", "ETH_POWER"),
    "STORAGE": ("CM5_USB3", "BRIDGE_SATA", "M2_SATA", "M2_3V3", "BRIDGE_CFG"),
    "SERVICE": ("SERVICE_USB2", "SERVICE_VBUS_SENSE", "SERVICE_RD", "SERVICE_GND"),
    "COOLING": ("COOLING_12V", "COOLING_PWM", "COOLING_TACH", "THERMAL_ALERT"),
    "DEBUG": ("UART", "RECOVERY", "POWER_PG_FAULT", "DEBUG_GND"),
}


def balanced(text: str, start: int) -> str:
    depth = 0
    quoted = False
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if quoted and escaped:
            escaped = False
        elif quoted and char == "\\":
            escaped = True
        elif char == '"':
            quoted = not quoted
        elif not quoted:
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    return text[start:index + 1]
    raise ValueError("unbalanced KiCad expression")


def make_uuid(number: int) -> str:
    return str(UUID(int=number))


def contract_symbol(name: str, ports: tuple[str, ...]) -> str:
    symbol_name = f"PiSXMeRevAClean:{name}_Contract"
    pins = "".join(
        f'''\n        (pin passive line
          (at -5.08 {index * 3} 0)
          (length 3.81)
          (name "{port}" (effects (font (size 1.27 1.27))))
          (number "{index + 1}" (effects (font (size 1.27 1.27)))))'''
        for index, port in enumerate(ports)
    )
    height = max(2.54, (len(ports) - 1) * 3 + 2.54)
    return f'''\n    (symbol "{symbol_name}"
      (pin_names (offset 1.0))
      (exclude_from_sim no)
      (in_bom yes)
      (on_board yes)
      (property "Reference" "X"
        (at 0 {-height / 2 - 1.27} 0)
        (effects (font (size 1.27 1.27))))
      (property "Value" "{name}_Contract"
        (at 0 {height / 2 + 1.27} 0)
        (effects (font (size 1.27 1.27))))
      (property "Footprint" ""
        (at 0 0 0)
        (effects (font (size 1.27 1.27)) (hide yes)))
      (property "Datasheet" "~"
        (at 0 0 0)
        (effects (font (size 1.27 1.27)) (hide yes)))
      (symbol "{name}_Contract_1_1"
        (rectangle (start -1.27 {-height / 2}) (end 1.27 {height / 2})
          (stroke (width 0.254) (type default)) (fill (type background)))
{pins}
      )
    )'''


def sheet_block(name: str, number: int) -> str:
    uid = make_uuid(0x10000000000000000000000000000000 + number)
    x = 35 + ((number - 1) % 5) * 35
    y = 45 + ((number - 1) // 5) * 30
    pins = "".join(
        f'''\n    (pin "{port}" bidirectional (at {x} {y + 2 + (index * 3)} 180)\n      (effects (font (size 1.27 1.27)) (justify left))\n      (uuid {make_uuid(0x40000000000000000000000000000000 + number * 100 + index)}))'''
        for index, port in enumerate(PORTS[name])
    )
    return f'''  (sheet
    (at {x} {y})
    (size 25 18)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (fields_autoplaced yes)
    (stroke (width 0.1524) (type solid))
    (fill (color 0 0 0 0.0))
    (uuid {uid})
    (property "Sheetname" "{name}" (at {x} {y - 1.27} 0)
      (effects (font (size 1.27 1.27)) (justify left bottom)))
    (property "Sheetfile" "{name}.kicad_sch" (at {x} {y + 19.27} 0)
      (effects (font (size 1.27 1.27)) (justify left top))){pins})
'''


def child(name: str, number: int, lib_symbols: str) -> str:
    sheet_path = f"{ROOT_UUID}/{make_uuid(0x10000000000000000000000000000000 + number)}"
    labels = "".join(
        f'''\n  (hierarchical_label "{port}"\n    (shape bidirectional)\n    (at 5 {10 + index * 3} 0)\n    (effects (font (size 1.27 1.27)) (justify left))\n    (uuid {make_uuid(0x50000000000000000000000000000000 + number * 100 + index)}))'''
        for index, port in enumerate(PORTS[name])
    )
    contract = contract_symbol(name, PORTS[name])
    instance_pins = "".join(
        f'    (pin "{index + 1}" (uuid {make_uuid(0x90000000000000000000000000000000 + number * 100 + index)}))\n'
        for index, _port in enumerate(PORTS[name])
    )
    contract_instance = f'''\n  (symbol
    (lib_id "PiSXMeRevAClean:{name}_Contract")
    (at 25 10 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom no)
    (on_board no)
    (dnp no)
    (uuid {make_uuid(0x80000000000000000000000000000000 + number)})
    (property "Reference" "X{name[:2]}"
      (at 25 5 0)
      (effects (font (size 1.27 1.27))))
    (property "Value" "{name}_Contract"
      (at 25 18 0)
      (effects (font (size 1.27 1.27))))
    (property "Footprint" ""
      (at 25 10 0)
      (effects (font (size 1.27 1.27)) (hide yes)))
    (property "Datasheet" "~"
      (at 25 10 0)
      (effects (font (size 1.27 1.27)) (hide yes)))
{instance_pins}
    (instances (project "PiSXMe_RevA_Clean"
      (path "/{sheet_path}" (reference "X{name[:2]}" ) (unit 1))))
  )'''
    contract_wires = "".join(
        f'''\n  (wire
    (pts (xy 5 {10 + index * 3}) (xy 19.92 {10 + index * 3}))
    (stroke (width 0) (type default))
    (uuid {make_uuid(0xa0000000000000000000000000000000 + number * 100 + index)}))'''
        for index, _port in enumerate(PORTS[name])
    )
    return f'''(kicad_sch (version 20230409) (generator "eeschema")
  (uuid {make_uuid(0x20000000000000000000000000000000 + number)})
  (paper "A4")
  {lib_symbols}{contract}
  {labels}
  {contract_wires}
  {contract_instance}
  (sheet_instances (path "/{sheet_path}" (page "{number}")))
)
'''.replace("\n  \n", "\n\n")


def main() -> None:
    source = TEMPLATE.read_text()
    start = source.index("(lib_symbols")
    lib_symbols = balanced(source, start)
    root = f'''(kicad_sch (version 20230409) (generator "eeschema")
  (uuid {make_uuid(0x30000000000000000000000000000000)})
  (paper "A4")
  (title_block (title "PiSXMe Rev A Clean") (date "2026-08-30") (rev "A")
    (company "nova-rey")
    (comment 1 "Phase 3 native hierarchy scaffold; no placement or routing")
    (comment 2 "PiSXMeRevAClean namespace")
    (comment 3 "Native KiCad connectivity authority")
    (comment 4 "M.2 SATA ONLY - NVMe NOT SUPPORTED"))
  {lib_symbols}
{''.join(sheet_block(name, index) for index, name in enumerate(SHEETS, 1))}
  (sheet_instances (path "/" (page "1")))
)
'''
    (ROOT / "PiSXMe_RevA_Clean.kicad_sch").write_text(root.replace("\n  \n", "\n\n"))
    for index, name in enumerate(SHEETS, 1):
        (ROOT / f"{name}.kicad_sch").write_text(child(name, index, lib_symbols))


if __name__ == "__main__":
    main()
