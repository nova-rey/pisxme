"""Build a disposable native KiCad USB2 hierarchy candidate.

The original clean scaffold modeled CM5 USB2 as one scalar contract even
though USB2 is DP/DM.  This candidate gives the two conductors distinct
hierarchical ports and connects the actual CM5 pins to them.  It never edits
the production sheets; the candidate directory is the comparison artifact.
"""
from pathlib import Path
import shutil
import re

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'phase20-hierarchy-candidate'

def copy_inputs():
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir()
    # KiCad resolves every child referenced by the root even though only two
    # sheets are being edited in this disposable experiment.
    for n in ROOT.glob('*.kicad_sch'):
        shutil.copy2(n, OUT/n.name)

def replace_once(t, old, new, label):
    if old not in t: raise RuntimeError('missing '+label)
    return t.replace(old,new,1)

def core():
    p=OUT/'CORE_CM5.kicad_sch'; t=p.read_text()
    t=replace_once(t,'(name "SERVICE_USB2" (effects (font (size 1.27 1.27))))\n          (number "10" (effects (font (size 1.27 1.27)))))\n        (pin passive line\n          (at -5.08 -30 0)\n          (length 3.81)\n          (name "CM5_POWER"', '(name "SERVICE_USB2_DP" (effects (font (size 1.27 1.27))))\n          (number "10" (effects (font (size 1.27 1.27)))))\n        (pin passive line\n          (at -5.08 -30 0)\n          (length 3.81)\n          (name "SERVICE_USB2_DM" (effects (font (size 1.27 1.27))))\n          (number "11" (effects (font (size 1.27 1.27)))))\n        (pin passive line\n          (at -5.08 -33 0)\n          (length 3.81)\n          (name "CM5_POWER"', 'CORE contract definition')
    t=t.replace('(name "CM5_POWER" (effects (font (size 1.27 1.27))))\n          (number "11"', '(name "CM5_POWER" (effects (font (size 1.27 1.27))))\n          (number "12"', 1)
    t=replace_once(t,'(pin "11" (uuid 90000000-0000-0000-0000-00000000006e))','(pin "11" (uuid 90000000-0000-0000-0000-000000000070))\n    (pin "12" (uuid 90000000-0000-0000-0000-00000000006e))', 'CORE contract instance')
    t=t.replace('(pin "11" (uuid 90000000-0000-0000-0000-00000000006e))\n    (pin "12" (uuid 90000000-0000-0000-0000-000000000070))', '(pin "11" (uuid 90000000-0000-0000-0000-000000000070))\n    (pin "12" (uuid 90000000-0000-0000-0000-00000000006e))', 1)
    t=replace_once(t,'(hierarchical_label "SERVICE_USB2"\n    (shape bidirectional)\n    (at 5 37 180)\n    (effects (font (size 1.27 1.27)) (justify right))\n    (uuid 50000000-0000-0000-0000-00000000006d))\n  (hierarchical_label "CM5_POWER"\n    (shape bidirectional)\n    (at 5 40 180)', '(hierarchical_label "SERVICE_USB2_DP"\n    (shape bidirectional)\n    (at 5 37 180)\n    (effects (font (size 1.27 1.27)) (justify right))\n    (uuid 50000000-0000-0000-0000-00000000006d))\n  (hierarchical_label "SERVICE_USB2_DM"\n    (shape bidirectional)\n    (at 5 40 180)\n    (effects (font (size 1.27 1.27)) (justify right))\n    (uuid 50000000-0000-0000-0000-000000000070))\n  (hierarchical_label "CM5_POWER"\n    (shape bidirectional)\n    (at 5 43 180)', 'CORE child labels')
    t=t.replace('(hierarchical_label "CM5_5V"\n    (shape bidirectional)\n    (at 5 43 180)', '(hierarchical_label "CM5_5V"\n    (shape bidirectional)\n    (at 5 46 180)',1)
    # Normalize the complete contract-label/wire region after insertion.
    a=t.index('  (hierarchical_label "SERVICE_USB2_DP"')
    z=t.index('  (symbol\n    (lib_id "PiSXMeRevAClean:CORE_CM5_Contract"',a)
    labels='''  (hierarchical_label "SERVICE_USB2_DP" (shape bidirectional) (at 5 37 180) (effects (font (size 1.27 1.27)) (justify right)) (uuid 50000000-0000-0000-0000-00000000006d))
  (hierarchical_label "SERVICE_USB2_DM" (shape bidirectional) (at 5 40 180) (effects (font (size 1.27 1.27)) (justify right)) (uuid 50000000-0000-0000-0000-000000000070))
  (hierarchical_label "CM5_POWER" (shape bidirectional) (at 5 43 180) (effects (font (size 1.27 1.27)) (justify right)) (uuid 50000000-0000-0000-0000-00000000006e))
  (hierarchical_label "CM5_5V" (shape bidirectional) (at 5 46 180) (effects (font (size 1.27 1.27)) (justify right)) (uuid 50000000-0000-0000-0000-00000000006f))
  (wire (pts (xy 5 37) (xy 19.92 37)) (stroke (width 0) (type default)) (uuid a0000000-0000-0000-0000-00000000006d))
  (wire (pts (xy 5 40) (xy 19.92 40)) (stroke (width 0) (type default)) (uuid a0000000-0000-0000-0000-000000000070))
  (wire (pts (xy 5 43) (xy 19.92 43)) (stroke (width 0) (type default)) (uuid a0000000-0000-0000-0000-00000000006e))
  (wire (pts (xy 5 46) (xy 19.92 46)) (stroke (width 0) (type default)) (uuid a0000000-0000-0000-0000-00000000006f))
'''
    t=t[:a]+labels+t[z:]
    # The module symbol's real USB2 pins are 103=N and 105=P.
    for y in ('41.58','44.12','155.88','158.42'):
        t=re.sub(r'\(no_connect \(at 270\.18 '+y+r'\) \(uuid [^)]+\)\)\s*','',t)
    t=t.rstrip()[:-1]+'\n(wire (pts (xy 270.18 41.58) (xy 260.18 41.58)) (stroke (width 0) (type default)) (uuid f0000000-0000-0000-0000-000000000203))\n(wire (pts (xy 270.18 44.12) (xy 260.18 44.12)) (stroke (width 0) (type default)) (uuid f0000000-0000-0000-0000-000000000205))\n(label "SERVICE_USB2_DM" (at 260.18 41.58 0) (effects (font (size 1.1 1.1))) (uuid f0000000-0000-0000-0000-000000000103))\n(label "SERVICE_USB2_DP" (at 260.18 44.12 0) (effects (font (size 1.1 1.1))) (uuid f0000000-0000-0000-0000-000000000105))\n)\n'
    p.write_text(t)

def service():
    p=OUT/'SERVICE.kicad_sch'; t=p.read_text()
    t=replace_once(t,'(name "SERVICE_USB2" (effects (font (size 1.27 1.27))))\n          (number "1" (effects (font (size 1.27 1.27)))))\n        (pin passive line\n          (at -5.08 -3 0)\n          (length 3.81)\n          (name "SERVICE_VBUS_SENSE"', '(name "SERVICE_USB2_DP" (effects (font (size 1.27 1.27))))\n          (number "1" (effects (font (size 1.27 1.27)))))\n        (pin passive line\n          (at -5.08 -3 0)\n          (length 3.81)\n          (name "SERVICE_USB2_DM" (effects (font (size 1.27 1.27))))\n          (number "2" (effects (font (size 1.27 1.27)))))\n        (pin passive line\n          (at -5.08 -6 0)\n          (length 3.81)\n          (name "SERVICE_VBUS_SENSE"', 'SERVICE contract definition')
    t=t.replace('(number "2" (effects (font (size 1.27 1.27)))))\n        (pin passive line\n          (at -5.08 -6 0)\n          (length 3.81)\n          (name "SERVICE_RD"', '(number "3" (effects (font (size 1.27 1.27)))))\n        (pin passive line\n          (at -5.08 -9 0)\n          (length 3.81)\n          (name "SERVICE_RD"',1)
    t=t.replace('(number "3" (effects (font (size 1.27 1.27)))))\n        (pin passive line\n          (at -5.08 -9 0)\n          (length 3.81)\n          (name "SERVICE_GND"', '(number "4" (effects (font (size 1.27 1.27)))))\n        (pin passive line\n          (at -5.08 -12 0)\n          (length 3.81)\n          (name "SERVICE_GND"',1)
    t=t.replace('(number "4" (effects (font (size 1.27 1.27)))))\n      )\n    )\n(symbol "PiSXMeRevAClean:USB2_UFP_CONNECTOR"', '(number "5" (effects (font (size 1.27 1.27)))))\n      )\n    )\n(symbol "PiSXMeRevAClean:USB2_UFP_CONNECTOR"',1)
    old='(hierarchical_label "SERVICE_USB2"\n    (shape bidirectional)\n    (at 5 10 180)'
    t=replace_once(t,old,'(hierarchical_label "SERVICE_USB2_DP"\n    (shape bidirectional)\n    (at 5 10 180)', 'SERVICE child DP label')
    t=t.replace('(hierarchical_label "SERVICE_VBUS_SENSE"\n    (shape bidirectional)\n    (at 5 13 180)', '(hierarchical_label "SERVICE_USB2_DM"\n    (shape bidirectional)\n    (at 5 13 180)\n    (effects (font (size 1.27 1.27)) (justify right))\n    (uuid 50000000-0000-0000-0000-000000000324))\n  (hierarchical_label "SERVICE_VBUS_SENSE"\n    (shape bidirectional)\n    (at 5 16 180)',1)
    a=t.index('  (hierarchical_label "SERVICE_USB2_DP"')
    z=t.index('  (symbol\n    (lib_id "PiSXMeRevAClean:SERVICE_Contract"',a)
    labels='''  (hierarchical_label "SERVICE_USB2_DP" (shape bidirectional) (at 5 10 180) (effects (font (size 1.27 1.27)) (justify right)) (uuid 50000000-0000-0000-0000-000000000320))
  (hierarchical_label "SERVICE_USB2_DM" (shape bidirectional) (at 5 13 180) (effects (font (size 1.27 1.27)) (justify right)) (uuid 50000000-0000-0000-0000-000000000324))
  (hierarchical_label "SERVICE_VBUS_SENSE" (shape bidirectional) (at 5 16 180) (effects (font (size 1.27 1.27)) (justify right)) (uuid 50000000-0000-0000-0000-000000000321))
  (hierarchical_label "SERVICE_RD" (shape bidirectional) (at 5 19 180) (effects (font (size 1.27 1.27)) (justify right)) (uuid 50000000-0000-0000-0000-000000000322))
  (hierarchical_label "SERVICE_GND" (shape bidirectional) (at 5 22 180) (effects (font (size 1.27 1.27)) (justify right)) (uuid 50000000-0000-0000-0000-000000000323))
  (wire (pts (xy 5 10) (xy 19.92 10)) (stroke (width 0) (type default)) (uuid a0000000-0000-0000-0000-000000000320))
  (wire (pts (xy 5 13) (xy 19.92 13)) (stroke (width 0) (type default)) (uuid a0000000-0000-0000-0000-000000000324))
  (wire (pts (xy 5 16) (xy 19.92 16)) (stroke (width 0) (type default)) (uuid a0000000-0000-0000-0000-000000000321))
  (wire (pts (xy 5 19) (xy 19.92 19)) (stroke (width 0) (type default)) (uuid a0000000-0000-0000-0000-000000000322))
  (wire (pts (xy 5 22) (xy 19.92 22)) (stroke (width 0) (type default)) (uuid a0000000-0000-0000-0000-000000000323))
'''
    t=t[:a]+labels+t[z:]
    # Add the new contract instance pin and shift the existing external wires.
    t=t.replace('(pin "4" (uuid 90000000-0000-0000-0000-000000000323))','(pin "4" (uuid 90000000-0000-0000-0000-000000000323))\n    (pin "5" (uuid 90000000-0000-0000-0000-000000000324))',1)
    t=t.replace('(pin "2" (uuid 90000000-0000-0000-0000-000000000321))\n    (pin "3" (uuid 90000000-0000-0000-0000-000000000322))\n    (pin "4" (uuid 90000000-0000-0000-0000-000000000323))\n    (pin "5" (uuid 90000000-0000-0000-0000-000000000324))', '(pin "2" (uuid 90000000-0000-0000-0000-000000000324))\n    (pin "3" (uuid 90000000-0000-0000-0000-000000000321))\n    (pin "4" (uuid 90000000-0000-0000-0000-000000000322))\n    (pin "5" (uuid 90000000-0000-0000-0000-000000000323))', 1)
    p.write_text(t)

def root():
    p=OUT/'PiSXMe_RevA_Clean.kicad_sch'; t=p.read_text()
    t=t.replace('(pin "SERVICE_USB2" bidirectional (at 35 74 180)', '(pin "SERVICE_USB2_DP" bidirectional (at 35 74 180)',1)
    t=t.replace('(pin "CM5_POWER" bidirectional (at 35 77 180)', '(pin "SERVICE_USB2_DM" bidirectional (at 35 77 180)\n      (effects (font (size 1.27 1.27)) (justify left))\n      (uuid 40000000-0000-0000-0000-000000000070))\n    (pin "CM5_POWER" bidirectional (at 35 80 180)',1)
    t=t.replace('(pin "CM5_5V" bidirectional (at 35 80 180)', '(pin "CM5_5V" bidirectional (at 35 83 180)',1)
    t=t.replace('(pin "SERVICE_USB2" bidirectional (at 105 147 180)', '(pin "SERVICE_USB2_DP" bidirectional (at 105 147 180)',1)
    t=t.replace('(pin "SERVICE_VBUS_SENSE" bidirectional (at 105 150 180)', '(pin "SERVICE_USB2_DM" bidirectional (at 105 150 180)\n      (effects (font (size 1.27 1.27)) (justify left))\n      (uuid 40000000-0000-0000-0000-000000000324))\n    (pin "SERVICE_VBUS_SENSE" bidirectional (at 105 153 180)',1)
    t=t.replace('(pin "SERVICE_RD" bidirectional (at 105 153 180)', '(pin "SERVICE_RD" bidirectional (at 105 156 180)',1)
    t=t.replace('(pin "SERVICE_GND" bidirectional (at 105 156 180)', '(pin "SERVICE_GND" bidirectional (at 105 159 180)',1)
    marker='  (sheet_instances (path "/" (page "1")))'
    wires='''  (wire (pts (xy 35 74) (xy 105 147)) (stroke (width 0) (type default)) (uuid c0000000-0000-0000-0000-000000000320))
  (wire (pts (xy 35 77) (xy 105 150)) (stroke (width 0) (type default)) (uuid c0000000-0000-0000-0000-000000000321))
'''
    t=replace_once(t,marker,wires+marker,'root service links')
    p.write_text(t)

def main():
    copy_inputs(); core(); service(); root(); print(OUT)
if __name__=='__main__': main()
