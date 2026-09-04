"""Exit U7 below the CM5 PER0 trunk, then cross it only on B.Cu."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb'; OUT=ROOT/'ACREAGE_PHASE19_SATA_POST_PER0.kicad_pcb'
W=pcbnew.FromMM(.15)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def pad(f,n): return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def tr(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); b.Add(t)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.5)); q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U7'); j=b.FindFootprintByReference('J3')
 u.SetPosition(V(110,105)); u.SetOrientationDegrees(180); j.SetPosition(V(220,60)); j.SetOrientationDegrees(0)
 # The F.Cu escape remains below y=82 until x>165, the PER0 endpoint.
 specs=(
  ('BRIDGE_SATA_TX_P','57','1',(166,100.5),(166,70),pcbnew.B_Cu),
  ('BRIDGE_SATA_RX_P','60','3',(168,100.5),(168,71),pcbnew.B_Cu),
  ('BRIDGE_SATA_TX_N','56','2',(167,100.5),(167,72),pcbnew.B_Cu),
  ('BRIDGE_SATA_RX_N','59','4',(169,100.5),(169,73),pcbnew.B_Cu))
 for name,up,jp,first,turn,layer in specs:
  n=b.FindNet('/STORAGE/'+name); a,z=pad(u,up),pad(j,jp); a.SetNet(n); z.SetNet(n)
  tr(b,n,xy(a),first,pcbnew.F_Cu); via(b,n,*first); tr(b,n,first,turn,layer); tr(b,n,turn,xy(z),layer)
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
