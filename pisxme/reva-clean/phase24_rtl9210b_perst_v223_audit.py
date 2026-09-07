import pcbnew
path='PHASE24_RTL9210B_PERST_U114_J1_50_V223.kicad_pcb';b=pcbnew.LoadBoard(path);b.BuildConnectivity();u=b.FindFootprintByReference('U1').FindPadByNumber('14');j=b.FindFootprintByReference('J1').FindPadByNumber('50');assert j in b.GetConnectivity().GetConnectedItems(u)
n=b.FindNet('PERST_N');nb=pcbnew.LoadBoard(path)
for t in list(nb.GetTracks()):
    if t.GetNetCode()==n.GetNetCode() and type(t).__name__=='PCB_TRACK': nb.Remove(t); break
nb.BuildConnectivity();u=nb.FindFootprintByReference('U1').FindPadByNumber('14');j=nb.FindFootprintByReference('J1').FindPadByNumber('50');assert j not in nb.GetConnectivity().GetConnectedItems(u);nb.Save(path.replace('.kicad_pcb','_NEGATIVE.kicad_pcb'));print('V223 native PERST U1/J1 connectivity PASS; trace-removal negative control PASS')
