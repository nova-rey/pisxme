import pcbnew

path = 'PHASE24_RTL9210B_SPISO3_U122_U2_V210.kicad_pcb'
b = pcbnew.LoadBoard(path); b.BuildConnectivity()
u1 = b.FindFootprintByReference('U1').FindPadByNumber('22')
u2 = b.FindFootprintByReference('U2').FindPadByNumber('7')
assert u2 in b.GetConnectivity().GetConnectedItems(u1)
nb = pcbnew.LoadBoard(path); net = nb.FindNet('SPISO3')
for t in list(nb.GetTracks()):
    if t.GetNetCode() == net.GetNetCode() and type(t).__name__ == 'PCB_TRACK':
        nb.Remove(t); break
nb.BuildConnectivity(); nu1 = nb.FindFootprintByReference('U1').FindPadByNumber('22'); nu2 = nb.FindFootprintByReference('U2').FindPadByNumber('7')
assert nu2 not in nb.GetConnectivity().GetConnectedItems(nu1)
nb.Save(path.replace('.kicad_pcb', '_NEGATIVE.kicad_pcb'))
print('V210 native SPISO3 connectivity PASS; trace-removal negative control PASS')
