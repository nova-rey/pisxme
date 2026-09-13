import pcbnew
b=pcbnew.LoadBoard('/workspace/project/pisxme/reva-clean/PHASE24_MPA_STORAGE_POWER_IMPLEMENTED_CANDIDATE.kicad_pcb')
b.BuildConnectivity(); c=b.GetConnectivity()
def key(p): return p.GetParentFootprint().GetReference()+'.'+str(p.GetNumber())
def connected(a,z):
 x=b.FindFootprintByReference(a[0]).FindPadByNumber(a[1]); y=b.FindFootprintByReference(z[0]).FindPadByNumber(z[1]); return key(y) in {key(i) for i in c.GetConnectedItems(x) if isinstance(i,pcbnew.PAD)}
checks=[(('J6','1'),('F2','1')), (('F2','1'),('U2','3')), (('F2','1'),('C4','2')), (('F2','5'),('D2','1')), (('F2','5'),('Q2','1')), (('F2','5'),('U2','6')), (('U2','5'),('Q2','3'))]
for a,z in checks: print(a,z,connected(a,z))
