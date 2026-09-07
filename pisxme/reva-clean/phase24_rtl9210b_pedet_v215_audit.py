import pcbnew
path='PHASE24_RTL9210B_PEDET_R2_U18_J1_69_V215.kicad_pcb';b=pcbnew.LoadBoard(path);b.BuildConnectivity();u=b.FindFootprintByReference('U1').FindPadByNumber('8');r=b.FindFootprintByReference('R2').FindPadByNumber('1');j=b.FindFootprintByReference('J1').FindPadByNumber('69');c=b.GetConnectivity();assert r in c.GetConnectedItems(u) and j in c.GetConnectedItems(u)
n=b.FindNet('PEDET');nb=pcbnew.LoadBoard(path)
for t in list(nb.GetTracks()):
    if t.GetNetCode()==n.GetNetCode() and type(t).__name__=='PCB_TRACK': nb.Remove(t); break
nb.BuildConnectivity();u=nb.FindFootprintByReference('U1').FindPadByNumber('8');r=nb.FindFootprintByReference('R2').FindPadByNumber('1');j=nb.FindFootprintByReference('J1').FindPadByNumber('69');assert r not in nb.GetConnectivity().GetConnectedItems(u) or j not in nb.GetConnectivity().GetConnectedItems(u);nb.Save(path.replace('.kicad_pcb','_NEGATIVE.kicad_pcb'));print('V215 native PEDET/R2/J1 connectivity PASS; trace-removal negative control PASS')
