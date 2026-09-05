"""Disposable XI-only branch probe from the stable U7 source escape."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_U7_CLOCK_SOURCE_ESCAPE.kicad_pcb'
OUT=R/'PHASE24_CLOCK_XI_BRANCH_PROBE.kicad_pcb'
NET='/STORAGE/BRIDGE_XI'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def main():
    b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet(NET)
    if n is None: raise RuntimeError('XI net missing')
    # The exact serialized source via and Y1.1 are queried from the board;
    # only the proposed route geometry is fixed by this probe.
    u=b.FindFootprintByReference('U7'); y=b.FindFootprintByReference('Y1')
    src=next(p for p in u.Pads() if str(p.GetNumber())=='52')
    target=next(p for p in y.Pads() if str(p.GetNumber())=='1')
    src_via=V(124,125.5); tx=pcbnew.ToMM(target.GetPosition().x); ty=pcbnew.ToMM(target.GetPosition().y)
    def T(a,z):
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(pcbnew.B_Cu)
        t.SetWidth(pcbnew.FromMM(.1321)); t.SetNet(n); b.Add(t)
    def X(p):
        v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30))
        v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
    T((124,125.5),(105,125.5)); T((105,125.5),(105,ty)); X((105,ty)); T((105,ty),(tx,ty))
    b.Save(str(OUT)); print(OUT, 'Y1.1=', tx, ty)
if __name__=='__main__': main()
