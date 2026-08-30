"""Create native KiCad topside/underside placement-study boards."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parent
def fp(path,x,y,layer='F.Cu'):
    t=path.read_text()
    m=re.search(r'\n(\t|  )\(at [^\n]+\)', t)
    if m:
        t=t[:m.start()]+('\n\t(at %g %g 0)'%(x,y))+t[m.end():]
    else:
        t=t.replace('\n','\n\t(at %g %g 0)\n'%(x,y),1)
    return t.replace('(layer "F.Cu")','(layer "%s")'%(layer),1)
def board(underside=False):
    d=ROOT/'PiSXMe_RevA_Clean.pretty'
    items=[fp(d/'V100_COOLER_BACKPLATE_ENVELOPE.kicad_mod',110,70),fp(d/'PiSXMeRevAClean_SXM2_74221_101LF.kicad_mod',110,70),fp(d/'PiSXMeRevAClean_Raspberry_Pi_5_Compute_Module.kicad_mod',45,42,'B.Cu' if underside else 'F.Cu'),fp(d/'M2_2280_RETENTION_ENVELOPE.kicad_mod',170,112,'B.Cu')]
    return '''(kicad_pcb (version 20240108) (generator pcbnew)
  (general (thickness 1.6))
  (paper "A4")
  (layers (0 "F.Cu" signal) (31 "B.Cu" signal) (36 "B.SilkS" user "b.silkscreen") (37 "F.SilkS" user "f.silkscreen") (44 "Edge.Cuts" user))
  (setup (pad_to_mask_clearance 0))
  (gr_rect (start 0 0) (end 220 140) (stroke (width 0.1) (type default)) (fill none) (layer "Edge.Cuts"))
  (gr_text "PiSXMe Rev A orientation study — NO ROUTING" (at 110 5) (layer "Dwgs.User") (effects (font (size 1.5 1.5) (thickness 0.25))))
%s
)'''%'\n'.join(items)
def main():
    (ROOT/'ORIENTATION_TOP.kicad_pcb').write_text(board())
    (ROOT/'ORIENTATION_BOTTOM.kicad_pcb').write_text(board(True))
    print('Phase 10 orientation boards generated')
if __name__=='__main__': main()
