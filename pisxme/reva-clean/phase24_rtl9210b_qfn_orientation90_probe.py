"""Disposable native orientation probe for a fresh RTL9210B source field."""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / 'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_RTL3V3_UPPER_V2.kicad_pcb'
OUT = HERE / 'PHASE24_RTL9210B_QFN_ORIENTATION0_PROBE.kicad_pcb'
LOCAL = {'RTL_5V','RTL_3V3','RTL_1V1','SPISI','SPICLK','SPISO3','SPISO','SPICS',
         'PEDET','CLKREQ_N','PERST_N','XTAL_IN','XTAL_OUT','RSET'}

b = pcbnew.LoadBoard(str(BASE))
for item in list(b.GetTracks()):
    if item.GetNetname() in LOCAL:
        b.RemoveNative(item)
u = b.FindFootprintByReference('U1')
center = u.FindPadByNumber('69').GetPosition()
old = center
u.SetOrientationDegrees(0)
new = u.FindPadByNumber('69').GetPosition()
u.SetPosition(pcbnew.VECTOR2I(u.GetPosition().x + old.x - new.x,
                              u.GetPosition().y + old.y - new.y))
b.BuildListOfNets()
b.Save(str(OUT))
print(OUT)
for num in ('16','17','20','34','36','39','40','50','51','52','53','54','55','60','61','62','63'):
    pad = u.FindPadByNumber(num)
    q = pad.GetPosition()
    print(f'U1.{num} {pcbnew.ToMM(q.x):.3f} {pcbnew.ToMM(q.y):.3f} {pad.GetNetname()}')
