"""Generate reviewed storage-island footprints from retained package authority."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent; LIB=ROOT/'PiSXMe_RevA_Clean.pretty'
def qfn(name,pins,body,pitch,pad_len,pad_w,ep=None):
    # TI RUA0042A is a 9.0 x 3.5 mm WQFN: 17 pins on each long side and
    # 4 pins on each short side (17 + 4 + 17 + 4 = 42).  The old generator
    # incorrectly made a square 10-pin-per-side package, overlapping pads.
    o=[f'(footprint "{name}" (version 20240108) (generator pcbnew)',' (layer "F.Cu")',f' (descr "{name}; TI RUA0042A, 9.0 x 3.5 mm WQFN")',' (property "Reference" "REF**" (at 0 -5.4 0) (layer "F.SilkS") (effects (font (size 0.8 0.8) (thickness 0.12))))',' (property "Value" "" (at 0 5.4 0) (layer "F.Fab") hide (effects (font (size 0.8 0.8))))',' (attr smd)',' (fp_rect (start -2.1 -4.6) (end 2.1 4.6) (stroke (width 0.05) (type default)) (fill none) (layer "F.CrtYd"))']
    counts=(17,4,17,4); number=1
    for side,count in enumerate(counts):
        for i in range(count):
            a=(i-(count-1)/2)*pitch
            if side==0: x,y,r=-1.8,a,0
            elif side==1: x,y,r=-a,4.5,90
            elif side==2: x,y,r=1.8,-a,0
            else: x,y,r=a,-4.5,90
            o.append(f' (pad "{number}" smd roundrect (at {x:g} {y:g} {r}) (size {pad_len:g} {pad_w:g}) (layers "F.Cu" "F.Paste" "F.Mask") (roundrect_rratio 0.2))')
            number += 1
    if ep:o.append(f' (pad "{ep}" smd rect (at 0 0) (size 2.05 7.55) (layers "F.Cu" "F.Paste" "F.Mask"))')
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
def symbol(name, ref, pinmap):
    o=[f' (symbol "PiSXMeRevAClean:{name}" (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes)',
       f'  (property "Reference" "{ref}" (at 0 -8 0) (effects (font (size 1 1))))',
       f'  (property "Value" "{name}" (at 0 8 0) (effects (font (size 1 1))))',
       '  (property "Footprint" "" (at 0 0 0) (effects (font (size 1 1)) (hide yes)))',
       f'  (symbol "{name}_1_1" (rectangle (start -15 -6) (end 15 6) (stroke (width 0.254) (type default)) (fill (type background)))']
    for i,(num,nm) in enumerate(pinmap):
        y=(i-(len(pinmap)-1)/2)*1.27
        o.append(f'   (pin passive line (at 20 {y:g} 180) (length 5) (name "{nm}" (effects (font (size 1 1)))) (number "{num}" (effects (font (size 1 1)))))')
    o.append('  ) (embedded_fonts no))'); return '\n'.join(o)
def storage_symbols():
    jms={1:'JMS_VDDREG_5V',2:'JMS_VCCK',3:'JMS_SPI_SO_DNP',4:'JMS_SPI_SCK_DNP',5:'JMS_SPI_SI_DNP',6:'JMS_VCCO',7:'JMS_SPI_CS_N_DNP',8:'JMS_GPIO4_NC',9:'JMS_GPIO5_NC',10:'JMS_VBUS_SENSE',11:'JMS_VCCO',12:'JMS_GPIO7_NC',13:'JMS_GPIO8_NC',14:'JMS_GPIO9_NC',15:'JMS_RESET_N',16:'VBUS',17:'USB_DM',18:'USB_DP',19:'JMS_AVDD33',20:'JMS_AVDDL',21:'U_TXP1',22:'U_TXN1',23:'U_TXN2',24:'U_TXP2',25:'JMS_AVDDL',26:'U_RXP1',27:'U_RXN1',28:'U_RXN2',29:'U_RXP2',30:'JMS_AVDDL',31:'JMS_VCCK',32:'JMS_VCCO',33:'JMS_AVDDL',34:'P_RXN1',35:'P_RXP1',36:'JMS_AVDDL',37:'P_TXN1',38:'P_TXP1',39:'JMS_REXT',40:'JMS_AVDDL',41:'P_RXN0',42:'P_RXP0',43:'JMS_AVDDL',44:'P_TXN0',45:'P_TXP0',46:'JMS_AVDDL',47:'CLKN',48:'CLKP',49:'JMS_AVDDL',50:'XIN',51:'XOUT',52:'JMS_XAVDDH',53:'JMS_VCCK',54:'P_RSTN',55:'P_CLKREQN',56:'JMS_VCCO',57:'JMS_GPIO12_NC',58:'JMS_GPIO11_NC',59:'JMS_GPIO10_NC',60:'TME',61:'JMS_CC2_NC',62:'JMS_CC1_NC',63:'GND',64:'LXO'}
    s6126={6:'HS_OE',9:'SEL',10:'GND',11:'SSA0P',12:'SSA0N',15:'SSA1P',16:'SSA1N',22:'SSC1N',23:'SSC1P',24:'SSC0N',25:'SSC0P',26:'SSB1N',27:'SSB1P',28:'SSB0N',29:'SSB0P',30:'VDD',31:'C1N',32:'C1P',33:'HSC_P',34:'HSC_N'}
    s3412={9:'SEL',5:'VDD',10:'GND',2:'A0P',3:'A0N',6:'A1P',7:'A1N',11:'A2P',12:'A2N',15:'A3P',16:'A3N',38:'B0P',37:'B0N',36:'B1P',35:'B1N',29:'B2P',28:'B2N',27:'B3P',26:'B3N',34:'C0P',33:'C0N',32:'C1P',31:'C1N',25:'C2P',24:'C2N',23:'C3P',22:'C3N'}
    def allpins(d,count): return [(i,d.get(i,'NC_'+str(i))) for i in range(1,count+1)]
    txt='(kicad_symbol_lib (version 20231120) (generator "PiSXMe Rev A Clean")\n'
    txt+=symbol('JMS583_QFN64','U',allpins(jms,64))+'\n'+symbol('HD3SS6126_RUA0042A','U',allpins(s6126,42))+'\n'+symbol('HD3SS3412_RUA0042A','U',allpins(s3412,42))+'\n)\n'
    (ROOT/'Storage_DualMode.kicad_sym').write_text(txt)
def main():
    LIB.mkdir(exist_ok=True)
    (LIB/'JMS583_QFN64_8x8.kicad_mod').write_text(qfn('JMS583_QFN64_8x8',64,8,.4,.7,.22))
    # Both retained TI datasheets point to package drawing RUA0042A. They
    # still receive separate library names because their pin functions differ.
    (LIB/'HD3SS6126_RUA0042A.kicad_mod').write_text(qfn('HD3SS6126_RUA0042A',42,3.6,.4,.6,.25,43))
    (LIB/'HD3SS3412_RUA0042A.kicad_mod').write_text(qfn('HD3SS3412_RUA0042A',42,3.6,.4,.6,.25,43))
    (LIB/'TE_1-2199230-4_MKEY.kicad_mod').write_text(mkey())
    storage_symbols()
if __name__=='__main__':main()
