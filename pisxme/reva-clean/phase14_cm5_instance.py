"""Promote the selected 200-pad CM5 symbol into the native CORE sheet."""
from pathlib import Path
import re
from phase3_scaffold import balanced, make_uuid

ROOT = Path(__file__).resolve().parent
SHEET = ROOT / 'CORE_CM5.kicad_sch'
LIB = ROOT / 'PiSXMe_RevA_Clean.kicad_sym'
NETS = {
    'PCIe_RX_P':'CM5_PER0_P','PCIe_RX_N':'CM5_PER0_N','PCIe_TX_P':'CM5_PET0_P','PCIe_TX_N':'CM5_PET0_N',
    'PCIe_CLK_P':'CM5_REFCLK_P','PCIe_CLK_N':'CM5_REFCLK_N','PCIe_nRST':'CM5_PERST',
    'USB3-0-TX_P':'CM5_USB3_TX_P','USB3-0-TX_N':'CM5_USB3_TX_N','USB3-0-RX_P':'CM5_USB3_RX_P','USB3-0-RX_N':'CM5_USB3_RX_N',
    'Ethernet_Pair0_P':'CM5_GBE_TD0_P','Ethernet_Pair0_N':'CM5_GBE_TD0_N','Ethernet_Pair1_P':'CM5_GBE_TD1_P','Ethernet_Pair1_N':'CM5_GBE_TD1_N',
    'Ethernet_Pair2_P':'CM5_GBE_TD2_P','Ethernet_Pair2_N':'CM5_GBE_TD2_N','Ethernet_Pair3_P':'CM5_GBE_TD3_P','Ethernet_Pair3_N':'CM5_GBE_TD3_N',
    '+5v_(Input)':'CM5_5V','GND':'POWER_GND',
}

def main():
    text = SHEET.read_text()
    if 'property "MPN" "ComputeModule5-CM5"' in text: return
    source = LIB.read_text(); start = source.index('(symbol "PiSXMeRevAClean:ComputeModule5-CM5"')
    definition = balanced(source, start)
    root_source = (ROOT / 'PiSXMe_RevA_Clean.kicad_sch').read_text()
    flag_start = root_source.index('(symbol "power:PWR_FLAG"')
    flag_definition = balanced(root_source, flag_start)
    def section(name):
        s = definition.index('(symbol "' + name + '"')
        return balanced(definition, s)
    def pins_in(section_text):
        out = []
        for m in re.finditer(r'\(pin [^\n]*\n\s*\(at ([^\n]+)\).*?\(name "([^"]+)".*?\(number "([^"]+)"', section_text, re.S):
            x, y, angle = m.group(1).split()
            out.append((m.group(2), m.group(3), float(x), float(y)))
        return out
    first, second = pins_in(section('ComputeModule5-CM5_1_1')), pins_in(section('ComputeModule5-CM5_2_1'))
    p = first + second
    assert len(p) == 200, len(p)
    s = text.index('(lib_symbols'); e = s + len(balanced(text, s)) - 1
    text = text[:e].rstrip() + '\n' + definition + '\n' + flag_definition + text[e:]
    uid = 0xe3000000000000000000000000000000
    def inst(unit, unit_pins, instance_uid):
        pins = ''.join(f'(pin "{number}" (uuid {make_uuid(instance_uid+i)}))\n' for i, (_,number,_,_) in enumerate(unit_pins))
        return f'''(symbol (lib_id "PiSXMeRevAClean:ComputeModule5-CM5") (at 100 100 0) (unit {unit}) (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (uuid {make_uuid(instance_uid)})
 (property "Reference" "J7" (at 100 25 0) (effects (font (size 1.1 1.1))))
 (property "Value" "ComputeModule5-CM5" (at 100 165 0) (effects (font (size 1.1 1.1))))
 (property "MPN" "ComputeModule5-CM5" (at 100 100 0) (effects (font (size 1 1)) (hide yes)))
 (property "Footprint" "PiSXMeRevAClean:PiSXMeRevAClean_Raspberry_Pi_5_Compute_Module" (at 100 100 0) (effects (font (size 1 1)) (hide yes)))
 {pins}(instances (project "PiSXMe_RevA_Clean" (path "/30000000-0000-0000-0000-000000000000/10000000-0000-0000-0000-000000000001" (reference "J7") (unit {unit})))) )'''
    instances = inst(1, first, uid) + inst(2, second, uid+150)
    # KiCad schematic coordinates have a downward-positive sheet Y axis;
    # library pin coordinates use the opposite sign when instantiated.
    labels = [f'(label "{NETS[name]}" (at {100+x:g} {100-y:g} 0) (effects (font (size 1 1)) (justify left)) (uuid {make_uuid(uid+300+i)}))' for i,(name,_,x,y) in enumerate(p) if name in NETS]
    nc = [f'(no_connect (at {100+x:g} {100-y:g}) (uuid {make_uuid(uid+500+i)}))' for i,(name,_,x,y) in enumerate(p) if name not in NETS]
    # +5 V is an externally supplied rail at this interface.  A local
    # PWR_FLAG documents that supply to ERC without changing CM5 pin types.
    pwr = next((100+x, 100-y) for name,_,x,y in p if name == '+5v_(Input)')
    flag = f'''(symbol (lib_id "power:PWR_FLAG") (at {pwr[0]:g} {pwr[1]:g} 0) (unit 1) (exclude_from_sim no) (in_bom no) (on_board no) (dnp no) (uuid {make_uuid(uid+700)})
 (property "Reference" "#FLG01" (at {pwr[0]:g} {pwr[1]-2.54:g} 0) (effects (font (size 1 1)) (hide yes)))
 (property "Value" "PWR_FLAG" (at {pwr[0]:g} {pwr[1]+2.54:g} 0) (effects (font (size 1 1)) (hide yes)))
 (pin "1" (uuid {make_uuid(uid+701)})) (instances (project "PiSXMe_RevA_Clean" (path "/30000000-0000-0000-0000-000000000000/10000000-0000-0000-0000-000000000001" (reference "#FLG01") (unit 1)))) )'''
    text = text.replace('  (sheet_instances ', '\n'.join(labels + nc) + '\n' + flag + '\n' + instances + '\n  (sheet_instances ', 1)
    SHEET.write_text(text); print(f'Phase 14 CM5 instance: J7; pins={len(p)}; mapped={len(labels)}')

if __name__ == '__main__': main()
