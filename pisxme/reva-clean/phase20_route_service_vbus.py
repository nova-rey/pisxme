"""Add a separated, connector-local VBUS alias network to the best data candidate."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent; IN=ROOT/'PHASE20_SERVICE_ALIAS_FINAL_CANDIDATE.kicad_pcb'; OUT=ROOT/'PHASE20_SERVICE_VBUS_CANDIDATE.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I(pcbnew.FromMM(x),pcbnew.FromMM(y))
def seg(b,n,l,pts,w=.13208):
 for a,z in zip(pts,pts[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetWidth(pcbnew.FromMM(w)); t.SetLayer(l); t.SetNet(n); b.Add(t)
def via(b,n,x,y):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(x,y)); v.SetWidth(pcbnew.FromMM(.55)); v.SetDrill(pcbnew.FromMM(.30)); v.SetNet(n); b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(IN)); n=b.FindNet('/SERVICE/SERVICE_VBUS_SENSE')
 # F.Cu pad necks, then a large B.Cu perimeter outside both data corridors.
 for x,y in [(39.5,98.75),(39.5,101.25),(51,98.75),(51,101.25)]: via(b,n,x,y)
 seg(b,n,pcbnew.F_Cu,[(43,98.75),(39.5,98.75)])
 seg(b,n,pcbnew.F_Cu,[(47,98.75),(51,98.75)])
 seg(b,n,pcbnew.F_Cu,[(43,101.25),(39.5,101.25)])
 seg(b,n,pcbnew.F_Cu,[(47,101.25),(51,101.25)])
 # Leave the A-side pads on F.Cu, then use an outer B.Cu perimeter.  The
 # transition at x=39.5 is left of the data alias fields and avoids the
 # primary DM vertical escape.
 seg(b,n,pcbnew.F_Cu,[(42,98.75),(39.5,98.75),(39.5,101.25),(42,101.25)])
 seg(b,n,pcbnew.B_Cu,[(39.5,98.75),(39.5,95),(51,95),(51,98.75)])
 seg(b,n,pcbnew.B_Cu,[(39.5,101.25),(39.5,98.75)])
 seg(b,n,pcbnew.B_Cu,[(51,101.25),(51,98.75)])
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
