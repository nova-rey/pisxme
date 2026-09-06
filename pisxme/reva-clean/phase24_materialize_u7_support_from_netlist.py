#!/usr/bin/env python3
"""Materialize corrected U7/R24/R32/R33 from the native netlist (fixture)."""
from pathlib import Path
import argparse, xml.etree.ElementTree as ET
import pcbnew

R=Path(__file__).resolve().parent
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('pcb'); ap.add_argument('output'); a=ap.parse_args()
    b=pcbnew.LoadBoard(a.pcb); xml=ET.parse(R/'PHASE24_CLEAN_TUSB_VBUS_DIVIDER.kicadxml').getroot()
    exp={(n.get('ref'),n.get('pin')):net.get('name') for net in xml.findall('.//nets/net') for n in net.findall('node')}
    # The replacement fixture already has TI U7. Add only the new divider and
    # retain R24 if present; all pad net assignment comes from native XML.
    for ref,foot,pos in [('R32','R_0402_1005Metric',(130,152)),('R33','R_0402_1005Metric',(135,152))]:
        old=b.FindFootprintByReference(ref)
        if old: b.Remove(old)
        f=pcbnew.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),foot); f.SetReference(ref); f.SetPosition(pcbnew.VECTOR2I_MM(*pos)); b.Add(f)
        for p in f.Pads():
            name=exp.get((ref,str(p.GetNumber())))
            if not name: raise SystemExit(f'missing native netlist node {ref}.{p.GetNumber()}')
            n=b.FindNet(name) or pcbnew.NETINFO_ITEM(b,name)
            if b.FindNet(name) is None: b.Add(n)
            p.SetNet(n)
    b.Save(a.output); print(f'materialized corrected U7 support from native netlist: {a.output}')
if __name__=='__main__': main()
