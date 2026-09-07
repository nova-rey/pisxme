import pcbnew
path='PHASE24_RTL9210B_SPISO3_U122_U2_V211.kicad_pcb';b=pcbnew.LoadBoard(path);b.BuildConnectivity();a=b.FindFootprintByReference('U1').FindPadByNumber('22');z=b.FindFootprintByReference('U2').FindPadByNumber('7');assert z in b.GetConnectivity().GetConnectedItems(a)
n=b.FindNet('SPISO3');nb=pcbnew.LoadBoard(path)
for t in list(nb.GetTracks()):
    if t.GetNetCode()==n.GetNetCode() and type(t).__name__=='PCB_TRACK': nb.Remove(t); break
nb.BuildConnectivity();a=nb.FindFootprintByReference('U1').FindPadByNumber('22');z=nb.FindFootprintByReference('U2').FindPadByNumber('7');assert z not in nb.GetConnectivity().GetConnectedItems(a);print('V211 native SPISO3 connectivity PASS; trace-removal negative control PASS')
