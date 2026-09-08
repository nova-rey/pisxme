"""V485: move only REFCLK_N's upper F.Cu corridor inward."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_FULL_SIX_NET_COALLOCATE_V484.kicad_pcb';out=H/'PHASE24_RTL9210B_FULL_SIX_NET_COALLOCATE_V485.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.13208)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(src));
for x in list(b.GetTracks()):
 if x.GetNetname()=='REFCLK_N':b.RemoveNative(x)
n=b.FindNet('REFCLK_N');s(b,n,F,(106.8,65.95),(106.8,70.1));s(b,n,F,(106.8,70.1),(112,70.1));v(b,n,(112,70.1));s(b,n,F,(112,70.1),(118,70.1));s(b,n,F,(118,70.1),(118,54));s(b,n,F,(118,54),(135,54));s(b,n,F,(135,54),(135,66));s(b,n,F,(135,66),(136.75,66));v(b,n,(136.75,66));s(b,n,F,(136.75,66),(136.75,62.725))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
