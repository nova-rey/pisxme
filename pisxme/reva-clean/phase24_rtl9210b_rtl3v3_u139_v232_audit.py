import pcbnew
path='PHASE24_RTL9210B_RTL3V3_U139_V232.kicad_pcb';b=pcbnew.LoadBoard(path);b.BuildConnectivity();u=b.FindFootprintByReference('U1').FindPadByNumber('39');c=b.FindFootprintByReference('C3').FindPadByNumber('1');assert c in b.GetConnectivity().GetConnectedItems(u)
n=b.FindNet('RTL_3V3');nb=pcbnew.LoadBoard(path); removed=False
for t in list(nb.GetTracks()):
    if t.GetNetCode()==n.GetNetCode() and type(t).__name__=='PCB_TRACK' and (round(t.GetStart().x/1e6,2),round(t.GetStart().y/1e6,2))==(94.05,60.4): nb.Remove(t); removed=True; break
assert removed
nb.BuildConnectivity();u=nb.FindFootprintByReference('U1').FindPadByNumber('39');c=nb.FindFootprintByReference('C3').FindPadByNumber('1');assert c not in nb.GetConnectivity().GetConnectedItems(u);nb.Save(path.replace('.kicad_pcb','_NEGATIVE.kicad_pcb'));print('V232 native U1.39/C3.1 connectivity PASS; trace-removal negative control PASS')
