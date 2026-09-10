"""Disposable V193 native XOUT escape around U11.  Copper only."""
from pathlib import Path
import sys, pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_V75_COAUTHORED_V193.kicad_pcb'; OUT=R/'PHASE24_STORAGE_V75_COAUTHORED_V194.kicad_pcb'
if len(sys.argv)>1: BASE=R/sys.argv[1]
if len(sys.argv)>2: OUT=R/sys.argv[2]
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('XOUT'); F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(a,z,l):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.13208));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.5));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
for t in list(b.GetTracks()):
 if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
tr((137.8,131.4),(137.8,128.5),F); via((137.8,128.5))
tr((137.8,128.5),(132.0,128.5),B); tr((132.0,128.5),(146.5,112.0),B); via((146.5,112.0))
tr((146.5,112.0),(148.9,115.85),F)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.BuildConnectivity();b.Save(str(OUT));print(OUT)
