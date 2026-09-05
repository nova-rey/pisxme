"""Audit Ethernet connectivity from saved native KiCad copper only.

The mapping below is assertion-only. Edges come exclusively from KiCad's
BuildConnectivity result; the negative control removes a real connected track
and requires the audit to fail.
"""
from pathlib import Path
import sys
import pcbnew

R=Path(__file__).resolve().parent
DEFAULT=R/'PHASE24_CM5IO_SERIALIZED_MDI_PHASE24.kicad_pcb'
MAP={
 'CM5_GBE_TD0_P':('J7.12','U6.1','J2.1'), 'CM5_GBE_TD0_N':('J7.10','U6.2','J2.2'),
 'CM5_GBE_TD1_P':('J7.4','U6.5','J2.3'), 'CM5_GBE_TD1_N':('J7.6','U6.4','J2.6'),
 'CM5_GBE_TD2_P':('J7.11','U9.1','J2.7'), 'CM5_GBE_TD2_N':('J7.9','U9.2','J2.8'),
 'CM5_GBE_TD3_P':('J7.3','U9.5','J2.9'), 'CM5_GBE_TD3_N':('J7.5','U9.4','J2.10')}
def token(p): return f'{p.GetParentFootprint().GetReference()}.{p.GetNumber()}'
def pads(b): return {token(p):p for f in b.GetFootprints() for p in f.Pads()}
def audit(path):
 b=pcbnew.LoadBoard(str(path)); b.BuildConnectivity(); c=b.GetConnectivity(); ps=pads(b)
 for net,members in MAP.items():
  for m in members:
   if m not in ps: raise AssertionError(f'missing {m}')
   if ps[m].GetNetname().rsplit('/',1)[-1] != net: raise AssertionError(f'wrong net {m}')
  for m in members:
   got={token(x) for x in c.GetConnectedItems(ps[m]) if type(x).__name__=='PAD'}|{m}
   if not set(members)<=got: raise AssertionError(f'{net} disconnected at {m}: {sorted(got & set(members))}')
 return b
def sig(x): return (x.GetNetCode(),int(x.GetLayer()),x.GetStart().x,x.GetStart().y,x.GetEnd().x,x.GetEnd().y,x.GetWidth())
def negative(path):
 b=audit(path); b.BuildConnectivity(); ps=pads(b)
 for m in MAP['CM5_GBE_TD0_P']:
  for x in b.GetConnectivity().GetConnectedItems(ps[m]):
   if type(x).__name__!='PCB_TRACK': continue
   wanted=sig(x); t=pcbnew.LoadBoard(str(path)); victim=next((y for y in t.GetTracks() if type(y).__name__=='PCB_TRACK' and sig(y)==wanted),None)
   if victim is None: continue
   t.RemoveNative(victim)
   try: audit_board(t)
   except AssertionError: return {'removed_member':m,'track_removal_fails':True}
 raise AssertionError('negative control found no necessary track')
def audit_board(b):
 b.BuildConnectivity(); c=b.GetConnectivity(); ps=pads(b)
 for members in MAP.values():
  for m in members:
   got={token(x) for x in c.GetConnectedItems(ps[m]) if type(x).__name__=='PAD'}|{m}
   if not set(members)<=got: raise AssertionError(m)
if __name__=='__main__':
 p=Path(sys.argv[1]) if len(sys.argv)>1 else DEFAULT
 audit(p); print('Phase24 Ethernet native connectivity: PASS')
 if len(sys.argv)>2 and sys.argv[2]=='--negative-controls': print('negative controls:',negative(p))
