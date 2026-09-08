"""Native connectivity and negative-control audit for RX pair V466."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent; PCB=ROOT/'PHASE24_RTL9210B_RX_PAIR_ENDPOINT_V466.kicad_pcb'
GROUPS={'LANE0_RXN':[('U1','65'),('J1','41')], 'LANE0_RXP':[('U1','64'),('J1','43')]}
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b,g):
 b.BuildConnectivity(); ps=pads(b); c=b.GetConnectivity().GetConnectedItems(ps[g[0]]); return all(ps[x] in c for x in g[1:])
def main():
 b=pcbnew.LoadBoard(str(PCB)); result={n:ok(b,g) for n,g in GROUPS.items()}; assert all(result.values()),result
 for n,g in GROUPS.items():
  t=pcbnew.LoadBoard(str(PCB)); victims=[x for x in t.GetTracks() if x.GetNetname()==n and not isinstance(x,pcbnew.PCB_VIA)]; assert victims,n
  t.RemoveNative(victims[0]); assert not ok(t,g),n
 print('PASS V466 native RX endpoint audit:',result)
 print('PASS V466 two trace-removal negative controls')
if __name__=='__main__': main()
