#!/usr/bin/env python3
"""Relocated R2/R3 control island with regenerated 3V3 and separated controls."""
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V1.kicad_pcb'
def remove_net_objects(text,net):
 pat=re.compile(r'(?ms)^\s*\((segment|via)\n.*?^\s*\)\n')
 return pat.sub(lambda m:'' if f'(net "{net}")' in m.group(0) else m.group(0),text)
def main():
 text=remove_net_objects(BASE.read_text(),'RTL_3V3')
 def s(net,a,b,l): return f'  (segment (start {a[0]:.3f} {a[1]:.3f}) (end {b[0]:.3f} {b[1]:.3f}) (width 0.200) (layer "{l}") (net "{net}"))'
 def v(net,p): return f'  (via (at {p[0]:.3f} {p[1]:.3f}) (size 0.600) (drill 0.300) (layers "F.Cu" "B.Cu") (net "{net}"))'
 r=[]
 # Regenerated 3V3 bus for relocated R2/R3, U2, and C3.
 for a,b in [((93.2,58),(93.2,42)),((99.2,58),(99.2,42)),((100.4,51),(100.4,42)),((72.2,48),(72.2,42)),((75.2,48),(75.2,42)),((72.2,42),(100.4,42))]: r.append(s('RTL_3V3',a,b,'F.Cu'))
 # PEDET: local U1 departure -> R2, then B.Cu to M-key.
 r += [s('PEDET',(79.6,65.95),(79.6,67),'F.Cu'),v('PEDET',(79.6,67)),s('PEDET',(79.6,67),(79.6,47),'B.Cu'),s('PEDET',(79.6,47),(71,47),'B.Cu'),v('PEDET',(71,47)),s('PEDET',(71,47),(71,48),'F.Cu'),s('PEDET',(71,47),(71,46),'B.Cu'),s('PEDET',(71,46),(114,46),'B.Cu'),s('PEDET',(114,46),(114,40.6),'B.Cu'),s('PEDET',(114,40.6),(116,40.6),'B.Cu'),s('PEDET',(116,40.6),(116,46),'B.Cu'),s('PEDET',(116,46),(140.75,46),'B.Cu'),s('PEDET',(140.75,46),(140.75,61.5),'B.Cu'),v('PEDET',(140.75,61.5)),s('PEDET',(140.75,61.5),(140.75,62.725),'F.Cu')]
 # CLKREQ: local source -> R3, then F.Cu upper corridor to M-key.
 r += [s('CLKREQ_N',(81.6,65.95),(81.6,69),'F.Cu'),s('CLKREQ_N',(81.6,69),(78.5,69),'F.Cu'),v('CLKREQ_N',(78.5,69)),s('CLKREQ_N',(78.5,69),(78.5,47),'B.Cu'),s('CLKREQ_N',(78.5,47),(74,47),'B.Cu'),v('CLKREQ_N',(74,47)),s('CLKREQ_N',(74,47),(74,48),'F.Cu'),s('CLKREQ_N',(74,47),(74,40.6),'F.Cu'),s('CLKREQ_N',(74,40.6),(136.5,40.6),'F.Cu'),s('CLKREQ_N',(136.5,40.6),(136.5,70.275),'F.Cu')]
 text=re.sub(r'(?m)^(\s*\(gr_rect\b)','\n'.join(r)+'\n\\1',text,count=1); OUT.write_text(text); print(OUT)
if __name__=='__main__': main()
