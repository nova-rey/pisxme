"""Audit only the transformed CM5IO USB3 source escapes against native J7."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_USB3_LOCAL_TI_MINIMAL.kicad_pcb'
ORACLE=R/'authority-inventory/cm5io-rev2/CM5IO.kicad_pcb'
OUT=R/'PHASE24_CM5IO_SOURCE_ANCHOR_AUDIT.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.147)
JOBS=(('CM5_USB3_RX_N','128','/CM5_HighSpeed/USB3-0-RX_N'),('CM5_USB3_RX_P','130','/CM5_HighSpeed/USB3-0-RX_P'),('CM5_USB3_TX_N','140','/CM5_HighSpeed/USB3-0-TX_N'),('CM5_USB3_TX_P','142','/CM5_HighSpeed/USB3-0-TX_P'))
def V(p):return pcbnew.VECTOR2I_MM(*p)
def mm(p):return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def xf(p):
 x,y=mm(p);return (230.50-x,203.50-y)
def track(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(a));t.SetEnd(V(z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);b.Add(t)
def via(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(p));v.SetWidth(pcbnew.FromMM(.45));v.SetDrill(pcbnew.FromMM(.20));v.SetLayerPair(F,pcbnew.B_Cu);v.SetNet(n);b.Add(v)
def native_prefix(o,name,padno):
 f=o.FindFootprintByReference('Module1'); start=f.FindPadByNumber(padno).GetPosition(); frontier={(start.x,start.y)};vias=set();items=[]
 for t in o.GetTracks():
  if t.GetNetname()!=name:continue
  if isinstance(t,pcbnew.PCB_VIA):vias.add((t.GetPosition().x,t.GetPosition().y))
  else:items.append((t.GetStart(),t.GetEnd(),t.GetLayer(),t.GetWidth()))
 out=[];used=set()
 while frontier:
  nxt=set()
  for i,(a,z,l,w) in enumerate(items):
   if i in used or ((a.x,a.y) not in frontier and (z.x,z.y) not in frontier):continue
   used.add(i);out.append((a,z,l,w));q=z if (a.x,a.y) in frontier else a
   if (q.x,q.y) in vias:return out,q
   nxt.add((q.x,q.y))
  frontier=nxt
 raise RuntimeError(name)

oracle=pcbnew.LoadBoard(str(ORACLE)); b=pcbnew.LoadBoard(str(BASE)); j=b.FindFootprintByReference('J7')
for t in list(b.GetTracks()):b.Remove(t)
for name,jp,oname in JOBS:
 n=b.FindNet('/CORE_CM5/'+name)
 if n is None:raise RuntimeError(name)
 copied,first=native_prefix(oracle,oname,jp)
 for a,z,l,w in copied:track(b,n,xf(a),xf(z),l)
 via(b,n,xf(first))
 print(name,'native_pad',mm(j.FindPadByNumber(jp).GetPosition()),'first_via',xf(first),'segments',len(copied))
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
