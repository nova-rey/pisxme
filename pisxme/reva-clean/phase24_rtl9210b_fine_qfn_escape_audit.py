"""Saved-board physical connectivity and negative controls for fine QFN escape."""
from pathlib import Path
import json
import pcbnew

H=Path(__file__).resolve().parent
PCB=H/'PHASE24_RTL9210B_FINE_QFN_ESCAPE_FIXTURE.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_FINE_QFN_ESCAPE_AUDIT.json'
names=('ISOLATEB','CLKREQ_N','PERST_N','RTL_1V1','RTL_5V')

def connected(board, a, z):
    board.BuildConnectivity()
    return z in board.GetConnectivity().GetConnectedItems(a)

b=pcbnew.LoadBoard(str(PCB)); u=b.FindFootprintByReference('U1')
closed={}
for name in names:
    src=next(p for p in u.Pads() if p.GetNetname()==name)
    dst=b.FindFootprintByReference('FQ_'+name).FindPadByNumber('1')
    assert connected(b,src,dst), name
    closed[name]='PASS'

negative={}
for name in names:
    q=pcbnew.LoadBoard(str(PCB)); uq=q.FindFootprintByReference('U1')
    src=next(p for p in uq.Pads() if p.GetNetname()==name)
    dst=q.FindFootprintByReference('FQ_'+name).FindPadByNumber('1')
    cut=next(x for x in q.GetTracks() if not isinstance(x,pcbnew.PCB_VIA) and x.GetNetname()==name)
    q.RemoveNative(cut)
    assert not connected(q,src,dst), name
    negative[name]='PASS'

# Scope guard: every fine-width track must remain in the immediate QFN
# escape window; a normal-width track must exist at the handoff.
fine=[]; outside=[]; normal_handoffs=[]
for q in b.GetTracks():
    if isinstance(q,pcbnew.PCB_VIA): continue
    ps=[q.GetStart(),q.GetEnd()]
    if abs(pcbnew.ToMM(q.GetWidth())-.15)<.001:
        fine.append(q)
        if any(not (97.0<=pcbnew.ToMM(p.x)<=103.0 and 73.0<=pcbnew.ToMM(p.y)<=88.5) for p in ps): outside.append(q)
    if abs(pcbnew.ToMM(q.GetWidth())-.20)<.001 and q.GetLayer()==pcbnew.F_Cu:
        normal_handoffs.append(q)
assert fine and not outside and normal_handoffs

OUT.write_text(json.dumps({'board':PCB.name,'physical_saved_board':True,
    'source_to_handoff':closed,'trace_removal_negative_controls':negative,
    'scope_guard':{'fine_trace_count':len(fine),'outside_window':len(outside),'normal_handoff_tracks':len(normal_handoffs)},
    'verdict':'PASS'},indent=2)+'\n')
print('PASS fine QFN physical connectivity and negative controls')
