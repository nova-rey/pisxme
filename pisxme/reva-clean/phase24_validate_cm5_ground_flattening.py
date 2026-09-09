"""Disposable proof that source-flattened CM5 POWER_GND matches board plane net."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = Path(__import__('os').environ.get('PISXME_GROUND_BASE', ROOT / 'PHASE24_STORAGE_VCCK_LOCAL_V1.kicad_pcb'))
OUT = Path(__import__('os').environ.get('PISXME_GROUND_OUT', ROOT / 'PHASE24_CM5_GROUND_FLATTENED_DISPOSABLE.kicad_pcb'))

b = pcbnew.LoadBoard(str(BASE))
old = b.FindNet('/CORE_CM5/POWER_GND')
new = b.FindNet('POWER_GND')
if old is None or new is None:
    raise SystemExit('required old/new ground nets not present')
old_code, new_code = old.GetNetCode(), new.GetNetCode()
count = 0
for item in list(b.GetPads()) + list(b.GetTracks()):
    if item.GetNetCode() == old_code:
        item.SetNetCode(new_code)
        count += 1
for z in b.Zones():
    if z.GetNetCode() == old_code:
        z.SetNetCode(new_code)
        count += 1
b.BuildListOfNets()
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(f'remapped_items={count} old_code={old_code} new_code={new_code} output={OUT}')
