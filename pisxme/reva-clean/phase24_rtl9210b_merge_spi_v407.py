"""V407: import native V311 SPI support routes onto V404."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_XTALIN_ENDPOINT_V404.kicad_pcb'; srcp=H/'PHASE24_RTL9210B_CLKREQ_ROUTE_V311.kicad_pcb'; out=H/'PHASE24_RTL9210B_MERGE_SPI_V407.kicad_pcb'
b=pcbnew.LoadBoard(str(base)); s=pcbnew.LoadBoard(str(srcp)); wanted={'SPICS','SPISO','SPISI','SPICLK','SPISO3'}
for x in s.GetTracks():
    if x.GetNetname() in wanted: b.Add(x.Duplicate())
b.BuildListOfNets(); b.Save(str(out)); print(out)
