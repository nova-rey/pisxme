"""V320: normalize the disposable J1 M.2 footprint coordinate frame.

The prior footprint encoded board-absolute pad positions under an origin at
(0,0). This preserves physical pad centers while giving the footprint a
real local origin, so future placement transforms are meaningful.
"""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_CLKREQ_ROUTE_V311.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_M2_NORMALIZED_V320.kicad_pcb'
def main():
 b=pcbnew.LoadBoard(str(BASE)); f=b.FindFootprintByReference('J1')
 before={p.GetPadName():(p.GetPosition().x,p.GetPosition().y) for p in f.Pads()}
 origin=pcbnew.VECTOR2I_MM(127,66)
 f.SetPosition(origin)
 for p in f.Pads():
  q=before[p.GetPadName()]; p.SetPosition(pcbnew.VECTOR2I(q[0],q[1]))
 b.BuildListOfNets();b.Save(str(OUT))
 r=pcbnew.LoadBoard(str(OUT)); g=r.FindFootprintByReference('J1')
 after={p.GetPadName():(p.GetPosition().x,p.GetPosition().y) for p in g.Pads()}
 assert before==after, (before,after)
 assert tuple(round(v/1e6,3) for v in (g.GetPosition().x,g.GetPosition().y))==(127.0,66.0)
 print('PASS V320 normalized J1 anchor; physical pad centers unchanged')
if __name__=='__main__':main()
