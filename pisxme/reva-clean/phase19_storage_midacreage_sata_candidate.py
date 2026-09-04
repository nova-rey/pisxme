"""Test SATA-only local island in the open mid-acreage region."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb';OUT=ROOT/'ACREAGE_PHASE19_STORAGE_MIDACREAGE_SATA.kicad_pcb';W=pcbnew.FromMM(.15)
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
 for name,upn,jpn,turn,approach,layer in (
  ('BRIDGE_SATA_TX_P','57','1',(120.5,132),(139.72,134.25),pcbnew.F_Cu),
  ('BRIDGE_SATA_RX_P','60','3',(119,131),(139.72,133.75),pcbnew.B_Cu),
  ('BRIDGE_SATA_TX_N','56','2',(121,133),(147.28,134),pcbnew.F_Cu),
  ('BRIDGE_SATA_RX_N','59','4',(119.5,134),(147.28,133.5),pcbnew.B_Cu)):
  n=b.FindNet('/STORAGE/'+name);a,z=up[upn],jp[jpn];tr(b,n,a,turn,pcbnew.F_Cu)
  if layer==pcbnew.B_Cu:
   via(b,n,*turn)
   final_via=(135,133.75) if name.endswith('RX_P') else (143,133.5)
   tr(b,n,turn,final_via,layer); via(b,n,*final_via); tr(b,n,final_via,approach,pcbnew.F_Cu)
  else:tr(b,n,turn,approach,layer)
  tr(b,n,approach,z,layer)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
