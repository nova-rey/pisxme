"""Audit the complete retained JMS583 support cohort after source co-authoring."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
PCB=R/'PHASE24_JMS583_THREE_EXIT_COAUTHOR.kicad_pcb'
NEG=R/'PHASE24_JMS583_FULL_SUPPORT_NEGATIVE.kicad_pcb'
PAIRS=(('U11','15','R81','1'),('U11','19','C80','1'),('U11','20','C83','1'),
 ('U11','6','C81','1'),('U11','2','C82','1'),('U11','1','L10','2'),
 ('U11','64','L10','1'),('U11','52','C84','1'),('U11','50','Y10','1'),
 ('U11','51','Y10','2'),('R81','1','C85','1'))
def joined(b):
 b.BuildConnectivity();c=b.GetConnectivity()
 return all(b.FindFootprintByReference(a).FindPadByNumber(ap) in c.GetConnectedItems(b.FindFootprintByReference(z).FindPadByNumber(zp)) for a,ap,z,zp in PAIRS)
b=pcbnew.LoadBoard(str(PCB))
if not joined(b): raise SystemExit('FAIL complete JMS583 support cohort')
for t in list(b.GetTracks()):
 if t.GetNetname()=='XIN': b.RemoveNative(t)
if joined(b): raise SystemExit('FAIL complete support negative control')
b.Save(str(NEG));print('PASS complete JMS583 support cohort; PASS trace-removal negative control')
