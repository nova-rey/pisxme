"""Disposable south-acreage coherent storage-island placement probe."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_SELECTED_MACRO_SWAP_ETH_STORAGE.kicad_pcb'
OUT=R/'PHASE24_STORAGE_SOUTH_COHERENT.kicad_pcb'
MOVES={
 'U7':(88,155,180),'J3':(145,155,90),
 'C30':(95,147,180),'C31':(95,163,180),'C32':(101,151,180),'C33':(101,159,180),
 'Y1':(80,168,0),'R23':(74,168,0),'C42':(74,164,0),'C43':(74,172,0),
 'C16':(87,143,0),'C17':(93,143,0),'C19':(99,143,0),
}
b=pcbnew.LoadBoard(str(BASE))
for ref,(x,y,r) in MOVES.items():
 f=b.FindFootprintByReference(ref)
 if f is None:raise RuntimeError('missing '+ref)
 f.SetPosition(pcbnew.VECTOR2I_MM(x,y));f.SetOrientationDegrees(r)
for t in list(b.GetTracks()):
 if any(k in t.GetNetname() for k in ('CM5_USB3_','BRIDGE_SATA_','SATA_M2_','BRIDGE_XI','BRIDGE_XO','BRIDGE_VSSOSC')):b.Remove(t)
b.Save(str(OUT));print(OUT)
