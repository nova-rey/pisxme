"""V712: move the 180-degree flash endpoint north of the clock field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_U117_V702.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_ORIENTATION180_PROBE_V712.kicad_pcb'
LOCAL={'RTL_1V1','RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','PEDET','CLKREQ_N','PERST_N','SPISI','SPICLK','SPISO3','SPISO','SPICS'}
b=pcbnew.LoadBoard(str(BASE))
for item in list(b.GetTracks()):
    if item.GetNetname() in LOCAL:b.RemoveNative(item)
u=b.FindFootprintByReference('U1');a=u.FindPadByNumber('69').GetPosition();u.SetOrientationDegrees(180);q=u.FindPadByNumber('69').GetPosition();u.SetPosition(pcbnew.VECTOR2I(u.GetPosition().x+a.x-q.x,u.GetPosition().y+a.y-q.y))
flash=b.FindFootprintByReference('U2');flash.SetPosition(flash.GetPosition()+pcbnew.VECTOR2I_MM(-42.5,-8.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
