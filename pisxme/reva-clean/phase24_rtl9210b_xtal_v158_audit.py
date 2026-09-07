"""Native V158 XTAL_IN/XTAL_OUT connectivity audit."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
PCB=ROOT/'PHASE24_RTL9210B_XTAL_IN_INNER_ENDPOINT_V158.kicad_pcb'
def pads(board,ref,num):
    board.BuildConnectivity();p=board.FindFootprintByReference(ref).FindPadByNumber(num)
    return {(x.GetParentFootprint().GetReference(),x.GetNumber()) for x in board.GetConnectivity().GetConnectedItems(p) if type(x).__name__=='PAD'}
def main():
    b=pcbnew.LoadBoard(str(PCB))
    if {('U1','53'),('Y1','1'),('C1','1')}-pads(b,'U1','53'): raise AssertionError('XTAL_IN incomplete')
    if {('U1','54'),('Y1','2'),('C2','1')}-pads(b,'U1','54'): raise AssertionError('XTAL_OUT incomplete')
    bad=pcbnew.LoadBoard(str(PCB))
    for x in list(bad.GetTracks()):
        if x.GetNetname() in ('XTAL_IN','XTAL_OUT'): bad.RemoveNative(x)
    if {('U1','53'),('Y1','1'),('C1','1')}-pads(bad,'U1','53') == set(): raise AssertionError('negative control unexpectedly passed')
    print('PASS V158 native crystal connectivity audit and negative control')
if __name__=='__main__':main()
