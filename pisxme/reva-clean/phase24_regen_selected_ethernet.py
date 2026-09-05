"""Disposable Ethernet regeneration on the selected macro placement."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_SELECTED_MACRO_PLACEMENT.kicad_pcb'
OUT=R/'PHASE24_SELECTED_MACRO_ETHERNET_REGEN.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=pcbnew.FromMM(.13208)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def p(b,ref,num):
 q=b.FindFootprintByReference(ref).FindPadByNumber(str(num)).GetPosition()
 return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def tr(b,n,pts,layer):
 for a,z in zip(pts,pts[1:]):
  if a==z: continue
  t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(layer);t.SetWidth(W);t.SetNet(n);b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*q));v.SetWidth(pcbnew.FromMM(.5));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);b.Add(v)

b=pcbnew.LoadBoard(str(BASE))
for t in list(b.GetTracks()):
 if any(k in t.GetNetname() for k in ('CM5_GBE_','/ETHERNET/','/GBE_')): b.Remove(t)

# Native CM5IO mapping, with pair-preserving west-side escapes. Alternate
# pairs use B.Cu after ordinary vias outside the J7 pad field.
mapping={
 'CM5_GBE_TD3_P':('3','U9','5','J2','9'), 'CM5_GBE_TD3_N':('5','U9','4','J2','10'),
 'CM5_GBE_TD2_N':('9','U9','2','J2','8'), 'CM5_GBE_TD2_P':('11','U9','1','J2','7'),
 'CM5_GBE_TD1_P':('4','U6','5','J2','3'), 'CM5_GBE_TD1_N':('6','U6','4','J2','6'),
 'CM5_GBE_TD0_N':('10','U6','2','J2','2'), 'CM5_GBE_TD0_P':('12','U6','1','J2','1')}
# Paths stop at actual native pad centers. Geometry is intentionally compact;
# this is a route experiment, not a promoted pass.
paths={
 'CM5_GBE_TD3_P':[(31.2,98.0),(29.0,103.8),(27.0,105.6)],
 'CM5_GBE_TD3_N':[(30.8,98.5),(28.5,104.2),(26.5,105.6)],
 'CM5_GBE_TD2_N':[(30.4,101.4),(28.0,104.8),(26.0,105.6)],
 'CM5_GBE_TD2_P':[(30.0,102.0),(27.5,105.2),(25.5,105.6)],
 'CM5_GBE_TD1_P':[(31.2,98.8),(29.5,96.0),(25.0,94.385)],
 'CM5_GBE_TD1_N':[(30.8,99.2),(29.0,96.5),(25.0,93.615)],
 'CM5_GBE_TD0_N':[(30.4,100.8),(28.0,95.8),(26.0,93.615)],
 'CM5_GBE_TD0_P':[(30.0,101.2),(27.5,95.2),(26.0,94.385)],}
for name,(j7,jref,ep,jref2,jp) in mapping.items():
 n=b.FindNet(name); start=p(b,'J7',j7); esd=p(b,jref,ep); jack=p(b,jref2,jp)
 if name.endswith(('TD2_N','TD2_P','TD3_N','TD3_P')):
  q=paths[name][0]; tr(b,n,[start,q],F); via(b,n,q); tr(b,n,[q]+paths[name][1:]+[esd],B); via(b,n,paths[name][-1])
 else:
  tr(b,n,[start]+paths[name]+[esd],F)
 # Connector-side launch runs toward the west edge; keep each pair together.
 side={
  'CM5_GBE_TD3_P':[(22,107),(18,107),(jack[0],jack[1])],
  'CM5_GBE_TD3_N':[(22,108),(17,108),(jack[0],jack[1])],
  'CM5_GBE_TD2_N':[(22,106),(14,106),(jack[0],jack[1])],
  'CM5_GBE_TD2_P':[(22,107.5),(13,107.5),(jack[0],jack[1])],
  'CM5_GBE_TD1_P':[(22,103),(16,103),(jack[0],jack[1])],
  'CM5_GBE_TD1_N':[(22,104),(11.5,104),(jack[0],jack[1])],
  'CM5_GBE_TD0_N':[(22,105),(15,105),(jack[0],jack[1])],
  'CM5_GBE_TD0_P':[(22,106),(18,106),(jack[0],jack[1])],}
 if name.endswith(('TD2_N','TD2_P','TD3_N','TD3_P')):
  q=paths[name][-1]; tr(b,n,[esd,q]+side[name][:-1],B); tr(b,n,[side[name][-2],jack],B)
 else:
  tr(b,n,[esd]+side[name],F)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
