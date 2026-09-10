"""V1554: inspect a 180-degree RTL9210B QFN source orientation."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; b=pcbnew.LoadBoard(str(H/'PHASE24_RTL9210B_ROTATED_U163_1V1_V1403.kicad_pcb')); out=H/'PHASE24_RTL9210B_ROTATED_180_BLANK_V1554.kicad_pcb'
for o in list(b.GetTracks()): b.RemoveNative(o)
for o in list(b.Zones()): b.RemoveNative(o)
for f in list(b.GetFootprints()):
    if f.GetReference() not in {'U1','Y1','C1','C2','R1'}: b.RemoveNative(f)
u=b.FindFootprintByReference('U1'); u.SetOrientationDegrees(180)
b.BuildListOfNets(); b.Save(str(out)); print(out)
for n in (52,53,54,55,61,62,63,64,65,66,67,68):
    p=next(p for p in u.Pads() if p.GetNumber()==str(n)); print(n, pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y), p.GetNetname())
