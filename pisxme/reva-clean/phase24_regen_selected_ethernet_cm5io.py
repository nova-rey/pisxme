"""Adapt the validated Phase-17 CM5IO split-layer Ethernet escape."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_SELECTED_MACRO_PLACEMENT.kicad_pcb'
OUT=R/'PHASE24_SELECTED_MACRO_ETHERNET_CM5IO_REGEN.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=pcbnew.FromMM(.127)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def pad(b,ref,num): return xy(b.FindFootprintByReference(ref).FindPadByNumber(str(num)).GetPosition())
def add(b,n,pts,layer):
 for a,z in zip(pts,pts[1:]):
  if a==z: continue
  t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(layer);t.SetWidth(W);t.SetNet(n);b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*q));v.SetWidth(pcbnew.FromMM(.45));v.SetDrill(pcbnew.FromMM(.20));v.SetLayerPair(F,B);v.SetNet(n);b.Add(v)

b=pcbnew.LoadBoard(str(BASE))
for ref,pos,rot in (('U9',(24,68),180),('U6',(30,68),180),('J2',(24,45),180)):
 f=b.FindFootprintByReference(ref);f.SetPosition(V(*pos));f.SetOrientationDegrees(rot)
for t in list(b.GetTracks()):
 if any(k in t.GetNetname() for k in ('CM5_GBE_','/ETHERNET/','/GBE_')): b.Remove(t)
names={
 'CM5_GBE_TD3_P':('3','U9','5','J2','9'),'CM5_GBE_TD3_N':('5','U9','4','J2','10'),
 'CM5_GBE_TD2_N':('9','U9','2','J2','8'),'CM5_GBE_TD2_P':('11','U9','1','J2','7'),
 'CM5_GBE_TD1_P':('4','U6','6','J2','3'),'CM5_GBE_TD1_N':('6','U6','7','J2','6'),
 'CM5_GBE_TD0_N':('10','U6','9','J2','2'),'CM5_GBE_TD0_P':('12','U6','10','J2','1')}
# Exact split-layer escape coordinates from the CM5IO-derived Phase-17
# rotated-west oracle. All transitions are outside SMD pads.
src_paths={
 'CM5_GBE_TD3_P':([(32.96,99.10),(30.0,99.10),(24.0,67.0)],F),
 'CM5_GBE_TD3_N':([(32.96,99.50),(30.5,99.50),(24.5,67.5)],F),
 'CM5_GBE_TD2_N':([(32.96,100.30),(30.0,100.30),(25.0,68.5)],B),
 'CM5_GBE_TD2_P':([(32.96,100.70),(30.8,100.70),(25.8,69.0)],B),
 'CM5_GBE_TD1_P':([(36.04,99.10),(38.0,99.10),(31.5,67.0)],B),
 'CM5_GBE_TD1_N':([(36.04,99.50),(38.8,99.50),(32.3,67.5)],B),
 'CM5_GBE_TD0_N':([(36.04,100.30),(39.6,100.30),(33.1,68.5)],B),
 'CM5_GBE_TD0_P':([(36.04,100.70),(40.4,100.70),(33.9,69.0)],B)}
for name,(j7,eref,epad,jref,jpad) in names.items():
 n=b.FindNet(name); end=pad(b,eref,epad); start=pad(b,'J7',j7)
 pts,layer=src_paths[name]
 if layer==F:
  add(b,n,[start]+pts[1:]+[end],F)
 else:
  sv=pts[1]; ev=pts[2]; add(b,n,[start,sv],F);via(b,n,sv);add(b,n,[sv,ev],B);via(b,n,ev);add(b,n,[ev,end],F)
# Connector-side monotonic corridors, using actual MagJack pad centers.
lanes={
 'CM5_GBE_TD3_P':([(23.615,67.0),(16.0,67.0),(16.0,54.5)],F),
 'CM5_GBE_TD3_N':([(23.615,67.5),(16.5,67.5),(16.5,53.5)],F),
 'CM5_GBE_TD2_N':([(23.615,68.5),(17.0,68.5),(17.0,52.5)],B),
 'CM5_GBE_TD2_P':([(23.615,69.0),(17.5,69.0),(17.5,51.5)],B),
 'CM5_GBE_TD1_P':([(29.615,67.0),(31.0,67.0),(31.0,54.5)],F),
 'CM5_GBE_TD1_N':([(29.615,67.5),(31.5,67.5),(31.5,53.5)],F),
 'CM5_GBE_TD0_N':([(29.615,68.5),(32.0,68.5),(32.0,52.5)],B),
 'CM5_GBE_TD0_P':([(29.615,69.0),(32.5,69.0),(32.5,51.5)],B)}
for name,(j7,eref,epad,jref,jpad) in names.items():
 n=b.FindNet(name); start=pad(b,eref,epad); end=pad(b,jref,jpad)
 pts,layer=lanes[name]
 if layer==F: add(b,n,[start]+pts+[end],F)
 else:
  ev=(start[0]-.9,start[1]);add(b,n,[start,ev],F);via(b,n,ev);add(b,n,[ev]+pts[1:]+[end],B)
b.BuildListOfNets();b.Save(str(OUT));print(OUT)
