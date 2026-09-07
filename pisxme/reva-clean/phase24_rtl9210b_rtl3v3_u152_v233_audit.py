import pcbnew
path='PHASE24_RTL9210B_RTL3V3_U152_V233.kicad_pcb';b=pcbnew.LoadBoard(path);b.BuildConnectivity();u=b.FindFootprintByReference('U1').FindPadByNumber('52');c=b.FindFootprintByReference('C3').FindPadByNumber('1');assert c in b.GetConnectivity().GetConnectedItems(u)
n=b.FindNet('RTL_3V3');nb=pcbnew.LoadBoard(path)
for t in list(nb.GetTracks()):
    if t.GetNetCode()==n.GetNetCode() and type(t).__name__=='PCB_TRACK' and round(t.GetStart().x/1e6,1)==94.8 and round(t.GetStart().y/1e6,1)==66.0: nb.Remove(t);break
nb.BuildConnectivity();u=nb.FindFootprintByReference('U1').FindPadByNumber('52');c=nb.FindFootprintByReference('C3').FindPadByNumber('1');assert c not in nb.GetConnectivity().GetConnectedItems(u);nb.Save(path.replace('.kicad_pcb','_NEGATIVE.kicad_pcb'));print('V233 native U1.52/C3.1 connectivity PASS; trace-removal negative control PASS')
