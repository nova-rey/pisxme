"""V255: obstacle-aware native-geometry A* escape for U1.40 RTL_1V1."""
from pathlib import Path
import heapq, math, pcbnew
HERE=Path(__file__).resolve().parent;BASE=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V242.kicad_pcb';OUT=HERE/'PHASE24_RTL9210B_RTL1V1_U136_U139_U152_V255.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu
S=.1; X0,X1,Y0,Y1=88.0,116.0,50.0,75.0; CLEAR=.10
def xy(q):return q.x/1e6,q.y/1e6
def P(x,y):return pcbnew.VECTOR2I_MM(x,y)
def dist(px,py,ax,ay,bx,by):
 dx,dy=bx-ax,by-ay; t=max(0,min(1,((px-ax)*dx+(py-ay)*dy)/(dx*dx+dy*dy or 1)));return math.hypot(px-(ax+t*dx),py-(ay+t*dy))
def main():
 b=pcbnew.LoadBoard(str(BASE));net=b.FindNet('RTL_1V1');u=b.FindFootprintByReference('U1');start=(round((94.05-X0)/S),round((60.8-Y0)/S),0);target=(round((103.5-X0)/S),round((57.5-Y0)/S),0)
 obs=[[],[]]
 for fp in b.GetFootprints():
  for p in fp.Pads():
   if p.GetNetCode()==net.GetNetCode():continue
   x,y=xy(p.GetPosition());r=max(p.GetSize().x,p.GetSize().y)/2e6+CLEAR
   if p.GetLayerSet().Contains(F):obs[0].append((x,y,r,None))
   if p.GetLayerSet().Contains(B):obs[1].append((x,y,r,None))
 for t in b.GetTracks():
  if t.GetNetCode()==net.GetNetCode():continue
  l=0 if t.GetLayer()==F else 1 if t.GetLayer()==B else -1
  if l<0:continue
  a=xy(t.GetStart());z=xy(t.GetEnd());obs[l].append((a[0],a[1],t.GetWidth()/2e6+CLEAR,(z[0],z[1])))
 for t in b.GetTracks():
  if type(t).__name__!='PCB_VIA' or t.GetNetCode()==net.GetNetCode():continue
  x,y=xy(t.GetPosition());r=t.GetWidth(0)/2e6+CLEAR
  for l in (0,1):obs[l].append((x,y,r,None))
 def blocked(x,y,l,allow=False):
  if not (X0<=x<=X1 and Y0<=y<=Y1):return True
  if allow and math.hypot(x-94.05,y-60.8)<=.45:return False
  if allow:return False
  return any((math.hypot(x-a,y-c)<=r if e is None else dist(x,y,a,c,e[0],e[1])<=r) for a,c,r,e in obs[l])
 def cell(k):return (X0+k[0]*S,Y0+k[1]*S)
 def coord(k):
  if k==start:return (94.05,60.8)
  if k==target:return (103.5,57.5)
  return cell(k)
 openq=[(0,start)];came={};g={start:0};seen=set()
 while openq:
  _,q=heapq.heappop(openq)
  if q in seen:continue
  seen.add(q)
  if q==target:break
  x,y=cell(q); dirs=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
  for dx,dy,dl in dirs:
   n=(q[0]+dx,q[1]+dy,q[2]+dl); nx,ny=cell(n)
   if n[2] not in (0,1) or not (0<=n[0]<=round((X1-X0)/S) and 0<=n[1]<=round((Y1-Y0)/S)):continue
   if dl==0 and blocked(nx,ny,n[2],q==start or n==target or n==start):continue
   if dl and (blocked(x,y,0) or blocked(x,y,1)) and q not in (start,target):continue
   cost=1 if dl==0 else 6; ng=g[q]+cost
   if ng<g.get(n,1e9):
    came[n]=q;g[n]=ng;h=abs(n[0]-target[0])+abs(n[1]-target[1])+3*abs(n[2]-target[2]);heapq.heappush(openq,(ng+h,n))
 if target not in came:raise RuntimeError('A* found no native obstacle-free path')
 path=[target]
 while path[-1]!=start:path.append(came[path[-1]])
 path=path[::-1]
 # emit compressed same-layer runs and ordinary vias at layer changes
 def add(a,z,l):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(F if l==0 else B);q.SetWidth(pcbnew.FromMM(.13));q.SetNet(net);q.SetNetCode(net.GetNetCode());b.Add(q)
 i=0
 while i<len(path)-1:
  q=path[i];n=path[i+1];a=coord(q)
  if q[2]!=n[2]:
   v=pcbnew.PCB_VIA(b);v.SetPosition(P(*a));v.SetWidth(pcbnew.FromMM(.50));v.SetDrill(pcbnew.FromMM(.25));v.SetLayerPair(F,B);v.SetNet(net);v.SetNetCode(net.GetNetCode());b.Add(v);i+=1;continue
  j=i+1
  while j+1<len(path) and path[j+1][2]==q[2] and (path[j][0]-q[0],path[j][1]-q[1])==(path[j+1][0]-path[j][0],path[j+1][1]-path[j][1]):j+=1
  add(a,coord(path[j]),q[2]);i=j
 b.BuildListOfNets();b.Save(str(OUT));print(OUT,'path_nodes',len(path),'cost',g[target])
if __name__=='__main__':main()
