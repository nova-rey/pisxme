"""Generate a schematic-independent acreage floorplan study, without routing."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def rect(x1,y1,x2,y2,label):
    return '(gr_rect (start %g %g) (end %g %g) (stroke (width 0.3) (type default)) (fill none) (layer "Dwgs.User"))\n  (gr_text "%s" (at %g %g) (layer "Dwgs.User") (effects (font (size 1.2 1.2) (thickness 0.2))))'%(x1,y1,x2,y2,label,(x1+x2)/2,(y1+y2)/2)

def main():
    base=(ROOT/'ORIENTATION_BOTTOM.kicad_pcb').read_text()
    base=base.replace('(end 220 140)', '(end 300 180)')
    base=base.replace('(at 45 42 0)', '(at 35 130 0)')
    base=base.replace('(at 170 112 0)', '(at 260 160 0)')
    base=base.replace('(at 110 70 0)', '(at 150 90 0)')
    zones='\n'.join((rect(5,5,32,55,'POWER INPUT'),rect(5,60,32,110,'REGULATORS'),rect(5,115,70,175,'SERVICE / DEBUG'),rect(75,42.5,225,137.5,'V100 COOLER + BACKPLATE KEEPout'),rect(240,20,295,70,'ETHERNET'),rect(235,80,295,125,'STORAGE BRIDGE'),rect(220,145,295,175,'M.2 2280 SERVICE'))) 
    head, tail = base.rsplit('\n)', 1)
    base=head+'\n  (gr_text "PHASE 11 ACREAGE FLOORPLAN — NO ROUTING" (at 150 177) (layer "Dwgs.User") (effects (font (size 1.3 1.3) (thickness 0.2))))\n  '+zones+'\n)'+tail
    (ROOT/'ACREAGE_FLOORPLAN.kicad_pcb').write_text(base)
    print('Phase 11 acreage floorplan generated')
if __name__=='__main__': main()
