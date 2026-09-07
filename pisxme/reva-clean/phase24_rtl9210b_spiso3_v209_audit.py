import pcbnew

path = 'PHASE24_RTL9210B_SPISO3_U122_U2_V209.kicad_pcb'
b = pcbnew.LoadBoard(path)
b.BuildConnectivity()
net = b.FindNet('SPISO3')
u1 = b.FindFootprintByReference('U1').FindPadByNumber('22')
u2 = b.FindFootprintByReference('U2').FindPadByNumber('7')
items1 = b.GetConnectivity().GetConnectedItems(u1)
items2 = b.GetConnectivity().GetConnectedItems(u2)
assert u2 in items1 and u1 in items2, 'SPISO3 endpoints are not connected'

negative = path.replace('.kicad_pcb', '_NEGATIVE.kicad_pcb')
nb = pcbnew.LoadBoard(path)
removed = False
for t in list(nb.GetTracks()):
    if t.GetNetCode() == net.GetNetCode() and type(t).__name__ == 'PCB_TRACK':
        nb.Remove(t); removed = True; break
assert removed, 'negative control could not remove a SPISO3 segment'
nb.BuildConnectivity()
nu1 = nb.FindFootprintByReference('U1').FindPadByNumber('22')
nu2 = nb.FindFootprintByReference('U2').FindPadByNumber('7')
assert nu2 not in nb.GetConnectivity().GetConnectedItems(nu1), 'negative control did not fail'
nb.Save(negative)
print('V209 native SPISO3 connectivity PASS; trace-removal negative control PASS')
