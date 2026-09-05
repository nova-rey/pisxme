"""Disposable B.Cu chain for the spaced bridge-1V1 capacitor field."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'PHASE24_LOCAL_REPAIRS_CLOCK_COMPLETE.kicad_pcb'
OUT=ROOT/'PHASE24_BRIDGE_1V1_CAP_CHAIN.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/REGULATORS/BRIDGE_1V1')
def v(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def track(layer,a,z,w=0.20):
    t=pcbnew.PCB_TRACK(b); t.SetLayer(layer); t.SetNet(n); t.SetWidth(pcbnew.FromMM(w)); t.SetStart(v(*a)); t.SetEnd(v(*z)); b.Add(t)
def via(x,y):
    q=pcbnew.PCB_VIA(b); q.SetNet(n); q.SetPosition(v(x,y)); q.SetWidth(pcbnew.FromMM(0.50)); q.SetDrill(pcbnew.FromMM(0.30)); b.Add(q)

# Each capacitor's rail pad is 2.70 mm left of its ground pad.  Offset the
# via 1.45 mm left of the pad center: this is adjacent escape, not via-in-pad.
caps=['C26','C27','C28','C29','C34','C35','C36','C37','C38','C39','C40','C41']
centers=[]
for ref in caps:
    pad=next(p for p in b.FindFootprintByReference(ref).Pads() if p.GetNumber()=='1')
    q=pad.GetPosition(); px=q.x/1e6; py=q.y/1e6; c=(px-1.45,py); centers.append(c)
    track(pcbnew.F_Cu,(px,py),c); via(*c)
for a,z in zip(centers,centers[1:]): track(pcbnew.B_Cu,a,z)
# Bridge the two capacitor rows at the left edge on B.Cu.
track(pcbnew.B_Cu,centers[0],centers[4])
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
