"""V101: safe U13/U14 pad escapes into a local In4 storage power island."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_AUTHORITY_J3_VERTICAL_V94.kicad_pcb'; OUT=R/'PHASE24_STORAGE_RAIL_IN4_U13_V101.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('STORAGE_3V3'); assert n
def tr(a,z):
 q=pcbnew.PCB_TRACK(b); q.SetLayer(pcbnew.F_Cu); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetWidth(pcbnew.FromMM(.22)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(a):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(*a)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); b.Add(q)
for pad,drop in [((178.5,133.4),(177.0,131.5)),((178.5,136.6),(176.5,138.5)),((179.8,139.5),(180.0,142.0)),((181.5,135.0),(185.0,135.0)),((211.1,149.05),(213.0,149.05))]: tr(pad,drop); via(drop)
z=pcbnew.ZONE(b); z.SetLayer(pcbnew.In4_Cu); z.SetNet(n); z.SetNetCode(n.GetNetCode()); z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL); z.SetLocalClearance(pcbnew.FromMM(.20)); z.SetMinThickness(pcbnew.FromMM(.20)); poly=pcbnew.VECTOR_VECTOR2I()
for xy in ((174,128),(188,128),(188,146),(216,146),(216,154),(174,154)): poly.append(P(*xy))
z.AddPolygon(poly); b.Add(z); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
