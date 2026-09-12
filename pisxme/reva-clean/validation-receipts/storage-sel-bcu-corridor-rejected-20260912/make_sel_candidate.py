import pcbnew
from pathlib import Path
R=Path('/workspace/project/pisxme/reva-clean'); b=pcbnew.LoadBoard(str(R/'PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb'));F,B=pcbnew.F_Cu,pcbnew.B_Cu
V=lambda x,y:pcbnew.VECTOR2I_MM(float(x),float(y))
def N(s): return b.FindNet(s)
def P(r,n):
 q=b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition();return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def T(n,a,z,l,w=.2):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.6));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
n=N('STORAGE_SEL'); a=P('U12',9); z=P('U13',9); q=(160,135); r=(182,135); s=(215,145); t=P('U14',4)
T(n,a,q,F);via(n,q);T(n,q,r,B);via(n,r);T(n,r,z,F)
T(n,z,r,F) # duplicate reverse landing? omit maybe same net overlaps
# route U13 side to U14 via independent B branch
T(n,r,(182,145),B);T(n,(182,145),s,B);via(n,s);T(n,s,(215,150.95),F);T(n,(215,150.95),t,F)
b.BuildListOfNets();o='/workspace/output/PHASE24_STORAGE_SEL_BCU_CORRIDOR_CANDIDATE.kicad_pcb';b.Save(o);print(o)
