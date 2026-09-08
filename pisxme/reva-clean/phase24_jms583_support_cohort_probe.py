"""Combine the validated JMS583 support sub-primitive corridors."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent;BASE=R/'PHASE24_DUAL_MODE_STORAGE_PLACEMENT_CURRENT.kicad_pcb';OUT=R/'PHASE24_JMS583_SUPPORT_COHORT_PROBE.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,a,z,w=.20):
    t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(pcbnew.F_Cu);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def via(b,n,q):
    v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def route(b,name,ref,pad,points):
    n=b.FindNet(name); f=b.FindFootprintByReference(ref); src=xy(f.FindPadByNumber(pad).GetPosition())
    pts=[src]+points
    for a,z in zip(pts,pts[1:]): seg(b,n,a,z)
b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U11')
placements={'R81':(125,145),'C80':(148,143),'C81':(148,147),'C82':(120,147)}
for ref,q in placements.items(): b.FindFootprintByReference(ref).SetPosition(P(*q))
b.FindFootprintByReference('L10').SetPosition(P(136,125));b.FindFootprintByReference('L10').SetOrientationDegrees(180)
b.FindFootprintByReference('Y10').SetPosition(P(150,115))
for name in ('JMS_RESET_N','JMS_AVDD33','JMS_VCCO','JMS_VCCK','JMS_VDDREG_5V','LXO'):
    n=b.FindNet(name)
    for x in list(b.GetTracks()):
        if x.GetNetCode()==n.GetNetCode(): b.RemoveNative(x)
# Each route leaves the appropriate QFN edge laterally and approaches the
# passive from its free pad side, as proven in the individual probes.
route(b,'JMS_RESET_N','U11','15',[(133,137.6),(133,143),(122,143),(122,145)])
route(b,'JMS_RESET_N','R81','1',[(122,145)])
route(b,'JMS_AVDD33','U11','19',[(142.2,140),(147,140),(147,143)])
route(b,'JMS_AVDD33','C80','1',[(147,143)])
n=b.FindNet('JMS_VCCO');s=xy(u.FindPadByNumber('6').GetPosition());d=xy(b.FindFootprintByReference('C81').FindPadByNumber('1').GetPosition())
seg(b,n,s,(134.5,s[1]));via(b,n,(134.5,s[1]));
for a,z in [((134.5,s[1]),(134.5,145)),((134.5,145),(147,145))]:
    t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(pcbnew.B_Cu);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
via(b,n,(147,145));seg(b,n,(147,145),(147,d[1]));seg(b,n,(147,d[1]),d)
route(b,'JMS_VCCK','U11','2',[(131,132.4),(131,142),(118,142),(118,147)])
route(b,'JMS_VCCK','C82','1',[(118,147)])
route(b,'JMS_VDDREG_5V','U11','1',[(133,132),(133,125)])
route(b,'JMS_VDDREG_5V','L10','2',[(133,125)])
route(b,'LXO','U11','64',[(146,131.4),(146,125)])
route(b,'LXO','L10','1',[(146,125)])
b.Save(str(OUT));print(OUT)
