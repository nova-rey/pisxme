"""V488: regenerate RTL9210B crystal/load routing from rotated U1 pads."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_FULL_SIX_NET_COALLOCATE_V487.kicad_pcb';out=H/'PHASE24_RTL9210B_CRYSTAL_SUPPORT_V488.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.13208)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(src));u=b.FindFootprintByReference('U1')
c1=b.FindFootprintByReference('C1')
c1.FindPadByNumber('2').SetLocalZoneConnection(pcbnew.ZONE_CONNECTION_NONE)
c2=b.FindFootprintByReference('C2')
c2.FindPadByNumber('2').SetLocalZoneConnection(pcbnew.ZONE_CONNECTION_NONE)
for name in ('XTAL_IN','XTAL_OUT'):
 for x in list(b.GetTracks()):
  if x.GetNetname()==name:b.RemoveNative(x)
n=b.FindNet('XTAL_IN');p=u.FindPadByNumber('53');pp=p.GetPosition();a=(pcbnew.ToMM(pp.x),pcbnew.ToMM(pp.y));s(b,n,F,a,(a[0],66.8));s(b,n,F,(a[0],66.8),(102.0,67.5));v(b,n,(102.0,67.5));s(b,n,B,(102.0,67.5),(102.0,42.0));s(b,n,B,(102.0,42.0),(115.3,42.0));v(b,n,(115.3,42.0));s(b,n,F,(115.3,42.0),(115.3,49.0));s(b,n,F,(115.3,49.0),(115.3,47.5));s(b,n,F,(115.3,47.5),(121.0,47.5));s(b,n,F,(121.0,47.5),(121.0,49.0));s(b,n,F,(121.0,49.0),(120.1,49.0))
n=b.FindNet('XTAL_OUT');p=u.FindPadByNumber('54');pp=p.GetPosition();a=(pcbnew.ToMM(pp.x),pcbnew.ToMM(pp.y));s(b,n,F,a,(a[0],66.8));s(b,n,F,(a[0],66.8),(105.0,67.5));v(b,n,(105.0,67.5));s(b,n,B,(105.0,67.5),(105.0,44.0));s(b,n,B,(105.0,44.0),(116.7,44.0));v(b,n,(116.7,44.0));s(b,n,F,(116.7,44.0),(123.0,44.0));s(b,n,F,(123.0,44.0),(123.0,52.0));s(b,n,F,(116.7,49.0),(116.7,52.0));s(b,n,F,(116.7,52.0),(123.0,52.0));s(b,n,F,(123.0,52.0),(120.4,52.0));s(b,n,F,(120.4,52.0),(120.4,53.0))
g=b.FindNet('GND');s(b,g,F,(118.9,49.0),(118.9,50.5));v(b,g,(118.9,50.5));s(b,g,F,(121.6,53.0),(140.0,53.0));s(b,g,F,(140.0,53.0),(140.0,56.0));v(b,g,(140.0,56.0))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
