"""V658 disposable: co-author XTAL_IN/XTAL_OUT/RSET support field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_ORIENTATION180_RSET_LOWER_CHANNEL_PROBE.kicad_pcb'; out=H/'PHASE24_RTL9210B_XTAL_RSET_COHERENT_PROBE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,xy):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*xy));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(base))
for name in ('XTAL_IN','XTAL_OUT','RSET'):
 for q in list(b.GetTracks()):
  if q.GetNetname()==name: b.RemoveNative(q)
ci,co,rs=(b.FindNet(x) for x in ('XTAL_IN','XTAL_OUT','RSET'))
# Dedicated source columns, with capacitor/junction landing on F.Cu.
t(b,ci,F,(101.95,72.8),(103.2,72.8));v(b,ci,(103.2,72.8));t(b,ci,B,(103.2,72.8),(103.2,75.8));v(b,ci,(103.2,75.8));t(b,ci,F,(103.2,75.8),(108.3,75.8));t(b,ci,F,(108.3,75.8),(109.6,78.0))
t(b,co,F,(101.95,72.4),(104.6,72.4));v(b,co,(104.6,72.4));t(b,co,B,(104.6,72.4),(104.6,77.0));v(b,co,(104.6,77.0));t(b,co,F,(104.6,77.0),(109.7,75.8));t(b,co,F,(109.7,75.8),(111.4,78.0))
t(b,rs,F,(101.2,73.95),(102.5,76.0));v(b,rs,(102.5,76.0));t(b,rs,B,(102.5,76.0),(112.0,76.0));t(b,rs,B,(112.0,76.0),(112.0,80.0));t(b,rs,B,(112.0,80.0),(108.4,80.0));v(b,rs,(108.4,80.0));t(b,rs,F,(108.4,80.0),(108.4,81.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
