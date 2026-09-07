#!/usr/bin/env python3
"""Route the corrected lower-left R2/R3 control placement from saved pads."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOWER_V2.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOWER_V2_ROUTED.kicad_pcb'
NETS={'RESET_N','PERST_N','PEDET','CLKREQ_N','RTL_3V3'}
def main():
    pat=re.compile(r'(?ms)^\s*\((segment|via)\n.*?^\s*\)\n')
    text=pat.sub(lambda m:'' if any(f'(net "{n}")' in m.group(0) for n in NETS) else m.group(0),BASE.read_text())
    def s(n,a,b,l): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{l}") (net "{n}"))'
    def v(n,p): return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net "{n}"))'
    r=[]
    # Lower B.Cu 3V3 collector with ordinary vias at every saved endpoint.
    for a,b in [((93.2,58),(93.2,82)),((99.2,58),(99.2,82)),((100.4,51),(100.4,82)),
                ((70.2,78),(70.2,82)),((73.2,78),(73.2,82))]:
        r.append(s('RTL_3V3',a,b,'F.Cu'))
    for p in [(93.2,82),(99.2,82),(100.4,82),(70.2,82),(73.2,82)]: r.append(v('RTL_3V3',p))
    r.append(s('RTL_3V3',(70.2,82),(100.4,82),'B.Cu'))
    # PEDET: local source to relocated R2 and separate B.Cu y=70 remote run.
    r += [s('PEDET',(79.6,65.95),(79.6,68.5),'F.Cu'),v('PEDET',(79.6,68.5)),
          s('PEDET',(79.6,68.5),(79.6,76),'B.Cu'),s('PEDET',(79.6,76),(69,76),'B.Cu'),
          v('PEDET',(69,76)),s('PEDET',(69,76),(69,78),'F.Cu'),
          s('PEDET',(69,76),(69,70),'B.Cu'),s('PEDET',(69,70),(142.5,70),'B.Cu'),
          s('PEDET',(142.5,70),(142.5,61.5),'B.Cu'),v('PEDET',(142.5,61.5)),
          s('PEDET',(142.5,61.5),(140.75,61.5),'F.Cu'),s('PEDET',(140.75,61.5),(140.75,62.725),'F.Cu')]
    # CLKREQ: source to R3 via x=72, remote B.Cu y=75.
    r += [s('CLKREQ_N',(81.6,65.95),(81.6,69.5),'F.Cu'),v('CLKREQ_N',(81.6,69.5)),
          s('CLKREQ_N',(81.6,69.5),(72,69.5),'B.Cu'),s('CLKREQ_N',(72,69.5),(72,76),'B.Cu'),
          v('CLKREQ_N',(72,76)),s('CLKREQ_N',(72,76),(72,78),'F.Cu'),
          s('CLKREQ_N',(72,76),(72,75),'B.Cu'),s('CLKREQ_N',(72,75),(137.5,75),'B.Cu'),
          s('CLKREQ_N',(137.5,75),(137.5,69.5),'B.Cu'),v('CLKREQ_N',(137.5,69.5)),
          s('CLKREQ_N',(137.5,69.5),(136.5,69.5),'F.Cu'),s('CLKREQ_N',(136.5,69.5),(136.5,70.275),'F.Cu')]
    # PERST: independent B.Cu y=72 and staggered M.2 launch.
    r += [s('PERST_N',(82,65.95),(82,68.5),'F.Cu'),s('PERST_N',(82,68.5),(84.5,68.5),'F.Cu'),
          v('PERST_N',(84.5,68.5)),s('PERST_N',(84.5,68.5),(84.5,72),'B.Cu'),
          s('PERST_N',(84.5,72),(135,72),'B.Cu'),s('PERST_N',(135,72),(135,69.5),'B.Cu'),
          v('PERST_N',(135,69.5)),s('PERST_N',(135,69.5),(136,70.275),'F.Cu')]
    # RESET is kept on F.Cu lower perimeter so it does not cross the PEDET
    # and CLKREQ B.Cu corridors.
    r += [s('RESET_N',(77.6,65.95),(76,69.5),'F.Cu'),s('RESET_N',(76,69.5),(76,80),'F.Cu'),
          s('RESET_N',(76,80),(108,80),'F.Cu'),s('RESET_N',(108,80),(108,78),'F.Cu')]
    text=re.sub(r'(?m)^(\s*\(gr_rect\b)','\n'.join(r)+'\n\\1',text,count=1)
    OUT.write_text(text); print(OUT)
if __name__=='__main__': main()
