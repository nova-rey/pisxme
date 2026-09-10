"""V99: storage rail on a local In4 power island with pad-aware vias."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_AUTHORITY_J3_VERTICAL_V94.kicad_pcb'; OUT=R/'PHASE24_STORAGE_RAIL_IN4_PLANE_V99.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('STORAGE_3V3'); assert n
def tr(a,z,w=.25):
 q=pcbnew.PCB_TRACK(b); q.SetLayer(pcbnew.F_Cu); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetWidth(pcbnew.FromMM(w)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); b.Add(q)
for pad,drop in [((153.5,136.6),(151.5,136.6)),((154.8,139.5),(154.8,141.5)),((156.5,135),(158.5,135)),((178.5,133.4),(176.5,133.4)),((178.5,136.6),(176.5,136.6)),((179.8,139.5),(179.8,141.5)),((181.5,135),(183.5,135)),((211.1,149.05),(213,149.05)),((125.5,145),(125.5,147))]:
 tr(pad,drop); via(drop)
z=pcbnew.ZONE(b); z.SetLayer(pcbnew.In4_Cu); z.SetNet(n); z.SetNetCode(n.GetNetCode()); z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL); z.SetLocalClearance(pcbnew.FromMM(.20)); z.SetMinThickness(pcbnew.FromMM(.20))
poly=pcbnew.VECTOR_VECTOR2I()
for xy in ((120,128),(190,128),(190,150),(240,150),(240,179),(120,179)): poly.append(P(*xy))
z.AddPolygon(poly); b.Add(z)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
