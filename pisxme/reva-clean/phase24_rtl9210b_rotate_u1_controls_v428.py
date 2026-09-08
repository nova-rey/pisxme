"""V428: disposable 90-degree U1 orientation with regenerated control launches."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_PEDET_NATIVE_ESCAPE_V418.kicad_pcb'; out=H/'PHASE24_RTL9210B_ROTATE_U1_CONTROLS_V428.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*q)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(src)); u=b.FindFootprintByReference('U1'); pos=u.GetPosition(); exp=u.FindPadByNumber('69').GetPosition(); u.SetOrientationDegrees(90); rot=u.FindPadByNumber('69').GetPosition(); u.SetPosition(pcbnew.VECTOR2I(pos.x+exp.x-rot.x,pos.y+exp.y-rot.y))
for x in list(b.GetTracks()):
 if x.GetNetname() in {'PEDET','CLKREQ_N','PERST_N'}: b.RemoveNative(x)
def route(name,source,jack,viaq,trunk):
 n=b.FindNet(name); seg(b,n,F,source,viaq); via(b,n,viaq); seg(b,n,B,viaq,trunk); via(b,n,trunk); seg(b,n,F,trunk,jack)
route('PEDET',(109.95,62.4),(140.75,62.725),(112,62.4),(140,62.4))
route('CLKREQ_N',(109.95,60.4),(136.5,70.275),(112,60.4),(136.5,60.4)); seg(b,b.FindNet('CLKREQ_N'),B,(136.5,60.4),(136.5,70.275))
route('PERST_N',(109.95,60.0),(136.0,70.275),(112,59.8),(134.5,59.8)); seg(b,b.FindNet('PERST_N'),B,(134.5,59.8),(134.5,74.0)); seg(b,b.FindNet('PERST_N'),F,(134.5,74.0),(136.0,70.275))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
