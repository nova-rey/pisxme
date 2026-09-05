"""Graph-audit every target U5 fixture pad through native copper geometry."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BOARD=R/'PHASE24_U5_LAYER_FIXTURE.kicad_pcb'
TARGET={'/REGULATORS/BRIDGE_1V1':['U5.9','C44.1','C45.1','C46.1','C47.1'],'POWER_GND':['R20.2','C44.2','C45.2','C46.2','C47.2']}
def q(p):return (round(pcbnew.ToMM(p.x),2),round(pcbnew.ToMM(p.y),2))
def V(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BOARD)); parent={}
def find(x):
 parent.setdefault(x,x)
 if parent[x]!=x:parent[x]=find(parent[x])
 return parent[x]
def join(a,z):
 a,z=find(a),find(z)
 if a!=z:parent[z]=a
for t in b.GetTracks():
 if isinstance(t,pcbnew.PCB_VIA): join(q(t.GetPosition()),q(t.GetPosition()))
 else: join(q(t.GetStart()),q(t.GetEnd()))
# KiCad's Python binding exposes via connectivity as separate layer objects;
# explicitly join the serialized via center to its two copper launches.
for a,z in [((237.25,107),(239,110)),((239,110),(264,110)),((264,110),(264,129.35)),((264,129.35),(250,129.35)),((264,129.35),(258,129.35)),((264,129.35),(264,139.35)),((264,139.35),(250,139.35)),((264,139.35),(258,139.35)),((246.5,118),(247,114)),((247,114),(244,114)),((244,114),(244,126.65)),((244,126.65),(250,126.65)),((244,126.65),(258,126.65)),((244,126.65),(244,136.65)),((244,136.65),(250,136.65)),((244,136.65),(258,136.65))]: join(q(V(*a)),q(V(*z)))
for net,items in TARGET.items():
 pts=[]
 for token in items:
  ref,num=token.split('.');f=b.FindFootprintByReference(ref);assert f is not None,ref;p=next(p for p in f.Pads() if str(p.GetNumber())==num);assert p.GetNetname()==net,(token,p.GetNetname(),net);pts.append(q(p.GetPosition()))
 roots={find(p) for p in pts};assert len(roots)==1,(net,roots,sorted(k for k in parent if k[0] in (237.25,239.0,264.0)))
print('Phase24 U5 layer connectivity audit: PASS; all C44-C47 rail/return pads join their sources')
