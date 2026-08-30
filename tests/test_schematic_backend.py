import hashlib
import json
import tempfile
import unittest
from enum import Enum
from pathlib import Path
from types import SimpleNamespace

from bridge.schematic_backend import SchematicBackend, _issues_to_dict, native_violation_delta


class Level(Enum):
    ERROR = "error"
    WARNING = "warning"


class FakeSchematic:
    def __init__(self, path=None, valid=True):
        self.path = Path(path) if path else None
        self.valid = valid
        self.components = FakeComponents()

    @classmethod
    def load(cls, path):
        path = Path(path)
        if "invalid" in path.name:
            raise ValueError("invalid test schematic")
        return cls(path)

    def get_statistics(self):
        return {"components": len(self.components.items)}

    def validate(self):
        if self.valid:
            return []
        return [SimpleNamespace(category="test", message="bad", level=Level.ERROR)]

    def save(self, path, preserve_format=True):
        if not self.valid:
            raise ValueError("cannot save invalid test schematic")
        Path(path).write_text("(kicad_sch (version 20250114))\n", encoding="utf-8")


class FakeComponents:
    def __init__(self):
        self.items = {}


class FakeLibrary:
    @staticmethod
    def load_schematic(path):
        return FakeSchematic.load(path)

    @staticmethod
    def create_schematic(name):
        return FakeSchematic()


class FakeNativeRunner:
    def __init__(self, report):
        self.report = report

    def validate(self, kind, input_file, output_file, report_format="json", timeout=120):
        self.assert_kind = kind
        Path(output_file).write_text(json.dumps(self.report), encoding="utf-8")
        return {"returncode": 0, "report": self.report, "succeeded": True}

    def export(self, kind, input_file, output, timeout=120):
        Path(output).write_text("(exported)", encoding="utf-8")
        return {"returncode": 0, "succeeded": True, "output_exists": True}


class SchematicBackendTests(unittest.TestCase):
    def test_issue_enums_are_json_safe_and_classified(self):
        result = _issues_to_dict([SimpleNamespace(level=Level.ERROR, context={"pin": 1})])
        self.assertEqual(result, [{"level": "error", "context": {"pin": 1}}])

    def test_open_records_source_hash_and_info(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "input.kicad_sch"
            path.write_text("(kicad_sch)\n", encoding="utf-8")
            document = SchematicBackend(lambda: FakeLibrary).open(path)
            self.assertEqual(document.source_sha256, hashlib.sha256(path.read_bytes()).hexdigest())
            self.assertEqual(document.info()["statistics"]["components"], 0)

    def test_save_is_atomic_and_reopens_output(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "input.kicad_sch"
            path.write_text("original\n", encoding="utf-8")
            document = SchematicBackend(lambda: FakeLibrary).open(path)
            result = document.save()
            self.assertEqual(Path(result["path"]).read_text(encoding="utf-8"), "(kicad_sch (version 20250114))\n")
            self.assertEqual(document.source_sha256, hashlib.sha256(path.read_bytes()).hexdigest())

    def test_failed_save_leaves_existing_target_unchanged(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "input.kicad_sch"
            path.write_text("original\n", encoding="utf-8")
            document = SchematicBackend(lambda: FakeLibrary).open(path)
            document.schematic.valid = False
            with self.assertRaises(Exception):
                document.save()
            self.assertEqual(path.read_text(encoding="utf-8"), "original\n")

    def test_native_violation_delta_counts_only_new_errors(self):
        baseline = {
            "sheets": [{"path": "/", "violations": [{"severity": "error", "type": "old"}]}]
        }
        candidate = {
            "sheets": [{"path": "/", "violations": [
                {"severity": "error", "type": "old"},
                {"severity": "error", "type": "new"},
                {"severity": "warning", "type": "warning"},
            ]}]
        }
        delta = native_violation_delta(baseline, candidate)
        self.assertEqual(delta["baseline_error_count"], 1)
        self.assertEqual(delta["candidate_error_count"], 2)
        self.assertEqual(delta["introduced_error_count"], 1)

    def test_native_validation_promotes_only_after_clean_report(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "input.kicad_sch"
            path.write_text("original\n", encoding="utf-8")
            document = SchematicBackend(lambda: FakeLibrary).open(path)
            output = Path(temp) / "netlist.net"
            result = document.save_and_native_validate(
                path, FakeNativeRunner({"sheets": [{"path": "/", "violations": []}]}), export_netlist=output
            )
            self.assertTrue(result["promoted"])
            self.assertTrue(output.is_file())

    def test_native_validation_does_not_promote_new_error(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "input.kicad_sch"
            path.write_text("original\n", encoding="utf-8")
            document = SchematicBackend(lambda: FakeLibrary).open(path)
            runner = FakeNativeRunner({"sheets": [{"path": "/", "violations": [
                {"severity": "error", "type": "new"}
            ]}]})
            result = document.save_and_native_validate(path, runner)
            self.assertFalse(result["promoted"])
            self.assertEqual(result["reason"], "introduced_native_erc_errors")
            self.assertEqual(path.read_text(encoding="utf-8"), "original\n")


if __name__ == "__main__":
    unittest.main()
