"""Transplant the native 0-DRC oscillator fixture's RSET route into V5."""
from pathlib import Path
import re
BASE=Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V5_NO_FIXTURE_STUBS.kicad_pcb")
DONOR=Path("PHASE24_RTL9210B_LOCAL_OSCILLATOR_V7.kicad_pcb")
OUT=Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V11_NATIVE_RSET.kicad_pcb")
def blocks(text):
 out=[]; i=0
 while i<len(text):
  if text.startswith("(segment", i) or text.startswith("(via", i) or text.startswith("  (segment", i) or text.startswith("  (via", i):
   d=0; j=i
   while j<len(text):
    if text[j]=='(': d+=1
    elif text[j]==')':
     d-=1
     if d==0:
      z=text[i:j+1]
      if '(net "RSET")' in z or re.search(r'\(net \d+\)',z) and False: out.append((i,j+1,z))
      i=j; break
    j+=1
  i+=1
 return out
def main():
 base=BASE.read_text(); donor=DONOR.read_text()
 # V5 uses named nets; remove only its RSET objects.
 cuts=blocks(base)
 for a,z,_ in reversed(cuts): base=base[:a]+base[z:]
 # The donor is an older numeric-net serialization; select blocks by the
 # donor's RSET net code, resolved from its net table.
 m=re.search(r'\(net (\d+) "RSET"\)',donor)
 if not m: raise SystemExit('donor RSET net missing')
 code=m.group(1); found=[]; i=0
 while i<len(donor):
  if donor.startswith("(segment", i) or donor.startswith("(via", i) or donor.startswith("  (segment", i) or donor.startswith("  (via", i):
   d=0; j=i
   while j<len(donor):
    if donor[j]=='(': d+=1
    elif donor[j]==')':
     d-=1
     if d==0:
      z=donor[i:j+1]
      if f'(net {code})' in z: found.append(z)
      i=j; break
    j+=1
  i+=1
 # Convert donor numeric-net fields to V5's named-net syntax.
 add='\n'.join(z.replace(f'(net {code})','(net "RSET")') for z in found)+'\n'
 base=re.sub(r'(?m)^(\s*\(gr_rect\b)',add+r'\1',base,count=1)
 OUT.write_text(base); print(f'{OUT} ({len(found)} objects)')
if __name__=='__main__': main()
