"""Saved-board U1.52 support-clear RTL_3V3 placement audit."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;PCB=H/'PHASE24_RTL9210B_V876_3V3_U152_SUPPORT_CLEAR_V879.kicad_pcb';ENDS=(('U1','52'),('U1','39'),('U2','3'),('U2','8'),('C3','1'))
def pads(b):return{(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p):return(p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p):b.BuildConnectivity();return{key(x)for x in b.GetConnectivity().GetConnectedItems(p)if type(x).__name__ in ('PAD','PCB_PAD')}
b=pcbnew.LoadBoard(str(PCB));p=pads(b);assert all(e in p and p[e].GetNetname()=='RTL_3V3'for e in ENDS);assert all(e in(reach(b,p[ENDS[0]])|{ENDS[0]})for e in ENDS);print('RTL_3V3 U1.52/U1.39/U2.3/U2.8/C3.1: PASS')
b=pcbnew.LoadBoard(str(PCB));q=pads(b);victim=next(x for x in b.GetTracks()if x.GetNetname()=='RTL_3V3'and x.GetStart()==pcbnew.VECTOR2I_MM(94.8,73.95));b.RemoveNative(victim);assert ENDS[4] not in(reach(b,q[ENDS[0]])|{ENDS[0]});print('RTL_3V3 negative control: PASS')
