"""V393: use ordinary 0.40/0.20 mm through-vias for oscillator transitions."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_XTALIN_ESCAPE_V392.kicad_pcb'; out=H/'PHASE24_RTL9210B_SIGNAL_VIA_GEOMETRY_V393.kicad_pcb'
b=pcbnew.LoadBoard(str(src))
for v in b.GetTracks():
    if type(v).__name__=='PCB_VIA' and v.GetNetname() in ('XTAL_IN','XTAL_OUT'):
        v.SetWidth(pcbnew.FromMM(.40)); v.SetDrill(pcbnew.FromMM(.20))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
