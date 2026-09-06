"""Disposable CM5IO-style J7 Ethernet source escape template.

Only the source-side escape segments are authored here.  The paths are
derived from native J7 pad centers and preserve a monotonic, pad-field-aware
F.Cu departure before the ESD/connector legs are added.
"""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb'
OUT=R/'PHASE24_SELECTED_MACRO_ETH_SOURCE_ESCAPE_TEMPLATE.kicad_pcb'
V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
routes={
 'CM5_GBE_TD3_P':('3',[(31.2,99.1),(31.2,97.2),(33.91,97.2),(33.91,97.72)]),
 'CM5_GBE_TD3_N':('5',[(30.6,99.5),(30.6,96.8),(34.29,96.8),(34.29,97.88)]),
 'CM5_GBE_TD1_P':('4',[(38.0,99.1),(38.0,96.6),(37.21,96.6),(37.21,97.12)]),
 'CM5_GBE_TD1_N':('6',[(38.6,99.5),(38.6,96.3),(37.59,96.3),(37.59,97.28)]),
 'CM5_GBE_TD2_P':('11',[(29.6,100.7),(29.6,95.8),(35.19,95.8),(35.19,98.28)]),
 'CM5_GBE_TD2_N':('9',[(29.0,100.3),(29.0,95.4),(34.81,95.4),(34.81,98.12)]),
 'CM5_GBE_TD0_P':('12',[(39.2,100.7),(39.2,95.0),(38.59,95.0),(38.59,98.98)]),
 'CM5_GBE_TD0_N':('10',[(39.8,100.3),(39.8,94.6),(38.21,94.6),(38.21,98.82)]),
}
for net_name,(pad_number,tail) in routes.items():
    p=b.FindFootprintByReference('J7').FindPadByNumber(pad_number)
    net=b.FindNet(net_name); points=[(pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y))]+tail
    for a,z in zip(points,points[1:]):
        t=pcbnew.PCB_TRACK(b); t.SetLayer(pcbnew.F_Cu); t.SetNet(net); t.SetWidth(pcbnew.FromMM(.127)); t.SetStart(V(*a)); t.SetEnd(V(*z)); b.Add(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
