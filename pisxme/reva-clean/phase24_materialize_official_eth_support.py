"""Materialize the production Ethernet support on the official MDI candidate."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_OFFICIAL_ETH_TRANSPLANT_CORRECTED_BASIS.kicad_pcb'
OUT=R/'PHASE24_OFFICIAL_ETH_SUPPORT_MATERIALIZED.kicad_pcb'
LIB=R/'PiSXMe_RevA_Clean.pretty'
PARTS={
 'C48':('C_0603_1608Metric',{'1':'ETH_CT1','2':'ETH_CT_BRANCH_1'},(68,70)),
 'R26':('R_0402_1005Metric',{'1':'ETH_CT_BRANCH_1','2':'ETH_CT_COMMON'},(68,76)),
 'C49':('C_0603_1608Metric',{'1':'ETH_CT2','2':'ETH_CT_BRANCH_2'},(76,70)),
 'R27':('R_0402_1005Metric',{'1':'ETH_CT_BRANCH_2','2':'ETH_CT_COMMON'},(76,76)),
 'C50':('C_0603_1608Metric',{'1':'ETH_CT3','2':'ETH_CT_BRANCH_3'},(84,70)),
 'R28':('R_0402_1005Metric',{'1':'ETH_CT_BRANCH_3','2':'ETH_CT_COMMON'},(84,76)),
 'C51':('C_0603_1608Metric',{'1':'ETH_CT4','2':'ETH_CT_BRANCH_4'},(92,70)),
 'R29':('R_0402_1005Metric',{'1':'ETH_CT_BRANCH_4','2':'ETH_CT_COMMON'},(92,76)),
 'C52':('C_1206_3216Metric',{'1':'ETH_CT_COMMON','2':'GBE_SHIELD'},(76,84)),
 'R30':('R_0402_1005Metric',{'1':'ETH_LEDY','2':'GBE_LED_Y_K'},(68,84)),
 'R31':('R_0402_1005Metric',{'1':'ETH_LEDG','2':'GBE_LED_G_K'},(84,84)),
}
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def net(b,n):
 q=b.FindNet(n)
 if q is None:
  q=pcbnew.NETINFO_ITEM(b,n);q.SetNetCode(b.GetNetCount()+1);b.Add(q)
 return q
b=pcbnew.LoadBoard(str(BASE));io=pcbnew.PCB_IO_KICAD_SEXPR()
names={n for _,m,_ in PARTS.values() for n in m.values()}|{'ETH_POWER','GBE_LED_Y_A','GBE_LED_G_A'}
nets={n:net(b,n) for n in names}
j2=b.FindFootprintByReference('J2');j7=b.FindFootprintByReference('J7')
for pn,n in {'11':'ETH_CT1','12':'ETH_CT2','13':'ETH_CT3','14':'ETH_CT4','15':'GBE_LED_Y_A','16':'GBE_LED_Y_K','17':'GBE_LED_G_A','18':'GBE_LED_G_K','19':'GBE_SHIELD','20':'GBE_SHIELD'}.items():
 p=j2.FindPadByNumber(pn);p.SetNet(nets[n]);p.SetNetCode(nets[n].GetNetCode())
for pn,n in {'15':'ETH_LEDG','17':'ETH_LEDY'}.items():
 p=j7.FindPadByNumber(pn);p.SetNet(nets[n]);p.SetNetCode(nets[n].GetNetCode())
for ref,(lib,m,pos) in PARTS.items():
 f=io.FootprintLoad(str(LIB),lib);f.SetReference(ref);f.SetLayer(pcbnew.B_Cu);f.SetPosition(V(*pos));b.Add(f)
 layers=pcbnew.LSET();layers.AddLayer(pcbnew.B_Cu);layers.AddLayer(pcbnew.B_Mask);layers.AddLayer(pcbnew.B_Paste)
 for p in f.Pads():
  n=nets[m[str(p.GetNumber())]];p.SetLayerSet(layers);p.SetNet(n);p.SetNetCode(n.GetNetCode())
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
