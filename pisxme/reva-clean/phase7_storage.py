"""Generate the schematic-only USB3-to-SATA storage island."""
from pathlib import Path
import re
from phase3_scaffold import balanced, make_uuid

ROOT=Path(__file__).resolve().parent
STORAGE_INSTANCE_PATH="/30000000-0000-0000-0000-000000000000/10000000-0000-0000-0000-000000000007"

def symbol(name,pins,reference='U'):
    rows=[]
    for i,p in enumerate(pins):
        y=(i-(len(pins)-1)/2)*2.5
        rows.append('(pin passive line (at 20 %g 180) (length 5) (name "%s" (effects (font (size 1 1)))) (number "%d" (effects (font (size 1 1)))))'%(y,p,i+1))
    return '(symbol "PiSXMeRevAClean:%s" (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes) (property "Reference" "%s" (at 0 -12 0) (effects (font (size 1 1)))) (property "Value" "%s" (at 0 12 0) (effects (font (size 1 1)))) (property "Footprint" "" (at 0 0 0) (effects (font (size 1 1)) (hide yes))) (symbol "%s_1_1" (rectangle (start -15 -10) (end 15 10) (stroke (width 0.254) (type default)) (fill (type background))) %s) (embedded_fonts no))'%(name,reference,name,name,'\n'.join(rows))

def part(lib,ref,mpn,nets,uid,footprint=''):
    labels=[]; pins=[]
    for i,net in enumerate(nets):
        y=95+(i-(len(nets)-1)/2)*2.5
        labels.append('(label "%s" (at 70 %g 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid %s))'%(net,y,make_uuid(uid+100+i)))
        pins.append('(pin "%d" (uuid %s))'%(i+1,make_uuid(uid+i)))
    return '\n'.join(labels)+'\n(symbol (lib_id "PiSXMeRevAClean:%s") (at 50 95 0) (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (uuid %s) (property "Reference" "%s" (at 50 82 0) (effects (font (size 1.1 1.1)))) (property "Value" "%s" (at 50 108 0) (effects (font (size 1.1 1.1)))) (property "MPN" "%s" (at 50 95 0) (effects (font (size 1 1)) (hide yes))) (property "Footprint" "%s" (at 50 95 0) (effects (font (size 1 1)) (hide yes))) %s (instances (project "PiSXMe_RevA_Clean" (path "%s" (reference "%s") (unit 1)))) )'%(lib,make_uuid(uid),ref,mpn,mpn,footprint,'\n'.join(pins),STORAGE_INSTANCE_PATH,ref)

def part_at(lib,ref,mpn,nets,uid,x,y,footprint=''):
    """Emit a small local storage-support part with labels on every pin."""
    labels=[]; pins=[]
    for i,net in enumerate(nets):
        # Schematic Y coordinates increase downward in the serialized file,
        # while the library pin rows are authored in the opposite visual
        # order.  Mirror the label rows so pin 1 lands on the first library
        # pin instead of silently inheriting the neighboring net.
        py=y-(i-(len(nets)-1)/2)*2.5
        labels.append('(label "%s" (at %g %g 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid %s))' % (net,x+20,py,make_uuid(uid+100+i)))
        pins.append('(pin "%d" (uuid %s))' % (i+1,make_uuid(uid+i)))
    return '\n'.join(labels)+'\n(symbol (lib_id "PiSXMeRevAClean:%s") (at %g %g 0) (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (uuid %s) (property "Reference" "%s" (at %g %g 0) (effects (font (size 1.1 1.1)))) (property "Value" "%s" (at %g %g 0) (effects (font (size 1.1 1.1)))) (property "MPN" "%s" (at %g %g 0) (effects (font (size 1 1)) (hide yes))) (property "Footprint" "%s" (at %g %g 0) (effects (font (size 1 1)) (hide yes))) %s (instances (project "PiSXMe_RevA_Clean" (path "%s" (reference "%s") (unit 1)))) )' % (lib,x,y,make_uuid(uid+50),ref,x,y-13,mpn,x,y+13,mpn,x,y,footprint,x,y,'\n'.join(pins),STORAGE_INSTANCE_PATH,ref)

def inline_cap_part(ref,mpn,net_in,net_out,uid,x=50,y=95):
    """Place a two-pin SATA coupling capacitor with distinct net sides."""
    labels=(
        '(label "%s" (at %g %g 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid %s))' % (net_in,x+20,y-1.25,make_uuid(uid+100)),
        '(label "%s" (at %g %g 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid %s))' % (net_out,x+20,y+1.25,make_uuid(uid+101)),
    )
    pins=( '(pin "1" (uuid %s))' % make_uuid(uid),
           '(pin "2" (uuid %s))' % make_uuid(uid+1) )
    body=f'''(symbol (lib_id "PiSXMeRevAClean:SATA_AC_CAP") (at {x:g} {y:g} 0)
 (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no)
 (uuid {make_uuid(uid+2)})
 (property "Reference" "{ref}" (at {x:g} {y-13:g} 0) (effects (font (size 1.1 1.1))))
 (property "Value" "100nF" (at {x:g} {y+13:g} 0) (effects (font (size 1.1 1.1))))
 (property "MPN" "{mpn}" (at {x:g} {y:g} 0) (effects (font (size 1 1)) (hide yes)))
 (property "Footprint" "PiSXMeRevAClean:C_0402_1005Metric" (at {x:g} {y:g} 0) (effects (font (size 1 1)) (hide yes)))
 {' '.join(pins)}
 (instances (project "PiSXMe_RevA_Clean" (path "{STORAGE_INSTANCE_PATH}" (reference "{ref}") (unit 1)))) )'''
    return '\n'.join(labels)+'\n'+body

# CM5 is the USB host side of the TUSB9261 device link: CM5 RX receives the
# bridge's SSTX, while CM5 TX drives the bridge's SSRX.
TUSB_PIN_NUMBERS=(46,45,43,42,57,56,60,59,24,41,4,21,30,31,52,53,54)

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

def ensure_sata_coupling_caps(text):
    """Add four distinct-net inline SATA coupling capacitors idempotently."""
    if '(symbol "PiSXMeRevAClean:SATA_AC_CAP"' not in text:
        cap_def=symbol('SATA_AC_CAP',('SATA_IN','SATA_OUT'),'C')
        s=text.index('(lib_symbols'); e=s+len(balanced(text,s))-1
        text=text[:e].rstrip()+'\n'+cap_def+text[e:]
    caps=(
        ('C30','BRIDGE_SATA_TX_P','SATA_M2_TX_P',0xee000000000000000000000000000000),
        ('C31','BRIDGE_SATA_TX_N','SATA_M2_TX_N',0xee000000000000000000000000000000+16),
        ('C32','BRIDGE_SATA_RX_P','SATA_M2_RX_P',0xee000000000000000000000000000000+32),
        ('C33','BRIDGE_SATA_RX_N','SATA_M2_RX_N',0xee000000000000000000000000000000+48),
    )
    instances='\n'.join(inline_cap_part(ref,'GRM155R71C104KA88D',src,dst,uid,80+i*12,120)
                         for i,(ref,src,dst,uid) in enumerate(caps))
    j3_start=text.index('(symbol (lib_id "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000")')
    j3_end=j3_start+len(balanced(text,j3_start))
    sheet=text.index('\n  (sheet_instances ',j3_end)
    text=text[:j3_end]+'\n'+instances+text[sheet:]
    # The connector terminates on the capacitor output side.
    start=text.index('(symbol (lib_id "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000")')
    j3_end=start+len(balanced(text,start))
    block=text[start:j3_end]
    for old,new in (
        ('BRIDGE_SATA_TX_P','SATA_M2_TX_P'),('BRIDGE_SATA_TX_N','SATA_M2_TX_N'),
        ('BRIDGE_SATA_RX_P','SATA_M2_RX_P'),('BRIDGE_SATA_RX_N','SATA_M2_RX_N')):
        block=block.replace('"%s"' % old,'"%s"' % new)
    # The six labels feeding J3 are outside its symbol block.  Rename only
    # that interconnect region; U7 labels remain on the bridge-side nets.
    label_start=text.rfind('(label "BRIDGE_SATA_TX_P"',0,start)
    if label_start >= 0:
        old_labels=text[label_start:start]
        labels=old_labels
        for old,new in (
            ('BRIDGE_SATA_TX_P','SATA_M2_TX_P'),('BRIDGE_SATA_TX_N','SATA_M2_TX_N'),
            ('BRIDGE_SATA_RX_P','SATA_M2_RX_P'),('BRIDGE_SATA_RX_N','SATA_M2_RX_N')):
            labels=labels.replace('(label "%s" (at 130 ' % old,
                                  '(label "%s" (at 130 ' % new)
        delta=len(labels)-len(old_labels)
        text=text[:label_start]+labels+text[start:]
        start += delta
        j3_end += delta
    return text[:start]+block+text[j3_end:]

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
    if n == 12:
        extra='\n'.join((
            '(pin passive line (at 20 -16.25 180) (length 5) (name "FREQSEL0" (effects (font (size 1 1)))) (number "30" (effects (font (size 1 1)))))',
            '(pin passive line (at 20 -18.75 180) (length 5) (name "FREQSEL1" (effects (font (size 1 1)))) (number "31" (effects (font (size 1 1)))))',
            '(pin passive line (at 20 -21.25 180) (length 5) (name "XI" (effects (font (size 1 1)))) (number "52" (effects (font (size 1 1)))))',
            '(pin passive line (at 20 -23.75 180) (length 5) (name "VSSOSC" (effects (font (size 1 1)))) (number "53" (effects (font (size 1 1)))))',
            '(pin passive line (at 20 -26.25 180) (length 5) (name "XO" (effects (font (size 1 1)))) (number "54" (effects (font (size 1 1)))))'))
        block=block.replace(')) (embedded_fonts no))','))\n'+extra+' (embedded_fonts no))',1)
        n=15
    block=_flip_pin_rows(block)
    if n != len(TUSB_PIN_NUMBERS):
        raise RuntimeError('TUSB9261 definition pin count mismatch')
    text=text[:start]+block+text[end:]

    start=text.index('(symbol (lib_id "PiSXMeRevAClean:TUSB9261IPVP_STORAGE")')
    end=text.index('(symbol (lib_id "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000")', start)
    block=text[start:end]
    block,n=_renumber_block(block,TUSB_PIN_NUMBERS)
    if n == 12:
        block=block.replace('(pin "21" (uuid db000000-0000-0000-0000-00000000010b))', '(pin "21" (uuid db000000-0000-0000-0000-00000000010b))\n(pin "30" (uuid db000000-0000-0000-0000-00000000010c))\n(pin "31" (uuid db000000-0000-0000-0000-00000000010d))\n(pin "52" (uuid db000000-0000-0000-0000-00000000010e))\n(pin "53" (uuid db000000-0000-0000-0000-00000000010f))\n(pin "54" (uuid db000000-0000-0000-0000-000000000110))',1)
        n=15
    elif n == 15:
        # Existing materialized children already have the three clock pins;
        # insert the two frequency-select entries before them by extending the
        # renumbered instance with the final XO/VSSOSC records.
        block=block.replace('(pin "52" (uuid db000000-0000-0000-0000-00000000010e))', '(pin "52" (uuid db000000-0000-0000-0000-00000000010e))\n(pin "53" (uuid db000000-0000-0000-0000-00000000010f))\n(pin "54" (uuid db000000-0000-0000-0000-000000000110))',1)
        n=17
    if n != len(TUSB_PIN_NUMBERS):
        raise RuntimeError('TUSB9261 instance pin count mismatch')
    text=text[:start]+block+text[end:]

    start=text.index('(symbol "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000"')
    end=text.index('\n  (hierarchical_label ', start)
    block=_normalize_j3_rows(text[start:end])
    text=text[:start]+block+text[end:]
    text=ensure_sata_coupling_caps(text)

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
    # Restore the bridge-side U7 labels explicitly after any prior malformed
    # run; only the connector-side labels use SATA_M2_* names.
    for old,new in (
        ('SATA_M2_TX_P','BRIDGE_SATA_TX_P'),('SATA_M2_TX_N','BRIDGE_SATA_TX_N'),
        ('SATA_M2_RX_P','BRIDGE_SATA_RX_P'),('SATA_M2_RX_N','BRIDGE_SATA_RX_N')):
        text=text.replace('(label "%s" (at 70 ' % old,
                          '(label "%s" (at 70 ' % new, 1)
    # The reference-clock pins are local to the storage island.  Keep them
    # off the root sheet contract while making the source-side connectivity
    # explicit and machine-visible.
    if '(label "BRIDGE_XI"' not in text:
        anchor=text.index('(symbol (lib_id "PiSXMeRevAClean:TUSB9261IPVP_STORAGE")')
        clock_labels='\n'.join((
            '(label "BRIDGE_3V3" (at 70 111.25 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid db000000-0000-0000-0000-000000000170))',
            '(label "BRIDGE_3V3" (at 70 113.75 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid db000000-0000-0000-0000-000000000171))',
            '(label "BRIDGE_XI" (at 70 116.25 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid db000000-0000-0000-0000-000000000172))',
            '(label "BRIDGE_VSSOSC" (at 70 118.75 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid db000000-0000-0000-0000-000000000173))',
            '(label "BRIDGE_XO" (at 70 121.25 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid db000000-0000-0000-0000-000000000174))'))
        text=text[:anchor]+clock_labels+'\n'+text[anchor:]
    # The legacy repair path above has historically performed broad suffix
    # rewrites. Re-run the idempotent storage-side normalization last so a
    # rerun can never leave duplicate J3 instances or stale cap-side labels.
    text=ensure_sata_coupling_caps(text)
    text=ensure_clock_network(text)
    return text

def ensure_clock_network(text):
    """Expose and populate TI's required 40 MHz crystal reference network."""
    defs='\n'.join((
        symbol('CLOCK_XTAL_4P',('XI','GND','XO','NC'),'Y'),
        symbol('CLOCK_R',('XI','XO'),'R'),
        symbol('CLOCK_C',('CLOCK','GND'),'C'),
    ))
    # Rebuild the four physical clock-support instances on every invocation;
    # this keeps the repair path idempotent while allowing corrected net names
    # and pin-row placement to replace an earlier experimental instance.
    for ref in ('Y1','R23','C42','C43'):
        token='(property "Reference" "%s"' % ref
        while token in text:
            prop=text.index(token)
            start=text.rfind('(symbol (lib_id',0,prop)
            if start < 0:
                raise RuntimeError('clock instance anchor missing for '+ref)
            text=text[:start]+text[start+len(balanced(text,start)):]
    # Keep these library definitions inside lib_symbols.  The legacy storage
    # child has its final SATA definition immediately before the lib_symbols
    # close, so inserting after that definition creates malformed top-level
    # symbols that native KiCad refuses to load.
    for name in ('CLOCK_XTAL_4P','CLOCK_R','CLOCK_C'):
        marker='(symbol "PiSXMeRevAClean:%s"' % name
        if marker in text:
            start=text.index(marker)
            text=text[:start]+text[start+len(balanced(text,start)):]
    marker='\n(symbol "PiSXMeRevAClean:SATA_AC_CAP"'
    text=text.replace(marker,'\n'+defs+marker,1)
    # Keep the abstract helper symbols away from the legacy SATA-cap labels;
    # coincident label coordinates can merge unrelated nets in KiCad's parser.
    y1=part_at('CLOCK_XTAL_4P','Y1','ECS-400-18-33-JGN-TR3',('BRIDGE_XI','BRIDGE_VSSOSC','BRIDGE_XO','BRIDGE_VSSOSC'),0xef000000000000000000000000000000,150,130,'PiSXMeRevAClean:Crystal_3225_4Pad')
    r23=part_at('CLOCK_R','R23','1M',('BRIDGE_XI','BRIDGE_XO'),0xef000000000000000000000000000010,150,140,'PiSXMeRevAClean:R_0402_1005Metric')
    c34=part_at('CLOCK_C','C42','18pF',('BRIDGE_XI','BRIDGE_VSSOSC'),0xef000000000000000000000000000020,180,130,'PiSXMeRevAClean:C_0402_1005Metric')
    c35=part_at('CLOCK_C','C43','18pF',('BRIDGE_XO','BRIDGE_VSSOSC'),0xef000000000000000000000000000030,180,140,'PiSXMeRevAClean:C_0402_1005Metric')
    marker=text.index('\n  (sheet_instances ')
    text=text[:marker]+'\n'+y1+'\n'+r23+'\n'+c34+'\n'+c35+text[marker:]
    return text

def main():
    path=ROOT/'STORAGE.kicad_sch'; text=path.read_text()
    if 'property "MPN" "TUSB9261IPVP"' in text:
        repaired=repair_authority(text)
        if repaired != text:
            path.write_text(repaired)
            print('Phase 18 storage authority repaired: TI physical pin mapping and isolated M.2 placement')
        return
    defs=(symbol('TUSB9261IPVP_STORAGE',('USB3_TX_P','USB3_TX_N','USB3_RX_P','USB3_RX_N','SATA_TX_P','SATA_TX_N','SATA_RX_P','SATA_RX_N','BRIDGE_3V3','BRIDGE_1V1','RESET','SPI_CFG','BRIDGE_XI','BRIDGE_VSSOSC','BRIDGE_XO')),
          symbol('JAE_SM3ZS067U410ABR1000',('SATA_TX_P','SATA_TX_N','SATA_RX_P','SATA_RX_N','M2_3V3','M2_GND')))
    s=text.index('(lib_symbols'); e=s+len(balanced(text,s))-1
    text=text[:e].rstrip()+'\n'+'\n'.join(defs)+text[e:]
    bridge=part('TUSB9261IPVP_STORAGE','U_STORAGE_BRIDGE','TUSB9261IPVP',('CM5_USB3_TX_P','CM5_USB3_TX_N','CM5_USB3_RX_P','CM5_USB3_RX_N','BRIDGE_SATA_TX_P','BRIDGE_SATA_TX_N','BRIDGE_SATA_RX_P','BRIDGE_SATA_RX_N','BRIDGE_3V3','BRIDGE_1V1','BRIDGE_RESET','BRIDGE_CFG','BRIDGE_XI','BRIDGE_VSSOSC','BRIDGE_XO'),0xdb000000000000000000000000000000,'PiSXMeRevAClean:TUSB9261IPVP')
    socket=part('JAE_SM3ZS067U410ABR1000','J_STORAGE_M2','SM3ZS067U410ABR1000',('BRIDGE_SATA_TX_P','BRIDGE_SATA_TX_N','BRIDGE_SATA_RX_P','BRIDGE_SATA_RX_N','M2_3V3','M2_GND'),0xdc000000000000000000000000000000,'PiSXMeRevAClean:SM3ZS067U410ABR1000')
    text=text.replace('  (sheet_instances ',bridge+'\n'+socket+'\n  (sheet_instances ',1)
    path.write_text(repair_authority(text))
    print('Phase 7 storage island generated: USB3 -> TUSB9261 -> SATA -> B-key M.2')

if __name__=='__main__': main()
