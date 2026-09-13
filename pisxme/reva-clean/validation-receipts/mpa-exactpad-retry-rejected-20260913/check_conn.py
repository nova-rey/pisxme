import pcbnew,collections
p='pisxme/reva-clean/PHASE24_MPA_STORAGE_POWER_EXACTPAD_CANDIDATE.kicad_pcb'; b=pcbnew.LoadBoard(p)
def key(p): return (int(p.x),int(p.y))
def pos(r,n): return key(b.FindFootprintByReference(r).FindPadByNumber(str(n)).GetPosition())
def check(net, refs):
 adj=collections.defaultdict(set); nodes=set()
 for t in b.GetTracks():
  if t.GetNetname()!=net: continue
  a=key(t.GetStart()); z=key(t.GetEnd());adj[a].add(z);adj[z].add(a);nodes.update([a,z])
 for f in b.GetFootprints():
  for p in f.Pads():
   if p.GetNetname()==net:nodes.add(key(p.GetPosition()))
 for v in b.GetTracks():
  if isinstance(v, pcbnew.PCB_VIA) and v.GetNetname()==net:nodes.add(key(v.GetPosition()))
 seen=set(); comps=[]
 for x in nodes:
  if x in seen:continue
  q=[x];seen.add(x); comp=set(q)
  while q:
   a=q.pop()
   for z in adj[a]:
    if z not in seen:seen.add(z);comp.add(z);q.append(z)
  comps.append(comp)
 cid={x:i for i,c in enumerate(comps) for x in c}
 return [(r,n,pos(r,n),cid.get(pos(r,n))) for r,n in refs]
checks=[('BRIDGE_SATA_TX_P',[('U7','57'),('C30','2')]),('BRIDGE_SATA_TX_N',[('U7','56'),('C31','2')]),('BRIDGE_SATA_RX_P',[('U7','60'),('C32','2')]),('BRIDGE_SATA_RX_N',[('U7','59'),('C33','2')]),('TUSB_SATA_TXP',[('C30','1'),('U13','38')]),('TUSB_SATA_TXN',[('C31','1'),('U13','37')]),('TUSB_SATA_RXP',[('C32','1'),('U13','36')]),('TUSB_SATA_RXN',[('C33','1'),('U13','35')]),('M2_SATA_A_P_PCIE_TXP0',[('U13','2'),('J3','49')]),('M2_SATA_A_N_PCIE_TXN0',[('U13','3'),('J3','47')]),('M2_SATA_B_P_PCIE_RXN0',[('U13','6'),('J3','41')]),('M2_SATA_B_N_PCIE_RXP0',[('U13','7'),('J3','43')]),('STORAGE_SEL',[('U12','9'),('U13','9'),('U14','4')]),('AUTO_PEDET',[('J3','69'),('J8','2')]),('MODE_IN',[('U14','2'),('J8','4')]),('12V_IN_B',[('J6','1'),('F2','1'),('U2','3'),('C4','2')]),('FUSED_12V_B',[('F2','5'),('D2','1'),('U2','6'),('Q2','1')])]
for net,refs in checks: print(net,check(net,refs))
