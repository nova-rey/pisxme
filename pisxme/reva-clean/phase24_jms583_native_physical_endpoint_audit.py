"""Verify JMS583 support endpoints using KiCad's saved-board connectivity."""
from pathlib import Path
import sys
import pcbnew
R=Path(__file__).resolve().parent
P=Path(sys.argv[1]) if len(sys.argv)>1 else R/'PHASE24_STORAGE_JMS583_CRYSTAL_VIAS_V23.kicad_pcb'
checks=[
 ('XIN','U11','50','Y10','1'),('XOUT','U11','51','Y10','2'),
 ('JMS_REXT','U11','39','R80','1'),('LXO','U11','64','L10','1'),
 ('JMS_VDDREG_5V','U11','1','L10','2'),('JMS_AVDD33','U11','19','C80','1'),
 ('JMS_AVDDL','U11','20','C83','1')]
b=pcbnew.LoadBoard(str(P)); b.BuildConnectivity(); c=b.GetConnectivity()
def pad(ref,num):
 f=b.FindFootprintByReference(ref)
 if f is None: raise RuntimeError('missing footprint '+ref)
 q=f.FindPadByNumber(num)
 if q is None: raise RuntimeError('missing pad '+ref+'.'+num)
 return q
def key(q): return (q.GetParentFootprint().GetReference(),str(q.GetNumber()))
failed=[]
for name,ra,pa,rb,pb in checks:
 a=pad(ra,pa); z=pad(rb,pb)
 if a.GetNetname()!=name or z.GetNetname()!=name:
  failed.append(name+': net ownership mismatch'); continue
 connected=[x for x in c.GetConnectedItems(a) if isinstance(x,pcbnew.PAD)]
 ok=key(z) in [key(x) for x in connected]
 print(name, 'PASS' if ok else 'FAIL', f'{ra}.{pa} <-> {rb}.{pb}')
 if not ok: failed.append(name+': disconnected')
if failed: raise SystemExit('FAIL native JMS583 physical endpoint audit: '+'; '.join(failed))
print('native JMS583 physical endpoint audit: PASS (%d/%d)'%(len(checks),len(checks)))
