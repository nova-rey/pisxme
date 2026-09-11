"""Build a disposable native-grid probe for the clean schematic hierarchy.

This is deliberately not a production rewriter.  It copies the current root
and child sheets, snaps only root graphical coordinates and generated child
contract geometry to 1.27 mm, and leaves actual child circuit geometry alone.
The probe tests whether the repeated ERC warnings are authoring/grid defects.
"""
from pathlib import Path
import re
import shutil

HERE = Path(__file__).resolve().parent
OUT = HERE / ".phase24_schematic_contract_grid_probe2"
ROOT_NAME = "PiSXMe_RevA_Clean.kicad_sch"
CHILDREN = (
    "CORE_CM5", "V100_PCIE", "V100_POWER", "POWER_INPUT", "REGULATORS",
    "ETHERNET", "STORAGE", "SERVICE", "COOLING", "DEBUG",
)
STEP = 1.27


def snap(value):
    return f"{round(float(value) / STEP) * STEP:.8g}"


def snap_pairs(text, token):
    pattern = re.compile(
        rf"(\({token}\s+)(-?(?:\d+(?:\.\d*)?|\.\d+))(\s+)"
        rf"(-?(?:\d+(?:\.\d*)?|\.\d+))"
    )
    return pattern.sub(lambda m: m.group(1) + snap(m.group(2)) +
                       m.group(3) + snap(m.group(4)), text)


def root_probe(text):
    start = text.index("(sheet")
    head, graph = text[:start], text[start:]
    # Sheet geometry, pins, wires, and labels share this coordinate domain.
    graph = snap_pairs(graph, "at")
    graph = snap_pairs(graph, "xy")
    return head + graph


def child_probe(text, index):
    # Only the generated contract label/wire coordinate family is touched.
    # The scaffold emitted 3 mm pitch from x=5 mm.  Use the native 2.54 mm
    # grid, but preserve each label's name/UUID and the parent root graph.
    for contract_index in range(12):
        old_y = 10 + contract_index * 3
        new_y = 10.16 + contract_index * 2.54
        text = text.replace(f"(at 5 {old_y} 180)", f"(at 5.08 {new_y:.2f} 180)")
        text = text.replace(f"(xy 5 {old_y})", f"(xy 5.08 {new_y:.2f})")
        text = text.replace(f"(xy 19.92 {old_y})", f"(xy 20.32 {new_y:.2f})")
    return text


def main():
    if OUT.exists():
        raise SystemExit(f"refusing to overwrite existing disposable probe: {OUT}")
    OUT.mkdir()
    shutil.copy2(HERE / ROOT_NAME, OUT / ROOT_NAME)
    # Keep the native root graph unchanged in this discriminator.  Snapping
    # root coordinates independently can detach already-associated sheet
    # pins; the question here is specifically whether generated child
    # contract geometry is the warning source.
    for index, name in enumerate(CHILDREN, 1):
        path = HERE / f"{name}.kicad_sch"
        target = OUT / path.name
        shutil.copy2(path, target)
        target.write_text(child_probe(target.read_text(), index))
    # Keep the probe's library resolution identical to the live project.  The
    # probe is disposable, but native ERC must not be confounded by a missing
    # project table or custom footprint/symbol namespace.
    for name in (
        "sym-lib-table", "fp-lib-table",
        "PiSXMe_RevA_Clean_complete.kicad_sym", "Storage_DualMode.kicad_sym",
        "PiSXMe_RevA_Clean.kicad_pro",
    ):
        source = HERE / name
        if source.exists():
            shutil.copy2(source, OUT / name)
    pretty = HERE / "PiSXMe_RevA_Clean.pretty"
    if pretty.exists():
        shutil.copytree(pretty, OUT / pretty.name)
    print(OUT)


if __name__ == "__main__":
    main()
