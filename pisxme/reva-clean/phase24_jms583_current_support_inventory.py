"""Inventory native support-net endpoint connectivity on the live basis."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; P=R/'PHASE24_DUAL_MODE_STORAGE_FULL7_VCCK_F_center.kicad_pcb'
PAIRS=[('JMS_REXT','U11','39','R80','1'),('XIN','U11','50','Y10','1'),('XOUT','U11','51','Y10','2'),('JMS_RESET_N','U11','15','R81','1'),('JMS_AVDD33','U11','19','C80','1'),('JMS_AVDDL','U11','20','C83','1'),('JMS_VCCO','U11','6','C81','1'),('JMS_VCCK','U11','2','C82','1'),('JMS_VDDREG_5V','U11','1','L10','2'),('LXO','U11','64','L10','1')]
b=pcbnew.LoadBoard(str(P));b.BuildConnectivity();c=b.GetConnectivity()
for name,ra,pa,rb,pb in PAIRS:
 a=b.FindFootprintByReference(ra).FindPadByNumber(pa);z=b.FindFootprintByReference(rb).FindPadByNumber(pb)
 print(f'{name}: {"CONNECTED" if z in c.GetConnectedItems(a) else "OPEN"}; tracks={sum(1 for t in b.GetTracks() if t.GetNetCode()==a.GetNetCode())}')
