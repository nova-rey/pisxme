import pcbnew
path='PHASE24_RTL9210B_RTL1V1_U136_U139_V239.kicad_pcb';b=pcbnew.LoadBoard(path);b.BuildConnectivity();c=b.GetConnectivity();u=b.FindFootprintByReference('U1').FindPadByNumber('36');u3=b.FindFootprintByReference('U1').FindPadByNumber('39');cap1=b.FindFootprintByReference('C4').FindPadByNumber('1');cap3=b.FindFootprintByReference('C3').FindPadByNumber('1');assert cap1 in c.GetConnectedItems(u) and cap3 in c.GetConnectedItems(u3)
for name,pad in [('U1','36'),('U1','39')]:
    n=b.FindNet('RTL_1V1' if pad=='36' else 'RTL_3V3');nb=pcbnew.LoadBoard(path);removed=False
    for t in list(nb.GetTracks()):
        if t.GetNetCode()==n.GetNetCode() and type(t).__name__=='PCB_TRACK' and round(t.GetStart().x/1e6,2)==(94.05 if pad in {'36','39'} else 0) and round(t.GetStart().y/1e6,1)==(59.2 if pad=='36' else 60.4): nb.Remove(t);removed=True;break
    assert removed;nb.BuildConnectivity();a=nb.FindFootprintByReference('U1').FindPadByNumber(pad);z=nb.FindFootprintByReference('C4' if pad=='36' else 'C3').FindPadByNumber('1');assert z not in nb.GetConnectivity().GetConnectedItems(a)
print('V239 native U1.36/U1.39 rail connectivity PASS; two trace-removal negative controls PASS')
