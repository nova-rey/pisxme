"""Open-acreage Phase 20 service placement and mixed-side USB2 trial."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
IN=ROOT/'PHASE20_SERVICE_AUTHORITY_BASE.kicad_pcb'; OUT=ROOT/'PHASE20_SERVICE_OPEN_ACREAGE.kicad_pcb'
W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I(pcbnew.FromMM(x),pcbnew.FromMM(y))
def tr(b,n,a,z,l):
 s=pcbnew.PCB_TRACK(b); s.SetStart(P(*a)); s.SetEnd(P(*z)); s.SetWidth(W); s.SetLayer(l); s.SetNet(n); b.Add(s)
def vi(b,n,x,y):
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(x,y)); v.SetWidth(pcbnew.FromMM(.45)); v.SetDrill(pcbnew.FromMM(.20)); v.SetNet(n); b.Add(v)
def path(b,n,pts,l):
 for a,z in zip(pts,pts[1:]): tr(b,n,a,z,l)
def main():
 b=pcbnew.LoadBoard(str(IN))
 # Place the complete service island in open acreage near the CM5 source;
 # leave the connector horizontal for uncomplicated cable access.
 for ref,xy,rot in [('U8',(75,100),0),('J4',(90,100),0),('R1',(82,108),90),('R2',(86,108),90)]:
  f=b.FindFootprintByReference(ref); f.SetPosition(P(*xy)); f.SetOrientationDegrees(rot)
 dp=b.FindNet('/SERVICE/SERVICE_USB2_DP'); dm=b.FindNet('/SERVICE/SERVICE_USB2_DM')
 # DP remains on F.Cu; DM uses B.Cu to avoid the compact ESD pad field.
 path(b,dp,[(66.96,99.5),(70,99.5),(72,101),(74.65,100.425)],pcbnew.F_Cu)
 path(b,dp,[(74.65,100.425),(80,98),(89.75,98)],pcbnew.F_Cu)
 vi(b,dm,65.8,99.1); tr(b,dm,(66.96,99.1),(65.8,99.1),pcbnew.F_Cu)
 path(b,dm,[(65.8,99.1),(70,98),(73,98),(76.2,101.2)],pcbnew.B_Cu)
 vi(b,dm,76.2,101.2); tr(b,dm,(76.2,101.2),(75.35,100.425),pcbnew.F_Cu)
 path(b,dm,[(75.35,100.425),(80,102),(89.75,102)],pcbnew.F_Cu)
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
