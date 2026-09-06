"""Add a parallel, ordinary-via U7 launch to the south-40 clock milestone."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
src=R/'PHASE24_SELECTED_MACRO_STORAGE_V26_CLOCK_V2_SOUTH40.kicad_pcb'
out=R/'PHASE24_SELECTED_MACRO_STORAGE_V26_CLOCK_V2_LAUNCH.kicad_pcb'
b=pcbnew.LoadBoard(str(src)); u=b.FindFootprintByReference('U7')
spec=[('52','/STORAGE/BRIDGE_XI',109.0),('53','/STORAGE/BRIDGE_VSSOSC',108.5),('54','/STORAGE/BRIDGE_XO',108.0)]
for num,name,x in spec:
    p=next(p for p in u.Pads() if p.GetNumber()==num); n=b.FindNet(name)
    start=p.GetPosition(); via_xy=pcbnew.VECTOR2I(pcbnew.FromMM(x), pcbnew.FromMM(121.0))
    v=pcbnew.PCB_VIA(b); v.SetPosition(via_xy); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
    dog=pcbnew.PCB_TRACK(b); dog.SetStart(start); dog.SetEnd(via_xy); dog.SetLayer(pcbnew.F_Cu); dog.SetWidth(pcbnew.FromMM(.15)); dog.SetNet(n); b.Add(dog)
    end=pcbnew.VECTOR2I(pcbnew.FromMM(x),pcbnew.FromMM(159.5))
    leg=pcbnew.PCB_TRACK(b); leg.SetStart(via_xy); leg.SetEnd(end); leg.SetLayer(pcbnew.B_Cu); leg.SetWidth(pcbnew.FromMM(.15)); leg.SetNet(n); b.Add(leg)
b.BuildListOfNets(); b.Save(str(out)); print(out)
