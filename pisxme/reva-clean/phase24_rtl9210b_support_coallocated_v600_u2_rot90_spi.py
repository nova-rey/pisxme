"""V600: rotate/move U2 locally, then trial direct native SPI escapes."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
base=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V595_CLKREQ_LOCAL.kicad_pcb'
out=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V600_U2_ROT90_SPI.kicad_pcb'
F=pcbnew.F_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(a);t.SetEnd(z);t.SetLayer(F);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
b=pcbnew.LoadBoard(str(base));u=b.FindFootprintByReference('U2')
u.SetPosition(P(96.0,62.0));u.SetOrientationDegrees(90.0)
for name,ref1,p1,ref2,p2 in [
 ('SPISI','U1','18','U2','5'),('SPICLK','U1','19','U2','6'),
 ('SPISO3','U1','22','U2','7'),('SPISO','U1','23','U2','2'),('SPICS','U1','24','U2','1')]:
 n=b.FindNet(name); a=b.FindFootprintByReference(ref1).FindPadByNumber(p1).GetPosition(); z=b.FindFootprintByReference(ref2).FindPadByNumber(p2).GetPosition(); seg(b,n,a,z)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
