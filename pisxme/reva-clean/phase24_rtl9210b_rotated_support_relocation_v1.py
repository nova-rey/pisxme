"""Disposable rotated-U1 crystal/RSET support relocation with normalized footprints."""
from pathlib import Path
import re,pcbnew
HERE=Path(__file__).resolve().parent;BASE=HERE/'PHASE24_RTL9210B_CHANNELIZED_FULL_SPI_V1.kicad_pcb';OUT=HERE/'PHASE24_RTL9210B_ROTATED_SUPPORT_RELOCATION_V3.kicad_pcb';SCRUB=HERE/'.phase24_rotated_support_relocation_scrubbed_v3.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20);NETS=('XTAL_IN','XTAL_OUT','RSET')
TARGET={'Y1':(107,63,70,55),'C1':(104,63,67,55),'C2':(110,63,73,55),'R1':(107,58,70,51)}
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
  ('XTAL_IN','XTAL_IN',F,[(101.95,72.8),(102.8,72.8),(102.8,62.0),(104.6,62.0),(104.6,63.0),(106.3,63.0)]),
  ('XTAL_OUT','XTAL_OUT',B,[(103.0,75.0),(103.0,61.0),(107.7,61.0),(107.7,62.0)]),
  ('RSET','RSET',B,[(103.5,75.5),(103.5,57.0),(106.4,57.0)])]:
  n=b.FindNet(net)
  if name=='XTAL_OUT':s(b,n,F,(101.95,72.4),(103.0,75.0))
  if name=='RSET':s(b,n,F,(101.2,73.95),(103.5,75.5))
  for a,z in zip(pts,pts[1:]):s(b,n,layer,a,z)
  if name in ('XTAL_OUT','RSET'):
   # Connect the F.Cu source and target pads through ordinary transitions.
   src=(103.0,75.0) if name=='XTAL_OUT' else (103.5,75.5)
   dst=(107.7,62.0) if name=='XTAL_OUT' else (106.4,57.0)
   v(b,n,src);v(b,n,dst);s(b,n,F,dst,(107.7,63.0) if name=='XTAL_OUT' else (106.4,58.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
