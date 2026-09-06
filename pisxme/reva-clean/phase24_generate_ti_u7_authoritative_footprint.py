#!/usr/bin/env python3
"""Generate the TI PVP0064A land-pattern basis from datasheet Rev-I.

TI package drawing: 0.4 mm pitch, 1.2 mm pad length, 0.2 mm pad width,
8.5 mm land-pattern envelope, and a 3.321--3.581 mm exposed-metal range.
The exposed pad uses a 3.45 mm solder-mask-defined metal opening and a
segmented paste pattern; its net is assigned by the consuming PCB authority.
"""
from pathlib import Path
import uuid

def u(): return str(uuid.uuid4())
def pad(n,x,y,rot='0'):
    return f'''  (pad "{n}" smd roundrect (at {x:.3f} {y:.3f} {rot}) (size 1.200 0.200)
    (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.20))'''

def main():
    out=Path(__file__).resolve().parent/'PiSXMe_RevA_Clean.pretty/TUSB9261IPVP_PVP0064A.kicad_mod'
    lines=['(footprint "TUSB9261IPVP_PVP0064A" (version 20240108) (generator pcbnew)',
      ' (layer "F.Cu")',
      ' (descr "TI TUSB9261IPVP PVP0064A; datasheet Rev-I package/land-pattern basis")',
      ' (property "Reference" "REF**" (at 0 -5.5 0) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))',
      ' (property "Value" "TUSB9261IPVP" (at 0 5.5 0) (layer "F.Fab") (hide yes) (effects (font (size 0.8 0.8) (thickness 0.12))))',
      ' (attr smd)',
      ' (fp_rect (start -4.25 -4.25) (end 4.25 4.25) (stroke (width 0.05) (type default)) (fill none) (layer "F.CrtYd"))',
      ' (fp_rect (start -3.6 -3.6) (end 3.6 3.6) (stroke (width 0.05) (type default)) (fill none) (layer "F.Fab"))']
    n=1
    for y in [ -3.0+i*.4 for i in range(16) ]: lines.append(pad(n,-3.8,y,'90')); n+=1
    for x in [ 3.0-i*.4 for i in range(16) ]: lines.append(pad(n,x,3.8,'0')); n+=1
    for y in [ 3.0-i*.4 for i in range(16) ]: lines.append(pad(n,3.8,y,'90')); n+=1
    for x in [ -3.0+i*.4 for i in range(16) ]: lines.append(pad(n,x,-3.8,'0')); n+=1
    lines += ['  (pad "65" smd rect (at 0 0) (size 3.450 3.450) (layers "F.Cu" "F.Mask"))']
    # Paste is intentionally omitted from pad 65 here.  TI's example calls
    # for a segmented stencil, which must be represented by an explicit
    # fabrication/stencil review rather than a guessed duplicate-pad pattern.
    lines.append(')')
    out.write_text('\n'.join(lines)+'\n')
    print(out)
if __name__=='__main__': main()
