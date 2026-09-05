"""Build a disposable native schematic fixture for Ethernet support.

The fixture starts from the saved clean Ethernet child, imports the already
installed native Device:R/C definitions, and adds real support instances with
labels at their actual pin endpoints.  It does not edit production files.
"""
from pathlib import Path
from uuid import uuid4
import re
import shutil

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "ETHERNET.kicad_sch"
TEMPLATE = ROOT / "REGULATORS.kicad_sch"
OUTPUT = ROOT / "PHASE24_ETHERNET_SUPPORT_FIXTURE.kicad_sch"
ROOT_OUTPUT = ROOT / "PHASE24_ETHERNET_SUPPORT_FIXTURE_ROOT.kicad_sch"

def balanced(text, start):
    depth = 0
    quoted = escaped = False
    for i in range(start, len(text)):
        c = text[i]
        if quoted and escaped:
            escaped = False
        elif quoted and c == "\\":
            escaped = True
        elif c == '"':
            quoted = not quoted
        elif not quoted:
            if c == "(": depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0: return text[start:i+1]
    raise ValueError("unbalanced expression")

def definition(text, name):
    start = text.index(f'(symbol "Device:{name}"')
    return balanced(text, start)

def uid():
    return str(uuid4())

def label(name, x, y, global_=False):
    kind = "global_label" if global_ else "label"
    shape = ' (shape bidirectional)' if global_ else ''
    return f'({kind} "{name}"{shape} (at {x:g} {y:g} 0) (effects (font (size 1 1)) (justify left)) (uuid "{uid()}"))'

def passive(kind, ref, value, mpn, footprint, x, y, top, bottom, global_top=False, global_bottom=False):
    return f'''(symbol (lib_id "Device:{kind}") (at {x:g} {y:g} 0) (unit 1)
 (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (uuid "{uid()}")
 (property "Reference" "{ref}" (at {x:g} {y-4:g} 0) (effects (font (size 1 1))))
 (property "Value" "{value}" (at {x:g} {y+4:g} 0) (effects (font (size 1 1))))
 (property "MPN" "{mpn}" (at {x:g} {y:g} 0) (effects (font (size 1 1)) (hide yes)))
 (property "Footprint" "{footprint}" (at {x:g} {y:g} 0) (effects (font (size 1 1)) (hide yes)))
 (pin "1" (uuid "{uid()}")) (pin "2" (uuid "{uid()}"))
 (instances (project "PiSXMe_RevA_Clean" (path "/30000000-0000-0000-0000-000000000000/10000000-0000-0000-0000-000000000006" (reference "{ref}") (unit 1)))) )
 {label(top, x, y-3.81, global_top)}
 {label(bottom, x, y+3.81, global_bottom)}'''

def main():
    text = SOURCE.read_text()
    defs = definition(TEMPLATE.read_text(), "C") + "\n" + definition(TEMPLATE.read_text(), "R")
    lib_start = text.index("(lib_symbols")
    lib_end = lib_start + len(balanced(text, lib_start)) - 1
    text = text[:lib_end].rstrip() + "\n" + defs + "\n" + text[lib_end:]
    # The EDAC anodes are fed from the Ethernet supply; cathodes are sunk by
    # the two official CM5 Ethernet LED outputs through current-limit resistors.
    text = text.replace("GBE_LED_Y_A", "ETH_POWER")
    text = text.replace("GBE_LED_G_A", "ETH_POWER")
    parts = []
    for i, net in enumerate(("ETH_CT1", "ETH_CT2", "ETH_CT3", "ETH_CT4"), 1):
        x = 100 + i * 8
        parts.append(passive("C", f"C{47+i}", "22nF 100V", "GRM188R72A223KAC4J", "PiSXMeRevAClean:C_0603_1608Metric", x, 50, net, f"ETH_CT_BRANCH_{i}"))
        parts.append(passive("R", f"R{25+i}", "75R", "CRCW040275R0FKEDC", "PiSXMeRevAClean:R_0402_1005Metric", x, 60, f"ETH_CT_BRANCH_{i}", "ETH_CT_COMMON"))
    parts.append(passive("C", "C52", "1nF 2kV", "1206GC102KAT2A", "PiSXMeRevAClean:C_1206_3216Metric", 108, 75, "ETH_CT_COMMON", "GBE_SHIELD", False, True))
    parts.append(passive("R", "R30", "470R", "RK73G1ETTP4700D", "PiSXMeRevAClean:R_0402_1005Metric", 145, 50, "CM5_ETH_LED2", "GBE_LED_Y_K", True, False))
    parts.append(passive("R", "R31", "470R", "RK73G1ETTP4700D", "PiSXMeRevAClean:R_0402_1005Metric", 155, 50, "CM5_ETH_LED3", "GBE_LED_G_K", True, False))
    sheet = text.index("(sheet_instances")
    text = text[:sheet] + "\n" + "\n".join(parts) + "\n" + text[sheet:]
    OUTPUT.write_text(text)
    root = (ROOT / "PiSXMe_RevA_Clean.kicad_sch").read_text()
    root = root.replace('(property "Sheetfile" "ETHERNET.kicad_sch"',
                        '(property "Sheetfile" "PHASE24_ETHERNET_SUPPORT_FIXTURE.kicad_sch"')
    ROOT_OUTPUT.write_text(root)
    print(OUTPUT)
    print(ROOT_OUTPUT)

if __name__ == "__main__":
    main()
