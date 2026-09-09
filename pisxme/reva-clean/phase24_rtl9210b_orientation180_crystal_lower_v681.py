"""V681: lower-shelf crystal relocation with a dedicated return corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ORIENTATION180_RSET_LOWER_CHANNEL_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_ORIENTATION180_CRYSTAL_LOWER_V681.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def t(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,a):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*a));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def xy(fp,num):
 p=fp.FindPadByNumber(num).GetPosition();return (pcbnew.ToMM(p.x),pcbnew.ToMM(p.y))
b=pcbnew.LoadBoard(str(BASE))
for ref,pos in [('Y1',(120,86)),('C1',(118,86)),('C2',(122,86))]: b.FindFootprintByReference(ref).SetPosition(P(*pos))
yi=b.FindFootprintByReference('Y1');c1=b.FindFootprintByReference('C1');c2=b.FindFootprintByReference('C2')
ni=b.FindNet('XTAL_IN');no=b.FindNet('XTAL_OUT'); yin=xy(yi,'1');yout=xy(yi,'2');c1p=xy(c1,'1');c2p=xy(c2,'1')
# Escape the adjacent U1 pins on F.Cu, then use B.Cu y=82 as a clear shelf.
t(b,ni,F,(101.95,72.8),(103.0,72.8));t(b,ni,F,(103.0,72.8),(103.0,82.0));v(b,ni,(103.0,82.0));t(b,ni,B,(103.0,82.0),(yin[0],82.0));v(b,ni,(yin[0],82.0));t(b,ni,F,(yin[0],82.0),yin);t(b,ni,F,yin,c1p)
t(b,no,F,(101.95,72.4),(104.0,72.4));t(b,no,F,(104.0,72.4),(104.0,82.0));v(b,no,(104.0,82.0));t(b,no,B,(104.0,82.0),(yout[0],82.0));v(b,no,(yout[0],82.0));t(b,no,F,(yout[0],82.0),yout);t(b,no,F,yout,c2p)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
