"""Try a short local SATA corridor with J3 below U7 in open acreage."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb'; OUT=ROOT/'ACREAGE_PHASE19_SATA_LOCAL_OPEN.kicad_pcb'
W=pcbnew.FromMM(.15)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def pad(f,n): return next(q for q in f.Pads() if str(q.GetNumber())==str(n))
def xy(q): return (pcbnew.ToMM(q.GetPosition().x),pcbnew.ToMM(q.GetPosition().y))
def tr(b,n,a,z,l):
 q=pcbnew.PCB_TRACK(b); q.SetStart(V(*a)); q.SetEnd(V(*z)); q.SetLayer(l); q.SetWidth(W); q.SetNet(n); b.Add(q)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.5)); q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U7'); j=b.FindFootprintByReference('J3')
 u.SetPosition(V(110,105)); u.SetOrientationDegrees(180)
 j.SetPosition(V(120,120)); j.SetOrientationDegrees(90)
 specs=(('BRIDGE_SATA_RX_P','60','3',(108,102)),('BRIDGE_SATA_RX_N','59','4',(109.5,103)),('BRIDGE_SATA_TX_P','57','1',(111,102)),('BRIDGE_SATA_TX_N','56','2',(112.5,103)))
 for name,up,jp,first in specs:
  n=b.FindNet('/STORAGE/'+name); a=pad(u,up); z=pad(j,jp); a.SetNet(n); z.SetNet(n)
  tr(b,n,xy(a),first,pcbnew.F_Cu); via(b,n,*first); tr(b,n,first,xy(z),pcbnew.F_Cu)
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
