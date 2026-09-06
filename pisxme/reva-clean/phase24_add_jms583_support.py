"""Materialize the JMS583 Rev 2.1 required support network in the child sheet."""
from phase24_integrate_dual_mode_storage import balanced, definition, instance, SCH

def main():
    text = SCH.read_text()
    if 'property "Reference" "R34"' in text:
        print('JMS583 support already present'); return
    # Values and obligations are taken from the retained JMS583 design
    # authority.  AC capacitors are explicit series elements, not labels
    # pretending to connect through the package.
    parts = [
      ('STORAGE_PASSIVE_2','R34','12k 1%','JMS_REXT','POWER_GND','R_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','L2','4.7uH','JMS_LXO','JMS_VDDREG_5V','L_2520_6332Metric'),
      ('STORAGE_CRYSTAL_4','Y2','25MHz +/-30ppm','JMS_XIN','JMS_XOUT','POWER_GND','POWER_GND','Crystal_SMD_3225-4Pin_3.2x2.5mm'),
      ('STORAGE_PASSIVE_2','C44','4.7uF','JMS_AVDD33','POWER_GND','C_0603_1608Metric'),
      ('STORAGE_PASSIVE_2','C45','100n','JMS_VCCO','POWER_GND','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C46','100n','JMS_VCCK','POWER_GND','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C47','100n','JMS_AVDDL','POWER_GND','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C48','100n','JMS_XAVDDH','POWER_GND','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','R35','10k reset pullup','JMS_RESET_N','STORAGE_3V3','R_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C49','100n reset delay','JMS_RESET_N','POWER_GND','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','R36','100k VBUS top','VBUS','JMS_VBUS_SENSE','R_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','R37','100k VBUS bottom','JMS_VBUS_SENSE','POWER_GND','R_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C50','100n USB TX1P','USB_TXP1','JMS_USB3_TXP','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C51','100n USB TX1N','USB_TXN1','JMS_USB3_TXN','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C52','100n USB TX2P','USB_TXP2','JMS_USB3_TXP2','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C53','100n USB TX2N','USB_TXN2','JMS_USB3_TXN2','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C54','220n PCIe TX0P','PCIE_TXP0','JMS_PCIE_TXP0','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C55','220n PCIe TX0N','PCIE_TXN0','JMS_PCIE_TXN0','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C56','220n PCIe TX1P','PCIE_TXP1','JMS_PCIE_TXP1','C_0402_1005Metric'),
      ('STORAGE_PASSIVE_2','C57','220n PCIe TX1N','PCIE_TXN1','JMS_PCIE_TXN1','C_0402_1005Metric'),
    ]
    defs = [definition('STORAGE_PASSIVE_2',{1:'P1',2:'P2'}),
            definition('STORAGE_CRYSTAL_4',{1:'P1',2:'P2',3:'P3',4:'P4'})]
    le=text.index('(lib_symbols'); lc=le+len(balanced(text,le))-1
    text=text[:lc].rstrip()+'\n'+'\n'.join(defs)+'\n'+text[lc:]
    uid=0xf1000000000000000000000000001600; items=[]
    for row in parts:
        name,ref,val,*rest=row; fp=rest[-1]; nets=rest[:-1]
        items.append(instance(name,ref,val,{i+1:n for i,n in enumerate(nets)},uid,300+(len(items)%4)*8,185+(len(items)//4)*6,fp))
        uid += 0x100
    marker='\n  (sheet_instances '
    text=text.replace(marker,'\n'+'\n'.join(items)+marker,1)
    SCH.write_text(text); print('added JMS583 support network:',len(parts),'parts')
if __name__=='__main__': main()
