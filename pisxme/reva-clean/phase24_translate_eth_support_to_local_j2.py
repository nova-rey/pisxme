"""Translate CM5IO support copper from oracle J2 to the saved local J2."""
from pathlib import Path
import os
import pcbnew

R=Path(__file__).resolve().parent
BASE=Path(os.environ.get('PISXME_ETH_SUPPORT_BASE', str(R/'PHASE24_SELECTED_MACRO_ETH_SUPPORT_V15.kicad_pcb')))
OUT=Path(os.environ.get('PISXME_ETH_SUPPORT_OUT', str(R/'PHASE24_SELECTED_MACRO_ETH_SUPPORT_V15_LOCAL.kicad_pcb')))
ORACLE_J2=(77.5,53.0)
extra_x, extra_y = (float(v) for v in os.environ.get('PISXME_ETH_SUPPORT_EXTRA_SHIFT', '0,0').split(','))
SUPPORT_REFS={'C48','C49','C50','C51','C52','R26','R27','R28','R29'}
SUPPORT_NETS={'/ETHERNET/ETH_CT1','/ETHERNET/ETH_CT2','/ETHERNET/ETH_CT3','/ETHERNET/ETH_CT4','/ETHERNET/ETH_CT_BRANCH_1','/ETHERNET/ETH_CT_BRANCH_2','/ETHERNET/ETH_CT_BRANCH_3','/ETHERNET/ETH_CT_BRANCH_4','/ETHERNET/ETH_CT_COMMON','/ETHERNET/GBE_SHIELD'}
def mm(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
b=pcbnew.LoadBoard(str(BASE)); j2=b.FindFootprintByReference('J2'); local=xy(j2.GetPosition()); dx,dy=local[0]-ORACLE_J2[0]+extra_x,local[1]-ORACLE_J2[1]+extra_y
for ref in SUPPORT_REFS:
 f=b.FindFootprintByReference(ref)
 if f: x,y=xy(f.GetPosition()); f.SetPosition(mm(x+dx,y+dy))
for item in b.GetTracks():
 if item.GetNetname() not in SUPPORT_NETS: continue
 if isinstance(item,pcbnew.PCB_VIA):
  x,y=xy(item.GetPosition()); item.SetPosition(mm(x+dx,y+dy))
 else:
  x,y=xy(item.GetStart()); item.SetStart(mm(x+dx,y+dy)); x,y=xy(item.GetEnd()); item.SetEnd(mm(x+dx,y+dy))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT,'delta',dx,dy)
