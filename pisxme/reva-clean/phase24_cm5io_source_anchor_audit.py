"""Audit only the transformed CM5IO USB3 source escapes against native J7."""
from pathlib import Path
import os
import pcbnew

R=Path(__file__).resolve().parent
BASE=Path(os.environ.get('P24_ANCHOR_BASE',str(R/'PHASE24_USB3_LOCAL_TI_MINIMAL.kicad_pcb')))
ORACLE=R/'authority-inventory/cm5io-rev2/CM5IO.kicad_pcb'
OUT=Path(os.environ.get('P24_ANCHOR_OUT',str(R/'PHASE24_CM5IO_SOURCE_ANCHOR_AUDIT.kicad_pcb')))
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
def local_escape(name,src,i):
 x=(74.0,76.0,78.0,80.0)[i]; y=(112.0,113.0,114.0,115.0)[i]
 return [src,(x,src[1]),(x,y),(60.0,y)],(60.0,y)
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
if os.environ.get('P24_ANCHOR_FULL')=='1':
 for t in list(b.GetTracks()):
  if any(name in t.GetNetname() for name,_,_ in JOBS):b.Remove(t)
else:
 for t in list(b.GetTracks()):b.Remove(t)
 for f in list(b.GetFootprints()):
  if f.GetReference()!='J7':b.RemoveNative(f)
for i,(name,jp,oname) in enumerate(JOBS):
 n=b.FindNet('/CORE_CM5/'+name)
 if n is None:raise RuntimeError(name)
 copied,first=native_prefix(oracle,oname,jp)
 if os.environ.get('P24_ANCHOR_LOCAL_B')=='1':
  src=mm(j.FindPadByNumber(jp).GetPosition())
  custom,first_local=local_escape(name,src,i)
  for a,z in zip(custom,custom[1:]):track(b,n,a,z,pcbnew.B_Cu)
  via(b,n,first_local)
  print(name,'local_b_first_via',first_local,'segments',len(custom)-1)
  continue
 for a,z,l,w in copied:
  # The reference launch is F.Cu, but PiSXMe J7 USB3 lands are native B.Cu
  # and the existing PCIe breakout occupies the corresponding carrier F.Cu
  # corridor.  This optional in-scope probe preserves shape/ordering while
  # testing a local B.Cu source escape.
  track(b,n,xf(a),xf(z),pcbnew.B_Cu if os.environ.get('P24_ANCHOR_FORCE_B')=='1' else l)
 via(b,n,xf(first))
 print(name,'native_pad',mm(j.FindPadByNumber(jp).GetPosition()),'first_via',xf(first),'segments',len(copied))
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
