"""V92 disposable test: common same-net M.2 power bus, one In2 pickup."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
base=R/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V79_M2_POWER_OWNER.kicad_pcb'
out=R/'PHASE24_STORAGE_M2_POWER_COMMON_BUS_V93.kicad_pcb'
b=pcbnew.LoadBoard(str(base)); net=b.FindNet('STORAGE_3V3'); assert net
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def track(layer,a,z,w=.20):
    t=pcbnew.PCB_TRACK(b); t.SetLayer(layer); t.SetStart(P(*a)); t.SetEnd(P(*z));
    t.SetWidth(pcbnew.FromMM(w)); t.SetNet(net); t.SetNetCode(net.GetNetCode()); b.Add(t)
def via(x,y):
    v=pcbnew.PCB_VIA(b); v.SetPosition(P(x,y)); v.SetNet(net); v.SetNetCode(net.GetNetCode());
    v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); b.Add(v)

# One source pickup, outside U13's pad field, then the designated In2 trunk.
track(pcbnew.F_Cu,(181.5,135.0),(182.5,135.0))
via(182.5,135.0); via(209.0,170.2)
track(pcbnew.In2_Cu,(182.5,135.0),(209.0,170.2),.35)

# Reserve the connector launch channel first. Every contact is the same net;
# adjacent non-power contacts remain physically outside the .20 mm corridor.
xs=(211.0,211.5,213.5,214.0,214.5,215.0,228.0,228.5,229.0)
for x in xs: track(pcbnew.F_Cu,(x,167.275),(x,169.0))
track(pcbnew.F_Cu,(209.0,170.2),(210.5,169.0))
track(pcbnew.F_Cu,(210.5,169.0),(229.0,169.0))
pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(out)); print(out)
