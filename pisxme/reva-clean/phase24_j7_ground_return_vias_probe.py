"""Disposable CM5 J7 ground-return via population for native open reduction."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_VCCK_LOCAL_V1.kicad_pcb'; OUT=R/'PHASE24_J7_GROUND_RETURN_VIAS_V1.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu
def V(x,y): return pcbnew.VECTOR2I(int(round(x*1e6)),int(round(y*1e6)))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
b=pcbnew.LoadBoard(str(BASE)); g=b.FindNet('POWER_GND') or b.FindNet('/CORE_CM5/POWER_GND')
if not g: raise RuntimeError('missing POWER_GND')
j=b.FindFootprintByReference('J7'); added=0
for p in j.Pads():
 if 'GND' not in p.GetNetname(): continue
 x,y=xy(p.GetPosition()); off=-1.0 if x<50 else 1.0; q=(x+off,y)
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(x,y));t.SetEnd(V(*q));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(.2));t.SetNet(g);t.SetNetCode(g.GetNetCode());b.Add(t)
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*q));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(g);v.SetNetCode(g.GetNetCode());b.Add(v);added+=1
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.BuildListOfNets();b.Save(str(OUT));print(OUT,'ground_vias',added)
