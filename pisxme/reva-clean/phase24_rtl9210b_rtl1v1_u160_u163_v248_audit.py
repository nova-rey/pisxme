import pcbnew
path='PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V248.kicad_pcb';b=pcbnew.LoadBoard(path);b.BuildConnectivity();c=b.GetConnectivity();u=b.FindFootprintByReference('U1');c4=b.FindFootprintByReference('C4').FindPadByNumber('1');c3=b.FindFootprintByReference('C3').FindPadByNumber('1');assert c4 in c.GetConnectedItems(u.FindPadByNumber('36'));assert c4 in c.GetConnectedItems(u.FindPadByNumber('60'));assert c4 in c.GetConnectedItems(u.FindPadByNumber('63'));assert c3 in c.GetConnectedItems(u.FindPadByNumber('39'));assert c3 in c.GetConnectedItems(u.FindPadByNumber('52'))
nb=pcbnew.LoadBoard(path);nb.BuildConnectivity();un=nb.FindFootprintByReference('U1');c4n=nb.FindFootprintByReference('C4').FindPadByNumber('1');removed=False;code=nb.FindNet('RTL_1V1').GetNetCode()
for t in list(nb.GetTracks()):
 if t.GetNetCode()==code: nb.RemoveNative(t);removed=True
assert removed;nb.BuildConnectivity();cn=nb.GetConnectivity();assert c4n not in cn.GetConnectedItems(un.FindPadByNumber('60'));print('V248 native U1.36/U1.60/U1.63 rail connectivity PASS; full-rail-removal negative control PASS')
