"""Phase 17 J7-only launch oracle: exact CM5 footprint, no acreage context."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_EDAC_CORRECTED_PHASE17.kicad_pcb'
MOD=ROOT/'PiSXMe_RevA_Clean.pretty/PiSXMeRevAClean_Raspberry_Pi_5_Compute_Module.kicad_mod'
OUT=ROOT/'CM5IO_J7_LAUNCH_FIXTURE.kicad_pcb'
MDI={3:'CM5_GBE_TD3_P',4:'CM5_GBE_TD1_P',5:'CM5_GBE_TD3_N',6:'CM5_GBE_TD1_N',
     9:'CM5_GBE_TD2_N',10:'CM5_GBE_TD0_N',11:'CM5_GBE_TD2_P',12:'CM5_GBE_TD0_P'}
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def track(b,n,a,z,layer):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(.20)); t.SetNet(n); b.Add(t)
def via(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.45)); q.SetDrill(pcbnew.FromMM(.20)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)
def edge(b,a,z):
    s=pcbnew.PCB_SHAPE(b); s.SetShape(pcbnew.SHAPE_T_SEGMENT); s.SetLayer(pcbnew.Edge_Cuts); s.SetStart(V(*a)); s.SetEnd(V(*z)); s.SetWidth(pcbnew.FromMM(.05)); b.Add(s)
def main():
    template=pcbnew.LoadBoard(str(BASE)).FindFootprintByReference('J7')
    b=pcbnew.NewBoard(''); b.SetCopperLayerCount(6)
    for layer,name in ((pcbnew.F_Cu,'F.Cu'),(pcbnew.In1_Cu,'In1.GND'),(pcbnew.In2_Cu,'In2.PWR'),(pcbnew.In3_Cu,'In3.PWR12V'),(pcbnew.In4_Cu,'In4.GND'),(pcbnew.B_Cu,'B.Cu')): b.SetLayerName(layer,name)
    all_names=[]
    for p in template.Pads():
        name=p.GetNetname() or f'unconnected-(J7-Pad{p.GetNumber()})'
        if name not in all_names: all_names.append(name)
    nets={name:pcbnew.NETINFO_ITEM(b,name) for name in all_names}
    for n in nets.values(): b.Add(n)
    f=pcbnew.FOOTPRINT(template)
    f.SetReference('J7'); f.SetPosition(V(35,130)); f.SetOrientationDegrees(0); b.Add(f)
    for p in template.Pads():
        q=f.FindPadByNumber(p.GetNumber()); name=p.GetNetname() or f'unconnected-(J7-Pad{p.GetNumber()})'; q.SetNet(nets[name])
    # Boundary PTH pads provide explicit, inspectable launch endpoints.
    bf=pcbnew.PCB_IO_KICAD_SEXPR().FootprintLoad(str(ROOT/'PiSXMe_RevA_Clean.pretty'),'J7_LAUNCH_BOUNDARY')
    if bf is None: raise RuntimeError('boundary footprint load failed')
    bf.SetReference('J7_BOUNDARY'); bf.SetPosition(V(0,0)); b.Add(bf)
    exits={}
    left_ep={3:(10.0,90.0),5:(12.0,92.0),9:(14.0,94.0),11:(16.0,96.0)}
    right_ep={4:(90.0,90.0),6:(92.0,92.0),10:(94.0,94.0),12:(96.0,96.0)}
    for index,(number,name) in enumerate(MDI.items()):
        jp=f.FindPadByNumber(str(number)); p=jp.GetPosition(); x,y=pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
        ep=left_ep[number] if number in left_ep else right_ep[number]; pad=bf.FindPadByNumber(str(number)); pad.SetPosition(V(*ep)); pad.SetNet(nets[name]); exits[name]=(x,y,ep)
    # Left CM5 source group escapes on B.Cu. Right group crosses to F.Cu
    # immediately outside the source pads, then escapes west; this clears
    # the opposing B.Cu pad field without routing through it.
    for number,name in MDI.items():
        x,y,ep=exits[name]; n=nets[name]
        if number in (3,5,9,11):
            track(b,n,(x,y),ep,pcbnew.B_Cu)
        else:
            idx={4:0,6:1,10:2,12:3}[number]; lane=38.0+0.8*idx; track(b,n,(x,y),(lane,y),pcbnew.B_Cu); track(b,n,(lane,y),(lane,75.0),pcbnew.B_Cu); track(b,n,(lane,75.0),ep,pcbnew.B_Cu)
    x0,y0,x1,y1=5,80,100,145
    for a,z in (((x0,y0),(x1,y0)),((x1,y0),(x1,y1)),((x1,y1),(x0,y1)),((x0,y1),(x0,y0))): edge(b,a,z)
    b.Save(str(OUT)); print('saved',OUT)
if __name__=='__main__': main()
