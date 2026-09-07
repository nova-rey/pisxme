"""Disposable single-net QFN dogbone probe; no Path-A/production CAD edits."""
from pathlib import Path
import re,pcbnew
HERE=Path(__file__).resolve().parent;BASE=HERE/'PHASE24_RTL9210B_ROTATE_U1_V1.kicad_pcb';OUT=HERE/'PHASE24_RTL9210B_U1_QFN_SINGLE_DOGBONE_V1.kicad_pcb';SCRUB=HERE/'.phase24_qfn_single_scrubbed.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
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
     q=text[a:i+1]
     if any(n in q for n in ('SPISI','XTAL_IN','XTAL_OUT','RSET')) and any(88<=float(x)<=110 and 55<=float(y)<=75 for x,y in re.findall(r'\((?:start|end|at)\s+([-\d.]+)\s+([-\d.]+)',q)):sp.append((a,i+1))
     break
 for a,z in reversed(sp):text=text[:a]+text[z:]
 SCRUB.write_text(text);b=pcbnew.LoadBoard(str(SCRUB));n=b.FindNet('SPISI')
 # 45-degree departure through the pad gap, then transition well outside QFN.
 t(b,n,F,(94.05,66.8),(93.45,66.2));t(b,n,F,(93.45,66.2),(92.5,66.2));v(b,n,(92.5,66.2));t(b,n,B,(92.5,66.2),(86.5,66.2))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
