"""V1242: regenerate QFN rail/GND support around the V1240 REFCLK exits."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_REFCLK_SOURCE_FIELD_CLEAR_V1240.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_RAILS_AROUND_REFCLK_V1242.kicad_pcb'
F,B,I1=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.In1_Cu
W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,n,pts,l,w=W):
    for a,z in zip(pts,pts[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(w); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,xy):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE))
one=b.FindNet('RTL_1V1'); three=b.FindNet('RTL_3V3'); gnd=b.FindNet('GND'); assert one and three and gnd
# Move the V1240 CLKREQ source cohort west so the regenerated GND return has a clear F.Cu drop.
for q in list(b.GetTracks()):
    if q.GetNetname()=='CLKREQ_N' and q.GetLayerName()=='F.Cu' and q.GetStart()==P(99.6,73.95) and q.GetEnd()==P(99.6,76.0): b.RemoveNative(q)
    if q.GetNetname()=='CLKREQ_N' and q.GetLayerName()=='B.Cu' and q.GetStart()==P(99.6,76.0) and q.GetEnd()==P(70.0,76.0): b.RemoveNative(q)
for q in list(b.GetTracks()):
    if q.GetNetname()=='CLKREQ_N' and type(q).__name__=='PCB_VIA' and q.GetPosition()==P(99.6,76.0): b.RemoveNative(q)
clk=b.FindNet('CLKREQ_N'); add(b,clk,[(99.6,73.95),(99.6,74.5),(97.8,74.5),(97.8,76.0)],F); via(b,clk,(97.8,76.0)); add(b,clk,[(97.8,76.0),(70.0,76.0)],B)
add(b,one,[(94.05,68.0),(92.0,68.0),(91.8,69.0)],F); via(b,one,(91.8,69.0)); add(b,one,[(91.8,69.0),(102.0,64.8)],pcbnew.In2_Cu)
add(b,one,[(94.05,70.0),(93.2,70.0),(92.5,69.0)],F); via(b,one,(92.5,69.0)); add(b,one,[(92.5,69.0),(102.0,64.8)],pcbnew.In2_Cu)
add(b,one,[(94.05,71.2),(93.2,71.2),(93.2,74.0)],F); via(b,one,(93.2,74.0)); add(b,one,[(93.2,74.0),(102.0,64.8)],pcbnew.In2_Cu)
add(b,one,[(95.2,66.05),(95.2,64.8),(97.8,64.8),(97.8,63.6)],F); via(b,one,(97.8,63.6)); add(b,one,[(97.8,63.6),(102.0,64.8)],pcbnew.In2_Cu)
add(b,one,[(99.2,66.05),(99.2,63.6),(97.8,63.6)],F)
add(b,three,[(94.05,66.8),(91.8,66.8),(91.8,66.2)],F); via(b,three,(91.8,66.2)); add(b,three,[(91.8,66.2),(91.8,59.0)],pcbnew.In2_Cu); add(b,three,[(99.6,66.05),(99.6,62.8)],F)
add(b,gnd,[(97.2,66.05),(97.2,67.6)],F); add(b,gnd,[(94.05,72.4),(95.6,72.4)],F); add(b,gnd,[(95.6,72.4),(99.5,72.4)],F); via(b,gnd,(99.5,72.4)); add(b,gnd,[(99.5,72.4),(99.5,80.0)],B); via(b,gnd,(99.5,80.0)); add(b,gnd,[(99.5,80.0),(94.0,62.0)],I1,W)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
