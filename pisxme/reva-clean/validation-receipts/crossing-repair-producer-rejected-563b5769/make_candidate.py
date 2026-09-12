import pcbnew
from pathlib import Path
root=Path('/workspace/project/pisxme/reva-clean')
board_path=root/'PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb'
out=root/'PHASE24_CROSSING_REPAIR_CANDIDATE.kicad_pcb'
b=pcbnew.LoadBoard(str(board_path))

def p(x,y): return pcbnew.VECTOR2I(pcbnew.FromMM(x),pcbnew.FromMM(y))
def add(a,z,net,width=.2):
 t=pcbnew.PCB_TRACK(b); t.SetLayer(pcbnew.B_Cu); t.SetWidth(pcbnew.FromMM(width)); t.SetNet(net); t.SetNetCode(net.GetNetCode()); t.SetStart(p(*a)); t.SetEnd(p(*z)); b.Add(t)

alltracks=list(b.GetTracks())
def remove_seg(net, a, z):
 for t in alltracks:
  if t.GetNetname()!=net: continue
  s,e=t.GetStart(),t.GetEnd(); sa=(pcbnew.ToMM(s.x),pcbnew.ToMM(s.y)); ea=(pcbnew.ToMM(e.x),pcbnew.ToMM(e.y))
  if (abs(sa[0]-a[0])<1e-4 and abs(sa[1]-a[1])<1e-4 and abs(ea[0]-z[0])<1e-4 and abs(ea[1]-z[1])<1e-4) or (abs(sa[0]-z[0])<1e-4 and abs(sa[1]-z[1])<1e-4 and abs(ea[0]-a[0])<1e-4 and abs(ea[1]-a[1])<1e-4):
   b.Remove(t); print('removed',net,sa,ea); return
 raise RuntimeError((net,a,z))

j=b.FindNet('JMS_AVDDL')
assert j
# Detour the two JMS_AVDDL B.Cu segments around the USB_RXN1/USB_RXP1 corridor.
remove_seg('JMS_AVDDL',(141.8,140.0),(154.5,150.5))
for a,z in zip([(141.8,140.0),(141.8,138.0),(137.8,138.0),(137.8,151.0),(154.5,151.0)],[(141.8,138.0),(137.8,138.0),(137.8,151.0),(154.5,151.0),(154.5,150.5)]): add(a,z,j)
remove_seg('JMS_AVDDL',(168.0,132.6),(168.0,150.5))
for a,z in zip([(168.0,132.6),(174.0,132.6),(174.0,151.0),(168.0,151.0)],[(174.0,132.6),(174.0,151.0),(168.0,151.0),(168.0,150.5)]): add(a,z,j)
pcbnew.SaveBoard(str(out),b)
print('saved',out)
