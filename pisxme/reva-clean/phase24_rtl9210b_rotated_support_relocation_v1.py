"""Disposable rotated-U1 crystal/RSET support relocation with normalized footprints."""
from pathlib import Path
import re,pcbnew
HERE=Path(__file__).resolve().parent;BASE=HERE/'PHASE24_RTL9210B_CHANNELIZED_FULL_SPI_V1.kicad_pcb';OUT=HERE/'PHASE24_RTL9210B_ROTATED_SUPPORT_RELOCATION_V8.kicad_pcb';SCRUB=HERE/'.phase24_rotated_support_relocation_scrubbed_v8.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20);NETS=('XTAL_IN','XTAL_OUT','RSET')
TARGET={'Y1':(105,72.8,70,55),'C1':(105,75,67,55),'C2':(108,75,73,55),'R1':(105,78,70,51)}
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def fpblock(text,ref):
 for m in re.finditer(r'\n\s*\(footprint "[^"]+"',text):
  st=m.start()+1;d=0
  for i in range(st,len(text)):
   if text[i]=='(':d+=1
   elif text[i]==')':
    d-=1
    if d==0:
     q=text[st:i+1]
     if re.search(r'\(property "Reference" "'+ref+r'"',q):return st,i+1,q
     break
 raise RuntimeError(ref)
def main():
 text=BASE.read_text()
 for ref,(nx,ny,ox,oy) in TARGET.items():
  st,en,fb=fpblock(text,ref);first=True
  def cv(m):
   nonlocal first
   x,y=float(m.group(1)),float(m.group(2));tail=m.group(3)
   if first:first=False;return f'(at {nx} {ny}' + (' 180)' if ref=='C1' else ')')
   return '(at %.4f %.4f%s)'%(x-ox,y-oy,tail)
  fb=re.sub(r'\(at\s+([-\d.]+)\s+([-\d.]+)((?:\s+[-\d.]+)?)\)',cv,fb);text=text[:st]+fb+text[en:]
 SCRUB.write_text(text);b=pcbnew.LoadBoard(str(SCRUB))
 for name,net,layer,pts in [
  ('XTAL_IN','XTAL_IN',F,[(101.95,72.8),(104.3,72.8),(105.6,75.0)]),
  ('XTAL_OUT','XTAL_OUT',B,[(103.5,70.5),(103.5,70.0),(104.8,70.0),(105.7,71.8)]),
  ('RSET','RSET',F,[(101.2,73.95),(104.4,78.0)])]:
  n=b.FindNet(net)
  if name=='XTAL_OUT':s(b,n,F,(101.95,72.4),(103.5,72.4));s(b,n,F,(103.5,72.4),(103.5,70.5));v(b,n,(103.5,70.5));v(b,n,(105.7,71.8));s(b,n,F,(105.7,71.8),(105.7,72.8));s(b,n,F,(105.7,72.8),(107.4,75.0))
  for a,z in zip(pts,pts[1:]):s(b,n,layer,a,z)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
