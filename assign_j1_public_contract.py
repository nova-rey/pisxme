from pathlib import Path
import re
p=Path('pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb')
s=p.read_text()
st=s.index('(footprint "PiSXMeRevAClean_SXM2_74221_101LF"')
en=s.find('\n\t(footprint ',st+10)
blk=s[st:en]
power={f'{c}{r}' for r in (22,23,25,26,28,29,31,32,34,35,37,38,40) for c in 'ABCDEFGHJK'}
ground={'J11', 'D15', 'A13', 'C24', 'E27', 'A27', 'F24', 'E10', 'H21', 'H4', 'C30', 'E19', 'F11', 'G24', 'C27', 'E12', 'D36', 'J3', 'E36', 'B18', 'K24', 'F17', 'D39', 'B6', 'F33', 'E16', 'D18', 'K1', 'A33', 'F1', 'K30', 'G7', 'J18', 'K27', 'F36', 'A4', 'H13', 'D7', 'G6', 'K7', 'K4', 'D24', 'C39', 'B24', 'E21', 'A1', 'B19', 'E8', 'F13', 'A19', 'B30', 'E4', 'B33', 'F5', 'F9', 'G36', 'H14', 'G15', 'G30', 'B15', 'F39', 'D21', 'D6', 'E33', 'C14', 'B27', 'K21', 'J21', 'B11', 'A17', 'E14', 'G19', 'G8', 'D8', 'F6', 'J6', 'J27', 'B36', 'J14', 'J33', 'F12', 'E17', 'E39', 'D14', 'E13', 'B21', 'E24', 'E1', 'F30', 'E3', 'D11', 'E9', 'J19', 'C36', 'F3', 'J24', 'K13', 'H30', 'G18', 'C1', 'K36', 'B3', 'F10', 'H39', 'J8', 'H1', 'C17', 'F15', 'J7', 'D3', 'J36', 'E2', 'G27', 'G39', 'F27', 'F16', 'C4', 'H27', 'F14', 'F8', 'H10', 'H33', 'A30', 'D33', 'D19', 'G11', 'E11', 'A14', 'C33', 'F19', 'A24', 'G21', 'H17', 'J15', 'K17', 'E30', 'E6', 'K10', 'E15', 'G3', 'J30', 'A10', 'E5', 'G33', 'B14', 'B7', 'C21', 'H7', 'H24', 'D30', 'A36', 'G14', 'H36', 'A39', 'K39', 'D27', 'A7', 'F21', 'B39', 'F2', 'K33', 'C10', 'A21', 'B8', 'K14', 'C7', 'C19', 'F4', 'J39', 'C13'}
def repl(m):
 n,body=m.group(1),m.group(0)
 if n in power or n in ground:
  if '(net ' not in body:
   net='12V_PROTECTED' if n in power else 'POWER_GND'
   body=body.replace('\n\t\t\t(solder_mask_margin',f'\n\t\t\t(net "{net}")\n\t\t\t(solder_mask_margin',1)
 return body
# bounded pad block through next pad or embedded_fonts
pat=re.compile(r'\(pad "([A-K]\d+)"[\s\S]*?(?=\n\t\t\(pad |\n\t\t\(embedded_fonts)',re.M)
newblk=pat.sub(repl,blk)
if newblk==blk: raise SystemExit('no change')
p.write_text(s[:st]+newblk+s[en:])
print('assigned',len(power),'power and',len(ground),'ground pads; unknowns untouched')
