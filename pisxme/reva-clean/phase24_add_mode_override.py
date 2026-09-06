"""Refresh the storage-local mode control without touching other storage blocks.

The strap is deliberately a passive configuration interface: FORCE_SATA,
AUTO_PEDET, and FORCE_NVME are selected with a power-off shunt.  U14 buffers
the selected MODE_IN node before it drives both high-speed selectors.
"""
from phase24_integrate_dual_mode_storage import balanced, definition, instance, SCH

def replace_block(text, needle, replacement):
    start = text.index(needle)
    return text[:start] + replacement + text[start + len(balanced(text, start)):]

def main():
    text = SCH.read_text()
    mode = {1:'NC_1', 2:'MODE_IN', 3:'POWER_GND', 4:'STORAGE_SEL', 5:'STORAGE_3V3'}
    u14 = instance('STORAGE_MODE_BUFFER', 'U14', 'SN74LVC1G17DBVR', mode,
                   0xf1000000000000000000000000001400, 280, 165,
                   'Package_TO_SOT_SMD:SOT-23-5')
    if 'property "Reference" "U14"' in text:
        # The prior buffer authoring pass left its five external labels in
        # place. Remove that exact UUID range before replacing the instance;
        # duplicate UUIDs are invalid native schematic serialization.
        import re
        text = re.sub(r'\(label "(?:NC_1|M2_PEDET|MODE_IN|POWER_GND|STORAGE_SEL|STORAGE_3V3)"[^\n]*uuid f1000000-0000-0000-0000-00000000146[5-9]\)\)', '', text)
        text = replace_block(text, '(symbol (lib_id "PiSXMeRevAClean:STORAGE_MODE_BUFFER")', u14)
    else:
        lib_end = text.index('(lib_symbols')
        lib_close = lib_end + len(balanced(text, lib_end)) - 1
        text = text[:lib_close].rstrip() + '\n' + definition('STORAGE_MODE_BUFFER', mode) + '\n' + text[lib_close:]
        text = text.replace('\n  (sheet_instances ', '\n' + u14 + '\n  (sheet_instances ', 1)

    override = {1:'FORCE_SATA', 2:'AUTO_PEDET', 3:'FORCE_NVME', 4:'MODE_IN'}
    mode_start = text.find('(symbol (lib_id "PiSXMeRevAClean:STORAGE_MODE_OVERRIDE")')
    if mode_start >= 0:
        old = balanced(text, mode_start)
        new = old.replace('property "Reference" "J4"', 'property "Reference" "J5"').replace('(reference "J4")', '(reference "J5")')
        text = text[:mode_start] + new + text[mode_start + len(old):]
    if 'property "Reference" "J5"' not in text:
        lib_end = text.index('(lib_symbols')
        lib_close = lib_end + len(balanced(text, lib_end)) - 1
        text = text[:lib_close].rstrip() + '\n' + definition('STORAGE_MODE_OVERRIDE', override) + '\n' + text[lib_close:]
        j4 = instance('STORAGE_MODE_OVERRIDE', 'J5', 'AUTO / FORCE SATA / FORCE NVMe', override,
                       0xf1000000000000000000000000001500, 330, 165,
                       'PiSXMeRevAClean:MODE_JUMPER_1x04')
        text = text.replace('\n  (sheet_instances ', '\n' + j4 + '\n  (sheet_instances ', 1)
    SCH.write_text(text)
    print('refreshed U14 MODE_IN buffer and added J4 mode override')

if __name__ == '__main__':
    main()
