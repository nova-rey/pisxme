import pcbnew
path='PHASE24_RTL9210B_CLKREQ_U113_J1_52_V218.kicad_pcb';b=pcbnew.LoadBoard(path);b.BuildConnectivity();u=b.FindFootprintByReference('U1').FindPadByNumber('13');j=b.FindFootprintByReference('J1').FindPadByNumber('52');assert j in b.GetConnectivity().GetConnectedItems(u)
n=b.FindNet('CLKREQ_N');nb=pcbnew.LoadBoard(path)
for t in list(nb.GetTracks()):
    if t.GetNetCode()==n.GetNetCode() and type(t).__name__=='PCB_TRACK': nb.Remove(t); break
nb.BuildConnectivity();u=nb.FindFootprintByReference('U1').FindPadByNumber('13');j=nb.FindFootprintByReference('J1').FindPadByNumber('52');assert j not in nb.GetConnectivity().GetConnectedItems(u);nb.Save(path.replace('.kicad_pcb','_NEGATIVE.kicad_pcb'));print('V218 native CLKREQ U1/J1 connectivity PASS; trace-removal negative control PASS')
