"""Materialize all Phase 24 schematic-authoritative missing components.

This is a disposable parity/materialization baseline.  It intentionally does
not claim routed closure; copper is added only by later validated island
authoring paths.
"""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb'
OUT=R/'PHASE24_ALL_AUTHORITATIVE_PARTS.kicad_pcb'
LIBS={'Y1':'Crystal_3225_4Pad','R23':'R_0402_1005Metric','C42':'C_0402_1005Metric','C43':'C_0402_1005Metric','C44':'C_1210_3225Metric','C45':'C_1210_3225Metric','C46':'C_1210_3225Metric','C47':'C_1210_3225Metric'}
MAP={'Y1':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC','3':'/STORAGE/BRIDGE_XO','4':'/STORAGE/BRIDGE_VSSOSC'},'R23':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_XO'},'C42':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC'},'C43':{'1':'/STORAGE/BRIDGE_XO','2':'/STORAGE/BRIDGE_VSSOSC'},'C44':{'1':'/REGULATORS/BRIDGE_1V1','2':'POWER_GND'},'C45':{'1':'/REGULATORS/BRIDGE_1V1','2':'POWER_GND'},'C46':{'1':'/REGULATORS/BRIDGE_1V1','2':'POWER_GND'},'C47':{'1':'/REGULATORS/BRIDGE_1V1','2':'POWER_GND'}}
POS={'Y1':(108,130),'R23':(101,130),'C42':(101,126),'C43':(101,134),'C44':(250,130),'C45':(256,130),'C46':(250,136),'C47':(256,136)}
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def main():
 b=pcbnew.LoadBoard(str(BASE));io=pcbnew.PCB_IO_KICAD_SEXPR()
 nets={}
 for name in sorted({n for m in MAP.values() for n in m.values()}):
  n=b.FindNet(name)
  if n is None:n=pcbnew.NETINFO_ITEM(b,name);n.SetNetCode(b.GetNetCount()+1);b.Add(n)
  nets[name]=n
 for ref in LIBS:
  old=b.FindFootprintByReference(ref)
  if old is not None:b.Remove(old)
  f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),LIBS[ref]);f.SetReference(ref);f.SetPosition(V(*POS[ref]));b.Add(f)
  for p in f.Pads():
   n=nets[MAP[ref][str(p.GetNumber())]];p.SetNet(n);p.SetNetCode(n.GetNetCode())
   ls=pcbnew.LSET();ls.AddLayer(pcbnew.B_Cu if ref in {'Y1','R23','C42','C43'} else pcbnew.F_Cu);p.SetLayerSet(ls)
 b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
