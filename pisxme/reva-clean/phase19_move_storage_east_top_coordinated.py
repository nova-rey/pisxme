"""Coordinated open-east-top storage island with regenerated USB3 and SATA."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb'; OUT=ROOT/'ACREAGE_PHASE19_STORAGE_EAST_TOP_COORDINATED.kicad_pcb'; W=pcbnew.FromMM(.15)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def pad(f,n): return next(p for p in list(f.Pads()) if str(p.GetNumber())==str(n))
def tr(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);b.Add(t)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b);q.SetPosition(V(x,y));q.SetWidth(pcbnew.FromMM(.5));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);q.SetNet(n);b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U7');j=b.FindFootprintByReference('J3');src=b.FindFootprintByReference('J7')
 u.SetPosition(V(200,60));u.SetOrientationDegrees(180);j.SetPosition(V(260,35));j.SetOrientationDegrees(0)
 sp={str(p.GetNumber()):xy(p) for p in list(src.Pads())}; up={str(p.GetNumber()):xy(p) for p in list(u.Pads())}; jp={str(p.GetNumber()):xy(p) for p in list(j.Pads())}
 for t in list(b.GetTracks()):
  if 'USB3' in t.GetNetname(): b.Remove(t)
 # Source-side launches use the proven J7 dogbones, then B.Cu stays west of
 # the x=170 PCIe vertical until its transition into the open east top.
 usb=(
  ('CM5_USB3_RX_N','128','42',(72,103.9),166.0,30.0,190.0),
  ('CM5_USB3_RX_P','130','43',(72,104.8),167.2,31.0,191.0),
  ('CM5_USB3_TX_N','140','45',(72,108.0),168.3,32.0,192.0),
  ('CM5_USB3_TX_P','142','46',(71,109.0),169.5,33.0,193.0))
 for name,spn,upn,srcpt,x,y,topx in usb:
  n=b.FindNet('/CORE_CM5/'+name); a=sp[spn]; z=up[upn]
  tr(b,n,a,srcpt,pcbnew.F_Cu); via(b,n,*srcpt)
  tr(b,n,srcpt,(x,srcpt[1]),pcbnew.B_Cu); via(b,n,x,srcpt[1])
  # Cross the J1/CM5 fanout on F.Cu below its pads, then rise at x=180.
  tr(b,n,(x,srcpt[1]),(180,srcpt[1]),pcbnew.F_Cu); tr(b,n,(180,srcpt[1]),(180,y),pcbnew.F_Cu); via(b,n,180,y)
  tr(b,n,(180,y),(topx,y),pcbnew.B_Cu); via(b,n,topx,y)
  tr(b,n,(topx,y),z,pcbnew.F_Cu)
 # Short local SATA launch; RX is on B.Cu and TX on F.Cu after a clean
 # upward escape from U7's top pad row.
 sata=(('BRIDGE_SATA_TX_P','57','1',(200.5,25),(250.75,25),pcbnew.F_Cu),('BRIDGE_SATA_RX_P','60','3',(199.5,24),(251.25,24),pcbnew.B_Cu),('BRIDGE_SATA_TX_N','56','2',(201,26),(251,26),pcbnew.F_Cu),('BRIDGE_SATA_RX_N','59','4',(200,27),(251.5,27),pcbnew.B_Cu))
 for name,upn,jpn,turn,approach,layer in sata:
  n=b.FindNet('/STORAGE/'+name);a,z=up[upn],jp[jpn];tr(b,n,a,turn,pcbnew.F_Cu)
  if layer==pcbnew.B_Cu:via(b,n,*turn);tr(b,n,turn,approach,layer)
  else:tr(b,n,turn,approach,layer)
  tr(b,n,approach,z,layer)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
