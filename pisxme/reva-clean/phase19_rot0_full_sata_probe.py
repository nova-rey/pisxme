from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
src=R/'PHASE19_U7ROT0_USB_VERTICAL17.kicad_pcb'
out=R/'PHASE19_U7ROT0_USB_SATA_V1.kicad_pcb'
b=pcbnew.LoadBoard(str(src))
MM=pcbnew.FromMM
V=lambda x,y: pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def fp(ref): return b.FindFootprintByReference(ref)
def pd(f,n): return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def n(name):
    q=b.FindNet(name)
    if q is None:
        q=pcbnew.NETINFO_ITEM(b,name); q.SetNetCode(b.GetNetCount()+1); b.Add(q)
    return q
def setp(p,q): p.SetNet(q); p.SetNetCode(q.GetNetCode())
def seg(q,a,z,layer=pcbnew.F_Cu,w=.20):
    if a!=z:
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer); t.SetWidth(MM(w)); t.SetNet(q); b.Add(t)
def via(q,p):
    v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(MM(.50)); v.SetDrill(MM(.30)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(q); b.Add(v)

u,j=fp('U7'),fp('J3')
j.SetPosition(V(220,140)); j.SetOrientationDegrees(180)
names=[('TX_P','57','1','C30',pcbnew.F_Cu),('TX_N','56','2','C31',pcbnew.F_Cu),
       ('RX_P','60','3','C32',pcbnew.B_Cu),('RX_N','59','4','C33',pcbnew.B_Cu)]
caps={}
for ref,yy in zip(('C30','C31','C32','C33'),(116,120,124,128)):
    f=fp(ref); f.SetPosition(V(286,yy)); f.SetOrientationDegrees(0); caps[ref]=f

for suffix,up,jp,ref,layer in names:
    bridge=n('/STORAGE/BRIDGE_SATA_'+suffix)
    socket=n('/STORAGE/SATA_M2_'+suffix)
    cp1,cp2=xy(pd(caps[ref],'1')),xy(pd(caps[ref],'2'))
    ua,ja=xy(pd(u,up)),xy(pd(j,jp))
    setp(pd(u,up),bridge); setp(pd(caps[ref],'2'),bridge)
    setp(pd(caps[ref],'1'),socket); setp(pd(j,jp),socket)
    # Escape the dense serialized U7 bottom row vertically, then transition
    # on ordinary through-vias outside the SMD pad field.  The monotonic
    # B.Cu fanout prevents same-layer pad-field crossings.
    bv=(ua[0],114.0 + {'TX_P':0,'TX_N':1.5,'RX_P':3.0,'RX_N':4.5}[suffix])
    seg(bridge,ua,bv); via(bridge,bv); seg(bridge,bv,cp2,pcbnew.B_Cu)
    # Socket-side pair corridors: TX stays F.Cu, RX changes to B.Cu at
    # ordinary vias outside both the capacitor and M.2 SMD pads.
    if layer==pcbnew.F_Cu:
        y=145.275 if suffix=='TX_P' else 137.725
        x=240
        seg(socket,cp1,(x,cp1[1])); seg(socket,(x,cp1[1]),(x,y)); seg(socket,(x,y),(ja[0],y)); seg(socket,(ja[0],y),ja)
    else:
        cv=(cp1[0]-1.5,cp1[1]); via(socket,cv); seg(socket,cp1,cv)
        y=145.275 if suffix=='RX_P' else 137.725
        x=240
        seg(socket,cv,(x,cv[1]),pcbnew.B_Cu); seg(socket,(x,cv[1]),(x,y),pcbnew.B_Cu)
        jv=(234.0,y); seg(socket,(x,y),jv,pcbnew.B_Cu); via(socket,jv); seg(socket,jv,ja)

b.Save(str(out)); print(out)
