#!/usr/bin/env python3
"""Lower V3: separate control corridors and early C3/3V3 transition."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOWER_V2.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOWER_V3.kicad_pcb'
NETS={'RESET_N','PERST_N','PEDET','CLKREQ_N','RTL_3V3'}
def main():
    pat=re.compile(r'(?ms)^\s*\((segment|via)\n.*?^\s*\)\n')
    text=pat.sub(lambda m:'' if any(f'(net "{n}")' in m.group(0) for n in NETS) else m.group(0),BASE.read_text())
    def s(n,a,b,l): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{l}") (net "{n}"))'
    def v(n,p): return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net "{n}"))'
    r=[]
    # 3V3: keep U2 drops on F.Cu, transition C3 before the TP4 field, and
    # collect the relocated pull-up pads on B.Cu y=82.
    r += [s('RTL_3V3',(93.2,58),(93.2,82),'F.Cu'),s('RTL_3V3',(99.2,58),(99.2,82),'F.Cu'),
          s('RTL_3V3',(100.4,51),(100.4,53),'F.Cu'),v('RTL_3V3',(100.4,53)),
          s('RTL_3V3',(100.4,53),(100.4,82),'B.Cu'),s('RTL_3V3',(70.2,78),(70.2,82),'F.Cu'),
          s('RTL_3V3',(73.2,78),(73.2,82),'F.Cu')]
    for p in [(93.2,82),(99.2,82),(100.4,82),(70.2,82),(73.2,82)]: r.append(v('RTL_3V3',p))
    r.append(s('RTL_3V3',(70.2,82),(100.4,82),'B.Cu'))
    # PEDET: source to relocated R2 on F.Cu, then a B.Cu y=68 remote run.
    r += [s('PEDET',(79.6,65.95),(79.6,76),'F.Cu'),s('PEDET',(79.6,76),(69,76),'F.Cu'),
          v('PEDET',(69,76)),s('PEDET',(69,76),(69,78),'F.Cu'),s('PEDET',(69,76),(69,68),'B.Cu'),
          s('PEDET',(69,68),(142.5,68),'B.Cu'),s('PEDET',(142.5,68),(142.5,61.5),'B.Cu'),
          v('PEDET',(142.5,61.5)),s('PEDET',(142.5,61.5),(140.75,61.5),'F.Cu'),
          s('PEDET',(140.75,61.5),(140.75,62.725),'F.Cu')]
    # CLKREQ: local R3 branch at y=68.5, remote corridor y=74.
    r += [s('CLKREQ_N',(81.6,65.95),(81.6,69.5),'F.Cu'),v('CLKREQ_N',(81.6,69.5)),
          s('CLKREQ_N',(81.6,69.5),(72,69.5),'B.Cu'),s('CLKREQ_N',(72,69.5),(72,76),'B.Cu'),
          v('CLKREQ_N',(72,76)),s('CLKREQ_N',(72,76),(72,78),'F.Cu'),
          s('CLKREQ_N',(72,76),(72,74),'B.Cu'),s('CLKREQ_N',(72,74),(137.5,74),'B.Cu'),
          s('CLKREQ_N',(137.5,74),(137.5,69.5),'B.Cu'),v('CLKREQ_N',(137.5,69.5)),
          s('CLKREQ_N',(137.5,69.5),(136.5,69.5),'F.Cu'),s('CLKREQ_N',(136.5,69.5),(136.5,70.275),'F.Cu')]
    # PERST corridor y=72.
    r += [s('PERST_N',(82,65.95),(82,68.5),'F.Cu'),s('PERST_N',(82,68.5),(84.5,68.5),'F.Cu'),
          v('PERST_N',(84.5,68.5)),s('PERST_N',(84.5,68.5),(84.5,72),'B.Cu'),
          s('PERST_N',(84.5,72),(135,72),'B.Cu'),s('PERST_N',(135,72),(135,69.5),'B.Cu'),
          v('PERST_N',(135,69.5)),s('PERST_N',(135,69.5),(136,70.275),'F.Cu')]
    # RESET bottom B.Cu path; PEDET is above it at y=68.
    r += [s('RESET_N',(77.6,65.95),(76,69.5),'F.Cu'),v('RESET_N',(76,69.5)),
          s('RESET_N',(76,69.5),(76,80),'B.Cu'),s('RESET_N',(76,80),(108,80),'B.Cu'),
          v('RESET_N',(108,80)),s('RESET_N',(108,80),(108,78),'F.Cu')]
    text=re.sub(r'(?m)^(\s*\(gr_rect\b)','\n'.join(r)+'\n\\1',text,count=1)
    OUT.write_text(text); print(OUT)
if __name__=='__main__': main()
