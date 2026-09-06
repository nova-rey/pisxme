"""Fail-closed audits for the dual-mode storage library candidates.

This checks only facts present in the saved native footprints. It deliberately
does not synthesize connectivity or treat the mode matrix as physical copper.
"""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent
LIB=ROOT/'PiSXMe_RevA_Clean.pretty'

def pads(path):
    return re.findall(r'\(pad "([^"]+)"\s+(\w+)', path.read_text())

def main():
    checks=[]
    p=pads(LIB/'JMS583_QFN64_8x8.kicad_mod')
    checks.append(('JMS583 has 64 pads',len(p)==64))
    checks.append(('JMS583 numbering is 1..64',[x[0] for x in p]==[str(i) for i in range(1,65)]))
    p=pads(LIB/'TE_1-2199230-4_MKEY.kicad_mod')
    expected=[str(i) for i in range(1,59)]+[str(i) for i in range(67,76)]
    checks.append(('TE M-key has 67 contacts plus four mechanical pads',len(p)==71))
    checks.append(('TE M-key preserves key gap 59..66',[x[0] for x in p[:67]]==expected))
    for name,ok in checks:
        print(('PASS' if ok else 'FAIL')+' '+name)
    if not all(ok for _,ok in checks): raise SystemExit(1)

if __name__=='__main__': main()
