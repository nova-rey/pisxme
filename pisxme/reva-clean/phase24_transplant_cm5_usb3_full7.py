"""Copy the validated FULL7 CM5 USB3 source geometry into the V3 basis."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_NETLIST_REGENERATED_V3.kicad_pcb'
DONOR=R/'PHASE24_DUAL_MODE_STORAGE_NC39_USB3_FULL7.kicad_pcb'
OUT=R/'PHASE24_STORAGE_USB3_FULL7_SOURCE_REPAIRED_V1.kicad_pcb'
NAMES={'CM5_USB3_RX_N','CM5_USB3_RX_P','CM5_USB3_TX_N','CM5_USB3_TX_P'}
def leaf(n): return n.rsplit('/',1)[-1]
def V(q): return pcbnew.VECTOR2I(q.x,q.y)

b=pcbnew.LoadBoard(str(BASE)); d=pcbnew.LoadBoard(str(DONOR))
target={n:b.FindNet(n) for n in NAMES}
if any(v is None for v in target.values()): raise SystemExit('target USB3 net missing')
for t in list(b.GetTracks()):
    if leaf(t.GetNetname()) in NAMES: b.RemoveNative(t)
for t in list(d.GetTracks()):
    n=leaf(t.GetNetname())
    if n not in NAMES: continue
    q=t.GetStart(); z=t.GetEnd(); net=target[n]
    if isinstance(t,pcbnew.PCB_VIA):
        x=pcbnew.PCB_VIA(b); x.SetPosition(V(q)); x.SetWidth(t.GetWidth(pcbnew.F_Cu)); x.SetDrill(t.GetDrill()); x.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu)
    else:
        x=pcbnew.PCB_TRACK(b); x.SetStart(V(q)); x.SetEnd(V(z)); x.SetLayer(t.GetLayer()); x.SetWidth(t.GetWidth())
    x.SetNet(net); x.SetNetCode(net.GetNetCode()); b.Add(x)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
