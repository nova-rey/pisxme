"""V1516: use the existing RTL_1V1 via pocket below U1.55."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RSET_WEST_V1508.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_U155_REHOME_V1516.kicad_pcb'; b=pcbnew.LoadBoard(str(BASE)); V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); n=b.FindNet('RTL_1V1'); assert n; F=pcbnew.F_Cu
for q in list(b.GetTracks()):
 if q.GetNetname()=='RTL_1V1' and q.GetLayer()==F:
  a=(q.GetStart()[0]/1e6,q.GetStart()[1]/1e6); z=(q.GetEnd()[0]/1e6,q.GetEnd()[1]/1e6)
  if {a,z} in ({(94.05,68.0),(92.0,68.0)},{(92.0,68.0),(92.0,64.0)}): b.RemoveNative(q)
for a,z in [((94.05,68.0),(92.8,68.0)),((92.8,68.0),(92.8,69.8))]:
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(F); t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
