import unittest

from bridge.core import ApiRegistry, FileScope, enum_name, enum_value
from kipy.board_types import BoardLayer


class BridgeUnitTests(unittest.TestCase):
    def test_scope_rejects_paths_outside_root(self):
        scope = FileScope("/Users/Cooper/Documents/ChatGPT/sxm2")
        with self.assertRaises(Exception):
            scope.resolve("../../private-file")

    def test_registry_discovers_installed_ipc_messages(self):
        registry = ApiRegistry()
        self.assertIn("kiapi.common.commands.GetVersion", registry.messages)
        self.assertIn("kiapi.common.commands.GetItems", registry.messages)
        self.assertEqual(registry.resolve_message("GetVersion").full_name, "kiapi.common.commands.GetVersion")

    def test_enum_round_trip(self):
        value = enum_value(BoardLayer, "F.Cu")
        self.assertEqual(enum_name(BoardLayer, value), "BL_F_Cu")


if __name__ == "__main__":
    unittest.main()
