"""U1.39/U2.8 lower RTL_3V3 discriminator with co-authored U1.40 escape."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;base=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_RTL3V3_UPPER_V2.kicad_pcb';out=H/'PHASE24_RTL9210B_SUPPORT_CLUSTER_MOVE_V35_U2_LEFT_RTL3V3_U139.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def p(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b);q.SetStart(p(*a));q.SetEnd(p(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b);x.SetPosition(p(*q));x.SetWidth(pcbnew.FromMM(.60));x.SetDrill(pcbnew.FromMM(.30));x.SetLayerPair(F,B);x.SetNet(n);x.SetNetCode(n.GetNetCode());b.Add(x)
b=pcbnew.LoadBoard(str(base))
# Rebuild lower 1V1 so U1.40 uses the outer x=90 channel, clear of U1.39's escape.
n1=b.FindNet('RTL_1V1')
for x in list(b.GetTracks()):
 if x.GetNetname()=='RTL_1V1': b.RemoveNative(x)
for src,esc in [((94.05,67.20),(87.0,67.20)),((94.05,68.80),(90.0,68.80)),((94.05,72.80),(89.0,72.80)),((96.0,73.95),(97.2,77.5)),((98.0,73.95),(98.0,84.0)),((99.2,73.95),(99.2,84.0))]:
 s(b,n1,F,src,esc)
 if esc[1]<84:s(b,n1,F,esc,(esc[0],84.0))
 v(b,n1,(esc[0],84.0))
s(b,n1,B,(87,84),(104,84));v(b,n1,(104,84));s(b,n1,F,(104,84),(104,82))
# U1.39 leaves on a steeper upper-left dogbone so the first segment clears
# the adjacent USB_DM pad under the active 0.20 mm width/clearance rules.
n3=b.FindNet('RTL_3V3');s(b,n3,F,(94.05,68.4),(92.0,67.6));v(b,n3,(92.0,67.6));s(b,n3,B,(92.0,67.6),(80.2,67.6));v(b,n3,(80.2,67.6));s(b,n3,F,(80.2,67.6),(80.2,80.0))
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(out));print(out)
