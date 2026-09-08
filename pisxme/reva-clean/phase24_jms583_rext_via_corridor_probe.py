"""Test a two-via REXT corridor around the corrected JMS583 QFN field."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent; BASE=R/'PHASE24_JMS583_SUPPORT_COHORT_PROBE.kicad_pcb'; OUT=R/'PHASE24_JMS583_SUPPORT_COHORT_REXT_VIA_V1.kicad_pcb'
P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def seg(b,n,a,z,l=pcbnew.F_Cu):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U11'); r=b.FindFootprintByReference('R80'); n=b.FindNet('JMS_REXT')
for x in list(b.GetTracks()):
 if x.GetNetCode()==n.GetNetCode(): b.RemoveNative(x)
s=xy(u.FindPadByNumber('39')); d=xy(r.FindPadByNumber('1')); a=(145,s[1]); z=(130.5,120)
seg(b,n,s,a); via(b,n,a)
seg(b,n,a,(145,120),pcbnew.B_Cu); seg(b,n,(145,120),z,pcbnew.B_Cu); via(b,n,z); seg(b,n,z,d)
b.Save(str(OUT)); print(OUT)
