"""V44: regenerate only Path-A selector-side SATA TX corridors from V41."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V41_SATA_TX_PAIR.kicad_pcb'
OUT=H/'PHASE24_STORAGE_CM5_USB4_MONOTONIC_V44_SELECTOR_TX_CORRIDOR.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
def route(n,pts,l):
    for a,z in zip(pts,pts[1:]):
        t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(n,p):
    v=pcbnew.PCB_VIA(b); v.SetPosition(P(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
for name,pts in (
    ('TUSB_SATA_TXP',[(104,116),(106,116),(116,110),(176,110),(184,130.8)]),
    ('TUSB_SATA_TXN',[(104,132),(106,132),(116,140),(176,140),(184,132)])):
    n=b.FindNet('/STORAGE/'+name) or b.FindNet(name); assert n, name
    for t in list(b.GetTracks()):
        if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
    route(n,pts[:2],F)
    via(n,pts[1])
    route(n,pts[1:],B)
    via(n,pts[-1])
    # retain the existing native endpoint dogbones by explicit short F launches
    end=(184,130.8) if name.endswith('TXP') else (184,132)
    dog=(181.5,131.8) if name.endswith('TXP') else (181.5,132.2)
    route(n,[end,dog],F)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
