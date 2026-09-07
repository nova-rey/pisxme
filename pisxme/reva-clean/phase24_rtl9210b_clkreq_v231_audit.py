import pcbnew
path='PHASE24_RTL9210B_CLKREQ_R3_U113_J1_52_V231.kicad_pcb';b=pcbnew.LoadBoard(path);b.BuildConnectivity();c=b.GetConnectivity();u=b.FindFootprintByReference('U1').FindPadByNumber('13');r=b.FindFootprintByReference('R3').FindPadByNumber('1');j=b.FindFootprintByReference('J1').FindPadByNumber('52');assert r in c.GetConnectedItems(u) and j in c.GetConnectedItems(u)
n=b.FindNet('CLKREQ_N');nb=pcbnew.LoadBoard(path)
for t in list(nb.GetTracks()):
    if t.GetNetCode()==n.GetNetCode() and type(t).__name__=='PCB_TRACK': nb.Remove(t); break
nb.BuildConnectivity();u=nb.FindFootprintByReference('U1').FindPadByNumber('13');r=nb.FindFootprintByReference('R3').FindPadByNumber('1');j=nb.FindFootprintByReference('J1').FindPadByNumber('52');assert r not in nb.GetConnectivity().GetConnectedItems(u) or j not in nb.GetConnectivity().GetConnectedItems(u);print('V231 native CLKREQ U1/R3/J1 connectivity PASS; trace-removal negative control PASS')
