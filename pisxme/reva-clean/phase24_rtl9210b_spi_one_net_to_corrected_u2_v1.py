"""Disposable SPISO3 handoff from validated U1 source escape to corrected U2."""
from pathlib import Path
import re,pcbnew
HERE=Path(__file__).resolve().parent;BASE=HERE/'PHASE24_RTL9210B_U1_QFN_FIVE_DOGBONES_V4.kicad_pcb';OUT=HERE/'PHASE24_RTL9210B_SPISO3_CORRECTED_U2_V2.kicad_pcb';SCRUB=HERE/'.phase24_spiso3_u2_scrubbed_v2.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 text=BASE.read_text();m=re.search(r'\n\s*\(footprint "BRINGUP_W25Q128_SPI_FLASH"',text);assert m;st=m.start()+1;d=0
 for i in range(st,len(text)):
  if text[i]=='(':d+=1
  elif text[i]==')':
   d-=1
   if d==0:en=i+1;break
 fb=text[st:en];first=True
 def cv(q):
  nonlocal first
  x,y=float(q.group(1)),float(q.group(2));tail=q.group(3)
  if first:first=False;return '(at 86 76 90)'
  return '(at %.4f %.4f%s)'%(x-95,y-58,tail)
 fb=re.sub(r'\(at\s+([-\d.]+)\s+([-\d.]+)((?:\s+[-\d.]+)?)\)',cv,fb);text=text[:st]+fb+text[en:]
 # Remove only any prior SPISO3 continuation from the U1 probe endpoint.
 spans=[]
 for m in re.finditer(r'\n\s+\((segment|via)\b',text):
  a=m.start()+1;dd=0
  for i in range(a,len(text)):
   if text[i]=='(':dd+=1
   elif text[i]==')':
    dd-=1
    if dd==0:
     q=text[a:i+1]
     if 'SPISO3' in q and any(88<=float(x)<=94 and 65<=float(y)<=72 for x,y in re.findall(r'\((?:start|end|at)\s+([-\d.]+)\s+([-\d.]+)',q)):spans.append((a,i+1))
     break
 for a,z in reversed(spans):text=text[:a]+text[z:]
 SCRUB.write_text(text);b=pcbnew.LoadBoard(str(SCRUB));n=b.FindNet('SPISO3')
 # Recreate the validated source dogbone, then use a north-side F.Cu handoff.
 s(b,n,F,(94.05,68.4),(93.0,68.4));s(b,n,F,(93.0,68.4),(92.2,68.4));v(b,n,(92.2,68.4))
 s(b,n,F,(92.2,68.4),(92.2,64.0));s(b,n,F,(92.2,64.0),(87.4,64.0));s(b,n,F,(87.4,64.0),(87.4,73.0));v(b,n,(87.4,73.0));s(b,n,F,(87.4,73.0),(86.0,73.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
