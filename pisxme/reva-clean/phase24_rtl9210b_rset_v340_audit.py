"""Native RSET connectivity audit and trace-removal negative control."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_RSET_ROUTE_V340.kicad_pcb'
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(n)
def main():
    b=pcbnew.LoadBoard(str(PCB)); b.BuildConnectivity(); c=b.GetConnectivity()
    assert pad(b,'R1','1') in c.GetConnectedItems(pad(b,'U1','51'))
    t=pcbnew.LoadBoard(str(PCB)); victim=next(x for x in t.GetTracks() if x.GetNetname()=='RSET'); t.RemoveNative(victim); t.BuildConnectivity()
    assert pad(t,'R1','1') not in t.GetConnectivity().GetConnectedItems(pad(t,'U1','51'))
    print('PASS V340 native RSET connectivity; trace-removal negative control PASS')
if __name__=='__main__': main()
