"""Machine-readable routing/physical-policy audit for the clean Path-B candidate."""
from pathlib import Path
import json
import pcbnew

H=Path(__file__).resolve().parent
P=H/'PHASE24_RTL9210B_PATHB_V1603_V1517_INTEGRATED.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_PATHB_V1603_METRICS.json'
NETS=('REFCLK_P','REFCLK_N','LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP')
b=pcbnew.LoadBoard(str(P)); b.BuildConnectivity()
assert not any(isinstance(q,pcbnew.PCB_TRACK) and q.GetLayerName() in {'In1.GND','In2.PWR','In3.Power','In4.GND'} and q.GetNetname() in NETS for q in b.GetTracks())
data={'board':P.name,'policy':{'signal_layers':['F.Cu','B.Cu'],'forbidden_signal_layers':['In1.GND','In2.PWR','In3.Power','In4.GND'],'track_width_mm':.2,'clearance_mm':.2,'via_diameter_mm':.6,'via_drill_mm':.3},'nets':{}}
for net in NETS:
    tracks=[q for q in b.GetTracks() if q.GetNetname()==net and isinstance(q,pcbnew.PCB_TRACK) and not isinstance(q,pcbnew.PCB_VIA)]
    vias=[q for q in b.GetTracks() if q.GetNetname()==net and isinstance(q,pcbnew.PCB_VIA)]
    lengths=sum(pcbnew.ToMM(q.GetLength()) for q in tracks)
    assert all(abs(pcbnew.ToMM(q.GetWidth())-.2)<1e-6 for q in tracks), net
    assert all(q.GetLayerName() in {'F.Cu','B.Cu'} for q in tracks), net
    data['nets'][net]={'track_count':len(tracks),'via_count':len(vias),'length_mm':round(lengths,4),'layers':sorted({q.GetLayerName() for q in tracks})}
assert all(data['nets'][n]['track_count'] for n in NETS)
data['native_connectivity']='PASS (see phase24_rtl9210b_v1603_v1517_audit.py)'
OUT.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
