"""Native connectivity audit and trace-removal negative control for V328."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_LANE0_ROUTE_V328.kicad_pcb'
ENDS={'LANE0_RXP':('64','43'),'LANE0_RXN':('65','41'),'LANE0_TXN':('67','47'),'LANE0_TXP':('68','49')}
def pads(b):
 return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b, net, pair):
 b.BuildConnectivity(); ps=pads(b); a=ps[('U1',pair[0])]; z=ps[('J1',pair[1])]
 return z in b.GetConnectivity().GetConnectedItems(a)
def main():
 b=pcbnew.LoadBoard(str(PCB))
 for net,pair in ENDS.items(): assert connected(b,net,pair), net
 trial=pcbnew.LoadBoard(str(PCB)); victim=next(x for x in trial.GetTracks() if x.GetNetname()=='LANE0_TXP')
 trial.RemoveNative(victim)
 assert not connected(trial,'LANE0_TXP',ENDS['LANE0_TXP'])
 print('PASS V328 native lane-0 connectivity; trace-removal negative control PASS')
if __name__=='__main__':main()
