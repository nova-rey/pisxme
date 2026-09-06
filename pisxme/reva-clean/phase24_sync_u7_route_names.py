#!/usr/bin/env python3
"""Normalize U7 high-speed route net names from the native netlist.

The operation changes net identity only where the native U7 ref/pin contract
provides the target name; it does not add graph edges or create copper.
"""
from pathlib import Path
import argparse, xml.etree.ElementTree as ET
import pcbnew

R=Path(__file__).resolve().parent
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('pcb'); ap.add_argument('output'); a=ap.parse_args()
    b=pcbnew.LoadBoard(a.pcb); f=b.FindFootprintByReference('U7')
    root=ET.parse(R/'PHASE24_CLEAN_TUSB_PINFIELD.kicadxml').getroot()
    exp={n.get('pin'):net.get('name') for net in root.findall('.//nets/net')
         for n in net.findall('node') if n.get('ref')=='U7'}
    # Existing candidate names are mapped by the authoritative pin field.
    old_to_new={}
    for p in f.Pads():
        if str(p.GetNumber()) in exp and p.GetNetname():
            old_to_new.setdefault(p.GetNetname(),set()).add(exp[str(p.GetNumber())])
    # Known aliases whose source-side names changed when hierarchy was fixed.
    old_to_new.update({
      '/CORE_CM5/CM5_USB3_RX_N': {'CM5_USB3_RX_N'},
      '/CORE_CM5/CM5_USB3_RX_P': {'CM5_USB3_RX_P'},
      '/CORE_CM5/CM5_USB3_TX_N': {'CM5_USB3_TX_N'},
      '/CORE_CM5/CM5_USB3_TX_P': {'CM5_USB3_TX_P'},
    })
    nets={}
    for targets in old_to_new.values():
        for name in targets:
            n=b.FindNet(name) or pcbnew.NETINFO_ITEM(b,name)
            if b.FindNet(name) is None: b.Add(n)
            nets[name]=n
    for p in f.Pads():
        num=str(p.GetNumber())
        if num in exp: p.SetNet(nets[exp[num]])
        elif p.GetNetname(): p.SetNetCode(0)
    for t in b.GetTracks():
        targets=old_to_new.get(t.GetNetname())
        if targets and len(targets)==1: t.SetNetCode(nets[next(iter(targets))].GetNetCode())
    b.SynchronizeNetsAndNetClasses(False); b.Save(a.output)
    print(f'normalized U7 native pads and route aliases; saved {a.output}')
if __name__=='__main__': main()
