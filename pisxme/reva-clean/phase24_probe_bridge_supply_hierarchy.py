"""Build a disposable native KiCad hierarchy-port repair for U7 supplies."""
from pathlib import Path
import shutil,re
import subprocess
R=Path(__file__).resolve().parent
src=R/'PiSXMe_RevA_Clean.kicad_sch'; out=R/'phase24_bridge_supply_hierarchy_probe'
if out.exists(): shutil.rmtree(out)
out.mkdir()
for p in R.glob('*.kicad_sch'): shutil.copy2(p,out/p.name)
root=(out/'PiSXMe_RevA_Clean.kicad_sch').read_text()
def add_sheet_pin(text,name,y):
    pat=r'(\(property "Sheetname" "'+re.escape(name)+r'"[\s\S]*?)(    \(instances)'
    m=re.search(pat,text)
    if not m: raise RuntimeError('root sheet '+name)
    pin=f'''    (pin "{y[0]}" bidirectional (at {y[1]} {y[2]} 180)
      (effects (font (size 1.27 1.27)) (justify left))
      (uuid {y[3]}))
'''
    return text[:m.start(2)]+pin+text[m.start(2):]
root=add_sheet_pin(root,'STORAGE',('BRIDGE_3V3',70,161,'40000000-0000-0000-0000-00000000a001'))
root=add_sheet_pin(root,'STORAGE',('BRIDGE_1V1',70,164,'40000000-0000-0000-0000-00000000a002'))
root=add_sheet_pin(root,'REGULATORS',('BRIDGE_3V3',175,59,'40000000-0000-0000-0000-00000000a003'))
root=add_sheet_pin(root,'REGULATORS',('BRIDGE_1V1',175,62,'40000000-0000-0000-0000-00000000a004'))
marker='  (global_label "V100_REFCLK_P"'
w='''  (wire (pts (xy 60 162) (xy 70 162)) (stroke (width 0) (type default)) (uuid d0000000-0000-0000-0000-00000000a001))
  (global_label "BRIDGE_3V3" (shape bidirectional) (at 60 162 0) (effects (font (size 1.27 1.27)) (justify right)) (uuid d0000000-0000-0000-0000-00000000a002))
  (wire (pts (xy 60 165) (xy 70 165)) (stroke (width 0) (type default)) (uuid d0000000-0000-0000-0000-00000000a003))
  (global_label "BRIDGE_1V1" (shape bidirectional) (at 60 165 0) (effects (font (size 1.27 1.27)) (justify right)) (uuid d0000000-0000-0000-0000-00000000a004))
  (wire (pts (xy 165 59) (xy 175 59)) (stroke (width 0) (type default)) (uuid d0000000-0000-0000-0000-00000000a005))
  (global_label "BRIDGE_3V3" (shape bidirectional) (at 165 59 0) (effects (font (size 1.27 1.27)) (justify right)) (uuid d0000000-0000-0000-0000-00000000a006))
  (wire (pts (xy 165 62) (xy 175 62)) (stroke (width 0) (type default)) (uuid d0000000-0000-0000-0000-00000000a007))
  (global_label "BRIDGE_1V1" (shape bidirectional) (at 165 62 0) (effects (font (size 1.27 1.27)) (justify right)) (uuid d0000000-0000-0000-0000-00000000a008))
'''
w=w.replace('60 162','60 161').replace('70 162','70 161').replace('60 165','60 164').replace('70 165','70 164')
root=root.replace(marker,w+marker,1); (out/src.name).write_text(root)
for fn,items in {
 'STORAGE.kicad_sch': [('BRIDGE_3V3','101.25','db000000-0000-0000-0000-00000000a101'),('BRIDGE_1V1','103.75','db000000-0000-0000-0000-00000000a102')],
 'REGULATORS.kicad_sch': [('BRIDGE_3V3','157','d6000000-0000-0000-0000-00000000a101'),('BRIDGE_1V1','207','d7000000-0000-0000-0000-00000000a102')],
}.items():
 t=(out/fn).read_text()
 labels=''
 for index,(name,y,uid) in enumerate(items,1):
  wire_uid=uid[:-4]+f'{0x200+index:04x}'
  labels += f'''\n(hierarchical_label "{name}" (shape bidirectional) (at 5 {y} 180) (effects (font (size 1 1)) (justify right)) (uuid {uid}))\n(wire (pts (xy 5 {y}) (xy 70 {y})) (stroke (width 0) (type default)) (uuid {wire_uid}))'''
 marker='\n(symbol (lib_id '
 if marker not in t: marker='\n\t(symbol (lib_id '
 if marker not in t: raise RuntimeError(f'missing child symbol marker {fn}')
 t=t.replace(marker,labels+marker,1)
 (out/fn).write_text(t)
if '--apply' in __import__('sys').argv:
 for fn in ('PiSXMe_RevA_Clean.kicad_sch','STORAGE.kicad_sch','REGULATORS.kicad_sch'):
  shutil.copy2(out/fn,R/fn)
 print('applied native hierarchy repair to clean schematic sources')
print(out)
