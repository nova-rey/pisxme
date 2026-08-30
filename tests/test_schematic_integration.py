"""Disposable real-library schematic-authoring checks.

These tests intentionally stop at the direct backend boundary.  Native KiCad
ERC and schematic-to-PCB parity are external validation gates, not substitutes
for the backend round-trip tests below.
"""

import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path


KSA_AVAILABLE = importlib.util.find_spec("kicad_sch_api") is not None


@unittest.skipUnless(KSA_AVAILABLE, "kicad-sch-api is not installed")
class RealSchematicBackendTests(unittest.TestCase):
    def test_create_hierarchy_and_reopen(self):
        from bridge.schematic_backend import SchematicBackend

        with tempfile.TemporaryDirectory() as temp:
            root_path = Path(temp) / "root.kicad_sch"
            child_path = Path(temp) / "child.kicad_sch"
            backend = SchematicBackend()
            child = backend.create("child")
            child.schematic.components.add("Device:R", reference="R1", value="10k", position=(100.33, 100.33))
            child.schematic.components.add("Device:C", reference="C1", value="100n", position=(119.38, 100.33))
            child.schematic.add_wire_between_pins("R1", "1", "C1", "1")
            child.schematic.add_hierarchical_label("CHILD_SIG", (100.33, 96.52), shape="output")
            child.save(child_path, validate=False)

            root = backend.create("root")
            root.schematic.components.add("74xx:74LS00", reference="U1", value="74LS00", position=(150, 100))
            sheet_uuid = root.schematic.add_sheet("CHILD", child_path.name, (80, 70), (40, 30))
            root.schematic.add_sheet_pin(sheet_uuid, "CHILD_SIG", "output", "left", 10)
            root.save(root_path, validate=False)

            reopened = backend.open(root_path)
            self.assertEqual(reopened.schematic.get_statistics()["sheets"]["total_sheets"], 1)
            self.assertTrue(backend.validate_hierarchy(reopened)["valid"])
            self.assertEqual(reopened.schematic.sheets.get_sheet_statistics()["total_sheet_pins"], 1)

    def test_existing_roundtrip_preserves_semantic_identity(self):
        from bridge.schematic_backend import SchematicBackend

        source = Path(__file__).parents[1] / "pisxme" / "PiSXMe.kicad_sch"
        if not source.is_file():
            self.skipTest("PiSXMe fixture is not present")
        with tempfile.TemporaryDirectory() as temp:
            work = Path(temp) / source.name
            shutil.copy2(source, work)
            shutil.copy2(source.with_suffix(".kicad_sym"), work.with_suffix(".kicad_sym"))
            backend = SchematicBackend()
            before = backend.open(work)
            refs_before = {c.reference: (c.lib_id, c.value, c.footprint, str(c.uuid)) for c in before.schematic.components.all()}
            wires_before = len(list(before.schematic.wires.all()))
            before.schematic.components.add(
                "Device:R", reference="R999", value="1k", position=(300, 300), footprint="Resistor_SMD:R_0603_1608Metric"
            )
            before.save(validate=False)
            after = backend.open(work)
            refs_after = {c.reference: (c.lib_id, c.value, c.footprint, str(c.uuid)) for c in after.schematic.components.all()}
            self.assertEqual(refs_before, {k: v for k, v in refs_after.items() if k != "R999"})
            self.assertEqual(wires_before, len(list(after.schematic.wires.all())))
            self.assertIn("R999", refs_after)


if __name__ == "__main__":
    unittest.main()
