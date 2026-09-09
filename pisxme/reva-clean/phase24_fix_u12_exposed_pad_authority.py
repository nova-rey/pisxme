"""Restore the native U12 library serialization before extension."""
from pathlib import Path
import subprocess

R = Path(__file__).resolve().parent
P = R / "STORAGE.kicad_sch"
s = P.read_text()
head = subprocess.check_output(["git", "show", "HEAD:pisxme/reva-clean/STORAGE.kicad_sch"], text=True)
live_start = s.index('(symbol "HD3SS6126_RUA0042A_1_1"')
live_end = s.index('(symbol "PiSXMeRevAClean:HD3SS3412_RUA0042A"', live_start)
head_start = head.index('(symbol "HD3SS6126_RUA0042A_1_1"')
head_end = head.index('(symbol "PiSXMeRevAClean:HD3SS3412_RUA0042A"', head_start)
s = s[:live_start] + head[head_start:head_end] + s[live_end:]
s = s.replace('(label "POWER_GND" (at 120 137.695 0) (effects (font (size 0.8 0.8)) (justify left)) (uuid f1000000-0000-0000-0000-000000000043))\n', '')
s = s.replace('(pin "43" (uuid f1000000-0000-0000-0000-00000000012b)) ', '')
unit_start = s.index('(symbol "HD3SS6126_RUA0042A_1_1"')
first_pin = s.index('(pin passive', unit_start)
pin43 = '(pin passive line (at 20 27.305 180) (length 5) (name "POWER_GND" (effects (font (size 1 1)))) (number "43" (effects (font (size 1 1))))) '
unit_end = s.index('(embedded_fonts no)', unit_start)
if '(number "43"' not in s[unit_start:unit_end]:
    s = s[:first_pin] + pin43 + s[first_pin:]
instance = s.index('(symbol (lib_id "PiSXMeRevAClean:HD3SS6126_RUA0042A")')
label = '(label "POWER_GND" (at 120 137.695 0) (effects (font (size 0.8 0.8)) (justify left)) (uuid f1000000-0000-0000-0000-000000000043))\n'
if label not in s:
    s = s[:instance] + label + s[instance:]
inst_pin = '(pin "43" (uuid f1000000-0000-0000-0000-00000000012b)) '
if inst_pin not in s[instance:]:
    instances = s.index('(instances (project', instance)
    s = s[:instances] + inst_pin + s[instances:]
P.write_text(s)
print(P)
