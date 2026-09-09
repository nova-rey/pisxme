"""V953: disposable U1 orientation probe for the SPI source field."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V942_U120_CLEANFIELD_V944.kicad_pcb'
LOCAL={'RTL_1V1','RTL_3V3','RTL_5V','RSET','XTAL_IN','XTAL_OUT','PEDET','CLKREQ_N','PERST_N','SPISI','SPICLK','SPISO3','SPISO','SPICS'}
for deg in (180,270):
    b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U1')
    anchor=u.FindPadByNumber('69').GetPosition(); u.SetOrientationDegrees(deg)
    now=u.FindPadByNumber('69').GetPosition(); u.SetPosition(u.GetPosition()+anchor-now)
    for item in list(b.GetTracks()):
        if item.GetNetname() in LOCAL: b.RemoveNative(item)
    out=H/f'PHASE24_RTL9210B_U1_ORIENTATION_{deg}_V953.kicad_pcb'; b.BuildListOfNets(); b.Save(str(out)); print(out)
    for num in ('18','19','20','22','23','24','69'):
        p=u.FindPadByNumber(num); q=p.GetPosition(); print(deg,'U1.'+num,round(pcbnew.ToMM(q.x),3),round(pcbnew.ToMM(q.y),3),p.GetNetname())
