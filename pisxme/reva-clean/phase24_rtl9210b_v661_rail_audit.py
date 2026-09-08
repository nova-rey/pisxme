"""Saved-board V661 RTL_5V audit with a branch-specific negative control."""
import sys
import pcbnew

GROUP=(('U1','17'),('U1','33'),('C5','1'))
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def connected(b):
    b.BuildConnectivity(); q=pads(b); c=b.GetConnectivity().GetConnectedItems(q[GROUP[0]])
    return all(q[x] in c for x in GROUP[1:])
def main(path):
    b=pcbnew.LoadBoard(path); assert connected(b), 'V661 RTL_5V endpoints disconnected'
    bad=pcbnew.LoadBoard(path)
    victims=[x for x in bad.GetTracks() if x.GetNetname()=='RTL_5V' and
             isinstance(x,pcbnew.PCB_TRACK) and
             abs(x.GetStart().x/1e6-95.2)<.01 and abs(x.GetEnd().x/1e6-116.4)<.01]
    assert victims, 'RTL_5V trunk not found'
    for victim in victims: bad.RemoveNative(victim)
    assert not connected(bad), 'branch-specific negative control unexpectedly passed'
    print('PASS V661 RTL_5V endpoint group and unique-trunk negative control')
if __name__=='__main__': main(sys.argv[1])
