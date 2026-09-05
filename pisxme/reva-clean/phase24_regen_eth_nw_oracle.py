"""Rigidly adapt the electrically clean CM5IO Ethernet oracle to live acreage.

The direct fixture and live J7 share the same transformed mating-view origin;
only the complete Ethernet endpoint island and its non-J7 copper are shifted.
"""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_SELECTED_MACRO_PLACEMENT.kicad_pcb'
ORACLE=R/'CM5IO_DIRECT_J7_ETHERNET_FIXTURE.kicad_pcb'
OUT=R/'PHASE24_ETH_NW_ORACLE_OPEN_REGEN.kicad_pcb'
# Keep the CM5IO source escape through its native branching point at about
# x=64.979 mm, then translate only the endpoint-side portion. This preserves
# the authoritative J7 launch while testing an open north-west island.
DX,DY=-10.0,-10.0
ORACLE_BRANCH_X=64.979
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def mm(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def near_j7(board,q):
 f=board.FindFootprintByReference('J7')
 return any(mm(p.GetPosition())==(round(q[0],6),round(q[1],6)) for p in f.Pads())
def shift(q):
 if near_j7(ot,q) or q[0] <= ORACLE_BRANCH_X: return q
 return (q[0]+DX,q[1]+DY)

ot=pcbnew.LoadBoard(str(ORACLE)); b=pcbnew.LoadBoard(str(BASE))
for t in list(b.GetTracks()):
 if any(k in t.GetNetname() for k in ('CM5_GBE_','/ETHERNET/','/GBE_')): b.Remove(t)
# Oracle direct positions: U6 81.1/65.215, U9 75.1/65.215, J2 77.5/53.
# Apply the selected endpoint translation to those coordinates, not to the
# already-moved positions in the input board.
for ref,(x,y) in {'U6':(81.1,65.215),'U9':(75.1,65.215),'J2':(77.5,53.0)}.items():
 f=b.FindFootprintByReference(ref); f.SetPosition(V(x+DX,y+DY))
for item in ot.GetTracks():
 short=item.GetNetname().rsplit('/',1)[-1]
 if not short.startswith('CM5_GBE_TD'): continue
 n=b.FindNet(short)
 if n is None: raise RuntimeError('missing live net '+short)
 a=shift(mm(item.GetStart())); z=shift(mm(item.GetEnd()))
 if a==z: continue
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(item.GetLayer());t.SetWidth(item.GetWidth());t.SetNet(n);b.Add(t)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
