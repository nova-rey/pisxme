"""Saved-board audit for the complete JMS583 support field.

Connectivity is derived from KiCad's native pads/tracks/vias only.  The
negative control removes every authored support track and must fail.
"""
from pathlib import Path
import os
import pcbnew

R=Path(__file__).resolve().parent
PCB=R/os.environ.get('PISXME_COMPLETE_SUPPORT_AUDIT_PCB','PHASE24_DUAL_MODE_STORAGE_NC39_QFN_ESCAPE_REPAIR_V3.kicad_pcb')
NEG=R/os.environ.get('PISXME_COMPLETE_SUPPORT_AUDIT_NEG','PHASE24_DUAL_MODE_STORAGE_NC39_QFN_ESCAPE_REPAIR_V3_NEGATIVE.kicad_pcb')
PAIRS=[
 ('JMS_REXT','U11','39','R80','1'), ('XIN','U11','50','Y10','1'),
 ('XOUT','U11','51','Y10','2'), ('JMS_RESET_N','U11','15','R81','1'),
 ('JMS_AVDD33','U11','19','C80','1'), ('JMS_AVDDL','U11','20','C83','1'),
 ('JMS_VCCO','U11','6','C81','1'), ('JMS_VCCK','U11','2','C82','1'),
 ('JMS_VDDREG_5V','U11','1','L10','2'), ('LXO','U11','64','L10','1'),
]
def conn(b,a,z):
 b.BuildConnectivity(); return z in b.GetConnectivity().GetConnectedItems(a)
b=pcbnew.LoadBoard(str(PCB));u=b.FindFootprintByReference('U11')
checks=[]
for name,ra,pa,rb,pb in PAIRS:
 a=b.FindFootprintByReference(ra).FindPadByNumber(pa);z=b.FindFootprintByReference(rb).FindPadByNumber(pb)
 if a is None or z is None or a.GetNetname()!=name or z.GetNetname()!=name: raise SystemExit('FAIL endpoint authority '+name)
 checks.append((a,z))
if not all(conn(b,a,z) for a,z in checks): raise SystemExit('FAIL complete JMS583 support connectivity')
codes={b.FindNet(name).GetNetCode() for name,*_ in PAIRS}
for item in list(b.GetTracks()):
 if item.GetNetCode() in codes:b.RemoveNative(item)
if any(conn(b,a,z) for a,z in checks): raise SystemExit('FAIL complete support negative control')
b.Save(str(NEG));print('PASS complete JMS583 support connectivity; PASS trace-removal negative control')
