"""Machine-check the eight Phase 24 component references and pad nets."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BOARD=R/'PHASE24_ALL_AUTHORITATIVE_PARTS.kicad_pcb'
EXPECTED={'Y1':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC','3':'/STORAGE/BRIDGE_XO','4':'/STORAGE/BRIDGE_VSSOSC'},'R23':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_XO'},'C42':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC'},'C43':{'1':'/STORAGE/BRIDGE_XO','2':'/STORAGE/BRIDGE_VSSOSC'},'C44':{'1':'/REGULATORS/BRIDGE_1V1','2':'POWER_GND'},'C45':{'1':'/REGULATORS/BRIDGE_1V1','2':'POWER_GND'},'C46':{'1':'/REGULATORS/BRIDGE_1V1','2':'POWER_GND'},'C47':{'1':'/REGULATORS/BRIDGE_1V1','2':'POWER_GND'}}
b=pcbnew.LoadBoard(str(BOARD))
for ref,m in EXPECTED.items():
 f=b.FindFootprintByReference(ref);assert f is not None,ref
 got={str(p.GetNumber()):p.GetNetname() for p in f.Pads()};assert got==m,(ref,got,m)
print('Phase24 authoritative component audit: PASS; 8 references and pad-net maps exact')
