"""Move U7/J3 to open east acreage; keep this candidate SATA-first."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb'; OUT=ROOT/'ACREAGE_PHASE19_STORAGE_EAST_ISLAND.kicad_pcb'; W=pcbnew.FromMM(.15)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def pad(f,n): return next(p for p in list(f.Pads()) if str(p.GetNumber())==str(n))
def tr(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);b.Add(t)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(V(x,y));q.SetWidth(pcbnew.FromMM(.5));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);q.SetNet(n);b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U7');j=b.FindFootprintByReference('J3')
 u.SetPosition(V(200,150));u.SetOrientationDegrees(180);j.SetPosition(V(225,150));j.SetOrientationDegrees(0)
 upos={str(p.GetNumber()):xy(p) for p in list(u.Pads())}; jpos={str(p.GetNumber()):xy(p) for p in list(j.Pads())}
 for t in list(b.GetTracks()):
  if 'USB3' in t.GetNetname(): b.Remove(t)
 sata=(('BRIDGE_SATA_TX_P','57','1',(200.5,142),pcbnew.F_Cu),('BRIDGE_SATA_RX_P','60','3',(201,143),pcbnew.B_Cu),('BRIDGE_SATA_TX_N','56','2',(201.5,144),pcbnew.F_Cu),('BRIDGE_SATA_RX_N','59','4',(202,145),pcbnew.B_Cu))
 for name,up,jp,turn,layer in sata:
  n=b.FindNet('/STORAGE/'+name);a,z=upos[up],jpos[jp];tr(b,n,a,turn,pcbnew.F_Cu)
  if layer==pcbnew.B_Cu:via(b,n,*turn);tr(b,n,turn,z,layer)
  else:tr(b,n,turn,z,layer)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
