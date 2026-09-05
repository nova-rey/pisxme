"""Route Rd_A/Rd_B in separated lower-acreage support corridors."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent; IN=ROOT/'PHASE20_SERVICE_VBUS_CANDIDATE.kicad_pcb'; OUT=ROOT/'PHASE20_SERVICE_RD_OUTER.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I(pcbnew.FromMM(x),pcbnew.FromMM(y))
def seg(b,n,l,pts,w=.15):
 for a,z in zip(pts,pts[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetWidth(pcbnew.FromMM(w)); t.SetLayer(l); t.SetNet(n); b.Add(t)
def via(b,n,x,y):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(x,y)); v.SetWidth(pcbnew.FromMM(.55)); v.SetDrill(pcbnew.FromMM(.30)); v.SetNet(n); b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(IN)); rda=b.FindNet('/SERVICE/SERVICE_RD_A'); rdb=b.FindNet('/SERVICE/SERVICE_RD_B')
 for ref,pos in [('R1',(60,145)),('R2',(80,145))]:
  f=b.FindFootprintByReference(ref); f.SetPosition(P(*pos)); f.SetOrientationDegrees(90)
 # A5 -> R1.1: left-side connector neck, then lower B.Cu corridor.
 via(b,rda,40,100.75); via(b,rda,60,145.5)
 seg(b,rda,pcbnew.F_Cu,[(43,100.75),(40,100.75)])
 seg(b,rda,pcbnew.B_Cu,[(40,100.75),(40,107),(45.5,107),(45.5,145.5),(60,145.5)])
 seg(b,rda,pcbnew.F_Cu,[(60,145.5),(60,145.5)])
 # B5 -> R2.1: right-side neck and a distinct B.Cu corridor.
 via(b,rdb,52,99.25); via(b,rdb,80,145.5)
 seg(b,rdb,pcbnew.F_Cu,[(47,99.25),(52,99.25)])
 seg(b,rdb,pcbnew.B_Cu,[(52,99.25),(52,114),(80,114),(80,145.5)])
 seg(b,rdb,pcbnew.F_Cu,[(80,145.5),(80,145.5)])
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
