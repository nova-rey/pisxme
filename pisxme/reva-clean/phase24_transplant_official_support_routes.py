"""Transplant complete CM5IO support geometry onto the official-placement PCB."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_OFFICIAL_ETH_TRANSPLANT_CORRECTED_BASIS.kicad_pcb'
ORACLE=R/'CM5IO_DIRECT_J7_ETHERNET_FIXTURE.kicad_pcb'
OUT=R/'PHASE24_OFFICIAL_ETH_FULL_SUPPORT_ROUTE.kicad_pcb'
LIB=R/'PiSXMe_RevA_Clean.pretty'
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def ensure(b,n):
 q=b.FindNet(n)
 if q is None: q=pcbnew.NETINFO_ITEM(b,n);q.SetNetCode(b.GetNetCount()+1);b.Add(q)
 return q
def target_net(name):
 if name=='ETH_GND': return 'POWER_GND'
 if name=='GBE_SHIELD': return '/ETHERNET/GBE_SHIELD'
 if name.startswith('ETH_CT') or name.startswith('ETH_CT_BRANCH_'): return '/ETHERNET/'+name
 return None
b=pcbnew.LoadBoard(str(BASE));o=pcbnew.LoadBoard(str(ORACLE));io=pcbnew.PCB_IO_KICAD_SEXPR()
part_map={'CCT1':('C48','C_0603_1608Metric'),'RCT1':('R26','R_0402_1005Metric'),
          'CCT2':('C49','C_0603_1608Metric'),'RCT2':('R27','R_0402_1005Metric'),
          'CCT3':('C50','C_0603_1608Metric'),'RCT3':('R28','R_0402_1005Metric'),
          'CCT4':('C51','C_0603_1608Metric'),'RCT4':('R29','R_0402_1005Metric'),
          'CCT':('C52','C_1206_3216Metric')}
names=set()
for sf, (ref,lib) in part_map.items():
 old=b.FindFootprintByReference(ref)
 if old is not None: b.Remove(old)
 src=o.FindFootprintByReference(sf); q=src.GetPosition()
 f=io.FootprintLoad(str(LIB),lib);f.SetReference(ref);f.SetPosition(q);f.SetOrientationDegrees(src.GetOrientationDegrees());f.SetLayer(pcbnew.B_Cu);b.Add(f)
 if lib.startswith('C_0603'): mapping={'1':'/ETHERNET/ETH_CT'+sf[-1] if sf!='CCT' else '/ETHERNET/ETH_CT_COMMON','2':'/ETHERNET/ETH_CT_BRANCH_'+sf[-1] if sf!='CCT' else '/ETHERNET/GBE_SHIELD'}
 elif sf.startswith('RCT'): mapping={'1':'/ETHERNET/ETH_CT_BRANCH_'+sf[-1],'2':'/ETHERNET/ETH_CT_COMMON'}
 else: mapping={'1':'/ETHERNET/ETH_CT_COMMON','2':'/ETHERNET/GBE_SHIELD'}
 layers=pcbnew.LSET();layers.AddLayer(pcbnew.B_Cu);layers.AddLayer(pcbnew.B_Mask);layers.AddLayer(pcbnew.B_Paste)
 for p in f.Pads():
  n=ensure(b,mapping[str(p.GetNumber())]);p.SetLayerSet(layers);p.SetNet(n);p.SetNetCode(n.GetNetCode());names.add(n.GetNetname())
# Copy support tracks only; MDI remains the already width-corrected target
# geometry. Source geometry is native and exact; target net names are mapped.
for item in o.GetTracks():
 src=item.GetNetname(); tn=target_net(src)
 if tn is None: continue
 net=ensure(b,tn)
 if isinstance(item,pcbnew.PCB_VIA):
  v=pcbnew.PCB_VIA(b);v.SetPosition(item.GetPosition());v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(net);b.Add(v)
 else:
  t=pcbnew.PCB_TRACK(b);t.SetStart(item.GetStart());t.SetEnd(item.GetEnd());t.SetLayer(item.GetLayer());t.SetWidth(max(item.GetWidth(),pcbnew.FromMM(.2)));t.SetNet(net);b.Add(t)
# Establish the production connector-side support net ownership.
j2=b.FindFootprintByReference('J2');j7=b.FindFootprintByReference('J7')
for pn,n in {'11':'/ETHERNET/ETH_CT1','12':'/ETHERNET/ETH_CT2','13':'/ETHERNET/ETH_CT3','14':'/ETHERNET/ETH_CT4','15':'/ETHERNET/ETH_POWER','16':'/ETHERNET/GBE_LED_Y_K','17':'/ETHERNET/ETH_POWER','18':'/ETHERNET/GBE_LED_G_K','19':'/ETHERNET/GBE_SHIELD','20':'/ETHERNET/GBE_SHIELD'}.items():
 q=ensure(b,n);p=j2.FindPadByNumber(pn);p.SetNet(q);p.SetNetCode(q.GetNetCode())
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
