"""Native connectivity audit for the official-placement Ethernet oracle.

Assertions describe required pad memberships only. Connectivity edges are
derived exclusively from KiCad's saved pads/tracks/vias/zones. The negative
control removes one real CT trace and requires the audit to fail.
"""
from pathlib import Path
import pcbnew
import sys

R=Path(__file__).resolve().parent
DEFAULT=R/'PHASE24_OFFICIAL_ETH_FULL_SUPPORT_ROUTE.kicad_pcb'
EXPECTED={
 'CM5_GBE_TD0_P':('J7.12','U6.1','J2.1'), 'CM5_GBE_TD0_N':('J7.10','U6.2','J2.2'),
 'CM5_GBE_TD1_P':('J7.4','U6.5','J2.3'), 'CM5_GBE_TD1_N':('J7.6','U6.4','J2.6'),
 'CM5_GBE_TD2_P':('J7.11','U9.1','J2.7'), 'CM5_GBE_TD2_N':('J7.9','U9.2','J2.8'),
 'CM5_GBE_TD3_P':('J7.3','U9.5','J2.9'), 'CM5_GBE_TD3_N':('J7.5','U9.4','J2.10'),
 '/ETHERNET/ETH_CT1':('J2.11','C48.1'), '/ETHERNET/ETH_CT2':('J2.12','C49.1'),
 '/ETHERNET/ETH_CT3':('J2.13','C50.1'), '/ETHERNET/ETH_CT4':('J2.14','C51.1'),
 '/ETHERNET/ETH_CT_BRANCH_1':('C48.2','R26.1'), '/ETHERNET/ETH_CT_BRANCH_2':('C49.2','R27.1'),
 '/ETHERNET/ETH_CT_BRANCH_3':('C50.2','R28.1'), '/ETHERNET/ETH_CT_BRANCH_4':('C51.2','R29.1'),
 '/ETHERNET/ETH_CT_COMMON':('C52.1','R26.2','R27.2','R28.2','R29.2'),
 '/ETHERNET/GBE_SHIELD':('J2.19','J2.20','C52.2'),
}
def token(p): return p.GetParentFootprint().GetReference()+'.'+p.GetNumber()
def audit_board(b):
 b.BuildConnectivity(); c=b.GetConnectivity()
 pads={token(p):p for f in b.GetFootprints() for p in f.Pads()}
 for net,members in EXPECTED.items():
  for m in members:
   assert m in pads, (net,m)
   assert pads[m].GetNetname()==net or pads[m].GetNetname().rsplit('/',1)[-1]==net.rsplit('/',1)[-1], (net,m,pads[m].GetNetname())
  for m in members:
   got={token(x) for x in c.GetConnectedItems(pads[m]) if type(x).__name__=='PAD'}|{m}
   assert set(members)<=got, (net,m,sorted(got&set(members)))
def audit(path):
 b=pcbnew.LoadBoard(str(path)); audit_board(b); return b
def negative(path):
 b=audit(path)
 victim=next((x for x in b.GetTracks() if x.GetNetname()=='/ETHERNET/ETH_CT1'),None)
 assert victim is not None, 'no real CT1 track found'
 b.RemoveNative(victim); b.BuildConnectivity()
 try: audit_board(b)
 except AssertionError: return True
 raise AssertionError('negative control unexpectedly passed after removing CT1 trace')
if __name__=='__main__':
 p=Path(sys.argv[1]) if len(sys.argv)>1 else DEFAULT
 audit(p); print('Phase24 official Ethernet full native connectivity: PASS')
 print('negative_control_removed_real_CT1_trace:',negative(p))
