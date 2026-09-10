"""V1547: bounded native sweep of compliant crystal source-spine positions."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RTL3V3_REHOME_U152_V1523.kicad_pcb'; V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y)); F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def tr(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):
  t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(F,B); q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
for xo in (90.6,91.0,91.4,91.8):
 for xi in (92.0,92.4,92.6,92.8):
  b=pcbnew.LoadBoard(str(BASE))
  for name in ('XTAL_IN','XTAL_OUT'):
   n=b.FindNet(name)
   for o in list(b.GetTracks()):
    if o.GetNetCode()==n.GetNetCode(): b.RemoveNative(o)
  no=b.FindNet('XTAL_OUT'); tr(b,no,[(94.05,67.6),(xo,67.6),(xo,62.8),(91,62.8),(91,62),(91,60.5),(89.4,59)],F)
  ni=b.FindNet('XTAL_IN'); tr(b,ni,[(94.05,67.2),(xi,67.2)],F); via(b,ni,xi,67.2); tr(b,ni,[(xi,67.2),(90.5,67.2)],B); via(b,ni,90.5,67.2); tr(b,ni,[(90.5,67.2),(90.5,63.2),(88,63.2),(88,62),(88,59)],F)
  out=H/f'PHASE24_RTL9210B_CRYSTAL_SWEEP_XO{xo:.1f}_XI{xi:.1f}.kicad_pcb'; b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(out)); print(out)
