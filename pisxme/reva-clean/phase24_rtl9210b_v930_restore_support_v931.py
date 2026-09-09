"""V931: restore prior RTL support copper onto the clean-field 1V1 allocation."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_V927_RTL1V1_CLEANFIELD_V930.kicad_pcb';SRC=H/'PHASE24_RTL9210B_V926_SPISI_REGEN_V927.kicad_pcb';OUT=H/'PHASE24_RTL9210B_V930_RESTORE_SUPPORT_V931.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE));s=pcbnew.LoadBoard(str(SRC));nets={'RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','GND'}
for x in s.GetTracks():
 if x.GetNetname() not in nets: continue
 if type(x).__name__=='PCB_TRACK':
  q=pcbnew.PCB_TRACK(b);q.SetStart(x.GetStart());q.SetEnd(x.GetEnd());q.SetLayer(x.GetLayer());q.SetWidth(x.GetWidth());q.SetNet(b.FindNet(x.GetNetname()));q.SetNetCode(q.GetNet().GetNetCode());b.Add(q)
 else:
  q=pcbnew.PCB_VIA(b);q.SetPosition(x.GetPosition());q.SetWidth(x.GetWidth());q.SetDrill(x.GetDrill());q.SetNet(b.FindNet(x.GetNetname()));q.SetNetCode(q.GetNet().GetNetCode());b.Add(q)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
