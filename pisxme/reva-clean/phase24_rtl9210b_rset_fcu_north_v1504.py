"""V1504: remove the obsolete R1 GND collector after plane replacement."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_GND_FIELD_REPLACE_V1502.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RSET_FCU_NORTH_V1504.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); r=b.FindNet('RSET'); g=b.FindNet('GND'); assert r and g
for q in list(b.GetTracks()):
 if q.GetNetname()=='GND' and q.GetLayer()==pcbnew.F_Cu:
  a=(q.GetStart()[0]/1e6,q.GetStart()[1]/1e6); z=(q.GetEnd()[0]/1e6,q.GetEnd()[1]/1e6)
  if {a,z}=={(89.2,65.0),(89.2,67.0)}: b.RemoveNative(q)
for a,z in [((94.8,66.05),(94.8,65.5)),((94.8,65.5),(88.0,65.5)),((88.0,65.5),(88.0,65.0))]:
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(r); t.SetNetCode(r.GetNetCode()); b.Add(t)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
