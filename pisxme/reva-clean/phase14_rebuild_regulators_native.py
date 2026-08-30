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
        7:f"VCC_{ref}_INTERNAL", 8:rail, 9:rail, 10:f"FB_{rail}",
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
    # Local labels keep every child connection explicit.  These two global
    # labels are the authoritative cross-hierarchy bridges to the root's
    # 12V_PROTECTED and POWER_GND nets; without them KiCad correctly prefixes
    # the child-local names with /REGULATORS/ in the exported netlist.
    bridges = "\n".join((
        f'(global_label "12V_PROTECTED" (shape bidirectional) (at {x + 20} {y0 + 20} 0) '
        f'(effects (font (size 1 1)) (justify left)) (uuid {make_uuid(base + 90)}))',
        f'(global_label "POWER_GND" (shape bidirectional) (at {x + 20} {y0 + 10} 0) '
        f'(effects (font (size 1 1)) (justify left)) (uuid {make_uuid(base + 91)}))',
    ))
    return "\n".join(labels) + "\n" + bridges + f'''\n(symbol (lib_id "PiSXMeRevAClean:{lib}") (at {x} {y0} 0)
 (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
 (uuid {make_uuid(base)})
 (property "Reference" "{ref}" (at {x} {y0 - 11} 0) (effects (font (size 1.1 1.1))))
 (property "Value" "TPSM63606RDLR" (at {x} {y0 + 11} 0) (effects (font (size 1.1 1.1))))
 (property "MPN" "TPSM63606RDLR" (at {x} {y0} 0) (effects (font (size 1 1)) (hide yes)))
 (property "Footprint" "PiSXMeRevAClean:TPSM63606RDLR_RDL0020")
 {pins}
 (instances (project "PiSXMe_RevA_Clean" (path "/30000000-0000-0000-0000-000000000000/10000000-0000-0000-0000-000000000005" (reference "{ref}") (unit 1)))) )'''

def main() -> None:
    # Preserve the native KiCad child serialization.  Reconstructing it from
    # the generic scaffold drops already-authoritative support instances and
    # is not a valid authoring path for this sheet.  This repair is idempotent
    # and only changes the association fields that the netlist audit proved
    # wrong.
    text = OUT.read_text()
    if '(global_label "12V_PROTECTED"' not in text:
        marker = '\t\t(uuid "d5000000-0000-0000-0000-00000000001f")\n\t)'
        bridge = '\n\t(global_label "12V_PROTECTED" (shape bidirectional) (at 70 115 0)\n\t\t(effects (font (size 1 1)) (justify left))\n\t\t(uuid "d5000000-0000-0000-0000-000000000090"))'
        text = text.replace(marker, marker + bridge, 1)
    if '(global_label "POWER_GND"' not in text:
        marker = '\t\t(uuid "d5000000-0000-0000-0000-000000000024")\n\t)'
        bridge = '\n\t(global_label "POWER_GND" (shape bidirectional) (at 70 105 0)\n\t\t(effects (font (size 1 1)) (justify left))\n\t\t(uuid "d5000000-0000-0000-0000-000000000091"))'
        text = text.replace(marker, marker + bridge, 1)
    text = text.replace('(label "VCC_INTERNAL"', '(label "VCC_U3_INTERNAL"', 1)
    text = text.replace('(label "VCC_INTERNAL"', '(label "VCC_U4_INTERNAL"', 1)
    text = text.replace('(label "VCC_INTERNAL"', '(label "VCC_U5_INTERNAL"', 1)
    OUT.write_text(text)
    print("native REGULATORS authority associations repaired")

if __name__ == "__main__":
    main()
