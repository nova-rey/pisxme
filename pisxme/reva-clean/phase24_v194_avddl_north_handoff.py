"""Disposable V194 AVDDL handoff trial around the U11 AVDD33 field."""
from pathlib import Path
import sys, pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_V75_COAUTHORED_V194.kicad_pcb'; OUT=R/'PHASE24_STORAGE_V75_COAUTHORED_V196.kicad_pcb'
if len(sys.argv)>1: BASE=R/sys.argv[1]
if len(sys.argv)>2: OUT=R/sys.argv[2]
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('JMS_AVDDL'); F,B=pcbnew.F_Cu,pcbnew.B_Cu
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(a,z,l):
 q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(pcbnew.FromMM(.13208));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def via(p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.5));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(F,B);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
for t in list(b.GetTracks()):
 if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
tr((141.8,138.6),(141.8,137.5),F); via((141.8,137.5))
tr((141.8,137.5),(150.0,137.5),B);tr((150.0,137.5),(150.0,126.0),B);tr((150.0,126.0),(154.5,126.0),B);via((154.5,126.0));tr((154.5,126.0),(154.5,147.0),F)
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.BuildConnectivity();b.Save(str(OUT));print(OUT)
