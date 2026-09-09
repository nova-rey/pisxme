"""V1053: rotate moved U2 to a horizontal endpoint row about pad 4."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_MOVE_U2_SUPPLY_V1052.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ROTATE_U2_HORIZONTAL_V1053.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U2'); a=u.FindPadByNumber('4').GetPosition(); u.SetOrientationDegrees(0); q=u.FindPadByNumber('4').GetPosition(); u.SetPosition(u.GetPosition()+pcbnew.VECTOR2I(a.x-q.x,a.y-q.y)); b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
