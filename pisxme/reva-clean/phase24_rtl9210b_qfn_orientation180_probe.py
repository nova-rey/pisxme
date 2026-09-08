"""Disposable native 180-degree RTL9210B package-orientation probe.

This is a placement discriminator only. It removes the local support copper
from the upper-V2 source field, preserves the exposed-pad datum, and lets
native KiCad report the transformed pad coordinates before any route is
authored.
"""
from pathlib import Path
import pcbnew

HERE = Path(__file__).resolve().parent
BASE = HERE / 'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_RTL3V3_UPPER_V2.kicad_pcb'
OUT = HERE / 'PHASE24_RTL9210B_QFN_ORIENTATION180_PROBE.kicad_pcb'
LOCAL = {'RTL_5V','RTL_3V3','RTL_1V1','SPISI','SPICLK','SPISO3','SPISO','SPICS',
         'PEDET','CLKREQ_N','PERST_N','XTAL_IN','XTAL_OUT','RSET'}

board = pcbnew.LoadBoard(str(BASE))
for item in list(board.GetTracks()):
    if item.GetNetname() in LOCAL:
        board.RemoveNative(item)
u1 = board.FindFootprintByReference('U1')
datum = u1.FindPadByNumber('69').GetPosition()
u1.SetOrientationDegrees(180)
new_datum = u1.FindPadByNumber('69').GetPosition()
u1.SetPosition(pcbnew.VECTOR2I(u1.GetPosition().x + datum.x - new_datum.x,
                                u1.GetPosition().y + datum.y - new_datum.y))
board.BuildListOfNets()
board.Save(str(OUT))
print(OUT)
for number in ('16','17','20','34','36','39','40','50','51','52','53','54','55','60','61','62','63'):
    pad = u1.FindPadByNumber(number)
    pos = pad.GetPosition()
    print(f'U1.{number} {pcbnew.ToMM(pos.x):.3f} {pcbnew.ToMM(pos.y):.3f} {pad.GetNetname()}')
