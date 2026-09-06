"""Expose CM5 USB3-0 USB2 pins to the storage child sheet.

The CM5 carrier symbol's USB3-0 D+/D- pins are the USB2 companion for the
same port.  Earlier storage work used free-standing CM5_USB2 names, which
were not connected to CORE_CM5.  This source-authority repair gives those
actual pins explicit hierarchy names; it is deliberately schematic-first.
"""
from pathlib import Path

R = Path(__file__).resolve().parent
ROOT = R / "PiSXMe_RevA_Clean.kicad_sch"
CORE = R / "CORE_CM5.kicad_sch"
STORAGE = R / "STORAGE.kicad_sch"

def add_once(path, marker, text):
    s = path.read_text()
    if text.strip() in s: return False
    i = s.index(marker)
    path.write_text(s[:i] + text + s[i:])
    return True

def main():
    # Child-sheet hierarchy labels are placed below the existing interface.
    core = CORE.read_text()
    if 'hierarchical_label "CM5_STORAGE_USB2_DP"' not in core:
        marker = '  (hierarchical_label "CM5_GBE"'
        ins = '''  (hierarchical_label "CM5_STORAGE_USB2_DP" (shape bidirectional) (at 5 49 180) (effects (font (size 1.27 1.27)) (justify right)) (uuid 50000000-0000-0000-0000-000000000071))
  (hierarchical_label "CM5_STORAGE_USB2_DM" (shape bidirectional) (at 5 52 180) (effects (font (size 1.27 1.27)) (justify right)) (uuid 50000000-0000-0000-0000-000000000072))
  (wire (pts (xy 5 49) (xy 19.92 49)) (stroke (width 0) (type default)) (uuid 50000000-0000-0000-0000-000000000073))
  (wire (pts (xy 5 52) (xy 19.92 52)) (stroke (width 0) (type default)) (uuid 50000000-0000-0000-0000-000000000074))
'''
        core = core.replace(marker, ins + marker, 1)
        # Actual CM5 symbol pins 134/136 are at these native child coordinates.
        core += '''\n(global_label "CM5_STORAGE_USB2_DP" (shape bidirectional) (at 209.22 120.32 0) (effects (font (size 1 1)) (justify left)) (uuid e3000000-0000-0000-0000-000000000220))
(global_label "CM5_STORAGE_USB2_DM" (shape bidirectional) (at 209.22 117.78 0) (effects (font (size 1 1)) (justify left)) (uuid e3000000-0000-0000-0000-000000000221))\n'''
        CORE.write_text(core)

    root = ROOT.read_text()
    if 'pin "CM5_STORAGE_USB2_DP"' not in root:
        root = root.replace('(size 25 38)', '(size 25 47)', 1)
        marker = '    (pin "CM5_GBE"'
        ins = '''    (pin "CM5_STORAGE_USB2_DP" bidirectional (at 35 84 180)
      (effects (font (size 1.27 1.27)) (justify left))
      (uuid 40000000-0000-0000-0000-000000000071))
    (pin "CM5_STORAGE_USB2_DM" bidirectional (at 35 87 180)
      (effects (font (size 1.27 1.27)) (justify left))
      (uuid 40000000-0000-0000-0000-000000000072))
'''
        root = root.replace(marker, ins + marker, 1)
        marker = '  (wire (pts (xy 25 71) (xy 35 71))'
        ins = '''  (wire (pts (xy 25 84) (xy 35 84)) (stroke (width 0) (type default)) (uuid d0000000-0000-0000-0000-000000000220))
  (global_label "CM5_STORAGE_USB2_DP" (shape bidirectional) (at 25 84 0) (effects (font (size 1.27 1.27)) (justify right)) (uuid d0000000-0000-0000-0000-000000000221))
  (wire (pts (xy 25 87) (xy 35 87)) (stroke (width 0) (type default)) (uuid d0000000-0000-0000-0000-000000000222))
  (global_label "CM5_STORAGE_USB2_DM" (shape bidirectional) (at 25 87 0) (effects (font (size 1.27 1.27)) (justify right)) (uuid d0000000-0000-0000-0000-000000000223))
'''
        root = root.replace(marker, ins + marker, 1)
        ROOT.write_text(root)

    storage = STORAGE.read_text()
    storage = storage.replace('CM5_USB2_DP', 'CM5_STORAGE_USB2_DP').replace('CM5_USB2_DM', 'CM5_STORAGE_USB2_DM')
    STORAGE.write_text(storage)
    print('CM5 storage USB2 source authority exposed')

if __name__ == '__main__': main()
