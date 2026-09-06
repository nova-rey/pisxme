#!/usr/bin/env python3
"""Replace only U7 in a disposable PCB with the TI 65-pad footprint."""
from pathlib import Path
import argparse
import xml.etree.ElementTree as ET
import pcbnew

R=Path(__file__).resolve().parent
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('pcb'); ap.add_argument('output'); ap.add_argument('--xml', default='PHASE24_CLEAN_TUSB_VBUS_DIVIDER.kicadxml'); a=ap.parse_args()
    b=pcbnew.LoadBoard(a.pcb); old=b.FindFootprintByReference('U7')
    if old is None: raise SystemExit('U7 missing')
    xml=ET.parse(R/a.xml).getroot()
    expected={n.get('pin'):net.get('name') for net in xml.findall('.//nets/net')
              for n in net.findall('node') if n.get('ref')=='U7'}
    new=pcbnew.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),'TUSB9261IPVP_PVP0064A')
    if new is None or new.GetPadCount()!=65: raise SystemExit('TI footprint load failed')
    new.SetReference('U7'); new.SetPosition(old.GetPosition()); new.SetOrientation(old.GetOrientation())
    nets={}
    for name in set(expected.values()):
        # The repaired export may contain local XML names while the saved PCB
        # carries the authoritative hierarchical spelling.  Resolve by exact
        # name first, then by an unambiguous hierarchical suffix; never create
        # a duplicate net merely because the export omitted its hierarchy.
        suffix = [b.GetNetsByName()[k] for k in b.GetNetsByName()
                  if str(k).endswith("/" + name)]
        # Prefer the carrier's canonical hierarchy for shared CM5 signals.
        # This also avoids SWIG FindNet() ambiguity when a stale local alias
        # exists in a disposable donor board.
        preferred = [n for n in suffix if str(n.GetNetname()).startswith("/CORE_CM5/")]
        n = preferred[0] if len(preferred) == 1 else (suffix[0] if len(suffix) == 1 else b.FindNet(name))
        if n is None:
            n=pcbnew.NETINFO_ITEM(b,name); b.Add(n)
        nets[name]=n
    for p in new.Pads():
        name=expected.get(str(p.GetNumber()))
        if name: p.SetNet(nets[name])
    b.Remove(old); b.Add(new); b.Save(a.output)
    print(f'replaced U7 with TI 65-pad footprint; assigned {len(expected)} native pin nets; saved {a.output}')
if __name__=='__main__': main()
