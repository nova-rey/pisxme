"""Add the documented PEDET Schmitt buffer to the storage child sheet."""
from pathlib import Path
from phase24_integrate_dual_mode_storage import balanced, definition, instance, SCH

def main():
    text = SCH.read_text()
    if 'property "Reference" "U14"' in text:
        print('mode buffer already present'); return
    mode = {1:'NC_1', 2:'M2_PEDET', 3:'POWER_GND', 4:'STORAGE_SEL', 5:'STORAGE_3V3'}
    lib_end = text.index('(lib_symbols')
    lib_block = lib_end + len(balanced(text, lib_end)) - 1
    text = text[:lib_block].rstrip() + '\n' + definition('STORAGE_MODE_BUFFER', mode) + '\n' + text[lib_block:]
    item = instance('STORAGE_MODE_BUFFER', 'U14', 'SN74LVC1G17DBVR', mode,
                    0xf1000000000000000000000000001400, 280, 165,
                    'Package_TO_SOT_SMD:SOT-23-5')
    marker = '\n  (sheet_instances '
    text = text.replace(marker, '\n' + item + marker, 1)
    SCH.write_text(text)
    print('added U14 PEDET Schmitt buffer')

if __name__ == '__main__': main()
