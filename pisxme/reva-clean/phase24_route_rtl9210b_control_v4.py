#!/usr/bin/env python3
"""V4: PEDET on B.Cu; CLKREQ_N on a separated F.Cu upper corridor."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RESET_PERST_V2.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_V4.kicad_pcb'
def main():
 text=BASE.read_text()
 def s(net,a,b,l): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{l}") (net "{net}"))'
 def v(net,p): return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net "{net}"))'
 r=[]
 r += [s('PEDET',(79.6,65.95),(79.6,67.0),'F.Cu'),s('PEDET',(79.6,67.0),(80.5,67.0),'F.Cu'),v('PEDET',(80.5,67.0)),s('PEDET',(80.5,67.0),(80.5,46.0),'B.Cu'),s('PEDET',(80.5,46.0),(140.75,46.0),'B.Cu'),s('PEDET',(140.75,46.0),(140.75,61.5),'B.Cu'),v('PEDET',(140.75,61.5)),s('PEDET',(140.75,61.5),(140.75,62.725),'F.Cu'),v('PEDET',(109.4,46.0)),s('PEDET',(109.4,46.0),(109.4,51.0),'F.Cu')]
 r += [s('CLKREQ_N',(81.6,65.95),(81.6,69.0),'F.Cu'),s('CLKREQ_N',(81.6,69.0),(78.5,69.0),'F.Cu'),v('CLKREQ_N',(78.5,69.0)),s('CLKREQ_N',(78.5,69.0),(78.5,40.5),'B.Cu'),v('CLKREQ_N',(78.5,40.5)),s('CLKREQ_N',(78.5,40.5),(136.5,40.5),'F.Cu'),s('CLKREQ_N',(136.5,40.5),(136.5,70.275),'F.Cu'),s('CLKREQ_N',(112.4,51.0),(112.4,53.0),'F.Cu'),s('CLKREQ_N',(112.4,53.0),(115.0,53.0),'F.Cu'),s('CLKREQ_N',(115.0,53.0),(115.0,40.5),'F.Cu')]
 text=re.sub(r'(?m)^(\s*\(gr_rect\b)','\n'.join(r)+'\n\\1',text,count=1); OUT.write_text(text); print(OUT)
if __name__=='__main__': main()
