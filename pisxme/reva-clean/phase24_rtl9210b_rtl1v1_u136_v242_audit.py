import pcbnew
path='PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V242.kicad_pcb';b=pcbnew.LoadBoard(path);b.BuildConnectivity();c=b.GetConnectivity();u=b.FindFootprintByReference('U1').FindPadByNumber('36');u39=b.FindFootprintByReference('U1').FindPadByNumber('39');u52=b.FindFootprintByReference('U1').FindPadByNumber('52');c4=b.FindFootprintByReference('C4').FindPadByNumber('1');c3=b.FindFootprintByReference('C3').FindPadByNumber('1');assert c4 in c.GetConnectedItems(u) and c3 in c.GetConnectedItems(u39) and c3 in c.GetConnectedItems(u52)
n=b.FindNet('RTL_1V1');nb=pcbnew.LoadBoard(path);removed=False
for t in list(nb.GetTracks()):
    if t.GetNetCode()==n.GetNetCode() and type(t).__name__=='PCB_TRACK' and round(t.GetStart().x/1e6,1)==94.0 and round(t.GetStart().y/1e6,1)==59.2: nb.Remove(t);removed=True;break
assert removed;nb.BuildConnectivity();u=nb.FindFootprintByReference('U1').FindPadByNumber('36');c4=nb.FindFootprintByReference('C4').FindPadByNumber('1');assert c4 not in nb.GetConnectivity().GetConnectedItems(u);print('V242 native coordinated rail connectivity PASS; trace-removal negative control PASS')
