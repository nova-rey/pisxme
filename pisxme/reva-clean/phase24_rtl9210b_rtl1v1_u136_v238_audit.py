import pcbnew
path='PHASE24_RTL9210B_RTL1V1_U136_V238.kicad_pcb';b=pcbnew.LoadBoard(path);b.BuildConnectivity();u=b.FindFootprintByReference('U1').FindPadByNumber('36');c=b.FindFootprintByReference('C4').FindPadByNumber('1');assert c in b.GetConnectivity().GetConnectedItems(u)
n=b.FindNet('RTL_1V1');nb=pcbnew.LoadBoard(path);removed=False
for t in list(nb.GetTracks()):
    if t.GetNetCode()==n.GetNetCode() and type(t).__name__=='PCB_TRACK' and round(t.GetStart().x/1e6,1)==94.0 and round(t.GetStart().y/1e6,1)==59.2: nb.Remove(t);removed=True;break
assert removed;nb.BuildConnectivity();u=nb.FindFootprintByReference('U1').FindPadByNumber('36');c=nb.FindFootprintByReference('C4').FindPadByNumber('1');assert c not in nb.GetConnectivity().GetConnectedItems(u);nb.Save(path.replace('.kicad_pcb','_NEGATIVE.kicad_pcb'));print('V238 native U1.36/C4.1 connectivity PASS; trace-removal negative control PASS')
