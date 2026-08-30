"""Rebuild REGULATORS from the native KiCad child-sheet skeleton.

This deliberately reconstructs only the child file; the root hierarchy and
all other sheets remain untouched.  It is the regression path for avoiding
probe-era serialization drift in generated child sheets.
"""
from pathlib import Path
from phase3_scaffold import TEMPLATE, balanced, child, make_uuid
from phase14_tpsm_native_pin_probe import definition, N
from phase14_regulator_support_native import LOCAL_LIB

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "REGULATORS.kicad_sch"

def add_defs(lib_symbols: str) -> str:
    end = len(lib_symbols) - 1
    defs = "\n".join(definition(name) for name in (
        "TPSM63606RDLR_5V", "TPSM63606RDLR_3V3", "TPSM63606RDLR_1V1"))
    local = LOCAL_LIB.read_text()
    st = local.index('(symbol "PiSXMeRevAClean:VCAP_100NF"')
    defs += "\n" + balanced(local, st)
    return lib_symbols[:end].rstrip() + "\n" + defs + lib_symbols[end:]

def regulator(ref: str, lib: str, base: int, rail: str, x: float, y0: float) -> str:
    labels = []
    nets = {
        1:"12V_PROTECTED", 2:f"SW_{rail}", 3:f"CBOOT_{rail}",
        4:f"RBOOT_{rail}", 5:"12V_PROTECTED", 6:"POWER_GND",
        7:"VCC_INTERNAL", 8:rail, 9:rail, 10:f"FB_{rail}",
        11:"POWER_GND", 12:f"RT_{rail}", 13:f"PG_{rail}",
        14:"12V_PROTECTED", 15:"NC", 16:"12V_PROTECTED",
        17:"POWER_GND", 18:"POWER_GND", 19:"POWER_GND", 20:"POWER_GND",
    }
    for n in range(1, 21):
        # KiCad's schematic Y axis is inverted relative to the symbol-local
        # definition coordinates; the pin endpoint for local y=-20 is y0+20.
        y = y0 - (-20 + (n - 1) * 2)
        labels.append(
            f'(label "{nets[n]}" (at {x + 20} {y} 0) '
            f'(effects (font (size 1 1)) (justify left)) '
            f'(uuid {make_uuid(base + 30 + n)}))')
        labels.append(
            f'(wire (pts (xy {x + 20} {y}) (xy {x + 15} {y})) '
            f'(stroke (width 0) (type default)) (uuid {make_uuid(base + 60 + n)}))')
    pins = "\n".join(f'(pin "{n}" (uuid {make_uuid(base+n)}))' for n in range(1, 21))
    return "\n".join(labels) + f'''\n(symbol (lib_id "PiSXMeRevAClean:{lib}") (at {x} {y0} 0)
 (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
 (uuid {make_uuid(base)})
 (property "Reference" "{ref}" (at {x} {y0 - 11} 0) (effects (font (size 1.1 1.1))))
 (property "Value" "TPSM63606RDLR" (at {x} {y0 + 11} 0) (effects (font (size 1.1 1.1))))
 (property "MPN" "TPSM63606RDLR" (at {x} {y0} 0) (effects (font (size 1 1)) (hide yes)))
 (property "Footprint" "PiSXMeRevAClean:TPSM63606RDLR_RDL0020")
 {pins}
 (instances (project "PiSXMe_RevA_Clean" (path "/30000000-0000-0000-0000-000000000000/10000000-0000-0000-0000-000000000005" (reference "{ref}") (unit 1)))) )'''

def main() -> None:
    source = TEMPLATE.read_text()
    lib_start = source.index("(lib_symbols")
    lib = add_defs(balanced(source, lib_start))
    base = child("REGULATORS", 5, lib)
    base = base.replace('(property "Reference" "X_REGULATORS"', '(property "Reference" "X5"')
    base = base.replace('(reference "X_REGULATORS"', '(reference "X5"')
    # Root export requires the complete root-to-child UUID path so local labels
    # remain attributed to this child sheet.
    base = base.replace(
        '(sheet_instances (path "/30000000-0000-0000-0000-000000000000/10000000-0000-0000-0000-000000000005" (page "5")))',
        '(sheet_instances (path "/30000000-0000-0000-0000-000000000000/10000000-0000-0000-0000-000000000005" (page "5")))')
    marker = "  (sheet_instances "
    at = base.index(marker)
    data = "\n".join((
        regulator("U3", "TPSM63606RDLR_5V", 0xd5000000000000000000000000000000, "CM5_5V", 50, 95),
        regulator("U4", "TPSM63606RDLR_3V3", 0xd6000000000000000000000000000000, "BRIDGE_3V3", 50, 145),
        regulator("U5", "TPSM63606RDLR_1V1", 0xd7000000000000000000000000000000, "BRIDGE_1V1", 50, 195),
    ))
    OUT.write_text(base[:at] + data + "\n" + base[at:])
    print("native REGULATORS child rebuilt")

if __name__ == "__main__":
    main()
