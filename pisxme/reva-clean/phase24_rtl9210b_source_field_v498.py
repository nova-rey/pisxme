"""V498: co-allocate U1.52, crystal, and RSET lower-QFN source escapes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;src=H/'PHASE24_RTL9210B_RTL3V3_U139_V496.kicad_pcb';out=H/'PHASE24_RTL9210B_SOURCE_FIELD_V498.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.13208)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(src))
for name in ('XTAL_IN','XTAL_OUT','RSET'):
 for x in list(b.GetTracks()):
  if x.GetNetname()==name:b.RemoveNative(x)
# Remove the obsolete unconnected RTL_3V3 test stub at (102.6,51.0);
# the retained U1.34/U1.20/U1.39/C3 rail does not depend on it.
for x in list(b.GetTracks()):
 if x.GetNetname()=='RTL_3V3':
  pts=[]
  if isinstance(x,pcbnew.PCB_VIA):
   q=x.GetPosition();pts=[(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y))]
  else:
   for q in (x.GetStart(),x.GetEnd()):pts.append((pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)))
  if any(abs(px-102.6)<0.01 and abs(py-51.0)<0.01 for px,py in pts) or any(100<=px<=103 and 50<=py<=52 for px,py in pts):b.RemoveNative(x)
u=b.FindFootprintByReference('U1')
# XTAL_IN: right-hand lower dogbone, left of the XTAL_OUT exit.
n=b.FindNet('XTAL_IN');p=u.FindPadByNumber('53');q=p.GetPosition();a=(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y));s(b,n,F,a,(a[0],66.5));s(b,n,F,(a[0],66.5),(102.5,67.5));v(b,n,(102.5,67.5));s(b,n,B,(102.5,67.5),(102.5,42.0));s(b,n,B,(102.5,42.0),(115.3,42.0));v(b,n,(115.3,42.0));s(b,n,F,(115.3,42.0),(115.3,49.0));s(b,n,F,(115.3,49.0),(115.3,47.5));s(b,n,F,(115.3,47.5),(121.0,47.5));s(b,n,F,(121.0,47.5),(121.0,49.0));s(b,n,F,(121.0,49.0),(120.1,49.0))
# XTAL_OUT: farther-right lower dogbone, with a separate upper B.Cu row.
n=b.FindNet('XTAL_OUT');p=u.FindPadByNumber('54');q=p.GetPosition();a=(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y));s(b,n,F,a,(a[0],66.5));s(b,n,F,(a[0],66.5),(105.0,68.5));v(b,n,(105.0,68.5));s(b,n,B,(105.0,68.5),(105.0,44.0));s(b,n,B,(105.0,44.0),(116.7,44.0));v(b,n,(116.7,44.0));s(b,n,F,(116.7,44.0),(123.0,44.0));s(b,n,F,(123.0,44.0),(123.0,52.0));s(b,n,F,(116.7,49.0),(116.7,52.0));s(b,n,F,(116.7,52.0),(123.0,52.0));s(b,n,F,(123.0,52.0),(120.4,52.0));s(b,n,F,(120.4,52.0),(120.4,53.0))
# RSET: left-side lower dogbone and isolated west return to R1.1.
n=b.FindNet('RSET');p=u.FindPadByNumber('51');q=p.GetPosition();a=(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y));s(b,n,F,a,(a[0],66.5));s(b,n,F,(a[0],66.5),(100.8,66.5));v(b,n,(100.8,66.5));s(b,n,B,(100.8,66.5),(100.8,73.0));v(b,n,(100.8,73.0));s(b,n,F,(100.8,73.0),(101.4,71.0))
# U1.52 joins the existing RTL_3V3 handoff at (100.5,56.5).
n=b.FindNet('RTL_3V3');p=u.FindPadByNumber('52');q=p.GetPosition();a=(pcbnew.ToMM(q.x),pcbnew.ToMM(q.y));s(b,n,F,a,(a[0],66.5));s(b,n,F,(a[0],66.5),(101.5,67.5));v(b,n,(101.5,67.5));s(b,n,B,(101.5,67.5),(101.5,56.5));s(b,n,B,(101.5,56.5),(100.5,56.5))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
