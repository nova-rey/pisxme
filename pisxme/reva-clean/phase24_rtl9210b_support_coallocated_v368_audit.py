"""Native V368 support audit and negative controls."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V368.kicad_pcb'
GROUPS={
 'RTL_1V1':[('U1','16'),('U1','25'),('U1','36'),('U1','40'),('U1','50'),('U1','55'),('U1','60'),('U1','63'),('C4','1')],
 'RTL_3V3':[('U1','20'),('U1','34'),('U1','39'),('U1','52'),('R2','2'),('R3','2'),('C3','1'),('U2','3'),('U2','8')],
 'XTAL_IN':[('U1','53'),('Y1','1'),('C1','1')],
 'XTAL_OUT':[('U1','54'),('Y1','2'),('C2','1')],
 'RSET':[('U1','51'),('R1','1')],
}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def check(b,g):
 b.BuildConnectivity(); ps=pads(b); c=b.GetConnectivity().GetConnectedItems(ps[g[0]])
 return all(ps[x] in c for x in g[1:])
def main():
 b=pcbnew.LoadBoard(str(PCB)); assert all(check(b,g) for g in GROUPS.values())
 for name in ('RTL_1V1','RSET'):
  t=pcbnew.LoadBoard(str(PCB)); victims=[x for x in t.GetTracks() if x.GetNetname()==name]; assert victims
  for victim in victims: t.RemoveNative(victim)
  assert not check(t,GROUPS[name])
 print('PASS V368 native 1V1/3V3/XTAL/RSET support; trace-removal negative controls PASS')
if __name__=='__main__': main()
