"""Spread-out acreage probe pads; only low-speed nets with PCB authority."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'PHASE21_CONTROLS_REGULATOR_CONTROLS_GATES.kicad_pcb'; OUTPUT=ROOT/'PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb'
POINTS=[
 ('TP1','/POWER_INPUT/12V_IN_A',(21.45,76.45),(26,76.45),(28,76.45)),
 ('TP2','/POWER_INPUT/FUSED_12V_A',(20.45,76.45),(20.45,80),(22.5,80)),
 ('TP3','12V_PROTECTED',(18.55,76.45),(15,76.45),(13,76.45)),
 ('TP4','/CORE_CM5/CM5_5V',(68.5,160),(68.5,157),(66.5,157)),
 ('TP5','/STORAGE/BRIDGE_3V3',(119,144.5),(119,147),(117,147)),
 ('TP6','/REGULATORS/PG_BRIDGE_3V3',(220.5,110),(220.5,110),(218.5,110)),
 ('TP7','/REGULATORS/PG_BRIDGE_1V1',(238.5,103),(238.5,103),(242.5,103)),
 ('TP8','/CORE_CM5/CM5_PERST',(64,125),(64,125),(64,125)),
 ('TP9','POWER_GND',(280,20),(280,20),(282,20)),
 ('TP10','/DEBUG/UART',(280,30),(280,30),(282,30)),
 ('TP11','/DEBUG/RECOVERY',(280,40),(280,40),(282,40)),
 ('TP12','/DEBUG/POWER_PG_FAULT',(280,50),(280,50),(282,50)),
 ('TP13','/DEBUG/DEBUG_GND',(280,60),(280,60),(282,60)),
]
def P(x,y): return pcbnew.VECTOR2I_MM(x,y)
def main():
 b=pcbnew.LoadBoard(str(INPUT)); lib='/app/extensions/Library/Footprints/footprints/TestPoint.pretty'
 for ref,name,src,via_xy,tp_xy in POINTS:
  net=b.FindNet(name)
  if not net:
   net=pcbnew.NETINFO_ITEM(b,name); b.Add(net); net=b.FindNet(name)
  assert net,name
  f=pcbnew.FootprintLoad(lib,'TestPoint_THTPad_D1.0mm_Drill0.5mm'); f.SetReference(ref); f.SetValue('REV_A_PROBE'); f.SetPosition(P(*tp_xy)); f.SetLayer(pcbnew.B_Cu)
  for p in f.Pads():
   p.SetNet(net)
  b.Add(f)
  if src != via_xy:
   t=pcbnew.PCB_TRACK(b);t.SetStart(P(*src));t.SetEnd(P(*via_xy));t.SetLayer(pcbnew.F_Cu);t.SetWidth(pcbnew.FromMM(.25));t.SetNet(net);b.Add(t)
  if src != via_xy:
   v=pcbnew.PCB_VIA(b);v.SetPosition(P(*via_xy));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(net);b.Add(v)
  if via_xy != tp_xy and (not name.startswith('/DEBUG/')) and name != 'POWER_GND':
   t=pcbnew.PCB_TRACK(b);t.SetStart(P(*via_xy));t.SetEnd(P(*tp_xy));t.SetLayer(pcbnew.B_Cu);t.SetWidth(pcbnew.FromMM(.25));t.SetNet(net);b.Add(t)
 b.Save(str(OUTPUT));print(OUTPUT)
if __name__=='__main__':main()
