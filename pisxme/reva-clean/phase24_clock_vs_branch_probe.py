"""Disposable VSSOSC-only branch probe after XI and XO."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CLOCK_XI_XO_BRANCH_PROBE.kicad_pcb'
OUT=R/'PHASE24_CLOCK_XI_XO_VS_BRANCH_PROBE.kicad_pcb'
NET='/STORAGE/BRIDGE_VSSOSC'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def main():
    b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet(NET)
    if n is None: raise RuntimeError('VSSOSC net missing')
    u=b.FindFootprintByReference('U7'); y=b.FindFootprintByReference('Y1')
    target=next(p for p in y.Pads() if str(p.GetNumber())=='2')
    tx=pcbnew.ToMM(target.GetPosition().x); ty=pcbnew.ToMM(target.GetPosition().y)
    def T(a,z,l):
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l)
        t.SetWidth(pcbnew.FromMM(.1321)); t.SetNet(n); b.Add(t)
    def X(p):
        v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3))
        v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
    # Perimeter on F.Cu, then one ordinary via and a short B.Cu pad launch.
    T((122.5,126.5),(116,126.5),pcbnew.F_Cu)
    T((116,126.5),(116,120),pcbnew.F_Cu)
    T((116,120),(105,120),pcbnew.F_Cu)
    T((105,120),(105,ty),pcbnew.F_Cu)
    X((105,ty)); T((105,ty),(tx,ty),pcbnew.B_Cu)
    b.Save(str(OUT)); print(OUT, 'Y1.2=',tx,ty)
if __name__=='__main__': main()
