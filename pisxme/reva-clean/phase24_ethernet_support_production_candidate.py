"""Make a disposable production-hierarchy candidate for Ethernet support.

This intentionally does not edit the production schematics.  It materializes
the sourced CT/LED support, replaces the opaque bundled LED hierarchy port
with the two official CM5 LED nets, and attaches those nets to the exact CM5
pad endpoints used by the saved CM5 symbol.
"""
from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import phase24_ethernet_support_fixture as fixture

OUT = ROOT / "PHASE24_ETHERNET_SUPPORT_PRODUCTION_CANDIDATE.kicad_sch"
ROOT_OUT = ROOT / "PHASE24_ETHERNET_SUPPORT_PRODUCTION_ROOT_CANDIDATE.kicad_sch"
CORE_OUT = ROOT / "PHASE24_ETHERNET_SUPPORT_PRODUCTION_CORE_CANDIDATE.kicad_sch"


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
                if depth == 0:
                    return text[start:i + 1]
    raise ValueError("unbalanced expression")


def remove_expr(text, needle):
    start = text.index(needle)
    return text[:start] + text[start + len(balanced(text, start)):]


def remove_pin_named(text, name):
    """Remove a native lib-symbol pin block by its authoritative pin name."""
    pos = 0
    while True:
        start = text.find('(pin passive line', pos)
        if start < 0:
            raise ValueError(f"pin {name} not found")
        block = balanced(text, start)
        if f'(name "{name}"' in block:
            return text[:start] + text[start + len(block):]
        pos = start + len(block)


def main():
    # Generate the authoritative disposable support child using the existing
    # native Device:R/C definitions and sourced MPNs.
    fixture.main()
    child = (ROOT / "PHASE24_ETHERNET_SUPPORT_FIXTURE.kicad_sch").read_text()

    # The aggregate LED hierarchy was the documented production mismatch.
    child = remove_expr(child, '(hierarchical_label "GBE_LED"')
    child = remove_pin_named(child, "GBE_LED")
    child = re.sub(
        r'\s*\(wire\s*\(pts \(xy 5 13\) \(xy 19\.92 13\)\).*?\(uuid [^)]+\)\)',
        '', child, count=1, flags=re.S)
    # CM5IO names are the authoritative source names for the two implemented
    # LEDs.  They attach to R30/R31 pin 1 in the generated child.
    child = child.replace("CM5_ETH_LED2", "ETH_LEDY")
    child = child.replace("CM5_ETH_LED3", "ETH_LEDG")
    x6 = child.index('(symbol\n    (lib_id "PiSXMeRevAClean:ETHERNET_Contract"')
    x6_end = child.index('(sheet_instances', x6)
    x6_block = child[x6:x6_end]
    x6_block = remove_expr(x6_block, '(pin "2"')
    child = child[:x6] + x6_block + child[x6_end:]
    OUT.write_text(child)

    root = (ROOT / "PiSXMe_RevA_Clean.kicad_sch").read_text()
    root = root.replace('(property "Sheetfile" "ETHERNET.kicad_sch"',
                        '(property "Sheetfile" "PHASE24_ETHERNET_SUPPORT_PRODUCTION_CANDIDATE.kicad_sch"')
    root = root.replace('(property "Sheetfile" "CORE_CM5.kicad_sch"',
                        '(property "Sheetfile" "PHASE24_ETHERNET_SUPPORT_PRODUCTION_CORE_CANDIDATE.kicad_sch"')
    root = remove_expr(root, '(pin "GBE_LED"')
    root = re.sub(
        r'\s*\(wire\s*\(pts \(xy 25 150\) \(xy 35 150\)\).*?\(uuid [^)]+\)\)',
        '', root, count=1, flags=re.S)
    root = remove_expr(root, '(global_label "GBE_LED"')
    ROOT_OUT.write_text(root)

    core = (ROOT / "CORE_CM5.kicad_sch").read_text()
    # The saved CM5 symbol's native loaded mating-view endpoints for pads 15
    # and 17 are the upper-right pair at y=64.44/61.90.  The lower-right
    # y=138.10/135.56 endpoints are SD pins and must retain their NC flags.
    # Remove only duplicated no-connect records at the actual LED endpoints;
    # pad 21 (LED_nACT) remains no-connect.
    core = re.sub(r'^\(no_connect \(at 127\.94 (?:64\.44|61\.9)\).*\n', '', core, flags=re.M)
    insert = (
        '\n(wire (pts (xy 127.94 64.44) (xy 130 64.44)) (stroke (width 0) (type default)) '
        '(uuid e3000000-0000-0000-0000-00000000f13))\n'
        '(global_label "ETH_LEDY" (shape bidirectional) (at 130 64.44 0) '
        '(effects (font (size 1 1)) (justify left)) (uuid e3000000-0000-0000-0000-00000000f15))\n'
        '(wire (pts (xy 127.94 61.9) (xy 130 61.9)) (stroke (width 0) (type default)) '
        '(uuid e3000000-0000-0000-0000-00000000f16))\n'
        '(global_label "ETH_LEDG" (shape bidirectional) (at 130 61.9 0) '
        '(effects (font (size 1 1)) (justify left)) (uuid e3000000-0000-0000-0000-00000000f17))\n'
    )
    marker = '(sheet_instances'
    core = core.replace(marker, insert + marker, 1)
    CORE_OUT.write_text(core)
    if "--promote" in sys.argv:
        # Promote only after the disposable native netlist/ERC check has been
        # run by the caller.  Restore production filenames in the root sheet.
        promoted_root = root.replace(
            "PHASE24_ETHERNET_SUPPORT_PRODUCTION_CANDIDATE.kicad_sch",
            "ETHERNET.kicad_sch",
        ).replace(
            "PHASE24_ETHERNET_SUPPORT_PRODUCTION_CORE_CANDIDATE.kicad_sch",
            "CORE_CM5.kicad_sch",
        )
        (ROOT / "ETHERNET.kicad_sch").write_text(child)
        (ROOT / "CORE_CM5.kicad_sch").write_text(core)
        (ROOT / "PiSXMe_RevA_Clean.kicad_sch").write_text(promoted_root)
        print("PROMOTED production Ethernet support hierarchy")
    print(OUT)
    print(ROOT_OUT)
    print(CORE_OUT)


if __name__ == "__main__":
    main()
