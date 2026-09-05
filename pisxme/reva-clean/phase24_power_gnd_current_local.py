"""Disposable current-candidate local POWER_GND joins from native pad centers."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb'; OUT=R/'PHASE24_POWER_GND_CURRENT_LOCAL.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('POWER_GND')
V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
def pad(ref,num='2'):
    f=b.FindFootprintByReference(ref)
    return next(p for p in f.Pads() if p.GetNumber()==num)
def join(a,z,layer=pcbnew.F_Cu):
    t=pcbnew.PCB_TRACK(b); t.SetLayer(layer); t.SetNet(n); t.SetWidth(pcbnew.FromMM(.20)); t.SetStart(a); t.SetEnd(z); b.Add(t)
# Only adjacent same-row/same-column pairs; no collector or cross-island trunk.
for a,z in [('C5','C6')]: join(pad(a).GetPosition(),pad(z).GetPosition())
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
