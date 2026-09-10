"""V93: connect all storage-island rail pads to an In1 power zone."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_AUTHORITY_REGEN_V91.kicad_pcb'; OUT=R/'PHASE24_STORAGE_STORAGE3V3_PLANE_V93.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('STORAGE_3V3'); assert n
def tr(layer,pts,w=.25):
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b); q.SetLayer(layer); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetWidth(pcbnew.FromMM(w)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(P(x,y)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); b.Add(q)
# Pad-aware escapes from every support/source rail pad, no via-in-pad.
for pad,drop in [((153.5,136.6),(151.5,136.6)),((154.8,139.5),(154.8,141.5)),((156.5,135),(158.5,135)),
                 ((178.5,133.4),(176.5,133.4)),((179.8,139.5),(179.8,141.5)),((181.5,135),(183.5,135)),
                 ((211.1,149.05),(213,149.05)),((125.5,145),(125.5,147))]:
 tr(pcbnew.F_Cu,[pad,drop]); via(*drop)
z=pcbnew.ZONE(b); z.SetLayer(pcbnew.In1_Cu); z.SetNet(n); z.SetNetCode(n.GetNetCode()); z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL); z.SetLocalClearance(pcbnew.FromMM(.20)); z.SetMinThickness(pcbnew.FromMM(.20))
poly=pcbnew.VECTOR_VECTOR2I()
for xy in ((120,128),(190,128),(190,150),(240,150),(240,179),(120,179)): poly.append(P(*xy))
z.AddPolygon(poly); b.Add(z)
# J3 power groups use the right-side F.Cu edge corridor, avoiding B.Cu signal field.
for g in [(211.0,211.5),(213.5,214.0,214.5,215.0),(228.0,228.5,229.0)]:
 for a,qx in zip(g,g[1:]): tr(pcbnew.F_Cu,[(a,167.275),(qx,167.275)])
 qx=g[-1]; endx=236.0 if qx==229.0 else qx; tr(pcbnew.F_Cu,[(qx,167.275),(endx,167.275),(endx,176)])
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
