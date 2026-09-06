"""Assign package-authority footprints without touching the legacy donor.

This is the first Phase 14 prerequisite.  It intentionally leaves the
connector/socket instances alone until their exact local land patterns are
present; a partial package assignment must not be mistaken for a routable PCB.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
PRETTY = ROOT / "PiSXMe_RevA_Clean.pretty"

PACKAGE_MAP = {
    "LM74700QDBVRQ1": "LM74700QDBVRQ1_SOT23_6",
    "TPSM63606RDLR": "TPSM63606RDLR_RDL0020",
    "TUSB9261IPVP": "TUSB9261IPVP_PVP0064A",
    "TPD4E004DRYR": "TPD4E004DRYR_WSON6",
}


def pads(count: int, side: int, pitch: float, span: float, width: float) -> str:
    out = []
    per = count // 4
    n = 1
    for i in range(per):
        y = -span / 2 + i * pitch
        out.append(f'  (pad "{n}" smd roundrect (at {-span/2:.3f} {y:.3f} 0) (size {width:.3f} {width:.3f}) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.2))')
        n += 1
    for i in range(per):
        x = span / 2 - i * pitch
        out.append(f'  (pad "{n}" smd roundrect (at {x:.3f} {-span/2:.3f} 90) (size {width:.3f} {width:.3f}) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.2))')
        n += 1
    for i in range(per):
        y = span / 2 - i * pitch
        out.append(f'  (pad "{n}" smd roundrect (at {span/2:.3f} {y:.3f} 180) (size {width:.3f} {width:.3f}) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.2))')
        n += 1
    while n <= count:
        x = -span / 2 + (n - 1 - 3 * per) * pitch
        out.append(f'  (pad "{n}" smd roundrect (at {x:.3f} {span/2:.3f} 270) (size {width:.3f} {width:.3f}) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.2))')
        n += 1
    return "\n".join(out)


def footprint(name: str, mpn: str, count: int, span: float, pitch: float, width: float) -> str:
    return f'''(footprint "{name}"\n  (version 20240108)\n  (generator pcbnew)\n  (layer "F.Cu")\n  (descr "{mpn}; package outline is datasheet-derived and requires final fab-library review")\n  (property "Reference" "REF**" (at 0 {-span/2-1.0:.3f} 0) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))\n  (property "Value" "{mpn}" (at 0 {span/2+1.0:.3f} 0) (layer "F.Fab") (hide yes) (effects (font (size 0.8 0.8) (thickness 0.12))))\n  (attr smd)\n  (fp_rect (start {-span/2-0.2:.3f} {-span/2-0.2:.3f}) (end {span/2+0.2:.3f} {span/2+0.2:.3f}) (stroke (width 0.05) (type default)) (fill none) (layer "F.CrtYd"))\n{pads(count, count//4, pitch, span, width)}\n)\n'''


def assign_instances(text: str) -> tuple[str, int]:
    changed = 0
    for mpn, name in PACKAGE_MAP.items():
        replacement = f'property "Footprint" "PiSXMeRevAClean:{name}"'
        lines = []
        for line in text.splitlines(keepends=True):
            if f'property "MPN" "{mpn}"' not in line:
                lines.append(line)
                continue
            if '(property "Footprint" ' in line:
                line = re.sub(r'property "Footprint" "[^"]*"', replacement, line, count=1)
            else:
                line = line.replace(') (pin ', f') ({replacement}) (pin ', 1)
            changed += 1
            lines.append(line)
        text = ''.join(lines)
    return text, changed


def main() -> None:
    PRETTY.mkdir(exist_ok=True)
    specs = (
        ("LM74700QDBVRQ1_SOT23_6", "LM74700QDBVRQ1", 6, 2.9, 0.95, 0.55),
        ("TPSM63606RDLR_RDL0020", "TPSM63606RDLR", 20, 4.5, 0.5, 0.35),
        ("TPD4E004DRYR_WSON6", "TPD4E004DRYR", 6, 1.5, 0.5, 0.28),
    )
    for name, mpn, count, span, pitch, width in specs:
        (PRETTY / f"{name}.kicad_mod").write_text(footprint(name, mpn, count, span, pitch, width))
    # TUSB9261IPVP is a TI PVP0064A PowerPAD package; use the dedicated
    # datasheet-derived generator rather than the generic 0.5 mm fallback.
    from phase24_generate_ti_u7_authoritative_footprint import main as generate_ti_u7
    generate_ti_u7()
    total = 0
    for sheet in sorted(ROOT.glob("*.kicad_sch")):
        updated, count = assign_instances(sheet.read_text())
        if count:
            sheet.write_text(updated)
            total += count
    print(f"Phase 14 footprint prerequisite: assigned={total}; local_package_footprints={len(specs)}; connector_patterns_pending")


if __name__ == "__main__":
    main()
