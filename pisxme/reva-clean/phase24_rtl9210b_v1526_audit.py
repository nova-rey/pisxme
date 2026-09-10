"""Saved-board native audits for V1526 crystal and U1.52 rail changes."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_XTALOUT_FCU_C2_DOGBONE_V1526.kicad_pcb'
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def key(p): return (p.GetParentFootprint().GetReference(),p.GetNumber())
def reach(b,p):
 b.BuildConnectivity(); return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__ in ('PAD','PCB_PAD')}
groups={'XTAL_OUT':(('U1','54'),('Y1','2'),('C2','1')), 'RTL_3V3':(('U1','52'),('U1','39'),('U2','3'),('U2','8'),('C3','1'))}
b=pcbnew.LoadBoard(str(PCB)); ps=pads(b)
for name,g in groups.items():
 assert all(x in ps and ps[x].GetNetname()==name for x in g),(name,g)
 rr=reach(b,ps[g[0]])|{g[0]}; print(name,sorted(rr)); assert all(x in rr for x in g[1:]),(name,'connectivity')
for name,g in groups.items():
 t=pcbnew.LoadBoard(str(PCB)); victim=next(x for x in t.GetTracks() if x.GetNetname()==name and type(x).__name__!='PCB_VIA' and ((name=='XTAL_OUT' and {round(x.GetStart().x/1e6,2),round(x.GetEnd().x/1e6,2)}=={93.2,94.05} and round(x.GetStart().y/1e6,2)==67.6 and round(x.GetEnd().y/1e6,2)==67.6) or (name=='RTL_3V3' and {round(x.GetStart().x/1e6,2),round(x.GetEnd().x/1e6,2)}=={94.05,94.05} and min(x.GetStart().y,x.GetEnd().y)/1e6<66.81)))
 t.RemoveNative(victim); q=pads(t)
 assert g[0] not in reach(t,q[g[1]])|{g[1]},(name,'negative control')
print('PASS V1526 XTAL_OUT and RTL_3V3 native connectivity; both trace-removal negative controls PASS')
