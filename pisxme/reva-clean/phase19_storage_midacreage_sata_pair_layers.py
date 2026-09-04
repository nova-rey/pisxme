"""Use one permitted copper layer per SATA pair with ordered launches."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb';OUT=ROOT/'ACREAGE_PHASE19_STORAGE_MIDACREAGE_SATA_PAIR_LAYERS.kicad_pcb';W=pcbnew.FromMM(.15)
def V(x,y):return pcbnew.VECTOR2I_MM(x,y)
def xy(p):return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def pad(f,n):return next(p for p in list(f.Pads()) if str(p.GetNumber())==str(n))
def tr(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);b.Add(t)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(V(x,y));q.SetWidth(pcbnew.FromMM(.5));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);q.SetNet(n);b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U7');j=b.FindFootprintByReference('J3')
 u.SetPosition(V(120,140));u.SetOrientationDegrees(180);j.SetPosition(V(145,125));j.SetOrientationDegrees(90)
 up={str(p.GetNumber()):xy(p) for p in list(u.Pads())};jp={str(p.GetNumber()):xy(p) for p in list(j.Pads())}
 # TX pair is monotonic on F.Cu.
 for name,upn,jpn,start,lane,final in (
  ('BRIDGE_SATA_TX_P','57','1',(120.5,120),(130,120),(130,134.25)),
  ('BRIDGE_SATA_TX_N','56','2',(121,122),(132,122),(132,134.0))):
  n=b.FindNet('/STORAGE/'+name);tr(b,n,up[upn],start,pcbnew.F_Cu);tr(b,n,start,lane,pcbnew.F_Cu);tr(b,n,lane,final,pcbnew.F_Cu);tr(b,n,final,jp[jpn],pcbnew.F_Cu)
 # RX pair is monotonic on B.Cu, with F.Cu dogbones only at the pads.
 for name,upn,jpn,start,lane,final in (
  ('BRIDGE_SATA_RX_P','60','3',(119,121),(136,121),(136,133.75)),
  ('BRIDGE_SATA_RX_N','59','4',(119.5,123),(144,123),(144,133.5))):
  n=b.FindNet('/STORAGE/'+name);tr(b,n,up[upn],start,pcbnew.F_Cu);via(b,n,*start);tr(b,n,start,lane,pcbnew.B_Cu);tr(b,n,lane,final,pcbnew.B_Cu);via(b,n,*final);tr(b,n,final,jp[jpn],pcbnew.F_Cu)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
