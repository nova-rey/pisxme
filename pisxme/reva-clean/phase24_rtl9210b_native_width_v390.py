"""V390: apply the board's 0.20 mm minimum to the imported lane tracks."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_LANE0_REALLOCATE_RSET_3V3_XTALOUT_V389.kicad_pcb'
out=H/'PHASE24_RTL9210B_LANE0_NATIVE_WIDTH_V390.kicad_pcb'
b=pcbnew.LoadBoard(str(src)); w=pcbnew.FromMM(.20)
for t in b.GetTracks():
    if t.GetNetname() in ('LANE0_TXP','LANE0_TXN','LANE0_RXP','LANE0_RXN') and type(t).__name__=='PCB_TRACK':
        t.SetWidth(w)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
