#!/usr/bin/env python3
"""QFN-safe coherent control regeneration for the relocated RTL9210B island."""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
BASE = HERE / 'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL.kicad_pcb'
OUT = HERE / 'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V5.kicad_pcb'
CONTROL_NETS = {'RESET_N', 'PERST_N', 'PEDET', 'CLKREQ_N', 'RTL_3V3'}

def remove_net_objects(text):
    pat = re.compile(r'(?ms)^\s*\((segment|via)\n.*?^\s*\)\n')
    return pat.sub(lambda m: '' if any(f'(net "{n}")' in m.group(0) for n in CONTROL_NETS) else m.group(0), text)

def main():
    text = remove_net_objects(BASE.read_text())
    def s(net, a, b, layer):
        return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{layer}") (net "{net}"))'
    def v(net, p):
        return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net "{net}"))'
    r=[]
    for a,b in [((93.2,58),(93.2,42)),((99.2,58),(99.2,42)),((100.4,51),(100.4,42)),
                ((72.2,48),(72.2,42)),((75.2,48),(75.2,42)),((72.2,42),(100.4,42))]:
        r.append(s('RTL_3V3',a,b,'F.Cu'))

    # QFN-safe local escapes: each source leaves vertically before a via or
    # lateral move; via centers are outside the 0.4-mm pitch pad field.
    r += [s('RESET_N',(77.6,65.95),(77.6,68.5),'F.Cu'), v('RESET_N',(77.6,68.5)),
          s('RESET_N',(77.6,68.5),(77.6,80),'B.Cu'),
          s('RESET_N',(77.6,80),(108,80),'B.Cu'), v('RESET_N',(108,80)),
          s('RESET_N',(108,80),(108,78),'F.Cu')]
    r += [s('PEDET',(79.6,65.95),(79.6,68.5),'F.Cu'), v('PEDET',(79.6,68.5)),
          s('PEDET',(79.6,68.5),(68,68.5),'B.Cu'), s('PEDET',(68,68.5),(68,43),'B.Cu'),
          v('PEDET',(68,43)), s('PEDET',(68,43),(68,40.6),'F.Cu'),
          s('PEDET',(68,40.6),(143,40.6),'F.Cu'), s('PEDET',(143,40.6),(143,61.5),'F.Cu'),
          s('PEDET',(143,61.5),(140.75,61.5),'F.Cu'),
          s('PEDET',(140.75,61.5),(140.75,62.725),'F.Cu')]
    r += [s('CLKREQ_N',(81.6,65.95),(81.6,68.5),'F.Cu'), v('CLKREQ_N',(81.6,68.5)),
          s('CLKREQ_N',(81.6,68.5),(81.6,74),'B.Cu'),
          s('CLKREQ_N',(81.6,74),(137.5,74),'B.Cu'), s('CLKREQ_N',(137.5,74),(137.5,69.5),'B.Cu'),
          v('CLKREQ_N',(137.5,69.5)), s('CLKREQ_N',(137.5,69.5),(136.5,69.5),'F.Cu'),
          s('CLKREQ_N',(136.5,69.5),(136.5,70.275),'F.Cu'),
          s('CLKREQ_N',(81.6,68.5),(81.6,46),'B.Cu'), s('CLKREQ_N',(81.6,46),(74,46),'B.Cu'),
          v('CLKREQ_N',(74,46)), s('CLKREQ_N',(74,46),(74,48),'F.Cu')]
    r += [s('PERST_N',(82,65.95),(82,68.5),'F.Cu'), s('PERST_N',(82,68.5),(83.5,68.5),'F.Cu'),
          v('PERST_N',(83.5,68.5)), s('PERST_N',(83.5,68.5),(83.5,71),'B.Cu'),
          s('PERST_N',(83.5,71),(135,71),'B.Cu'), s('PERST_N',(135,71),(135,69.5),'B.Cu'),
          v('PERST_N',(135,69.5)), s('PERST_N',(135,69.5),(136,70.275),'F.Cu')]
    text = re.sub(r'(?m)^(\s*\(gr_rect\b)', '\n'.join(r)+'\n\\1', text, count=1)
    OUT.write_text(text)
    print(OUT)
if __name__ == '__main__': main()
