"""Phase 19 underside M.2 endpoint trial; U7/USB3 are unchanged."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent; BASE=ROOT/'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb'; OUT=ROOT/'ACREAGE_PHASE19_SATA_UNDERSIDE_ENDPOINT.kicad_pcb'; W=pcbnew.FromMM(.13208)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def pad(f,n): return next(p for p in list(f.Pads()) if str(p.GetNumber())==str(n))
def tr(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);b.Add(t)
def via(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(V(*p));q.SetWidth(pcbnew.FromMM(.5));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);q.SetNet(n);b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE));u=b.FindFootprintByReference('U7');j=b.FindFootprintByReference('J3');j.SetPosition(V(180,125));j.SetOrientationDegrees(0);j.SetLayer(pcbnew.B_Cu)
 up={str(p.GetNumber()):xy(p) for p in list(u.Pads())};jp={str(p.GetNumber()):xy(p) for p in list(j.Pads())}
 for name,un,jn in (('BRIDGE_SATA_TX_P','57','1'),('BRIDGE_SATA_TX_N','56','2'),('BRIDGE_SATA_RX_P','60','3'),('BRIDGE_SATA_RX_N','59','4')):
  n=b.FindNet('/STORAGE/'+name);pad(u,un).SetNet(n);pad(j,jn).SetNet(n)
 # TX pair on F.Cu, then connector-side transitions outside the bottom pads.
 for name,un,jn,src,mid,esc in (('BRIDGE_SATA_TX_P','57','1',(110.5,96),(150,96),(169,116)),('BRIDGE_SATA_TX_N','56','2',(111,97),(151,97),(169,124))):
  n=b.FindNet('/STORAGE/'+name);tr(b,n,up[un],src,pcbnew.F_Cu);tr(b,n,src,mid,pcbnew.F_Cu);tr(b,n,mid,esc,pcbnew.F_Cu);via(b,n,esc);tr(b,n,esc,jp[jn],pcbnew.B_Cu)
 # RX pair drops early to B.Cu and remains there to the connector launch.
 for name,un,jn,src,mid,turn,esc in (('BRIDGE_SATA_RX_P','60','3',(109,103),(150,103),(175,118),(173,118)),('BRIDGE_SATA_RX_N','59','4',(109.5,105.5),(151,105.5),(176,126),(173,126))):
  n=b.FindNet('/STORAGE/'+name);tr(b,n,up[un],src,pcbnew.F_Cu);via(b,n,src);tr(b,n,src,mid,pcbnew.B_Cu);tr(b,n,mid,(turn[0],mid[1]),pcbnew.B_Cu);tr(b,n,(turn[0],mid[1]),turn,pcbnew.B_Cu);tr(b,n,turn,esc,pcbnew.B_Cu);via(b,n,esc);tr(b,n,esc,jp[jn],pcbnew.B_Cu)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
