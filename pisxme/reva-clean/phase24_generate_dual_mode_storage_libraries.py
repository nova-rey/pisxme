"""Generate reviewed storage-island footprints from retained package authority."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent; LIB=ROOT/'PiSXMe_RevA_Clean.pretty'
def qfn(name,pins,body,pitch,pad_len,pad_w,ep=None):
    o=[f'(footprint "{name}" (version 20240108) (generator pcbnew)',' (layer "F.Cu")',f' (descr "{name}; manufacturer package drawing")',' (property "Reference" "REF**" (at 0 -5.4 0) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))',' (property "Value" "" (at 0 5.4 0) (layer "F.Fab") hide (effects (font (size 0.8 0.8))))',' (attr smd)',f' (fp_rect (start {-body/2-.25:g} {-body/2-.25:g}) (end {body/2+.25:g} {body/2+.25:g}) (stroke (width 0.05) (type default)) (fill none) (layer "F.CrtYd"))']
    ns=pins//4
    for n in range(1,pins+1):
        side=(n-1)//ns; i=(n-1)%ns; a=(i-(ns-1)/2)*pitch
        if side==0:x,y,r=-body/2,a,0
        elif side==1:x,y,r=-a,body/2,90
        elif side==2:x,y,r=body/2,-a,0
        else:x,y,r=a,-body/2,90
        o.append(f' (pad "{n}" smd roundrect (at {x:g} {y:g} {r}) (size {pad_len:g} {pad_w:g}) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.2))')
    if ep:o.append(f' (pad "{ep}" smd rect (at 0 0) (size 4.46 4.46) (layers "F.Cu" "F.Paste" "F.Mask"))')
    o.append(')'); return '\n'.join(o)+'\n'
def mkey():
    o=['(footprint "TE_1-2199230-4_MKEY" (version 20240108) (generator pcbnew)',' (layer "F.Cu")',' (descr "TE 1-2199230-4 M.2 Socket 3 Key-M; TE 114-115006 Rev C")',' (property "Reference" "REF**" (at 14.25 -6.8 0) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))',' (property "Value" "1-2199230-4" (at 14.25 6.8 0) (layer "F.Fab") hide (effects (font (size 0.8 0.8))))',' (attr smd)',' (fp_rect (start -1 -5.5) (end 30.5 5.5) (stroke (width 0.05) (type default)) (fill none) (layer "F.CrtYd"))']
    for n in list(range(1,59))+list(range(67,76)):
        # TP-053 contact positions are 0.5 mm pitch by contact number, with
        # odd/even contacts on opposing rows.  TE Figure 2 locates pad 1 at
        # -9.25 mm and pad 75 at +9.25 mm (18.5 mm datum span).
        x=-9.25+(n-1)*.25; y=-5.275 if n%2 else 2.275
        o.append(f' (pad "{n}" smd rect (at {x:g} {y:g}) (size .30 1.55) (layers "F.Cu" "F.Paste" "F.Mask") (solder_mask_margin .05))')
    o += [' (pad "M1" thru_hole circle (at -10.35 -1.5) (size 1.65 1.65) (drill 1.25) (layers "*.Cu" "*.Mask"))',
          ' (pad "M2" thru_hole circle (at 10.35 -1.5) (size 1.65 1.65) (drill 1.25) (layers "*.Cu" "*.Mask"))',
          ' (pad "S1" smd rect (at -10.35 -4.5) (size 1.2 2.75) (layers "F.Cu" "F.Paste" "F.Mask"))',
          ' (pad "S2" smd rect (at 10.35 -4.5) (size 1.2 2.75) (layers "F.Cu" "F.Paste" "F.Mask"))']
    o.append(')'); return '\n'.join(o)+'\n'
def main():
    LIB.mkdir(exist_ok=True)
    (LIB/'JMS583_QFN64_8x8.kicad_mod').write_text(qfn('JMS583_QFN64_8x8',64,8,.4,.7,.22))
    (LIB/'TE_1-2199230-4_MKEY.kicad_mod').write_text(mkey())
if __name__=='__main__':main()
