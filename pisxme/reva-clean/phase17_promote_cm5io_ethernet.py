"""Promote the validated CM5IO TPD4EUSB30 topology into clean Ethernet."""
from pathlib import Path
import re
from phase3_scaffold import balanced, make_uuid

ROOT = Path(__file__).resolve().parent
SCHEMATIC = ROOT / "ETHERNET.kicad_sch"

def symbol_def():
    # The flow-through package exposes ten physical pads. Pins 1/10, 2/9,
    # 4/7, and 5/6 are the two ends of the four protected channels; pins 3/8
    # are both GND and pin 6/5 are the second channel's paired lands. Keeping
    # the duplicated physical pins in the native symbol is required so the
    # exported netlist can drive every USON pad.
    # Use unique schematic pin names; the duplicated physical lands are
    # joined by the repeated net labels in each instance, not by duplicate
    # library pin names (which KiCad's exporter can collapse).
    names = ("IO1_A", "IO2_A", "GND_A", "IO3_A", "IO4_A", "IO4_B", "IO3_B", "GND_B", "IO2_B", "IO1_B")
    pins=[]
    for i, name in enumerate(names):
        y=((len(names)-1)/2-i)*2.5
        pins.append('(pin passive line (at 20 %g 180) (length 5) (name "%s" (effects (font (size 1 1)))) (number "%d" (effects (font (size 1 1)))))' % (y,name,i+1))
    return '(symbol "PiSXMeRevAClean:TPD4EUSB30DQAR" (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes) (property "Reference" "U" (at 0 -12 0) (effects (font (size 1 1)))) (property "Value" "TPD4EUSB30DQAR" (at 0 12 0) (effects (font (size 1 1)))) (property "Footprint" "PiSXMeRevAClean:USON-10_2.5x1.0mm_P0.5mm" (at 0 0 0) (effects (font (size 1 1)) (hide yes))) (symbol "TPD4EUSB30DQAR_1_1" (rectangle (start -15 -10) (end 15 10) (stroke (width 0.254) (type default)) (fill (type background))) %s) (embedded_fonts no))' % '\n'.join(pins)

def instance(ref, nets, uid, x, y):
    labels=[]; pins=[]
    for i, net in enumerate(nets):
        py=y+(i-(len(nets)-1)/2)*2.5
        labels.append('(label "%s" (at %g %g 0) (effects (font (size 1.1 1.1)) (justify left)) (uuid %s))' % (net,x+20,py,make_uuid(uid+100+i)))
        pins.append('(pin "%d" (uuid %s))' % (i+1,make_uuid(uid+0x100+i)))
    return '\n'.join(labels)+'\n(symbol (lib_id "PiSXMeRevAClean:TPD4EUSB30DQAR") (at %s %s 0) (unit 1) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (uuid %s) (property "Reference" "%s" (at %s %s 0) (effects (font (size 1.1 1.1)))) (property "Value" "TPD4EUSB30DQAR" (at %s %s 0) (effects (font (size 1.1 1.1)))) (property "MPN" "TPD4EUSB30DQAR" (at %s %s 0) (effects (font (size 1 1)) (hide yes))) (property "Footprint" "PiSXMeRevAClean:USON-10_2.5x1.0mm_P0.5mm" (at %s %s 0) (effects (font (size 1 1)) (hide yes))) %s (instances (project "PiSXMe_RevA_Clean" (path "/30000000-0000-0000-0000-000000000000" (reference "%s") (unit 1)))) )' % (x,y,make_uuid(uid),ref,x,y-13,x,y+13,x,y,x,y,'\n'.join(pins),ref)

def replace_balanced(text, start, replacement):
    return text[:start] + replacement + text[start+len(balanced(text,start)):]

def main():
    text=SCHEMATIC.read_text()
    old='(symbol "PiSXMeRevAClean:TPD4E004DRYR"'
    if old in text:
        start=text.index(old); text=replace_balanced(text,start,symbol_def())
    else:
        old='(symbol "PiSXMeRevAClean:TPD4EUSB30DQAR"'
        start=text.index(old); text=replace_balanced(text,start,symbol_def())
    wanted = (
        ('U6',('CM5_GBE_TD0_P','CM5_GBE_TD0_N','ETH_GND','CM5_GBE_TD1_N','CM5_GBE_TD1_P','CM5_GBE_TD1_P','CM5_GBE_TD1_N','ETH_GND','CM5_GBE_TD0_N','CM5_GBE_TD0_P'),0xDC000000000000000000000000000000,50,140),
        ('U9',('CM5_GBE_TD2_P','CM5_GBE_TD2_N','ETH_GND','CM5_GBE_TD3_N','CM5_GBE_TD3_P','CM5_GBE_TD3_P','CM5_GBE_TD3_N','ETH_GND','CM5_GBE_TD2_N','CM5_GBE_TD2_P'),0xDD000000000000000000000000000000,50,180))
    needle='(symbol (lib_id "PiSXMeRevAClean:TPD4E004DRYR")'
    if needle not in text: needle='(symbol (lib_id "PiSXMeRevAClean:TPD4EUSB30DQAR")'
    positions=[]; cursor=0
    while True:
        pos=text.find(needle,cursor)
        if pos < 0: break
        positions.append(pos); cursor=pos+len(needle)
    assert len(positions) >= 2, f'expected two Ethernet ESD instances, found {len(positions)}'
    for pos, item in reversed(list(zip(positions[-2:], wanted))):
        ref,nets,uid,x,y=item
        text=replace_balanced(text,pos,instance(ref,nets,uid,x,y))
    text=text.replace('TPD4E004DRYR','TPD4EUSB30DQAR')
    text=text.replace('Package_DFN_QFN:WSON-6-1EP_1.5x1.5mm_P0.5mm_EP0.95x0.95mm','Package_SON:USON-10_2.5x1.0mm_P0.5mm')
    text=text.replace('Package_SON:USON-10_2.5x1.0mm_P0.5mm','PiSXMeRevAClean:USON-10_2.5x1.0mm_P0.5mm')
    SCHEMATIC.write_text(text); print('CM5IO Ethernet promotion applied')

if __name__=='__main__': main()
