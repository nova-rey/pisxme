"""Phase 20 candidate: separated duplicate USB-C alias corridors."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent; IN=ROOT/'PHASE20_SERVICE_AUTHORITY_BASE.kicad_pcb'; OUT=ROOT/'PHASE20_SERVICE_ALIAS_FINAL_CANDIDATE.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I(pcbnew.FromMM(x),pcbnew.FromMM(y))
def seg(b,n,l,pts,w=.13208):
 for a,z in zip(pts,pts[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetWidth(pcbnew.FromMM(w)); t.SetLayer(l); t.SetNet(n); b.Add(t)
def via(b,n,x,y):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(x,y)); v.SetWidth(pcbnew.FromMM(.55)); v.SetDrill(pcbnew.FromMM(.30)); v.SetNet(n); b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(IN))
 for ref,pos,rot in [('U8',(58,100),90),('J4',(45,100),90),('R1',(50,106),90),('R2',(54,106),90)]:
  f=b.FindFootprintByReference(ref); f.SetPosition(P(*pos)); f.SetOrientationDegrees(rot)
 dp=b.FindNet('/CORE_CM5/SERVICE_USB2_DP'); dm=b.FindNet('/CORE_CM5/SERVICE_USB2_DM')
 # Primary A6/A7 escape. DM leaves the pair corridor before the B6/B7 row.
 seg(b,dm,pcbnew.F_Cu,[(66.96,99.1),(64,99.1),(61,99.65),(58.425,99.65),(59,99.65),(59,99.0),(54,99.0),(53,97.5),(46,97.5),(46,99.75),(43,99.75)])
 seg(b,dp,pcbnew.F_Cu,[(66.96,99.5),(64,99.5),(61,100.35),(58.425,100.35),(59,100.35),(59,101.0),(54,101.0),(54,102.5),(46,102.5),(46,100.25),(43,100.25)])
 # DP B6 (47,99.75) -> A6 (43,100.25), upper B.Cu corridor.
 via(b,dp,49,99.75); via(b,dp,41,100.25)
 seg(b,dp,pcbnew.F_Cu,[(47,99.75),(49,99.75)])
 seg(b,dp,pcbnew.B_Cu,[(49,99.75),(49,97),(41,97),(41,100.25)])
 seg(b,dp,pcbnew.F_Cu,[(41,100.25),(43,100.25)])
 # DM B7 (47,100.25) -> A7 (43,99.75), lower F.Cu corridor.
 via(b,dm,50,100.25); via(b,dm,41.5,99.60)
 seg(b,dm,pcbnew.F_Cu,[(47,100.25),(50,100.25)],w=.15)
 seg(b,dm,pcbnew.B_Cu,[(50,100.25),(50,106),(41.5,106),(41.5,99.60)],w=.15)
 seg(b,dm,pcbnew.F_Cu,[(41.5,99.60),(43,99.75)],w=.15)
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
