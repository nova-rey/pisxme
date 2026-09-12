#!/usr/bin/env python3
"""Emit a reproducible cluster census from a native KiCad ERC report."""
from collections import Counter, defaultdict
from pathlib import Path
import json, re, sys

def census(path: Path):
    lines=path.read_text(encoding='utf-8').splitlines()
    sheet='/'; typ=None; counts=Counter(); by_sheet=Counter(); xs=defaultdict(Counter); labels=defaultdict(Counter); label_coords=defaultdict(Counter)
    for line in lines:
        if 'Sheet ' in line and line.startswith('*'):
            sheet=line.split('Sheet ',1)[1].strip() or '/'
        if line.startswith('[') and ']:' in line:
            typ=line[1:line.index(']')]; counts[typ]+=1; by_sheet[(sheet,typ)]+=1
        if typ:
            m=re.search(r'@\(([-+0-9.]+) mm,',line)
            if m: xs[typ][m.group(1)]+=1
            m=re.search(r"(?:Global Label|Label) '([^']+)'",line)
            if m:
                labels[typ][m.group(1)]+=1
                xy=re.search(r'@\(([-+0-9.]+) mm,\s*([-+0-9.]+) mm\)',line)
                if xy: label_coords[typ][(m.group(1),xy.group(1),xy.group(2))]+=1
    return {
        'report': str(path), 'counts': dict(counts),
        'by_sheet': {f'{s}|{t}': n for (s,t),n in sorted(by_sheet.items())},
        'coordinate_x_top': {t: xs[t].most_common(20) for t in sorted(xs)},
        'label_top': {t: labels[t].most_common(40) for t in sorted(labels)},
        'duplicate_label_coordinates': {
            t: [[list(k), n] for k,n in label_coords[t].most_common() if n > 1][:80]
            for t in sorted(label_coords)
        },
    }

if __name__ == '__main__':
    src=Path(sys.argv[1]) if len(sys.argv)>1 else Path('PHASE24_CURRENT_LIVE_erc.rpt')
    out=Path(sys.argv[2]) if len(sys.argv)>2 else Path('PHASE24_ERC_CLUSTER_CENSUS_20260911.json')
    out.write_text(json.dumps(census(src), indent=2)+'\n', encoding='utf-8')
    print(out)
