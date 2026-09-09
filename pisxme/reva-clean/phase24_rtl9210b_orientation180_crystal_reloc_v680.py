"""V680: relocate the crystal trio to a clear upper storage-field shelf."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_RSET_LOWER_CHANNEL_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_CRYSTAL_RELOC_V680.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def xy(p): return (pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y))
b=pcbnew.LoadBoard(str(BASE))
for ref,pos in [('Y1',(120,50)),('C1',(118,50)),('C2',(122,50))]: b.FindFootprintByReference(ref).SetPosition(P(*pos))
yi=b.FindFootprintByReference('Y1'); c1=b.FindFootprintByReference('C1'); c2=b.FindFootprintByReference('C2')
ni=b.FindNet('XTAL_IN'); no=b.FindNet('XTAL_OUT')
yin=xy(yi.FindPadByNumber('1')); yout=xy(yi.FindPadByNumber('2')); c1p=xy(c1.FindPadByNumber('1')); c2p=xy(c2.FindPadByNumber('1'))
# Separate upper B.Cu corridors; local cap joins remain on F.Cu.
t(b,ni,F,(101.95,72.8),(103,72.8));t(b,ni,F,(103,72.8),(103,48));v(b,ni,(103,48));t(b,ni,B,(103,48),(yin[0],48));v(b,ni,(yin[0],48));t(b,ni,F,(yin[0],48),yin)
t(b,no,F,(101.95,72.4),(104,72.4));t(b,no,F,(104,72.4),(104,46));v(b,no,(104,46));t(b,no,B,(104,46),(yout[0],46));v(b,no,(yout[0],46));t(b,no,F,(yout[0],46),yout)
t(b,ni,F,yin,c1p);t(b,no,F,yout,c2p)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
