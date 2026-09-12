from pathlib import Path
import re
p=Path('pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb')
s=p.read_text()
st=s.index('(footprint "PiSXMeRevAClean_SXM2_74221_101LF"')
en=s.find('\n\t(footprint ',st+10)
blk=s[st:en]
power={f'{c}{r}' for r in (22,23,25,26,28,29,31,32,34,35,37,38,40) for c in 'ABCDEFGHJK'}
ground={f'{c}{r}' for r in (21,24,27,30,33,36,39) for c in 'ABCDEFGHJK'}
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
