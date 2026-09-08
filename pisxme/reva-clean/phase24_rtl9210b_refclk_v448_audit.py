"""Native REFCLK connectivity audit and trace-removal negative controls."""
import pcbnew
from pathlib import Path
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_REFCLK_DEEP_JOG_V448.kicad_pcb'
GROUPS={'REFCLK_P':[('U1','61'),('J1','55')],'REFCLK_N':[('U1','62'),('J1','53')]}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b,g):
 b.BuildConnectivity(); ps=pads(b); c=b.GetConnectivity().GetConnectedItems(ps[g[0]])
 return all(ps[x] in c for x in g[1:])
def main():
 b=pcbnew.LoadBoard(str(PCB)); assert all(connected(b,g) for g in GROUPS.values())
 for name,g in GROUPS.items():
  t=pcbnew.LoadBoard(str(PCB)); victims=[x for x in t.GetTracks() if x.GetNetname()==name]; assert victims
  for x in victims: t.RemoveNative(x)
  assert not connected(t,g),name
 print('PASS V448 REFCLK native connectivity; two trace-removal negative controls PASS')
if __name__=='__main__': main()
