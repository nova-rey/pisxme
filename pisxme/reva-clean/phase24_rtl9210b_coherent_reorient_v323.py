"""V323: cleared 180-degree U1/support placement probe."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_M2_NORMALIZED_V320.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_COHERENT_REORIENT_V323.kicad_pcb'
LOCAL={'RTL_5V','RTL_3V3','RTL_1V1','SPISI','SPICLK','SPISO3','SPISO','SPICS','PEDET','CLKREQ_N','PERST_N','XTAL_IN','XTAL_OUT','RSET','LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP','REFCLK_P','REFCLK_N'}
def main():
    b=pcbnew.LoadBoard(str(BASE))
    for x in list(b.GetTracks()):
        if x.GetNetname() in LOCAL: b.RemoveNative(x)
    for ref in ['U1','U2','Y1','C1','C2','R1','R2','R3','C3','C4','C5']:
        f=b.FindFootprintByReference(ref)
        if f:
            if ref=='U1': f.SetPosition(pcbnew.VECTOR2I_MM(106,62)); f.SetOrientationDegrees(180)
            else: f.SetPosition(f.GetPosition()+pcbnew.VECTOR2I_MM(8,0))
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
    for ref in ['U1','U2','J1']:
        f=b.FindFootprintByReference(ref); print(ref,round(f.GetPosition().x/1e6,2),round(f.GetPosition().y/1e6,2),f.GetOrientation().AsDegrees())
if __name__=='__main__': main()
