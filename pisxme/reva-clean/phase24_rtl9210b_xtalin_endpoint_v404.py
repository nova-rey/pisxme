"""V404: connect the XTAL_IN trunk to the actual C1.1 pad."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_XTALOUT_CLEARANCE_V403.kicad_pcb'; out=H/'PHASE24_RTL9210B_XTALIN_ENDPOINT_V404.kicad_pcb'
b=pcbnew.LoadBoard(str(src)); n=b.FindNet('XTAL_IN')
t=pcbnew.PCB_TRACK(b); t.SetStart(pcbnew.VECTOR2I_MM(120.1,48)); t.SetEnd(pcbnew.VECTOR2I_MM(120.1,49)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
