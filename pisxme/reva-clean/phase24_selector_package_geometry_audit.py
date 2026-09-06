"""Regression audit for the TI RUA0042A selector land pattern."""
from pathlib import Path
import re

P = Path(__file__).resolve().parent / "PiSXMe_RevA_Clean.pretty"

def pads(path):
    return [(int(n), float(x), float(y)) for n,x,y in re.findall(
        r'\(pad "([0-9]+)"[^\n]*\(at ([^ ]+) ([^ )]+)', path.read_text())
        if int(n) <= 42]

def main():
    failures=[]
    for fn in ("HD3SS6126_RUA0042A.kicad_mod", "HD3SS3412_RUA0042A.kicad_mod"):
        ps=pads(P/fn); nums=[n for n,_,_ in ps]
        if nums != list(range(1,43)): failures.append(f"{fn}: numbering is not 1..42")
        if len({(round(x,4),round(y,4)) for _,x,y in ps}) != 42:
            failures.append(f"{fn}: overlapping pad coordinates")
        if not (len([n for n,_,_ in ps if n<=17])==17 and
                len([n for n,_,_ in ps if 18<=n<=21])==4 and
                len([n for n,_,_ in ps if 22<=n<=38])==17 and
                len([n for n,_,_ in ps if 39<=n<=42])==4):
            failures.append(f"{fn}: RUA0042A 17/4/17/4 perimeter not represented")
    if failures:
        for f in failures: print("FAIL",f)
        raise SystemExit(1)
    print("PASS TI RUA0042A selector geometry: unique 17/4/17/4 pad perimeter")

if __name__ == '__main__': main()
