"""V98: selective U13 storage-rail fanout to an east-side B.Cu trunk."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_AUTHORITY_J3_VERTICAL_V94.kicad_pcb'; OUT=R/'PHASE24_STORAGE_RAIL_U13_LOCAL_V98.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,l,a,z,w=.22):
 q=pcbnew.PCB_TRACK(b); q.SetLayer(l); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetWidth(pcbnew.FromMM(w)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def vi(b,n,a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetDrill(pcbnew.FromMM(.30)); q.SetWidth(pcbnew.FromMM(.60)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('STORAGE_3V3'); assert n
# QFN pads escape only to nearby ordinary through-vias; shared trunk remains B.Cu.
fan=[((178.5,133.4),(177.3,132.2)),((178.5,136.6),(177.3,137.8)),((179.8,139.5),(179.8,141.0)),((181.5,135.0),(183.0,135.0))]
for pad,v in fan: tr(b,n,pcbnew.F_Cu,pad,v); vi(b,n,v)
for a,z in [((177.3,132.2),(183.0,132.2)),((177.3,137.8),(183.0,137.8)),((179.8,141.0),(183.0,141.0)),((183.0,132.2),(183.0,135.0)),((183.0,137.8),(183.0,135.0)),((183.0,141.0),(183.0,135.0)),((183.0,135.0),(190.0,135.0)),((190.0,135.0),(190.0,143.0)),((190.0,143.0),(210.0,143.0)),((210.0,143.0),(210.0,149.05))]: tr(b,n,pcbnew.B_Cu,a,z)
vi(b,n,(210.0,149.05)); tr(b,n,pcbnew.F_Cu,(210.0,149.05),(211.1,149.05))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
