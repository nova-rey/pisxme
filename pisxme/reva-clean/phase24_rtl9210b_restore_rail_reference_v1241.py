"""V1241: restore V1195 rail/GND copper onto the V1240 REFCLK basis."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_REFCLK_SOURCE_FIELD_CLEAR_V1240.kicad_pcb'
REF=H/'PHASE24_RTL9210B_QFN_XTAL_3V3_COAUTHOR_V1195.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_RAIL_REFERENCE_RESTORE_V1241.kicad_pcb'
NETS={'RTL_1V1','RTL_3V3','GND'}
b=pcbnew.LoadBoard(str(BASE)); r=pcbnew.LoadBoard(str(REF))
for q in list(b.GetTracks()):
    if q.GetNetname() in NETS: b.RemoveNative(q)
for q in r.GetTracks():
    if q.GetNetname() not in NETS: continue
    if type(q).__name__=='PCB_VIA':
        z=pcbnew.PCB_VIA(b); z.SetPosition(q.GetPosition()); z.SetWidth(q.GetWidth()); z.SetDrill(q.GetDrill()); z.SetNet(b.FindNet(q.GetNetname())); z.SetNetCode(z.GetNet().GetNetCode()); b.Add(z)
    else:
        z=pcbnew.PCB_TRACK(b); z.SetStart(q.GetStart()); z.SetEnd(q.GetEnd()); z.SetLayer(q.GetLayer()); z.SetWidth(q.GetWidth()); z.SetNet(b.FindNet(q.GetNetname())); z.SetNetCode(z.GetNet().GetNetCode()); b.Add(z)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
