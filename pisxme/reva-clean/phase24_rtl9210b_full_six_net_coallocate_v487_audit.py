"""Native connectivity audit for the complete V487 six-net channel."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent;PCB=ROOT/'PHASE24_RTL9210B_FULL_SIX_NET_COALLOCATE_V487.kicad_pcb'
GROUPS={'REFCLK_P':[('U1','61'),('J1','55')],'REFCLK_N':[('U1','62'),('J1','53')],'LANE0_RXN':[('U1','65'),('J1','41')],'LANE0_RXP':[('U1','64'),('J1','43')],'LANE0_TXN':[('U1','67'),('J1','47')],'LANE0_TXP':[('U1','68'),('J1','49')]}
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b,g):
 b.BuildConnectivity();ps=pads(b);c=b.GetConnectivity().GetConnectedItems(ps[g[0]]);return all(ps[x] in c for x in g[1:])
def main():
 b=pcbnew.LoadBoard(str(PCB));r={n:ok(b,g) for n,g in GROUPS.items()};assert all(r.values()),r
 for n,g in GROUPS.items():
  t=pcbnew.LoadBoard(str(PCB));victims=[x for x in t.GetTracks() if x.GetNetname()==n and not isinstance(x,pcbnew.PCB_VIA)];assert victims,n;t.RemoveNative(victims[0]);assert not ok(t,g),n
 print('PASS V487 native six-net endpoint audit:',r);print('PASS V487 six trace-removal negative controls')
if __name__=='__main__':main()
