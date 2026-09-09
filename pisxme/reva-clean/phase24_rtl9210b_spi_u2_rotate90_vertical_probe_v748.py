"""V748: rotate the flash so its SPI pads form a vertical endpoint field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SPI_U1_ROTATE90_PROBE_V730.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_U2_ROTATE90_VERTICAL_PROBE_V748.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE))
u=b.FindFootprintByReference('U2'); anchor=u.FindPadByNumber('4').GetPosition()
u.SetOrientationDegrees(90)
now=u.FindPadByNumber('4').GetPosition()
u.SetPosition(u.GetPosition()+pcbnew.VECTOR2I(anchor.x-now.x,anchor.y-now.y))
# Keep the vertical endpoint field in open acreage, with pad 1 at 105,80.
p1=u.FindPadByNumber('1').GetPosition()
u.SetPosition(u.GetPosition()+pcbnew.VECTOR2I(pcbnew.FromMM(105)-p1.x,pcbnew.FromMM(80)-p1.y))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT))
print(OUT)
for num in ('1','2','5','6','7','4'):
 p=u.FindPadByNumber(num); q=p.GetPosition()
 print('U2.'+num,round(pcbnew.ToMM(q.x),3),round(pcbnew.ToMM(q.y),3),p.GetNetname())
