"""Second Phase 20 routing experiment: ordinary-via B.Cu service pair."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
IN=ROOT/'PHASE20_SERVICE_AUTHORITY_BASE.kicad_pcb'; OUT=ROOT/'PHASE20_SERVICE_USB2_BCU.kicad_pcb'
W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I(pcbnew.FromMM(x),pcbnew.FromMM(y))
def seg(b,n,a,z,layer):
 s=pcbnew.PCB_TRACK(b); s.SetStart(P(*a)); s.SetEnd(P(*z)); s.SetWidth(W); s.SetLayer(layer); s.SetNet(n); b.Add(s)
def via(b,n,x,y):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(x,y)); v.SetWidth(pcbnew.FromMM(.6)); v.SetDrill(pcbnew.FromMM(.3)); v.SetNet(n); b.Add(v)
def path(b,n,pts,layer):
 for a,z in zip(pts,pts[1:]): seg(b,n,a,z,layer)
def main():
 b=pcbnew.LoadBoard(str(IN)); b.FindFootprintByReference('U8').SetOrientationDegrees(180)
 dp=b.FindNet('/SERVICE/SERVICE_USB2_DP'); dm=b.FindNet('/SERVICE/SERVICE_USB2_DM')
 # B.Cu carries each pair through an ordinary via transition.  The short
 # F.Cu dogbones stay outside the SMD pads and the ESD ground pad.
 for n, pts in [(dp,[(66.0,99.5),(66,120),(52,138),(43,144)]),
                (dm,[(66.0,99.1),(64,120),(50,140),(40.9,144)])]: path(b,n,pts,pcbnew.B_Cu)
 via(b,dp,66,99.5); via(b,dp,43,144); seg(b,dp,(43,144),(42.35,144.575),pcbnew.F_Cu)
 via(b,dm,66,99.1); via(b,dm,40.9,144); seg(b,dm,(40.9,144),(41.65,144.575),pcbnew.F_Cu)
 path(b,dp,[(43,144),(35,141),(28,141),(24.75,142)],pcbnew.B_Cu); via(b,dp,24.75,142); seg(b,dp,(24.75,142),(24.75,143),pcbnew.F_Cu)
 path(b,dm,[(40.9,144),(36,149),(28,149),(24.75,148)],pcbnew.B_Cu); via(b,dm,24.75,148); seg(b,dm,(24.75,148),(24.75,147),pcbnew.F_Cu)
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
