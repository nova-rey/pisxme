import pcbnew
path='PHASE24_RTL9210B_QFN_SIDEBAND_SPISO3_PERST_V227.kicad_pcb';b=pcbnew.LoadBoard(path);b.BuildConnectivity();c=b.GetConnectivity()
for ref,pad_a,pad_z in [('U1','22','7'),('U1','14','50')]:
    a=b.FindFootprintByReference(ref).FindPadByNumber(pad_a); z=b.FindFootprintByReference('U2' if pad_z=='7' else 'J1').FindPadByNumber(pad_z); assert z in c.GetConnectedItems(a), (ref,pad_a,pad_z)
for name,ref,pad_a,pad_z in [('SPISO3','U1','22','7'),('PERST_N','U1','14','50')]:
    net=b.FindNet(name); nb=pcbnew.LoadBoard(path)
    for t in list(nb.GetTracks()):
        if t.GetNetCode()==net.GetNetCode() and type(t).__name__=='PCB_TRACK': nb.Remove(t); break
    nb.BuildConnectivity(); a=nb.FindFootprintByReference(ref).FindPadByNumber(pad_a); z=nb.FindFootprintByReference('U2' if pad_z=='7' else 'J1').FindPadByNumber(pad_z); assert z not in nb.GetConnectivity().GetConnectedItems(a), name
print('V227 native SPISO3/PERST connectivity PASS; two trace-removal negative controls PASS')
