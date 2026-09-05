"""Disposable XO-only branch probe composed after the XI probe."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_CLOCK_XI_BRANCH_PROBE.kicad_pcb'
OUT=R/'PHASE24_CLOCK_XI_XO_BRANCH_PROBE.kicad_pcb'
NET='/STORAGE/BRIDGE_XO'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def main():
    b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet(NET)
    if n is None: raise RuntimeError('XO net missing')
    u=b.FindFootprintByReference('U7'); y=b.FindFootprintByReference('Y1')
    target=next(p for p in y.Pads() if str(p.GetNumber())=='3')
    tx=pcbnew.ToMM(target.GetPosition().x); ty=pcbnew.ToMM(target.GetPosition().y)
    def T(a,z,l=pcbnew.B_Cu):
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l)
        t.SetWidth(pcbnew.FromMM(.1321)); t.SetNet(n); b.Add(t)
    def X(p):
        v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3))
        v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
    # Keep the source dogbone outside the U7 pad row, then use a separate
    # lower B.Cu lane before the final Y1.3 launch.
    T((120.5,137.5),(112,137.5)); T((112,137.5),(112,ty)); X((112,ty)); T((112,ty),(tx,ty))
    b.Save(str(OUT)); print(OUT, 'Y1.3=',tx,ty)
if __name__=='__main__': main()
