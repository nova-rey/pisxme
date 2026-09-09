"""Restore the superseded Y1 support labels after a disposable probe."""
from pathlib import Path
import re

p = Path(__file__).resolve().parent / "STORAGE.kicad_sch"
s = p.read_text()
names = {
    'db000000-0000-0000-0000-000000000172':'BRIDGE_XI',
    'db000000-0000-0000-0000-000000000173':'BRIDGE_VSSOSC',
    'db000000-0000-0000-0000-000000000174':'BRIDGE_XO',
    'ef000000-0000-0000-0000-000000000064':'BRIDGE_XI',
    'ef000000-0000-0000-0000-000000000065':'BRIDGE_VSSOSC',
    'ef000000-0000-0000-0000-000000000066':'BRIDGE_XO',
    'ef000000-0000-0000-0000-000000000067':'BRIDGE_VSSOSC',
    'ef000000-0000-0000-0000-000000000074':'BRIDGE_XI',
    'ef000000-0000-0000-0000-000000000075':'BRIDGE_XO',
    'ef000000-0000-0000-0000-000000000084':'BRIDGE_XI',
    'ef000000-0000-0000-0000-000000000085':'BRIDGE_VSSOSC',
    'ef000000-0000-0000-0000-000000000094':'BRIDGE_XO',
    'ef000000-0000-0000-0000-000000000095':'BRIDGE_VSSOSC',
}
for uid, name in names.items():
    s = re.sub(r'\(label "[^"]+"([^\n]*\(uuid ' + uid + r'\)\))',
               r'(label "' + name + r'"\1', s)
p.write_text(s)
print('restored', len(names), 'superseded Y1 aliases')
