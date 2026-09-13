from pathlib import Path
import pcbnew
R=Path('/workspace/project/pisxme/reva-clean')
BASE=R/'PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb'
OUT=R/'PHASE24_MPA_STORAGE_POWER_REVISION_CANDIDATE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=pcbnew.FromMM(0.20); W_FINE=pcbnew.FromMM(0.10); W_PWR=pcbnew.FromMM(2.0)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def mm(p): return (pcbnew.ToMM(p.x),pcbnew.ToMM(p.y))
def fp(r):
 f=board.FindFootprintByReference(r)
 if f is None: raise RuntimeError('missing footprint '+r)
 return f
def pad(r,n):
 p=fp(r).FindPadByNumber(str(n))
 if p is None: raise RuntimeError(f'missing pad {r}.{n}')
 return p
def pxy(r,n): return mm(pad(r,n).GetPosition())
def net(name):
 n=board.FindNet(name)
 if n is None: raise RuntimeError('missing net '+name)
 return n
def seg(n,a,z,layer=F,width=W):
 t=pcbnew.PCB_TRACK(board); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer); t.SetWidth(width); t.SetNet(n); t.SetNetCode(n.GetNetCode()); board.Add(t)
def path(n,pts,layer=F,width=W):
 for a,z in zip(pts,pts[1:]): seg(n,a,z,layer,width)
def via(n,p,width=.55,drill=.30):
 v=pcbnew.PCB_VIA(board); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(width)); v.SetDrill(pcbnew.FromMM(drill)); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); board.Add(v)
def pad_to(n,r,num,pts,layer=F,width=W): path(n,[pxy(r,num),*pts],layer,width)
board=pcbnew.LoadBoard(str(BASE))
if board is None: raise SystemExit('cannot load baseline')
# Binding MPA revision: only U13/coupling cohort/F2/D2 move.
for r,(x,y,rot) in {'U13':(180,135,180),'C30':(103.5,116,180),'C32':(103.5,120,180),'C33':(103.5,128,180),'C31':(103.5,132,180),'F2':(90,60,0),'D2':(110,60,0)}.items():
 f=fp(r); f.SetPosition(V(x,y)); f.SetOrientationDegrees(rot)
# U7 to coupling caps: exact pad launches, short F.Cu escapes, separated B.Cu lanes.
for name,up,cap,uv,lanes in [
 ('BRIDGE_SATA_TX_P','57','C30',(95.8,130.0),[(95.8,130.0),(97.0,130.0),(97.0,116.0),(102.0,116.0)]),
 ('BRIDGE_SATA_TX_N','56','C31',(96.2,133.0),[(96.2,133.0),(98.0,133.0),(98.0,136.0),(101.0,136.0),(101.0,132.0)]),
 ('BRIDGE_SATA_RX_P','60','C32',(94.6,132.0),[(94.6,132.0),(99.0,132.0),(99.0,120.0),(102.0,120.0)]),
 ('BRIDGE_SATA_RX_N','59','C33',(95.0,134.0),[(95.0,134.0),(100.0,134.0),(100.0,128.0),(102.0,128.0)])]:
 n=net(name); pad_to(n,'U7',up,[uv],F,W_FINE); via(n,uv); via_end=lanes[-1]; path(n,lanes,B,W); via(n,via_end); pad_to(n,cap,'2',[via_end],F,W_FINE)
# Cap to U13 Port-B. TX uses separated upper F.Cu channels; RX uses lower B.Cu channels.
# TXP all-F with a bounded dogleg; TXN transitions once outside fields to avoid a shared final crossing.
n=net('TUSB_SATA_TXP'); pad_to(n,'C30','1',[(108.0,110.0),(165.0,110.0),(174.0,120.0),(174.0,136.0),pxy('U13','38')],F,W)
n=net('TUSB_SATA_TXN'); pad_to(n,'C31','1',[(108.0,114.0)],F,W); via(n,(108.0,114.0)); path(n,[(108.0,114.0),(160.0,114.0),(172.0,124.0),(172.0,136.0),(177.0,137.8)],B,W); via(n,(177.0,137.8)); seg(n,(177.0,137.8),pxy('U13','37'),F,W_FINE)
# RX channels are lower B.Cu below U11/U12, then local top-side landings.
for name,cap,padnum,via0,pts,v1 in [
 ('TUSB_SATA_RXP','C32','1',(108.0,145.0),[(108.0,145.0),(160.0,145.0),(174.0,145.0),(177.0,137.4)],(177.0,137.4)),
 ('TUSB_SATA_RXN','C33','1',(108.0,147.0),[(108.0,147.0),(158.0,147.0),(171.0,142.0),(176.0,140.0),(177.0,137.0)],(177.0,137.0))]:
 n=net(name); pad_to(n,cap,padnum,[via0],F,W_FINE); via(n,via0); path(n,pts,B,W); via(n,v1); seg(n,v1,pxy('U13',{'TUSB_SATA_RXP':'36','TUSB_SATA_RXN':'35'}[name]),F,W_FINE)
# Port-A: four exact pad transitions and ordered, separated differential corridors to J3.
for name,un,jp,start,pts,final in [
 ('M2_SATA_A_P_PCIE_TXP0','2','49',(185.0,138.0),[(185.0,138.0),(188.0,138.0),(188.0,145.0),(207.0,145.0),(214.0,155.0)],(214.0,155.0)),
 ('M2_SATA_A_N_PCIE_TXN0','3','47',(185.0,137.0),[(185.0,137.0),(190.0,137.0),(190.0,147.0),(205.0,147.0),(213.0,154.0)],(213.0,154.0)),
 ('M2_SATA_B_P_PCIE_RXN0','6','41',(185.0,136.0),[(185.0,136.0),(192.0,136.0),(192.0,151.0),(203.0,151.0),(212.0,156.0)],(212.0,156.0)),
 ('M2_SATA_B_N_PCIE_RXP0','7',(43),(185.0,135.0),[(185.0,135.0),(194.0,135.0),(194.0,153.0),(201.0,153.0),(211.0,157.0)],(211.0,157.0))]:
 n=net(name); pad_to(n,'U13',un,[start],F,W_FINE); via(n,start); path(n,pts,B,W); via(n,final); seg(n,final,pxy('J3',jp),F,W_FINE)
# STORAGE_SEL dedicated east/lower control corridor: U12 -> branch -> U14/U13 exact pads.
n=net('STORAGE_SEL'); u12=pxy('U12','9'); u13=pxy('U13','9'); u14=pxy('U14','4')
pad_to(n,'U12','9',[(165.0,135.0),(165.0,140.0)],F,W_FINE); via(n,(165.0,140.0)); path(n,[(165.0,140.0),(180.0,140.0),(205.0,140.0),(205.0,147.0)],B,W); via(n,(205.0,147.0)); seg(n,(205.0,147.0),u14,F,W_FINE)
via(n,(180.0,140.0)); seg(n,(180.0,140.0),u13,F,W_FINE)
# AUTO_PEDET dedicated east control corridor.
n=net('AUTO_PEDET'); pad_to(n,'U14','2',[(207.0,150.0)],F,W_FINE); via(n,(207.0,150.0)); path(n,[(207.0,150.0),(216.0,150.0),(224.0,155.0)],B,W); via(n,(224.0,155.0)); seg(n,(224.0,155.0),pxy('J3','69'),F,W_FINE)
# Branch-B raw input: J6 -> F2 input field, then dedicated trunks to U2.3 and C4.2.
n=net('12V_IN_B'); j6=pxy('J6','1'); f21=pxy('F2','1'); u23=pxy('U2','3'); c42=pxy('C4','2')
pad_to(n,'J6','1',[(12.0,55.0)],F,W); via(n,(12.0,55.0)); path(n,[(12.0,55.0),(75.0,55.0),(80.0,55.0)],B,W); via(n,(80.0,55.0)); path(n,[(80.0,55.0),f21],B,W_PWR)
# F2 input through-pad field, local width where pad pitch requires it.
for num in ['2','3','4']: seg(n,pxy('F2',num),f21,F,W_PWR)
seg(n,f21,(80.0,55.0),F,W_PWR)
# U2.3 branch and C4.2 branch use local pad necks before the 2-mm trunk.
seg(n,u23,(25.0,92.0),F,W_FINE); via(n,(25.0,92.0)); path(n,[(25.0,92.0),(30.0,92.0),(30.0,55.0),(80.0,55.0)],B,W_PWR)
seg(n,c42,(15.8,87.0),F,W_FINE); via(n,(15.8,87.0)); path(n,[(15.8,87.0),(18.0,82.0),(30.0,70.0),(30.0,55.0)],B,W_PWR)
# Branch-B fused output: F2 -> D2 and separate west-side trunk to U2.6/Q2.1.
n=net('FUSED_12V_B'); f25=pxy('F2','5'); d21=pxy('D2','1'); u26=pxy('U2','6'); q21=pxy('Q2','1')
for num in ['6','7','8']: seg(n,pxy('F2',num),f25,F,W_PWR)
seg(n,f25,d21,F,W_PWR)
seg(n,f25,(100.0,55.0),F,W_PWR); via(n,(100.0,55.0)); path(n,[(100.0,55.0),(100.0,70.0),(40.0,70.0),(40.0,92.0)],B,W_PWR)
seg(n,u26,(24.0,92.0),F,W_FINE); via(n,(24.0,92.0)); path(n,[(24.0,92.0),(40.0,92.0)],B,W_PWR)
path(n,[(40.0,92.0),(40.0,104.0),(15.0,104.0)],B,W_PWR); seg(n,(15.0,104.0),(7.46,108.0),B,W_FINE)
# Preserve all existing 12V_PROTECTED/GATE_B copper; no GATE_B modification.
board.BuildListOfNets(); board.Save(str(OUT)); print(OUT)
