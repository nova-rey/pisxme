"""Sweep compact clock-support positions from the V5 rot180 ancestor."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb'
IO=pcbnew.PCB_IO_KICAD_SEXPR()
N={'XI':'/STORAGE/BRIDGE_XI','VS':'/STORAGE/BRIDGE_VSSOSC','XO':'/STORAGE/BRIDGE_XO'}
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def P(f,n): return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def main():
    candidates={'west':(100,140),'nearwest':(108,130),'south':(120,160),'east':(270,100),'north':(120,105),'farwest':(70,120)}
    for tag,(cx,cy) in candidates.items():
        b=pcbnew.LoadBoard(str(BASE)); nets={}
        for k,name in N.items():
            nets[k]=b.FindNet(name)
            if nets[k] is None:
                nets[k]=pcbnew.NETINFO_ITEM(b,name); nets[k].SetNetCode(b.GetNetCount()+1); b.Add(nets[k])
        u=b.FindFootprintByReference('U7'); u.SetOrientationDegrees(180)
        for num,k in [('52','XI'),('53','VS'),('54','XO')]:
            p=P(u,num); p.SetNet(nets[k]); p.SetNetCode(nets[k].GetNetCode())
        for t in list(b.GetTracks()):
            if t.GetNetname() in N.values(): b.RemoveNative(t)
        y=IO.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),'Crystal_3225_4Pad'); y.SetReference('Y1'); y.SetPosition(V(cx,cy)); y.SetOrientationDegrees(0); b.Add(y)
        for p in y.Pads():
            k={'1':'XI','2':'VS','3':'XO','4':'VS'}[str(p.GetNumber())]; p.SetNet(nets[k]); p.SetNetCode(nets[k].GetNetCode()); p.SetLayer(pcbnew.B_Cu)
        def S(k,a,z,l=pcbnew.B_Cu):
            t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.1321)); t.SetNet(nets[k]); b.Add(t)
        def X(k,p):
            v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(nets[k]); b.Add(v)
        pads={k:xy(P(y,n)) for k,n in [('XI','1'),('VS','2'),('XO','3')]}
        xi,vs,xo=(xy(P(u,n)) for n in ('52','53','54'))
        # proven rot180 exits, then short orthogonal B.Cu corridors to the crystal.
        # All three oscillator pads are inside a 0.5-mm-pitch top row. Leave
        # outward (toward the package edge) before turning; lateral escape at
        # the pad row collides with adjacent no-connect/SATA pads.
        exits={'XI':((123,134.5),(124,131.5)),
               'VS':((122.5,133.5),(122.5,130.5)),
               'XO':((122,132.5),(122,129.5))}
        for k in ('XI','VS','XO'):
            a,e=exits[k]; S(k,{'XI':xi,'VS':vs,'XO':xo}[k],a,pcbnew.F_Cu); S(k,a,e,pcbnew.F_Cu); X(k,e)
        # route each lane with a distinct y offset before the final pad approach.
        routes={'XI':(124,cy-1.0),'VS':(122.5,cy),'XO':(122,cy+1.0)}
        for k in ('XI','VS','XO'):
            ex=exits[k][1]; lane=routes[k]; end=pads[k]
            S(k,ex,(lane[0],lane[1])); S(k,(lane[0],lane[1]),(end[0],lane[1])); S(k,(end[0],lane[1]),end)
        out=R/f'PHASE24_CLOCK_SWEEP_{tag}.kicad_pcb'; b.Save(str(out)); print(tag,out)
if __name__=='__main__': main()
