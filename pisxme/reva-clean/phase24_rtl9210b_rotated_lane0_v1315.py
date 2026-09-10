"""V1315: V1311 lane repair with below-pad SPISO bypass and separated exits."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_SPI_U1_ROTATE90_SPICS_SPISO_V735.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_ROTATED_LANE0_V1315.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,ps):
    for a,z in zip(ps,ps[1:]):
        q=pcbnew.PCB_TRACK(b); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def v(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(P(*p)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30)); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U1'); j=b.FindFootprintByReference('J1')
for q in list(b.GetTracks()):
    if q.GetNetname() in {'LANE0_RXP','LANE0_RXN','LANE0_TXN','LANE0_TXP'}: b.RemoveNative(q)
def pad(n,p):
    q=u.FindPadByNumber(p).GetPosition(); return (pcbnew.ToMM(q.x),pcbnew.ToMM(q.y))
def jp(p):
    q=j.FindPadByNumber(p).GetPosition(); return (pcbnew.ToMM(q.x),pcbnew.ToMM(q.y))
# RXP leaves vertically, then moves outward below the QFN row before its
# transition; the F.Cu jog around x=102.5 bypasses the retained SPISO trunk.
n=b.FindNet('LANE0_RXP'); src=pad(n,'64'); s(b,n,F,[src,(99.6,76.0),(98.8,76.0)]); v(b,n,(98.8,76.0)); s(b,n,B,[(98.8,76.0),(101.5,76.0)]); v(b,n,(101.5,76.0)); s(b,n,F,[(101.5,76.0),(104.0,76.0)]); v(b,n,(104.0,76.0)); s(b,n,B,[(104.0,76.0),(130.0,76.0)]); v(b,n,(130.0,76.0)); s(b,n,F,[(130.0,76.0),(130.0,60.0)]); v(b,n,(130.0,60.0)); s(b,n,B,[(130.0,60.0),(134.25,60.0)]); v(b,n,(134.25,60.0)); s(b,n,F,[(134.25,60.0),jp('43')])
n=b.FindNet('LANE0_RXN'); src=pad(n,'65'); s(b,n,F,[src,(100.0,77.5)]); v(b,n,(100.0,77.5)); s(b,n,B,[(100.0,77.5),(131.0,77.5)]); v(b,n,(131.0,77.5)); s(b,n,F,[(131.0,77.5),(131.0,58.0)]); v(b,n,(131.0,58.0)); s(b,n,B,[(131.0,58.0),(133.75,58.0)]); v(b,n,(133.75,58.0)); s(b,n,F,[(133.75,58.0),jp('41')])
n=b.FindNet('LANE0_TXN'); src=pad(n,'67'); s(b,n,F,[src,(100.8,80.0)]); v(b,n,(100.8,80.0)); s(b,n,B,[(100.8,80.0),(133.0,80.0)]); v(b,n,(133.0,80.0)); s(b,n,F,[(133.0,80.0),(133.0,56.0)]); v(b,n,(133.0,56.0)); s(b,n,B,[(133.0,56.0),(135.25,56.0)]); v(b,n,(135.25,56.0)); s(b,n,F,[(135.25,56.0),jp('47')])
n=b.FindNet('LANE0_TXP'); src=pad(n,'68'); s(b,n,F,[src,(101.2,78.0),(103.0,78.0)]); v(b,n,(103.0,78.0)); s(b,n,F,[(103.0,78.0),(103.0,82.5)]); v(b,n,(103.0,82.5)); s(b,n,B,[(103.0,82.5),(134.0,82.5)]); v(b,n,(134.0,82.5)); s(b,n,B,[(134.0,82.5),(134.0,54.0),(135.75,54.0)]); v(b,n,(135.75,54.0)); s(b,n,F,[(135.75,54.0),jp('49')])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
