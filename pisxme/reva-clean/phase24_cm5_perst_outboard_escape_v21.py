"""V21: disposable low-speed CM5_PERST outboard escape around storage USB."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_USB_TX_PAIR_UPPER_DETOUR_V13.kicad_pcb')); F=pcbnew.F_Cu
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(n,a,z,w=.13208):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(F);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
n=b.FindNet('CM5_PERST')
for t in list(b.GetTracks()):
 if t.GetNetCode()==n.GetNetCode():b.RemoveNative(t)
# Keep the J7 launch, move the vertical trunk to the open outboard side,
# and rejoin the existing upper endpoint dogbone.
tr(n,(66.96,100.3),(64.0,100.3));tr(n,(64.0,100.3),(64.0,150.0));tr(n,(64.0,150.0),(166.0,150.0));tr(n,(166.0,150.0),(166.0,88.73));tr(n,(166.0,88.73),(153.175,89.365))
b.BuildListOfNets();out=R/'PHASE24_CM5_PERST_OUTBOARD_ESCAPE_V21.kicad_pcb';b.Save(str(out));print(out)
