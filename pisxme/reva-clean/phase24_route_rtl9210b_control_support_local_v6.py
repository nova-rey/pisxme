#!/usr/bin/env python3
"""V6: localized fixes to the QFN-safe four-control regeneration."""
from pathlib import Path
import re

HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V6.kicad_pcb'
NETS={'RESET_N','PERST_N','PEDET','CLKREQ_N','RTL_3V3'}

def main():
    pat=re.compile(r'(?ms)^\s*\((segment|via)\n.*?^\s*\)\n')
    text=pat.sub(lambda m:'' if any(f'(net "{n}")' in m.group(0) for n in NETS) else m.group(0),BASE.read_text())
    def s(n,a,b,l): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{l}") (net "{n}"))'
    def v(n,p): return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net "{n}"))'
    r=[]
    # 3V3 crosses the inherited RTL_5V vertical on B.Cu around the bridge;
    # use a short F.Cu departure and a named-net B.Cu bus around it.
    r += [s('RTL_3V3',(93.2,58),(93.2,42),'F.Cu'),s('RTL_3V3',(99.2,58),(99.2,42),'F.Cu'),
          s('RTL_3V3',(100.4,51),(100.4,42),'F.Cu'),s('RTL_3V3',(72.2,48),(72.2,42),'F.Cu'),
          s('RTL_3V3',(75.2,48),(75.2,42),'F.Cu'),s('RTL_3V3',(72.2,42),(82,42),'F.Cu'),
          v('RTL_3V3',(82,42)),s('RTL_3V3',(82,42),(100.4,42),'B.Cu'),v('RTL_3V3',(100.4,42))]
    # RESET bottom perimeter; delay its B.Cu entry so PEDET's local B.Cu
    # departure at y=68.5 is not crossed.
    r += [s('RESET_N',(77.6,65.95),(77.6,69.5),'F.Cu'),v('RESET_N',(77.6,69.5)),
          s('RESET_N',(77.6,69.5),(77.6,80),'B.Cu'),s('RESET_N',(77.6,80),(108,80),'B.Cu'),
          v('RESET_N',(108,80)),s('RESET_N',(108,80),(108,78),'F.Cu')]
    # PEDET left-side return and F.Cu upper run; the M.2 launch moves one mm
    # farther outboard to avoid the inherited GND via at x=143.
    r += [s('PEDET',(79.6,65.95),(79.6,68.5),'F.Cu'),v('PEDET',(79.6,68.5)),
          s('PEDET',(79.6,68.5),(68,68.5),'B.Cu'),s('PEDET',(68,68.5),(68,48),'B.Cu'),
          v('PEDET',(68,48)),s('PEDET',(68,48),(71,48),'F.Cu'),s('PEDET',(68,48),(68,43),'B.Cu'),
          v('PEDET',(68,43)),s('PEDET',(68,43),(68,40.6),'F.Cu'),s('PEDET',(68,40.6),(144,40.6),'F.Cu'),
          s('PEDET',(144,40.6),(144,61.5),'F.Cu'),s('PEDET',(144,61.5),(140.75,61.5),'F.Cu'),
          s('PEDET',(140.75,61.5),(140.75,62.725),'F.Cu')]
    # CLKREQ source via is staggered below the QFN edge; the R3 pull-up joins
    # the same B.Cu spine from a separate upper branch.
    r += [s('CLKREQ_N',(81.6,65.95),(81.6,69.5),'F.Cu'),v('CLKREQ_N',(81.6,69.5)),
          s('CLKREQ_N',(81.6,69.5),(81.6,74),'B.Cu'),s('CLKREQ_N',(81.6,74),(137.5,74),'B.Cu'),
          s('CLKREQ_N',(137.5,74),(137.5,69.5),'B.Cu'),v('CLKREQ_N',(137.5,69.5)),
          s('CLKREQ_N',(137.5,69.5),(136.5,69.5),'F.Cu'),s('CLKREQ_N',(136.5,69.5),(136.5,70.275),'F.Cu'),
          s('CLKREQ_N',(81.6,69.5),(81.6,46),'B.Cu'),s('CLKREQ_N',(81.6,46),(74,46),'B.Cu'),
          v('CLKREQ_N',(74,46)),s('CLKREQ_N',(74,46),(74,48),'F.Cu')]
    # PERST route remains on its own B.Cu corridor, between CLKREQ and RESET.
    r += [s('PERST_N',(82,65.95),(82,68.5),'F.Cu'),s('PERST_N',(82,68.5),(83.5,68.5),'F.Cu'),
          v('PERST_N',(83.5,68.5)),s('PERST_N',(83.5,68.5),(83.5,71),'B.Cu'),
          s('PERST_N',(83.5,71),(135,71),'B.Cu'),s('PERST_N',(135,71),(135,69.5),'B.Cu'),
          v('PERST_N',(135,69.5)),s('PERST_N',(135,69.5),(136,70.275),'F.Cu')]
    text=re.sub(r'(?m)^(\s*\(gr_rect\b)','\n'.join(r)+'\n\\1',text,count=1)
    OUT.write_text(text); print(OUT)
if __name__=='__main__': main()
