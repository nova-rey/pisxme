import pcbnew
path='PHASE24_RTL9210B_PEDET_U18_J1_69_V212.kicad_pcb';b=pcbnew.LoadBoard(path);b.BuildConnectivity();a=b.FindFootprintByReference('U1').FindPadByNumber('8');z=b.FindFootprintByReference('J1').FindPadByNumber('69');assert z in b.GetConnectivity().GetConnectedItems(a)
n=b.FindNet('PEDET');nb=pcbnew.LoadBoard(path)
for t in list(nb.GetTracks()):
    if t.GetNetCode()==n.GetNetCode() and type(t).__name__=='PCB_TRACK': nb.Remove(t); break
nb.BuildConnectivity();a=nb.FindFootprintByReference('U1').FindPadByNumber('8');z=nb.FindFootprintByReference('J1').FindPadByNumber('69');assert z not in nb.GetConnectivity().GetConnectedItems(a);nb.Save(path.replace('.kicad_pcb','_NEGATIVE.kicad_pcb'));print('V212 native PEDET connectivity PASS; trace-removal negative control PASS')
