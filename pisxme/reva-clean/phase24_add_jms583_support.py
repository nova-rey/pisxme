"""Materialize the JMS583 Rev 2.1 required support network in the child sheet."""
from phase24_integrate_dual_mode_storage import balanced, definition, support_instance, SCH

SUPPORT_LABELS = {
    'f1000000-0000-0000-0000-000000001665': ('POWER_GND', '320 184.365'),
    'f1000000-0000-0000-0000-000000001666': ('JMS_REXT', '320 185.635'),
    'f1000000-0000-0000-0000-000000001765': ('JMS_VDDREG_5V', '328 184.365'),
    'f1000000-0000-0000-0000-000000001766': ('LXO', '328 185.635'),
    'f1000000-0000-0000-0000-000000001865': ('POWER_GND', '336 183.095'),
    'f1000000-0000-0000-0000-000000001866': ('POWER_GND', '336 184.365'),
    'f1000000-0000-0000-0000-000000001867': ('XOUT', '336 185.635'),
    'f1000000-0000-0000-0000-000000001868': ('XIN', '336 186.905'),
}

def reconcile_existing_support(text):
    """Migrate the one prior support cohort by full UUID and known old atom.

    This is intentionally fail-closed: every target must occur exactly once,
    and no broad coordinate/name substitution is permitted.
    """
    for uid, (name, xy) in SUPPORT_LABELS.items():
        marker = '(label "'
        start = text.find('(uuid ' + uid + '))')
        if start < 0:
            raise ValueError('missing support label UUID ' + uid)
        atom_start = text.rfind(marker, 0, start)
        atom_end = text.find('))', start) + 2
        atom = text[atom_start:atom_end]
        if f'(label "{name}" (at {xy} 0)' in atom:
            continue
        import re
        updated = re.sub(r'\(label "[^"]+" \(at [^)]+\)',
                         f'(label "{name}" (at {xy} 0)', atom, count=1)
        if updated == atom:
            raise ValueError('could not rewrite support label UUID ' + uid)
        text = text[:atom_start] + updated + text[atom_end:]
    return text

def main():
    text = SCH.read_text()
    if 'property "Reference" "R80"' in text:
        text = reconcile_existing_support(text)
        SCH.write_text(text)
        print('reconciled existing JMS583 support label frame/net names')
        return
    # Values and obligations are taken from the retained JMS583 design
    # authority.  AC capacitors are explicit series elements, not labels
    # pretending to connect through the package.
    parts = [
      ('STORAGE_PASSIVE_2','R80','12k 1%','JMS_REXT','POWER_GND','R_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','L10','4.7uH','LXO','JMS_VDDREG_5V','L_2520_6332Metric'),
      ('STORAGE_CRYSTAL_4','Y10','25MHz +/-30ppm','XIN','XOUT','POWER_GND','POWER_GND','Crystal_SMD_3225-4Pin_3.2x2.5mm'),
      ('STORAGE_PASSIVE_2','C80','4.7uF','JMS_AVDD33','POWER_GND','C_0603_1608Metric'),
      ('STORAGE_PASSIVE_2','C81','100n','JMS_VCCO','POWER_GND','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C82','100n','JMS_VCCK','POWER_GND','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C83','100n','JMS_AVDDL','POWER_GND','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C84','100n','JMS_XAVDDH','POWER_GND','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','R81','10k reset pullup','JMS_RESET_N','STORAGE_3V3','R_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C85','100n reset delay','JMS_RESET_N','POWER_GND','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','R82','100k VBUS top','VBUS','JMS_VBUS_SENSE','R_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','R83','100k VBUS bottom','JMS_VBUS_SENSE','POWER_GND','R_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C86','100n USB TX1P','USB_TXP1','JMS_USB3_TXP','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C87','100n USB TX1N','USB_TXN1','JMS_USB3_TXN','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C88','100n USB TX2P','USB_TXP2','JMS_USB3_TXP2','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C89','100n USB TX2N','USB_TXN2','JMS_USB3_TXN2','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C90','220n PCIe TX0P','PCIE_TXP0','JMS_PCIE_TXP0','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C91','220n PCIe TX0N','PCIE_TXN0','JMS_PCIE_TXN0','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C92','220n PCIe TX1P','PCIE_TXP1','JMS_PCIE_TXP1','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C93','220n PCIe TX1N','PCIE_TXN1','JMS_PCIE_TXN1','C_0402_1005Metric'),
    ]
    defs = [definition('STORAGE_PASSIVE_2',{1:'P1',2:'P2'}),
            definition('STORAGE_CRYSTAL_4',{1:'P1',2:'P2',3:'P3',4:'P4'})]
    le=text.index('(lib_symbols'); lc=le+len(balanced(text,le))-1
    text=text[:lc].rstrip()+'\n'+'\n'.join(defs)+'\n'+text[lc:]
    uid=0xf1000000000000000000000000001600; items=[]
    for row in parts:
        name,ref,val,*rest=row; fp=rest[-1]; nets=rest[:-1]
        items.append(support_instance(name,ref,val,{i+1:n for i,n in enumerate(nets)},uid,300+(len(items)%4)*8,185+(len(items)//4)*6,fp))
        uid += 0x100
    marker='\n  (sheet_instances '
    text=text.replace(marker,'\n'+'\n'.join(items)+marker,1)
    SCH.write_text(text); print('added JMS583 support network:',len(parts),'parts')
if __name__=='__main__': main()
