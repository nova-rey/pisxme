"""Disposable three-pad CM5-ground escape discriminator."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_BRIDGE_3V3_CAP_CHAIN_V2.kicad_pcb'
OUT=R/'PHASE24_CM5_GROUND_THREE_PAD.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('/CORE_CM5/POWER_GND');f=b.FindFootprintByReference('J7')
V=lambda x,y:pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(a,z):
    t=pcbnew.PCB_TRACK(b);t.SetLayer(pcbnew.F_Cu);t.SetNet(n);t.SetWidth(pcbnew.FromMM(.20));t.SetStart(V(*a));t.SetEnd(V(*z));b.Add(t)
for y in (110.7,111.9,113.1): tr((66.96,y),(65.50,y))
tr((65.50,110.7),(65.50,113.1))
q=pcbnew.PCB_VIA(b);q.SetNet(n);q.SetPosition(V(65.50,113.10));q.SetWidth(pcbnew.FromMM(.50));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);b.Add(q)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
