#!/usr/bin/env python3
"""Lower-perimeter control corridors for the relocated RTL9210B island (V3)."""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
BASE = HERE / 'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL.kicad_pcb'
OUT = HERE / 'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V3.kicad_pcb'

def remove_net_objects(text, net):
    pat = re.compile(r'(?ms)^\s*\((segment|via)\n.*?^\s*\)\n')
    return pat.sub(lambda m: '' if f'(net "{net}")' in m.group(0) else m.group(0), text)

def main():
    text = remove_net_objects(BASE.read_text(), 'RTL_3V3')
    def s(net, a, b, layer):
        return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{layer}") (net "{net}"))'
    def v(net, p):
        return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net "{net}"))'
    r=[]
    for a,b in [((93.2,58),(93.2,42)),((99.2,58),(99.2,42)),((100.4,51),(100.4,42)),
                ((72.2,48),(72.2,42)),((75.2,48),(75.2,42)),((72.2,42),(100.4,42))]:
        r.append(s('RTL_3V3',a,b,'F.Cu'))
    # PEDET stays F.Cu through the local escape, then uses a lower B.Cu
    # perimeter corridor to the right-side M.2 launch.
    r += [s('PEDET',(79.6,65.95),(79.6,68),'F.Cu'),
          s('PEDET',(79.6,68),(71,68),'F.Cu'),
          s('PEDET',(71,68),(71,48),'F.Cu'),
          v('PEDET',(71,68)),
          s('PEDET',(71,68),(71,73),'B.Cu'),
          s('PEDET',(71,73),(142,73),'B.Cu'),
          s('PEDET',(142,73),(142,61.5),'B.Cu'),
          v('PEDET',(142,61.5)),
          s('PEDET',(142,61.5),(140.75,61.5),'F.Cu'),
          s('PEDET',(140.75,61.5),(140.75,62.725),'F.Cu')]
    # CLKREQ uses a separate lower F/B corridor and a staggered right-side
    # launch to contact 52, clear of PERST contact 50.
    r += [s('CLKREQ_N',(81.6,65.95),(82.5,68),'F.Cu'),
          s('CLKREQ_N',(82.5,68),(82.5,76),'F.Cu'),
          v('CLKREQ_N',(82.5,76)),
          s('CLKREQ_N',(82.5,76),(137.5,76),'B.Cu'),
          s('CLKREQ_N',(137.5,76),(137.5,69.5),'B.Cu'),
          v('CLKREQ_N',(137.5,69.5)),
          s('CLKREQ_N',(137.5,69.5),(136.5,69.5),'F.Cu'),
          s('CLKREQ_N',(136.5,69.5),(136.5,70.275),'F.Cu'),
          s('CLKREQ_N',(74,48),(74,47),'F.Cu'),
          v('CLKREQ_N',(74,47)),
          s('CLKREQ_N',(74,47),(82.5,47),'B.Cu'),
          s('CLKREQ_N',(82.5,47),(82.5,68),'B.Cu'),
          v('CLKREQ_N',(82.5,68))]
    text = re.sub(r'(?m)^(\s*\(gr_rect\b)', '\n'.join(r)+'\n\\1', text, count=1)
    OUT.write_text(text)
    print(OUT)
if __name__ == '__main__': main()
