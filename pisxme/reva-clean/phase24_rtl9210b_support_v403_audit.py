"""Native connectivity and negative controls for the V403 support basis."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_XTALIN_ENDPOINT_V404.kicad_pcb'
GROUPS={
 'RTL_3V3':[('U1','20'),('U1','34'),('U1','39'),('U1','52'),('R2','2'),('R3','2'),('C3','1'),('U2','3'),('U2','8')],
 'XTAL_IN':[('U1','53'),('Y1','1'),('C1','1')],
 'XTAL_OUT':[('U1','54'),('Y1','2'),('C2','1')],
 'RSET':[('U1','51'),('R1','1')],
 'LANE0_RXP':[('U1','64'),('J1','43')], 'LANE0_RXN':[('U1','65'),('J1','41')],
 'LANE0_TXP':[('U1','68'),('J1','49')], 'LANE0_TXN':[('U1','67'),('J1','47')],
}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b,g):
 b.BuildConnectivity(); ps=pads(b); c=b.GetConnectivity().GetConnectedItems(ps[g[0]])
 return all(ps[x] in c for x in g[1:])
def main():
 b=pcbnew.LoadBoard(str(PCB)); result={k:connected(b,g) for k,g in GROUPS.items()}; assert all(result.values()),result
 for name in ('RTL_3V3','XTAL_OUT','RSET','LANE0_RXP'):
  t=pcbnew.LoadBoard(str(PCB)); victims=[x for x in t.GetTracks() if x.GetNetname()==name]; assert victims
  for x in victims: t.RemoveNative(x)
  assert not connected(t,GROUPS[name]),name
 print('PASS V404 native lane/support connectivity; four trace-removal negative controls PASS')
if __name__=='__main__': main()
