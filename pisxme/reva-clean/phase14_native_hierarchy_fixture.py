"""Create a disposable native hierarchy fixture through kicad-sch-api."""
from pathlib import Path
from bridge.schematic_backend import SchematicBackend

OUT = Path(__file__).resolve().parent / "native-hierarchy-fixture"

def main():
    OUT.mkdir(exist_ok=True)
    backend = SchematicBackend()
    child_path = OUT / "child.kicad_sch"
    root_path = OUT / "root.kicad_sch"

    child = backend.create("child")
    child.schematic.components.add("Device:R", reference="R1", value="10k", position=(100.33, 100.33))
    child.schematic.components.add("Device:C", reference="C1", value="100n", position=(119.38, 100.33))
    child.schematic.add_wire_between_pins("R1", "1", "C1", "1")
    child.schematic.add_hierarchical_label("CHILD_SIG_A", (100.33, 96.52), shape="output")
    child.schematic.add_hierarchical_label("CHILD_SIG_B", (119.38, 96.52), shape="output")
    child.save(child_path, validate=False)

    root = backend.create("root")
    sheet_uuid = root.schematic.add_sheet("CHILD", child_path.name, (80, 70), (40, 30))
    root.schematic.add_sheet_pin(sheet_uuid, "CHILD_SIG_A", "output", "left", 10)
    root.schematic.add_sheet_pin(sheet_uuid, "CHILD_SIG_B", "output", "left", 13)
    root.save(root_path, validate=False)

    reopened = backend.open(root_path)
    result = backend.validate_hierarchy(reopened)
    if not result.get("valid"):
        raise SystemExit(result)
    print(f"fixture written: {root_path}")
    print(result)

if __name__ == "__main__":
    main()
