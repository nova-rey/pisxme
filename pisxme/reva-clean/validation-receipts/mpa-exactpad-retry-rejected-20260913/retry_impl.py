from pathlib import Path
import pcbnew, sys, json
R=Path('/workspace/project/pisxme/reva-clean')
BASE=R/'PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb'
OUT=R/'PHASE24_MPA_STORAGE_POWER_EXACTPAD_CANDIDATE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=pcbnew.FromMM(0.20); W_FINE=pcbnew.FromMM(0.10); VIA_W=pcbnew.FromMM(0.50); VIA_D=pcbnew.FromMM(0.30)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return (pcbnew.ToMM(p.x),pcbnew.ToMM(p.y))
def fp(r):
 f=board.FindFootprintByReference(r)
 if f is None: raise RuntimeError('missing '+r)
 return f
def pad(r,n):
 p=fp(r).FindPadByNumber(str(n))
 if p is None: raise RuntimeError(f'missing pad {r}.{n}')
 return p
def pxy(r,n): return xy(pad(r,n).GetPosition())
def net(name):
 n=board.FindNet(name)
 if n is None: raise RuntimeError('missing net '+name)
 return n
def seg(n,a,z,layer=F,w=W):
 t=pcbnew.PCB_TRACK(board); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer); t.SetWidth(w); t.SetNet(n); t.SetNetCode(n.GetNetCode()); board.Add(t)
def path(n,pts,layer=F,w=W):
 for a,z in zip(pts,pts[1:]): seg(n,a,z,layer,w)
def via(n,p):
 v=pcbnew.PCB_VIA(board); v.SetPosition(V(*p)); v.SetWidth(VIA_W); v.SetDrill(VIA_D); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); board.Add(v)
def launch(n,r,num,v,layer=F,w=W_FINE):
 seg(n,pxy(r,num),v,layer,w); via(n,v)
def land(n,v,r,num,layer=F,w=W_FINE):
 via(n,v); seg(n,v,pxy(r,num),layer,w)

def move():
 for r,(x,y,rot) in {'U13':(180,135,180),'C30':(103.5,116,180),'C32':(103.5,120,180),'C33':(103.5,128,180),'C31':(103.5,132,180),'F2':(90,60,0),'D2':(110,60,0)}.items():
  f=fp(r); f.SetPosition(V(x,y)); f.SetOrientationDegrees(rot)

def group_bridge():
 # Each U7/cap pair has its own vias and B.Cu corridor; endpoints use native pad centers.
 defs=[
  ('BRIDGE_SATA_TX_P','U7','57','C30','2',(92,124),(100,115),[(92,124),(96,124),(100,124),(100,115)]),
  ('BRIDGE_SATA_TX_N','U7','56','C31','2',(92,126),(101,132),[(92,126),(97,126),(101,126),(101,132)]),
  ('BRIDGE_SATA_RX_P','U7','60','C32','2',(92,130),(100,120),[(92,130),(96,130),(100,130),(100,120)]),
  ('BRIDGE_SATA_RX_N','U7','59','C33','2',(92,132),(101,128),[(92,132),(97,132),(101,132),(101,128)]),]
 for name,sr,sn,dr,dn,v0,v1,pts in defs:
  n=net(name); launch(n,sr,sn,v0); path(n,pts,B,W); land(n,v1,dr,dn)

def group_usb():
 # Coupling caps to U13 Port-B; four independent through-via endpoints.
 defs=[
  ('TUSB_SATA_TXP','C30','1','U13','38',(106,116),(175.5,139),[(106,116),(135,116),(160,120),(175.5,139)]),
  ('TUSB_SATA_TXN','C31','1','U13','37',(107,132),(174,141),[(107,132),(135,132),(158,128),(174,141)]),
  ('TUSB_SATA_RXP','C32','1','U13','36',(106,120),(172.5,143),[(106,120),(135,120),(157,136),(172.5,143)]),
  ('TUSB_SATA_RXN','C33','1','U13','35',(107,128),(171,145),[(107,128),(135,128),(156,140),(171,145)]),]
 for name,sr,sn,dr,dn,v0,v1,pts in defs:
  n=net(name); launch(n,sr,sn,v0); path(n,pts,B,W); land(n,v1,dr,dn)

def group_porta():
 # Four U13 Port-A pads fan out to unique east vias and ordered B.Cu corridors to J3.
 defs=[
  ('M2_SATA_A_P_PCIE_TXP0','2','49',(184.5,137.8),(218,151),[(184.5,137.8),(194,137.8),(207,145),(218,151)]),
  ('M2_SATA_A_N_PCIE_TXN0','3','47',(184.5,139.8),(218,153),[(184.5,139.8),(195,139.8),(208,147),(218,153)]),
  ('M2_SATA_B_P_PCIE_RXN0','6','41',(184.5,141.8),(218,155),[(184.5,141.8),(196,141.8),(209,149),(218,155)]),
  ('M2_SATA_B_N_PCIE_RXP0','7','43',(184.5,143.8),(218,157),[(184.5,143.8),(197,143.8),(210,151),(218,157)]),]
 for name,un,jp,v0,v1,pts in defs:
  n=net(name); launch(n,'U13',un,v0); path(n,pts,B,W); land(n,v1,'J3',jp)

def group_control():
 # Correct control contracts: STORAGE_SEL is U12.9/U13.9/U14.4;
 # AUTO_PEDET is J3.69/J8.2; U14.2 is MODE_IN and routes to J8.4.
 n=net('STORAGE_SEL')
 v0=(162,138); v1=(184,133); v2=(213,151)
 launch(n,'U12','9',v0); path(n,[v0,(170,138),(180,145),(200,145),(213,151)],B,W); land(n,v2,'U14','4'); launch(n,'U13','9',v1); path(n,[v1,(190,133),(200,140),(200,145)],B,W)
 n=net('AUTO_PEDET'); v0=(230,158); v1=(244,150)
 launch(n,'J3','69',v0); path(n,[v0,(236,158),(244,150)],B,W); land(n,v1,'J8','2')
 n=net('MODE_IN'); v0=(207,152); v1=(244,153)
 launch(n,'U14','2',v0); path(n,[v0,(220,152),(235,153),(244,153)],B,W); land(n,v1,'J8','4')

def group_power():
 # Branch-B PTH contact fields are native centers. Use only normal 0.20-mm copper;
 # no shared vias and no changes to existing GATE_B/12V_PROTECTED copper.
 n=net('12V_IN_B');
 # F2 input field
 f=[pxy('F2',str(i)) for i in range(1,5)]
 path(n,[f[0],f[1]],F,W); path(n,[f[1],f[3]],F,W); path(n,[f[0],f[2]],F,W); path(n,[f[2],f[3]],F,W)
 path(n,[pxy('J6','1'),(60,45),(60,52),(f[0][0],f[0][1])],B,W)
 path(n,[f[0],(75,65),(55,75),(35,85),pxy('C4','2')],B,W)
 path(n,[(35,85),pxy('U2','3')],B,W)
 n=net('FUSED_12V_B'); f=[pxy('F2',str(i)) for i in range(5,9)]
 path(n,[f[0],f[1]],F,W); path(n,[f[1],f[3]],F,W); path(n,[f[0],f[2]],F,W); path(n,[f[2],f[3]],F,W)
 path(n,[f[0],pxy('D2','1')],F,W)
 path(n,[f[0],(100,68),(70,72),(45,82),pxy('U2','6')],B,W)
 path(n,[pxy('U2','6'),(45,95),pxy('Q2','1')],B,W)

board=pcbnew.LoadBoard(str(BASE))
if board is None: raise RuntimeError('load failed')
move()
g=int(sys.argv[1]) if len(sys.argv)>1 else 0
if g>=1: group_bridge()
if g>=2: group_usb()
if g>=3: group_porta()
if g>=4: group_control()
if g>=5: group_power()
board.BuildListOfNets(); board.Save(str(OUT)); print(str(OUT))
