"""Test native POWER_GND access for one JMS583 decoupler pad."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_JMS583_SUPPORT_COHORT_FILLED.kicad_pcb'; OUT=R/'PHASE24_JMS583_C80_GROUND_STITCH_PROBE.kicad_pcb'
P=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('POWER_GND'); f=b.FindFootprintByReference('C80'); p=f.FindPadByNumber('2')
q=p.GetPosition(); qx,qy=pcbnew.ToMM(q.x),pcbnew.ToMM(q.y); v=pcbnew.PCB_VIA(b); v.SetPosition(P(qx+1.0,qy)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
t=pcbnew.PCB_TRACK(b); t.SetStart(P(qx,qy)); t.SetEnd(P(qx+1.0,qy)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
u=b.FindFootprintByReference('U11'); p=u.FindPadByNumber('63'); q=p.GetPosition(); qx,qy=pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
v=pcbnew.PCB_VIA(b); v.SetPosition(P(qx,qy-1.4)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
t=pcbnew.PCB_TRACK(b); t.SetStart(P(qx,qy)); t.SetEnd(P(qx,qy-1.4)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
