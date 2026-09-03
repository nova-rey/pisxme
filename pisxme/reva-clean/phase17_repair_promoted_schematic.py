"""Make the CM5IO Ethernet promotion deterministic and idempotent."""
from pathlib import Path
from phase3_scaffold import balanced
from phase17_promote_cm5io_ethernet import symbol_def, instance

ROOT=Path(__file__).resolve().parent
PATH=ROOT/'ETHERNET.kicad_sch'

def remove_generated(text):
    out=[]; cursor=0
    while cursor < len(text):
        starts=('(label ', '(global_label ', '(symbol (lib_id ')
        pos=min((p for p in (text.find(s,cursor) for s in starts) if p >= 0), default=-1)
        if pos < 0: out.append(text[cursor:]); break
        out.append(text[cursor:pos])
        expr=balanced(text,pos)
        stale = ('uuid da000000-' in expr or 'uuid db000000-' in expr or
                 'uuid dc000000-' in expr or 'uuid dd000000-' in expr or
                 ('(symbol (lib_id "PiSXMeRevAClean:TPD4EUSB30DQAR")' in expr and
                  ('Reference" "U6"' in expr or 'Reference" "U9"' in expr)))
        if not stale: out.append(expr)
        cursor=pos+len(expr)
    return ''.join(out)

def main():
    text=remove_generated(PATH.read_text())
    old='(symbol "PiSXMeRevAClean:TPD4EUSB30DQAR"'
    pos=text.index(old); text=text[:pos]+symbol_def()+text[pos+len(balanced(text,pos)):]
    body='\n'.join((
        instance('U6',('CM5_GBE_TD0_P','CM5_GBE_TD0_N','ETH_GND','CM5_GBE_TD1_N','CM5_GBE_TD1_P','CM5_GBE_TD1_P','CM5_GBE_TD1_N','ETH_GND','CM5_GBE_TD0_N','CM5_GBE_TD0_P'),0xDC000000000000000000000000000000,50,140),
        instance('U9',('CM5_GBE_TD2_P','CM5_GBE_TD2_N','ETH_GND','CM5_GBE_TD3_N','CM5_GBE_TD3_P','CM5_GBE_TD3_P','CM5_GBE_TD3_N','ETH_GND','CM5_GBE_TD2_N','CM5_GBE_TD2_P'),0xDD000000000000000000000000000000,50,180),
    ))
    marker='  (sheet_instances '
    assert marker in text
    text=text.replace(marker,body+'\n'+marker,1)
    PATH.write_text(text); print('promoted Ethernet schematic repaired deterministically')

if __name__=='__main__': main()
