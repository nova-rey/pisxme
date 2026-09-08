"""Audit the co-authored JMS583 analog/crystal source-field cohort."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
PCB=R/'PHASE24_JMS583_THREE_EXIT_COAUTHOR.kicad_pcb'
NEG=R/'PHASE24_JMS583_THREE_EXIT_COAUTHOR_NEGATIVE.kicad_pcb'
PAIRS=(('U11','50','Y10','1'),('U11','51','Y10','2'),('U11','52','C84','1'))
def ok(b):
 b.BuildConnectivity();c=b.GetConnectivity()
 return all(b.FindFootprintByReference(fa).FindPadByNumber(pa) in c.GetConnectedItems(b.FindFootprintByReference(fb).FindPadByNumber(pb)) for fa,pa,fb,pb in PAIRS)
b=pcbnew.LoadBoard(str(PCB))
if not ok(b): raise SystemExit('FAIL co-authored XIN/XOUT/XAVDDH connectivity')
for t in list(b.GetTracks()):
 if t.GetNetname() in ('XIN','XOUT','JMS_XAVDDH'): b.RemoveNative(t)
if ok(b): raise SystemExit('FAIL co-authored source-field negative control')
b.Save(str(NEG));print('PASS co-authored XIN/XOUT/XAVDDH; PASS trace-removal negative control')
