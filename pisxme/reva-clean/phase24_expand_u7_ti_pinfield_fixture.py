#!/usr/bin/env python3
"""Build a disposable STORAGE sheet with the complete TI U7 pin field."""
from pathlib import Path
import argparse, re, shutil

EXTRA = {
 '1':'BRIDGE_1V1','7':'BRIDGE_3V3','12':'BRIDGE_1V1','19':'BRIDGE_1V1',
 '32':'BRIDGE_1V1','33':'BRIDGE_1V1','34':'BRIDGE_3V3','35':'BRIDGE_USB_DM',
 '36':'BRIDGE_USB_DP','38':'BRIDGE_R1','39':'BRIDGE_R1RTN','40':'BRIDGE_3V3',
 '44':'POWER_GND','47':'BRIDGE_1V1','48':'BRIDGE_3V3','49':'BRIDGE_1V1',
 '50':'CM5_5V','51':'BRIDGE_3V3','55':'BRIDGE_1V1','58':'POWER_GND',
 '61':'BRIDGE_1V1','62':'BRIDGE_3V3','63':'BRIDGE_1V1','65':'POWER_GND',
}
EXISTING = [('46','USB3_TX_P',13.75),('45','USB3_TX_N',11.25),('43','USB3_RX_P',8.75),
 ('42','USB3_RX_N',6.25),('57','SATA_TX_P',3.75),('56','SATA_TX_N',1.25),
 ('60','SATA_RX_P',-1.25),('59','SATA_RX_N',-3.75),('24','BRIDGE_3V3',-6.25),
 ('41','BRIDGE_1V1',-8.75),('4','RESET',-11.25),('21','SPI_CFG',-13.75),
 ('30','FREQSEL0',-16.25),('31','FREQSEL1',-18.75),('52','XI',-21.25),
 ('53','VSSOSC',-23.75),('54','XO',-26.25)]

def pin(num,name,y,kind='passive'):
    return f'(pin {kind} line (at 20 {y:.2f} 180) (length 5) (name "{name}" (effects (font (size 1 1)))) (number "{num}" (effects (font (size 1 1)))))'

def make_symbol():
    lines=['(symbol "PiSXMeRevAClean:TUSB9261IPVP_STORAGE" (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes) (property "Reference" "U" (at 0 -12 0) (effects (font (size 1 1)))) (property "Value" "TUSB9261IPVP_STORAGE" (at 0 12 0) (effects (font (size 1 1)))) (property "Footprint" "" (at 0 0 0) (effects (font (size 1 1)) (hide yes))) (symbol "TUSB9261IPVP_STORAGE_1_1" (rectangle (start -15 -10) (end 15 10) (stroke (width 0.254) (type default)) (fill (type background)))']
    for num,name,y in EXISTING: lines.append(pin(num,name,y))
    for i,(num,net) in enumerate(EXTRA.items()): lines.append(pin(num,net,-30-2.5*i))
    lines.append(') (embedded_fonts no))')
    return '\n'.join(lines)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',default='phase24_u7_ti_pinfield_fixture'); ap.add_argument('--apply',action='store_true'); a=ap.parse_args()
    root=Path(__file__).resolve().parent; out=root/a.out
    if a.apply:
        out=root
    else:
        if out.exists(): shutil.rmtree(out)
        out.mkdir()
        for p in root.glob('*.kicad_sch'): shutil.copy2(p,out/p.name)
    f=out/'STORAGE.kicad_sch'; s=f.read_text()
    start=s.index('(symbol "PiSXMeRevAClean:TUSB9261IPVP_STORAGE"')
    end=s.index('(symbol "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000"',start)
    s=s[:start]+make_symbol()+'\n'+s[end:]
    start=s.index('(symbol (lib_id "PiSXMeRevAClean:TUSB9261IPVP_STORAGE")')
    end=s.index('(symbol (lib_id "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000")',start)
    block=s[start:end]
    uuids=[]
    for i,num in enumerate(EXTRA):
        uid=f'db000000-0000-0000-0000-{i+300:012d}'
        uuids.append((num,uid))
    insert='\n'.join(f'(pin "{n}" (uuid {u}))' for n,u in uuids)+'\n'
    block=block.replace('(instances ',insert+'(instances ',1)
    s=s[:start]+block+s[end:]
    labels=[]
    for i,(num,net) in enumerate(EXTRA.items()):
        y=125+2.5*i; uid=f'de000000-0000-0000-0000-{i+300:012d}'
        labels.append(f'(global_label "{net}" (shape bidirectional) (at 70 {y:.2f} 0) (effects (font (size 1 1)) (justify left)) (uuid {uid}))')
    marker='\n(symbol (lib_id "PiSXMeRevAClean:JAE_SM3ZS067U410ABR1000")'
    s=s.replace(marker,'\n'+'\n'.join(labels)+marker,1)
    f.write_text(s)
    print(out)
if __name__=='__main__': main()
