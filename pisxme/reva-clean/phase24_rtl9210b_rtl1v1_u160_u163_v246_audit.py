import pcbnew
path='PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V246.kicad_pcb';b=pcbnew.LoadBoard(path);b.BuildConnectivity();c=b.GetConnectivity();u=b.FindFootprintByReference('U1');c4=b.FindFootprintByReference('C4').FindPadByNumber('1');c3=b.FindFootprintByReference('C3').FindPadByNumber('1');assert c4 in c.GetConnectedItems(u.FindPadByNumber('36'));assert c4 in c.GetConnectedItems(u.FindPadByNumber('60'));assert c4 in c.GetConnectedItems(u.FindPadByNumber('63'));assert c3 in c.GetConnectedItems(u.FindPadByNumber('39'));assert c3 in c.GetConnectedItems(u.FindPadByNumber('52'))
nb=pcbnew.LoadBoard(path);nb.BuildConnectivity();un=nb.FindFootprintByReference('U1');c4n=nb.FindFootprintByReference('C4').FindPadByNumber('1');removed=False
for t in list(nb.GetTracks()):
 if t.GetNetCode()==nb.FindNet('RTL_1V1').GetNetCode() and type(t).__name__=='PCB_TRACK' and round(t.GetStart().x/1e6,2)==98.0 and round(t.GetStart().y/1e6,2)==65.95: nb.Remove(t);removed=True;break
assert removed;nb.BuildConnectivity();assert c4n not in nb.GetConnectivity().GetConnectedItems(un.FindPadByNumber('60'));print('V246 native U1.36/U1.60/U1.63 rail connectivity PASS; trace-removal negative control PASS')
