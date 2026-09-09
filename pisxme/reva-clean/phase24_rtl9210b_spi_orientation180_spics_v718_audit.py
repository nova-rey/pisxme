"""Native V718 SPICS endpoint audit with a required-trace negative control."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_SPI_ORIENTATION180_SPICS_V718.kicad_pcb'
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b):
 b.BuildConnectivity();p=pads(b);a=p[('U1','24')];c=b.GetConnectivity().GetConnectedItems(a)
 return p[('U2','1')] in c and str(a.GetNetname())=='SPICS' and str(p[('U2','1')].GetNetname())=='SPICS'
b=pcbnew.LoadBoard(str(PCB));assert ok(b),'V718 SPICS endpoint connectivity failed'
t=pcbnew.LoadBoard(str(PCB));victim=next((x for x in t.GetTracks() if x.GetNetname()=='SPICS' and round(pcbnew.ToMM(x.GetStart().x),2)==93.5),None);assert victim is not None,'SPICS trunk missing'
t.RemoveNative(victim);assert not ok(t),'SPICS trunk removal unexpectedly preserved connectivity'
print('PASS V718 native U1.24/U2.1 SPICS connectivity; trunk-removal negative control PASS')
