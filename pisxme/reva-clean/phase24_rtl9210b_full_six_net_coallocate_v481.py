"""V481: replace only V480 REFCLK with separated upper detours."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
src=H/'PHASE24_RTL9210B_FULL_SIX_NET_COALLOCATE_V480.kicad_pcb';out=H/'PHASE24_RTL9210B_FULL_SIX_NET_COALLOCATE_V481.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.13208)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(P(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(src))
for name in ('REFCLK_P','REFCLK_N'):
 for x in list(b.GetTracks()):
  if x.GetNetname()==name:b.RemoveNative(x)
# P: leave the source via on F.Cu and stay above the B.Cu lane/control field.
n=b.FindNet('REFCLK_P');s(b,n,F,(111,71),(130,71));s(b,n,F,(130,71),(130,54));s(b,n,F,(130,54),(137.25,54));s(b,n,F,(137.25,54),(137.25,60.5));v(b,n,(137.25,60.5));s(b,n,F,(137.25,60.5),(137.25,62.725))
# N: stay on B.Cu, using a separate vertical and an upper row; its endpoint
# transition is the proven V448 position.
n=b.FindNet('REFCLK_N');s(b,n,B,(112,70.1),(129,70.1));s(b,n,B,(129,70.1),(129,53));s(b,n,B,(129,53),(136,53));s(b,n,B,(136,53),(136,64.5));s(b,n,B,(136,64.5),(136.75,64.5));v(b,n,(136.75,64.5));s(b,n,F,(136.75,64.5),(136.75,62.725))
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
