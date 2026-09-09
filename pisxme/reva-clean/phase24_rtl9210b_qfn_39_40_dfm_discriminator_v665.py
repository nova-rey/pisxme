"""Bounded RTL9210B U1.39/U1.40 escape discriminator; no rule changes."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V661_LOWER_3V3_PROBE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_QFN_39_40_DFM_DISCRIMINATOR_V665.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def addt(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def addv(b,n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n33=b.FindNet('RTL_3V3'); n11=b.FindNet('RTL_1V1')
# Remove only the V661 lower-3V3 trial branch and its collector segment.
for q in list(b.GetTracks()):
 a=q.GetStart(); z=q.GetEnd(); ax,ay=a.x/1e6,a.y/1e6; zx,zy=z.x/1e6,z.y/1e6
 if q.GetNetname()=='RTL_3V3' and ((abs(ax-94.05)<.02 and abs(ay-68.4)<.02) or (abs(ax-90.5)<.02 and abs(ay-68.4)<.02) or (abs(ax-90.5)<.02 and abs(zx-90.5)<.02)):
  b.RemoveNative(q)
# Keep U1.40's existing leftward F.Cu escape. Give U1.39 its own
# outward-then-north channel; the transition is not between pads 39/40.
addt(b,n33,F,(94.05,68.4),(92.6,68.4))
addt(b,n33,F,(92.6,68.4),(91.8,67.0))
addv(b,n33,91.8,67.0)
addt(b,n33,B,(91.8,67.0),(91.8,55.0))
# Join the existing RTL_3V3 collector at its native transition endpoint.
addt(b,n33,B,(91.8,55.0),(93.8,55.0))
addt(b,n33,F,(93.8,55.0),(93.8,75.2))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
