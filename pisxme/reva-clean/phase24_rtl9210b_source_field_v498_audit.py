"""Native saved-board audit for the V498 co-allocated source field."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_SOURCE_FIELD_V498.kicad_pcb'
GROUPS={'XTAL_IN':[('U1','53'),('Y1','1'),('C1','1')],'XTAL_OUT':[('U1','54'),('Y1','2'),('C2','1')],'RSET':[('U1','51'),('R1','1')],'RTL_3V3':[('U1','52'),('U1','39'),('U1','20'),('U1','34'),('C3','1')]}
def m(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b,g):
 b.BuildConnectivity();q=m(b);c=b.GetConnectivity().GetConnectedItems(q[g[0]]);return all(q[x] in c for x in g[1:])
def main():
 b=pcbnew.LoadBoard(str(PCB));r={k:ok(b,g) for k,g in GROUPS.items()};assert all(r.values()),r
 for name,g in GROUPS.items():
  t=pcbnew.LoadBoard(str(PCB));vs=[x for x in t.GetTracks() if x.GetNetname()==name];assert vs,name
  for x in vs:t.RemoveNative(x)
  assert not ok(t,g),name
 print('PASS V498 native source-field connectivity; four trace-removal negative controls PASS')
if __name__=='__main__':main()
