"""Disposable five-net rotated-U1 QFN dogbone source-field probe."""
from pathlib import Path
import re,pcbnew
HERE=Path(__file__).resolve().parent;BASE=HERE/'PHASE24_RTL9210B_ROTATE_U1_V1.kicad_pcb';OUT=HERE/'PHASE24_RTL9210B_U1_QFN_FIVE_DOGBONES_V4.kicad_pcb';SCRUB=HERE/'.phase24_qfn_five_scrubbed_v4.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20);NETS=('SPISI','SPICLK','SPISO3','SPISO','SPICS','XTAL_IN','XTAL_OUT','RSET')
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
def main():
 text=BASE.read_text();sp=[]
 for m in re.finditer(r'\n\s+\((segment|via)\b',text):
  a=m.start()+1;d=0
  for i in range(a,len(text)):
   if text[i]=='(':d+=1
   elif text[i]==')':
    d-=1
    if d==0:
     q=text[a:i+1];pts=[(float(x),float(y)) for x,y in re.findall(r'\((?:start|end|at)\s+([-\d.]+)\s+([-\d.]+)',q)]
     if any(n in q for n in NETS) and any(88<=x<=110 and 55<=y<=75 for x,y in pts):sp.append((a,i+1))
     break
 for a,z in reversed(sp):text=text[:a]+text[z:]
 SCRUB.write_text(text);b=pcbnew.LoadBoard(str(SCRUB))
 lanes=[('SPISI',(94.05,66.8),(93.0,66.8),(92.2,66.0)),('SPICLK',(94.05,67.2),(93.0,67.2),(91.0,67.8)),('SPISO3',(94.05,68.4),(93.0,68.4),(90.0,68.4)),('SPISO',(94.05,68.8),(92.5,68.8),(91.0,70.0)),('SPICS',(94.05,69.2),(93.0,69.2),(92.2,71.2))]
 for name,src,el,viaq in lanes:
  n=b.FindNet(name);t(b,n,F,src,el);t(b,n,F,el,viaq);v(b,n,viaq);t(b,n,B,viaq,(88.0,viaq[1]))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
