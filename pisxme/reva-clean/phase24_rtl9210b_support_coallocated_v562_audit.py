"""Native V562 RTL9210B support audit with route-and-zone negative control."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; PCB=H/'PHASE24_RTL9210B_SUPPORT_COALLOCATED_V562.kicad_pcb'
G=[('U1',n) for n in ['16','25','36','40','50','55','60','63']]+[('C4','1')]
def pads(b):return {(f.GetReference(),str(p.GetNumber())):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b,group):
 b.BuildConnectivity();q=pads(b);c=b.GetConnectivity().GetConnectedItems(q[group[0]]);return all(q[x] in c for x in group[1:])
def main():
 b=pcbnew.LoadBoard(str(PCB));assert connected(b,G)
 t=pcbnew.LoadBoard(str(PCB))
 for x in list(t.GetTracks()):
  if x.GetNetname()=='RTL_1V1':t.RemoveNative(x)
 for z in list(t.Zones()):
  if z.GetNetname()=='RTL_1V1':t.RemoveNative(z)
 assert not connected(t,G)
 print('PASS V562 native all-eight RTL_1V1-to-C4 connectivity; route+zone negative control PASS')
if __name__=='__main__':main()
