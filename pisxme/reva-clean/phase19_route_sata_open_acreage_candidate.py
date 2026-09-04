"""SATA island in open acreage: escape U7 above all frozen trunks."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb'; OUT=ROOT/'ACREAGE_PHASE19_SATA_OPEN_ACREAGE.kicad_pcb'
W=pcbnew.FromMM(.15)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def pad(f,n): return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def tr(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); b.Add(t)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.5)); q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U7'); j=b.FindFootprintByReference('J3'); c=b.FindFootprintByReference('C4')
 u.SetPosition(V(110,105)); u.SetOrientationDegrees(180); j.SetPosition(V(220,60)); j.SetOrientationDegrees(0)
 # C4 is local bridge support; move it clear of the U7 SATA escape.
 c.SetPosition(V(130,95))
 specs=(
  ('BRIDGE_SATA_RX_P','60','3',(116,74),(165,70),pcbnew.B_Cu),
  ('BRIDGE_SATA_RX_N','59','4',(118,75),(166,71),pcbnew.B_Cu),
  ('BRIDGE_SATA_TX_P','57','1',(120,78),(218,78),pcbnew.F_Cu),
  ('BRIDGE_SATA_TX_N','56','2',(122,79),(219,79),pcbnew.F_Cu))
 for name,up,jp,first,turn,layer in specs:
  n=b.FindNet('/STORAGE/'+name); a,z=pad(u,up),pad(j,jp); a.SetNet(n); z.SetNet(n)
  tr(b,n,xy(a),first,pcbnew.F_Cu); via(b,n,*first); tr(b,n,first,turn,layer); tr(b,n,turn,xy(z),layer)
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
