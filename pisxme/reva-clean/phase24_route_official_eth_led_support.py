"""Add and route the production CM5/J2 Ethernet LED support on the oracle."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_OFFICIAL_ETH_FULL_SUPPORT_ROUTE.kicad_pcb'
OUT=R/'PHASE24_OFFICIAL_ETH_COMPLETE_SUPPORT_ROUTE.kicad_pcb'
LIB=R/'PiSXMe_RevA_Clean.pretty'
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def ensure(b,n):
 q=b.FindNet(n)
 if q is None: q=pcbnew.NETINFO_ITEM(b,n);q.SetNetCode(b.GetNetCount()+1);b.Add(q)
 return q
def P(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def seg(b,net,a,z,layer=pcbnew.B_Cu):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(layer);t.SetWidth(pcbnew.FromMM(.20));t.SetNet(net);b.Add(t)
def via(b,net,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(net);b.Add(v)
b=pcbnew.LoadBoard(str(BASE));io=pcbnew.PCB_IO_KICAD_SEXPR()
nets={n:ensure(b,n) for n in ('ETH_LEDY','ETH_LEDG','/ETHERNET/GBE_LED_Y_K','/ETHERNET/GBE_LED_G_K','ETH_POWER')}
j2=b.FindFootprintByReference('J2');j7=b.FindFootprintByReference('J7')
# Physical EDAC aliases: schematic LEDY_K pin14→physical pad16 and LEDG_K
# pin16→physical pad18; anodes/power are physical pads15/17.
for pn,n in {'15':'ETH_POWER','16':'/ETHERNET/GBE_LED_Y_K','17':'ETH_POWER','18':'/ETHERNET/GBE_LED_G_K'}.items():
 p=P(b,'J2',pn);p.SetNet(nets[n]);p.SetNetCode(nets[n].GetNetCode())
for pn,n in {'15':'ETH_LEDG','17':'ETH_LEDY'}.items():
 p=P(b,'J7',pn);p.SetNet(nets[n]);p.SetNetCode(nets[n].GetNetCode())
for ref,x,y in [('R30',24,106),('R31',20,106)]:
 f=io.FootprintLoad(str(LIB),'R_0402_1005Metric');f.SetReference(ref);f.SetPosition(V(x,y));f.SetLayer(pcbnew.F_Cu);b.Add(f)
 f.SetOrientationDegrees(90)
 layers=pcbnew.LSET();layers.AddLayer(pcbnew.F_Cu);layers.AddLayer(pcbnew.F_Mask);layers.AddLayer(pcbnew.F_Paste)
 for p in f.Pads(): p.SetLayerSet(layers)
P(b,'R30','1').SetNet(nets['ETH_LEDY']);P(b,'R30','1').SetNetCode(nets['ETH_LEDY'].GetNetCode());P(b,'R30','2').SetNet(nets['/ETHERNET/GBE_LED_Y_K']);P(b,'R30','2').SetNetCode(nets['/ETHERNET/GBE_LED_Y_K'].GetNetCode())
P(b,'R31','1').SetNet(nets['ETH_LEDG']);P(b,'R31','1').SetNetCode(nets['ETH_LEDG'].GetNetCode());P(b,'R31','2').SetNet(nets['/ETHERNET/GBE_LED_G_K']);P(b,'R31','2').SetNetCode(nets['/ETHERNET/GBE_LED_G_K'].GetNetCode())
# Keep the two source launches on separate ordinary B.Cu corridors after
# explicit F.Cu-to-B.Cu vias outside the J7 pad field.
for name,src,ref,via_xy,pts in [
 ('ETH_LEDY','17',( 'R30'),(0,0),[(32.96,101.9),(30,101.9),(27,104),(24,105.5)]),
 ('ETH_LEDG','15',( 'R31'),(0,0),[(32.96,101.5),(29,101.5),(24,102),(20,105.5)])]:
 net=nets[name];last=xy(P(b,'J7',src))
 for q in pts[1:]:seg(b,net,last,q,pcbnew.F_Cu);last=q
# Connector cathodes use distinct launch heights to avoid a crossing at J2.
for name,pn,ref,via_xy,pts in [
    ('/ETHERNET/GBE_LED_Y_K','16','R30',(27,109),[(81.59,48.94),(79,48.94),(79,45),(10,45),(10,109)]),
    ('/ETHERNET/GBE_LED_G_K','18','R31',(23,109),[(70.87,48.94),(68,48.94),(68,40),(8,40),(8,109)])]:
    net=nets[name];last=xy(P(b,'J2',pn));z=xy(P(b,ref,'2'));via(b,net,via_xy)
    seg(b,net,last,pts[1],pcbnew.F_Cu);last=pts[1]
    for q in pts[2:]:seg(b,net,last,q,pcbnew.B_Cu);last=q
    seg(b,net,last,via_xy,pcbnew.B_Cu)
    seg(b,net,via_xy,z,pcbnew.F_Cu)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
