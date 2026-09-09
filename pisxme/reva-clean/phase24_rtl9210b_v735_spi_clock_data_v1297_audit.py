"""V1297 native SPISI/SPICLK endpoint and source-removal audit."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_V735_SPI_CLOCK_DATA_V1297.kicad_pcb'
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def chk(b,p,a,z): b.BuildConnectivity(); assert p[z] in b.GetConnectivity().GetConnectedItems(p[a])
b=pcbnew.LoadBoard(str(P)); p=pads(b); chk(b,p,('U1','18'),('U2','5')); chk(b,p,('U1','19'),('U2','6'))
t=pcbnew.LoadBoard(str(P)); p=pads(t)
for q in list(t.GetTracks()):
    if q.GetNetname() in ('SPISI','SPICLK'): t.RemoveNative(q)
t.BuildConnectivity(); assert p[('U2','5')] not in t.GetConnectivity().GetConnectedItems(p[('U1','18')]); assert p[('U2','6')] not in t.GetConnectivity().GetConnectedItems(p[('U1','19')])
print('PASS V1297 native rotated SPISI/SPICLK endpoints and saved-board negative controls')
