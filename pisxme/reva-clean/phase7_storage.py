"""Generate the schematic-only USB3-to-SATA storage island."""
from pathlib import Path
import re
from phase3_scaffold import balanced, make_uuid

ROOT=Path(__file__).resolve().parent

def symbol(name,pins):
    rows=[]
    for i,p in enumerate(pins):
        y=(i-(len(pins)-1)/2)*2.5
        rows.append('(pin passive line (at 20 %g 180) (length 5) (name "%s" (effects (font (size 1 1)))) (number "%d" (effects (font (size 1 1)))))'%(y,p,i+1))
    return '(symbol "PiSXMeRevAClean:%s" (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes) (property "Reference" "U" (at 0 -12 0) (effects (font (size 1 1)))) (property "Value" "%s" (at 0 12 0) (effects (font (size 1 1)))) (property "Footprint" "" (at 0 0 0) (effects (font (size 1 1)) (hide yes))) (symbol "%s_1_1" (rectangle (start -15 -10) (end 15 10) (stroke (width 0.254) (type default)) (fill (type background))) %s) (embedded_fonts no))'%(name,name,name,'\n'.join(rows))

def part(lib,ref,mpn,nets,uid,footprint=''):
    labels=[]; pins=[]
    for i,net in enumerate(nets):
        y=95+(i-(len(nets)-1)/2)*2.5
        labels.append('(label "%s" (at 70 %g 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid %s))'%(net,y,make_uuid(uid+100+i)))
        pins.append('(pin "%d" (uuid %s))'%(i+1,make_uuid(uid+i)))
    return '\n'.join(labels)+'\n(symbol (lib_id "PiSXMeRevAClean:%s") (at 50 95 0) (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (uuid %s) (property "Reference" "%s" (at 50 82 0) (effects (font (size 1.1 1.1)))) (property "Value" "%s" (at 50 108 0) (effects (font (size 1.1 1.1)))) (property "MPN" "%s" (at 50 95 0) (effects (font (size 1 1)) (hide yes))) (property "Footprint" "%s" (at 50 95 0) (effects (font (size 1 1)) (hide yes))) %s (instances (project "PiSXMe_RevA_Clean" (path "/30000000-0000-0000-0000-000000000000" (reference "%s") (unit 1)))) )'%(lib,make_uuid(uid),ref,mpn,mpn,footprint,'\n'.join(pins),ref)

TUSB_PIN_NUMBERS=(43,42,46,45,57,56,60,59,24,41,4,21)

def _renumber_block(block, numbers):
    i=0
    def repl(match):
        nonlocal i
        if i >= len(numbers): return match.group(0)
        value=str(numbers[i]); i+=1
        return '(%s "%s"' % (match.group(1), value)
    return re.sub(r'\((number|pin) "(\d+)"', repl, block), i

def _flip_pin_rows(block):
    rows=list(re.finditer(r'\(pin passive line \(at 20 ([^ ]+) 180\)', block))
    if not rows or float(rows[0].group(1)) >= 0:
        return block
    ys=[m.group(1) for m in rows][::-1]
    for m,y in reversed(list(zip(rows,ys))):
        a,b=m.start(1),m.end(1)
        block=block[:a]+y+block[b:]
    return block

def _normalize_j3_rows(block):
    rows=list(re.finditer(r'\(pin passive line \(at 20 ([^ ]+) 180\)', block))
    if rows and float(rows[0].group(1)) < 0:
        ys=[m.group(1) for m in rows][::-1]
        for m,y in reversed(list(zip(rows,ys))):
            block=block[:m.start(1)]+y+block[m.end(1):]
    return block

def repair_authority(text):
    """Repair the legacy generated island using TI physical pin numbers.

    The original generator used ordinal pins for a 64-pin device and placed
    U7/J3 on top of one another.  This repair is deterministic and idempotent
    so future generation cannot silently recreate either defect.
    """
    start=text.index('(symbol "PiSXMeRevAClean:TUSB9261IPVP_STORAGE"')
    end=text.index('(symbol "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000"', start)
    block=text[start:end]
    block,n=_renumber_block(block,TUSB_PIN_NUMBERS)
    block=_flip_pin_rows(block)
    if n != len(TUSB_PIN_NUMBERS):
        raise RuntimeError('TUSB9261 definition pin count mismatch')
    text=text[:start]+block+text[end:]

    start=text.index('(symbol (lib_id "PiSXMeRevAClean:TUSB9261IPVP_STORAGE")')
    end=text.index('(symbol (lib_id "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000")', start)
    block=text[start:end]
    block,n=_renumber_block(block,TUSB_PIN_NUMBERS)
    if n != len(TUSB_PIN_NUMBERS):
        raise RuntimeError('TUSB9261 instance pin count mismatch')
    text=text[:start]+block+text[end:]

    start=text.index('(symbol "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000"')
    end=text.index('\n  (hierarchical_label ', start)
    block=_normalize_j3_rows(text[start:end])
    text=text[:start]+block+text[end:]

    # Normalize the U7 labels independently from the J3 labels.  A previous
    # broad replacement moved U7's SATA labels while trying to move J3.
    for name, y in (
        ('BRIDGE_SATA_TX_P', '91.25'), ('BRIDGE_SATA_TX_N', '93.75'),
        ('BRIDGE_SATA_RX_P', '96.25'), ('BRIDGE_SATA_RX_N', '98.75')):
        text=text.replace('(label "%s" (at 130 %s ' % (name, y),
                          '(label "%s" (at 70 %s ' % (name, y), 1)
    # Keep the M.2 connector outboard in the schematic and make its labels
    # follow it, avoiding accidental connectivity from coincident graphics.
    j3_start=text.index('(symbol (lib_id "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000")')
    label_start=text.index('(label "BRIDGE_SATA_TX_P"', text.index('(symbol (lib_id "PiSXMeRevAClean:TUSB9261IPVP_STORAGE")'))
    label_end=j3_start
    labels=text[label_start:label_end]
    for name in ('BRIDGE_SATA_TX_P','BRIDGE_SATA_TX_N','BRIDGE_SATA_RX_P','BRIDGE_SATA_RX_N','M2_3V3','M2_GND'):
        labels=labels.replace('(label "%s" (at 70 ' % name,
                              '(label "%s" (at 130 ' % name, 1)
    text=text[:label_start]+labels+text[label_end:]
    for name in ('CM5_USB3_TX_P','CM5_USB3_TX_N','CM5_USB3_RX_P','CM5_USB3_RX_N'):
        text=text.replace('(label "%s" ' % name, '(global_label "%s" (shape bidirectional) ' % name, 1)
    start=text.index('(symbol (lib_id "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000")')
    block=text[start:]
    block=block.replace('(at 50 95 0)', '(at 110 95 0)', 1)
    text=text[:start]+block
    return text

def main():
    path=ROOT/'STORAGE.kicad_sch'; text=path.read_text()
    if 'property "MPN" "TUSB9261IPVP"' in text:
        repaired=repair_authority(text)
        if repaired != text:
            path.write_text(repaired)
            print('Phase 18 storage authority repaired: TI physical pin mapping and isolated M.2 placement')
        return
    defs=(symbol('TUSB9261IPVP_STORAGE',('USB3_TX_P','USB3_TX_N','USB3_RX_P','USB3_RX_N','SATA_TX_P','SATA_TX_N','SATA_RX_P','SATA_RX_N','BRIDGE_3V3','BRIDGE_1V1','RESET','SPI_CFG')),
          symbol('JAE_SM3ZS067U410ABR1000',('SATA_TX_P','SATA_TX_N','SATA_RX_P','SATA_RX_N','M2_3V3','M2_GND')))
    s=text.index('(lib_symbols'); e=s+len(balanced(text,s))-1
    text=text[:e].rstrip()+'\n'+'\n'.join(defs)+text[e:]
    bridge=part('TUSB9261IPVP_STORAGE','U_STORAGE_BRIDGE','TUSB9261IPVP',('CM5_USB3_TX_P','CM5_USB3_TX_N','CM5_USB3_RX_P','CM5_USB3_RX_N','BRIDGE_SATA_TX_P','BRIDGE_SATA_TX_N','BRIDGE_SATA_RX_P','BRIDGE_SATA_RX_N','BRIDGE_3V3','BRIDGE_1V1','BRIDGE_RESET','BRIDGE_CFG'),0xdb000000000000000000000000000000,'PiSXMeRevAClean:TUSB9261IPVP')
    socket=part('JAE_SM3ZS067U410ABR1000','J_STORAGE_M2','SM3ZS067U410ABR1000',('BRIDGE_SATA_TX_P','BRIDGE_SATA_TX_N','BRIDGE_SATA_RX_P','BRIDGE_SATA_RX_N','M2_3V3','M2_GND'),0xdc000000000000000000000000000000,'PiSXMeRevAClean:SM3ZS067U410ABR1000')
    text=text.replace('  (sheet_instances ',bridge+'\n'+socket+'\n  (sheet_instances ',1)
    path.write_text(repair_authority(text))
    print('Phase 7 storage island generated: USB3 -> TUSB9261 -> SATA -> B-key M.2')

if __name__=='__main__': main()
