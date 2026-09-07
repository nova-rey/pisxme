#!/usr/bin/env python3
"""Route PEDET, CLKREQ_N, PERST_N, and RESET_N on the isolated fixture."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_5V_1V1_SUPPORT_V6.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_V1.kicad_pcb'
def main():
 text=BASE.read_text()
 def s(net,a,b,l): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{l}") (net "{net}"))'
 def v(net,p): return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net "{net}"))'
 r=[]
 # PEDET: U1 -> R2 -> M-key contact 69, B.Cu y=46.
 r += [s('PEDET',(79.6,65.95),(79.6,67.0),'F.Cu'),s('PEDET',(79.6,67.0),(80.5,67.0),'F.Cu'),v('PEDET',(80.5,67.0)),s('PEDET',(80.5,67.0),(80.5,46.0),'B.Cu'),s('PEDET',(80.5,46.0),(140.75,46.0),'B.Cu'),s('PEDET',(140.75,46.0),(140.75,61.5),'B.Cu'),v('PEDET',(140.75,61.5)),s('PEDET',(140.75,61.5),(140.75,62.725),'F.Cu'),s('PEDET',(109.4,46.0),(109.4,50.0),'B.Cu'),v('PEDET',(109.4,50.0)),s('PEDET',(109.4,50.0),(109.4,51.0),'F.Cu')]
 # CLKREQ_N: stagger left on F.Cu, B.Cu y=47, then R3 and socket.
 r += [s('CLKREQ_N',(81.6,65.95),(81.6,69.0),'F.Cu'),s('CLKREQ_N',(81.6,69.0),(78.5,69.0),'F.Cu'),v('CLKREQ_N',(78.5,69.0)),s('CLKREQ_N',(78.5,69.0),(78.5,47.0),'B.Cu'),s('CLKREQ_N',(78.5,47.0),(136.5,47.0),'B.Cu'),s('CLKREQ_N',(136.5,47.0),(136.5,69.3),'B.Cu'),v('CLKREQ_N',(136.5,69.3)),s('CLKREQ_N',(136.5,69.3),(136.5,70.275),'F.Cu'),s('CLKREQ_N',(112.4,47.0),(112.4,50.0),'B.Cu'),v('CLKREQ_N',(112.4,50.0)),s('CLKREQ_N',(112.4,50.0),(112.4,51.0),'F.Cu')]
 # PERST_N and RESET_N retain the corrected distinct endpoints.
 r += [s('PERST_N',(82.0,65.95),(82.0,72.0),'F.Cu'),s('PERST_N',(82.0,72.0),(136.0,72.0),'F.Cu'),s('PERST_N',(136.0,72.0),(136.0,70.275),'F.Cu'),s('RESET_N',(77.6,65.95),(77.6,76.0),'F.Cu'),s('RESET_N',(77.6,76.0),(108.0,76.0),'F.Cu'),s('RESET_N',(108.0,76.0),(108.0,78.0),'F.Cu')]
 text=re.sub(r'(?m)^(\s*\(gr_rect\b)','\n'.join(r)+'\n\\1',text,count=1); OUT.write_text(text); print(OUT)
if __name__=='__main__': main()
