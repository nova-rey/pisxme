"""V1255: isolated full lane path on a cleared upper B.Cu corridor."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent;BASE=H/'PHASE24_RTL9210B_LANE0_ALL_LOWER_LEFT_V1250.kicad_pcb';OUT=H/'PHASE24_RTL9210B_FULL_LANE_UPPER_ISOLATED_V1255.kicad_pcb';F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def inside(p):return 85<=pcbnew.ToMM(p.x)<=140 and 39<=pcbnew.ToMM(p.y)<=80
def s(b,n,l,ps):
 for a,z in zip(ps,ps[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(P(*a));q.SetEnd(P(*z));q.SetLayer(l);q.SetWidth(W);q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
def v(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(P(*p));q.SetWidth(pcbnew.FromMM(.60));q.SetDrill(pcbnew.FromMM(.30));q.SetNet(n);q.SetNetCode(n.GetNetCode());b.Add(q)
b=pcbnew.LoadBoard(str(BASE));
for q in list(b.GetTracks()):
 if inside(q.GetStart()) or inside(q.GetEnd()):b.RemoveNative(q)
for q in list(b.GetTracks()):
 if type(q).__name__=='PCB_VIA' and inside(q.GetPosition()):b.RemoveNative(q)
u=b.FindFootprintByReference('U1');j=b.FindFootprintByReference('J1')
# Correct V1250 source escape, followed by separated upper B.Cu rows.
src=[('LANE0_RXP','64',[(94.05,71.6),(95.0,71.6),(95.0,72.4)],(95.0,72.4),42.0,134.5,'43'),('LANE0_RXN','65',[(94.05,72.0),(93.2,72.0)],(93.2,72.0),42.8,133.0,'41'),('LANE0_TXN','67',[(94.05,72.8),(92.2,72.8),(92.2,72.6)],(92.2,72.6),44.0,135.0,'47'),('LANE0_TXP','68',[(94.05,73.2),(90.8,73.2),(90.8,76.8)],(90.8,76.8),44.8,137.0,'49')]
for name,pad,fp,vp,row,ex,jpad in src:
 n=b.FindNet(name);s(b,n,F,fp);v(b,n,vp);s(b,n,B,[vp,(vp[0],row),(ex,row)]);v(b,n,(ex,row));d=j.FindPadByNumber(jpad).GetPosition();dst=(pcbnew.ToMM(d.x),pcbnew.ToMM(d.y));s(b,n,F,[(ex,row),(dst[0],row),dst])
b.BuildListOfNets();pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
