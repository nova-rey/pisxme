#!/usr/bin/env python3
"""Remove the unsourced TP5 probe and only its explicit board-only launch."""
import argparse
import pcbnew

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pcb'); ap.add_argument('output')
    a = ap.parse_args(); b = pcbnew.LoadBoard(a.pcb)
    fp = next((x for x in b.GetFootprints() if x.GetReference() == 'TP5'), None)
    if fp is None: raise SystemExit('TP5 not found')
    p = next(iter(fp.Pads())).GetPosition()
    # The saved candidate has a board-only branch ending at TP5 (117,147),
    # plus a zero-length serialization artifact. Remove only those segments;
    # retain the adjacent BRIDGE_3V3 rail grid ending at (119,146.5).
    removed = 0
    for t in list(b.GetTracks()):
        s, e = t.GetStart(), t.GetEnd()
        touches_probe = (s.x == p.x and s.y == p.y) or (e.x == p.x and e.y == p.y)
        if touches_probe or (s.x == e.x == 119000000 and s.y == e.y == 147000000):
            b.Remove(t); removed += 1
    b.Remove(fp)
    b.Save(a.output)
    print(f'removed TP5 and {removed} unsourced launch segments; saved {a.output}')

if __name__ == '__main__': main()
