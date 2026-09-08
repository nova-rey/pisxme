"""Native connectivity audit for REFCLK layer-split V479."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent;PCB=ROOT/'PHASE24_RTL9210B_REFCLK_LAYER_SPLIT_V479.kicad_pcb'
GROUPS={'REFCLK_P':[('U1','61'),('J1','55')],'REFCLK_N':[('U1','62'),('J1','53')]}
def pads(b):return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def ok(b,g):
 b.BuildConnectivity();ps=pads(b);c=b.GetConnectivity().GetConnectedItems(ps[g[0]]);return all(ps[x] in c for x in g[1:])
def main():
 b=pcbnew.LoadBoard(str(PCB));r={n:ok(b,g) for n,g in GROUPS.items()};assert all(r.values()),r
 for n,g in GROUPS.items():
  t=pcbnew.LoadBoard(str(PCB));victims=[x for x in t.GetTracks() if x.GetNetname()==n and not isinstance(x,pcbnew.PCB_VIA)];assert victims,n;t.RemoveNative(victims[0]);assert not ok(t,g),n
 print('PASS V479 native REFCLK endpoint audit:',r);print('PASS V479 two trace-removal negative controls')
if __name__=='__main__':main()
