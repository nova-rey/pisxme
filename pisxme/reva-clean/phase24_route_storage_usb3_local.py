"""Disposable local USB3 bridge-to-JMS routing on the canonical NC39 basis."""
from pathlib import Path
import os
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/os.environ.get('PISXME_STORAGE_USB3_BASE','PHASE24_DUAL_MODE_STORAGE_NC39_CANONICAL_USB3.kicad_pcb')
OUT=R/os.environ.get('PISXME_STORAGE_USB3_OUT','PHASE24_DUAL_MODE_STORAGE_NC39_USB3_LOCAL.kicad_pcb')
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p):return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def pad(b,r,n):return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def seg(b,n,a,z,layer=B,w=.147):
 if a==z:return
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(layer);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def clear(b,name):
 n=b.FindNet(name)
 for i in list(b.GetTracks()):
  if i.GetNetCode()==n.GetNetCode():b.RemoveNative(i)
 return n
b=pcbnew.LoadBoard(str(BASE))
# Co-locate the two TX coupling capacitors with the bridge/QFN boundary.
b.FindFootprintByReference('C86').SetPosition(P(147,145))
b.FindFootprintByReference('C87').SetPosition(P(147,149))
# Each QFN departure is vertical on F.Cu before its ordinary via; the longer
# corridors are on B.Cu over the designated reference plane.
for name,ref,up,ycap,uv,cv,bridge in [
 ('USB_TXP1','C86',21,145,(141.4,144.0),(146.0,144.0),(147.5,145.0)),
 ('USB_TXN1','C87',22,149,(141.0,146.0),(146.0,148.0),(147.5,149.0)),
]:
    n=clear(b,name);s=xy(pad(b,'U11',up));c=xy(pad(b,ref,1));
    # Keep the TX pair on F.Cu through the coupling capacitors.  The source
    # QFN departures are ordered to avoid the RX pair, and the bridge-side
    # launches use separate outboard channels because U12 reverses the pad
    # order.  This is a disposable route experiment; no edges are inferred.
    seg(b,n,s,(s[0],uv[1]),F);seg(b,n,(s[0],uv[1]),(c[0],uv[1]),F);seg(b,n,(c[0],uv[1]),c,F)
    n2=clear(b,'JMS_USB3_TXP' if ref=='C86' else 'JMS_USB3_TXN');c2=xy(pad(b,ref,2));d=xy(pad(b,'U12',25 if ref=='C86' else 24));ev=(159.0,d[1]) if ref=='C86' else (161.0,d[1])
    channel=162.0 if ref=='C86' else 164.0
    seg(b,n2,c2,(channel,c2[1]),F);seg(b,n2,(channel,c2[1]),(channel,d[1]),F);seg(b,n2,(channel,d[1]),d,F)
for name,up,down,v1,v2 in [
 ('USB_RXP1',26,23,(139.4,142.0),(158.5,142.0)),
 ('USB_RXN1',27,22,(139.0,143.0),(160.5,143.0)),
]:
 n=clear(b,name);s=xy(pad(b,'U11',up));d=xy(pad(b,'U12',down));ev=(159.0,d[1]) if name=='USB_RXP1' else (161.0,d[1])
 seg(b,n,s,(s[0],v1[1]),F);via(b,n,v1);seg(b,n,v1,ev,B);via(b,n,ev);seg(b,n,ev,d,F)
b.Save(str(OUT));print(OUT)
