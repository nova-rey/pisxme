"""Create a storage-only native PCB fixture without mutating SWIG objects."""
from pathlib import Path
import re
R=Path(__file__).resolve().parent
src=(R/'ACREAGE_CLOCK_CANDIDATE5.kicad_pcb').read_text()
keep={'J7','U7','J3','C30','C31','C32','C33','Y1','R23','C42','C43'}
def blocks(text):
 out=[]
 for m in re.finditer(r'(?m)^\t\(',text):
  s=m.start(); depth=0; quote=False; esc=False
  for i in range(s,len(text)):
   c=text[i]
   if quote:
    if esc: esc=False
    elif c=='\\': esc=True
    elif c=='"': quote=False
   elif c=='"': quote=True
   elif c=='(': depth+=1
   elif c==')':
    depth-=1
    if depth==0: out.append((s,i+1)); break
 return out
root=src.index('\n\t(general')
end=src.rfind('\n)')
parts=[]; cursor=root
for s,e in blocks(src):
 if s<root or s>=end or s<cursor: continue
 b=src[s:e]; parts.append(src[cursor:s])
 if not re.match(r'\t\((segment|via|zone)\b',b):
  if not b.startswith('\t(footprint '):
   parts.append(b)
  else:
   ref=re.search(r'\(property "Reference" "([^"]+)"',b)
   if ref and ref.group(1) in keep: parts.append(b)
 cursor=e
parts.append(src[cursor:end])
output_text = src[:root] + ''.join(parts)
output_text += chr(10) + ')' + chr(10)
(R/'.phase19_storage_isolated_base.kicad_pcb').write_text(output_text)
print(R/'.phase19_storage_isolated_base.kicad_pcb')
