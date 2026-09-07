#!/usr/bin/env python3
"""V6: bounded B.Cu detours around RTL_5V and RTL_1V1 corridors."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_RESET_PERST_V2.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_V6.kicad_pcb'
def main():
 text=BASE.read_text()
 def s(net,a,b,l): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{l}") (net "{net}"))'
 def v(net,p): return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net "{net}"))'
 r=[]
 # PEDET source is a vertical escape; its B.Cu corridor detours above RTL_5V.
 r += [s('PEDET',(79.6,65.95),(79.6,67.0),'F.Cu'),v('PEDET',(79.6,67.0)),s('PEDET',(79.6,67.0),(79.6,46.0),'B.Cu'),s('PEDET',(79.6,46.0),(114.0,46.0),'B.Cu'),s('PEDET',(114.0,46.0),(114.0,40.6),'B.Cu'),s('PEDET',(114.0,40.6),(116.0,40.6),'B.Cu'),s('PEDET',(116.0,40.6),(116.0,46.0),'B.Cu'),s('PEDET',(116.0,46.0),(140.75,46.0),'B.Cu'),s('PEDET',(140.75,46.0),(140.75,61.5),'B.Cu'),v('PEDET',(140.75,61.5)),s('PEDET',(140.75,61.5),(140.75,62.725),'F.Cu'),v('PEDET',(109.4,46.0)),s('PEDET',(109.4,46.0),(109.4,51.0),'F.Cu')]
 # CLKREQ source is left; its B.Cu corridor detours around RTL_1V1.
 r += [s('CLKREQ_N',(81.6,65.95),(81.6,69.0),'F.Cu'),s('CLKREQ_N',(81.6,69.0),(78.5,69.0),'F.Cu'),v('CLKREQ_N',(78.5,69.0)),s('CLKREQ_N',(78.5,69.0),(78.5,47.0),'B.Cu'),s('CLKREQ_N',(78.5,47.0),(82.5,47.0),'B.Cu'),s('CLKREQ_N',(82.5,47.0),(82.5,42.0),'B.Cu'),s('CLKREQ_N',(82.5,42.0),(104.5,42.0),'B.Cu'),s('CLKREQ_N',(104.5,42.0),(104.5,47.0),'B.Cu'),s('CLKREQ_N',(104.5,47.0),(136.5,47.0),'B.Cu'),s('CLKREQ_N',(136.5,47.0),(136.5,68.5),'B.Cu'),v('CLKREQ_N',(136.5,68.5)),s('CLKREQ_N',(136.5,68.5),(136.5,70.275),'F.Cu'),s('CLKREQ_N',(112.4,47.0),(112.4,49.0),'B.Cu'),v('CLKREQ_N',(112.4,49.0)),s('CLKREQ_N',(112.4,49.0),(112.4,51.0),'F.Cu')]
 text=re.sub(r'(?m)^(\s*\(gr_rect\b)','\n'.join(r)+'\n\\1',text,count=1); OUT.write_text(text); print(OUT)
if __name__=='__main__': main()
