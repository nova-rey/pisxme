"""Try the fully outboard SATA corridor beyond the frozen PCIe trunk."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb'
OUT=ROOT/'ACREAGE_PHASE19_SATA_RIGHT_EDGE.kicad_pcb'
W=pcbnew.FromMM(.15)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(q): return (pcbnew.ToMM(q.GetPosition().x),pcbnew.ToMM(q.GetPosition().y))
def pad(f,n): return next(q for q in f.Pads() if str(q.GetNumber())==str(n))
def tr(b,net,a,z,layer):
 q=pcbnew.PCB_TRACK(b); q.SetStart(V(*a)); q.SetEnd(V(*z)); q.SetLayer(layer); q.SetWidth(W); q.SetNet(net); b.Add(q)
def via(b,net,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.5)); q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(net); b.Add(q)

def main():
 b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U7'); j=b.FindFootprintByReference('J3')
 if not u or not j: raise RuntimeError('U7/J3 missing')
 u.SetPosition(V(110,105)); u.SetOrientationDegrees(180)
 j.SetPosition(V(230,100)); j.SetOrientationDegrees(90)
 specs=(
  ('BRIDGE_SATA_RX_P','60','3',(108,98),(214,98),(214,108.75),pcbnew.B_Cu),
  ('BRIDGE_SATA_RX_N','59','4',(109.5,99),(212,99),(212,108.5),pcbnew.B_Cu),
  ('BRIDGE_SATA_TX_P','57','1',(111,96),(220,96),(220,109.25),pcbnew.F_Cu),
  ('BRIDGE_SATA_TX_N','56','2',(112.5,97),(218,97),(218,109.0),pcbnew.F_Cu),
 )
 for name,up,jp,first,turn,down,layer in specs:
  net=b.FindNet('/STORAGE/'+name)
  if not net: raise RuntimeError('missing '+name)
  a=pad(u,up); z=pad(j,jp); a.SetNet(net); z.SetNet(net)
  tr(b,net,xy(a),first,pcbnew.F_Cu); via(b,net,*first)
  tr(b,net,first,turn,layer); tr(b,net,turn,down,layer); tr(b,net,down,xy(z),layer)
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
