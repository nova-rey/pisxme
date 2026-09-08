"""V479: REFCLK_P layer split around XTAL_OUT, REFCLK_N on B.Cu."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_ROTATED_SOURCE_PLANAR_V462.kicad_pcb'; out=H/'PHASE24_RTL9210B_REFCLK_LAYER_SPLIT_V479.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(src));u=b.FindFootprintByReference('U1')
for name in ('REFCLK_P','REFCLK_N'):
 for x in list(b.GetTracks()):
  if x.GetNetname()==name:b.RemoveNative(x)
# REFCLK_N stays on B.Cu below the crystal; REFCLK_P changes to F.Cu before
# crossing the crystal-side boundary.
n=b.FindNet('REFCLK_N');p=u.FindPadByNumber('62');pp=p.GetPosition();a=(pcbnew.ToMM(pp.x),pcbnew.ToMM(pp.y));seg(b,n,F,a,(a[0],70.1));seg(b,n,F,(a[0],70.1),(112,70.1));via(b,n,(112,70.1));seg(b,n,B,(112,70.1),(118,70.1));seg(b,n,B,(118,70.1),(118,56));seg(b,n,B,(118,56),(136,56));seg(b,n,B,(136,56),(136.75,64.5));via(b,n,(136.75,64.5));seg(b,n,F,(136.75,64.5),(136.75,62.725))
n=b.FindNet('REFCLK_P');p=u.FindPadByNumber('61');pp=p.GetPosition();a=(pcbnew.ToMM(pp.x),pcbnew.ToMM(pp.y));seg(b,n,F,a,(a[0],71));seg(b,n,F,(a[0],71),(111,71));via(b,n,(111,71));seg(b,n,B,(111,71),(119,71));via(b,n,(119,71));seg(b,n,F,(119,71),(119,55));seg(b,n,F,(119,55),(137.25,55));seg(b,n,F,(137.25,55),(137.25,60.5));via(b,n,(137.25,60.5));seg(b,n,F,(137.25,60.5),(137.25,62.725))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
