"""V577: edit V576's existing U1.34 handoff without rebuilding other 3V3."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V576_RESTORE_3V3_BRIDGES.kicad_pcb'; out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V577_NATIVE_HANDOFF.kicad_pcb'
def mm(p): return (round(pcbnew.ToMM(p.x),4),round(pcbnew.ToMM(p.y),4))
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(base)); changed=False
for x in list(b.GetTracks()):
 if x.GetNetname()!='RTL_3V3' or x.GetLayer()!=pcbnew.F_Cu: continue
 a,z=mm(x.GetStart()),mm(x.GetEnd())
 if a==(102.05,65.2) and z==(104.4,65.2): b.RemoveNative(x); changed=True
 if a==(104.4,65.2) and z==(104.4,65.95): x.SetStart(P(104.4,65.25)); changed=True
assert changed
n=b.FindNet('RTL_3V3'); t=pcbnew.PCB_TRACK(b); t.SetStart(P(102.05,65.2)); t.SetEnd(P(104.4,65.25)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
