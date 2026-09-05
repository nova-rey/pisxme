"""Route the disposable Phase 20 CM5 service USB2 path on F.Cu."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
IN=ROOT/'PHASE20_SERVICE_AUTHORITY_BASE.kicad_pcb'
OUT=ROOT/'PHASE20_SERVICE_USB2_ROUTED.kicad_pcb'
W=pcbnew.FromMM(0.20)

def pt(x,y): return pcbnew.VECTOR2I(pcbnew.FromMM(x),pcbnew.FromMM(y))
def route(b,name,points):
    net=b.FindNet(name)
    if net is None: raise RuntimeError(name)
    for a,z in zip(points,points[1:]):
        s=pcbnew.PCB_TRACK(b); s.SetStart(pt(*a)); s.SetEnd(pt(*z)); s.SetWidth(W); s.SetLayer(pcbnew.F_Cu); s.SetNet(net); b.Add(s)

def main():
    b=pcbnew.LoadBoard(str(IN))
    dp='/SERVICE/SERVICE_USB2_DP'; dm='/SERVICE/SERVICE_USB2_DM'
    # Put the ESD ground pad on the south side so the incoming pair can
    # approach the two signal pads from the open north corridor.
    b.FindFootprintByReference('U8').SetOrientationDegrees(180)
    # Keep the pair together down the open west-side corridor, then launch
    # monotonically into the connector-side ESD footprint.
    route(b,dp,[(66.96,99.5),(62,99.5),(62,120),(52,136),(42.35,140),(42.35,144.575),(40,141),(35,141),(30,141),(24.75,143)])
    route(b,dm,[(66.96,99.1),(60,99.1),(60,121),(48,138),(41.65,140),(41.65,144.575),(44,149),(36,149),(30,149),(24.75,147)])
    b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
