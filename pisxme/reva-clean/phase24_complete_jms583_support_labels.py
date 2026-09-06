"""Refresh the embedded JMS583 definition/instance from the retained pin map."""
from pathlib import Path
from phase24_integrate_dual_mode_storage import JMS, definition, instance, balanced, make_uuid, SCH

def replace_block(text, start, block):
    return text[:start] + block + text[start + len(balanced(text, start)):]

def main():
    text = SCH.read_text()
    dstart = text.index('(symbol "PiSXMeRevAClean:JMS583_QFN64"')
    dend = dstart + len(balanced(text, dstart))
    text = text[:dstart] + definition('JMS583_QFN64', JMS) + text[dend:]
    istart = text.index('(symbol (lib_id "PiSXMeRevAClean:JMS583_QFN64"')
    new = instance('JMS583_QFN64', 'U11', 'JMS583-QHFA3A', JMS,
                   0xf1000000000000000000000000001000, 50, 165,
                   'PiSXMeRevAClean:JMS583_QFN64_8x8')
    text = replace_block(text, istart, new)
    SCH.write_text(text)
    print('refreshed JMS583 authority labels and support pins')

if __name__ == '__main__':
    main()
