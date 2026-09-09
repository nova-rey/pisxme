"""V709: corrected U2 translation for the 180-degree QFN probe."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_SUPPORT_RELOCATION_5V_U117_V702.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_SPI_ORIENTATION180_PROBE_V709.kicad_pcb'
LOCAL={'RTL_1V1','RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','PEDET','CLKREQ_N','PERST_N','SPISI','SPICLK','SPISO3','SPISO','SPICS'}
b=pcbnew.LoadBoard(str(BASE))
for item in list(b.GetTracks()):
    if item.GetNetname() in LOCAL: b.RemoveNative(item)
u=b.FindFootprintByReference('U1'); anchor=u.FindPadByNumber('69').GetPosition()
u.SetOrientationDegrees(180); now=u.FindPadByNumber('69').GetPosition()
u.SetPosition(pcbnew.VECTOR2I(u.GetPosition().x+anchor.x-now.x,u.GetPosition().y+anchor.y-now.y))
flash=b.FindFootprintByReference('U2'); flash.SetPosition(flash.GetPosition()+pcbnew.VECTOR2I_MM(-42.5,12.0))
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
for num in ('18','19','22','23','24','25','69'):
 p=u.FindPadByNumber(num);q=p.GetPosition();print('U1.'+num,round(pcbnew.ToMM(q.x),3),round(pcbnew.ToMM(q.y),3),p.GetNetname())
for num in ('1','2','5','6','7'):
 p=flash.FindPadByNumber(num);q=p.GetPosition();print('U2.'+num,round(pcbnew.ToMM(q.x),3),round(pcbnew.ToMM(q.y),3),p.GetNetname())
