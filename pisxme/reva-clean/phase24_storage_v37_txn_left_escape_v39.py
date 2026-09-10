"""V39: V38 with a native endpoint return via restored at U12."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V37_FILLED.kicad_pcb'; OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V39_TXN_LEFT_ESCAPE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/CORE_CM5/CM5_USB3_TX_N') or b.FindNet('CM5_USB3_TX_N'); assert n
for t in list(b.GetTracks()):
    if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
j=b.FindFootprintByReference('J7'); u=b.FindFootprintByReference('U12'); assert j and u
def xy(q): return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
s=xy(j.FindPadByNumber('140').GetPosition()); e=xy(u.FindPadByNumber('12').GetPosition())
def seg(a,z,l):
    t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
for a,z in zip([s,(67.0,s[1]),(67.0,92.0),(77.0,92.0)],[(67.0,s[1]),(67.0,92.0),(77.0,92.0),(77.0,92.0)]):
    if a!=z: seg(a,z,F)
v0=pcbnew.PCB_VIA(b); v0.SetPosition(P(77,92)); v0.SetWidth(pcbnew.FromMM(.5)); v0.SetDrill(pcbnew.FromMM(.3)); v0.SetLayerPair(F,B); v0.SetNet(n); v0.SetNetCode(n.GetNetCode()); b.Add(v0)
seg((77,92),(159,136.2),B); seg((159,136.2),(149.8,136.2),B)
v1=pcbnew.PCB_VIA(b); v1.SetPosition(P(149.8,136.2)); v1.SetWidth(pcbnew.FromMM(.5)); v1.SetDrill(pcbnew.FromMM(.3)); v1.SetLayerPair(F,B); v1.SetNet(n); v1.SetNetCode(n.GetNetCode()); b.Add(v1)
seg((149.8,136.2),e,F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
