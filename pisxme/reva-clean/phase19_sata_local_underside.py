"""Phase 19 local underside M.2 trial; preserve U7 and Phase 18 USB3."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; B0=R/'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb'; O=R/'ACREAGE_PHASE19_SATA_LOCAL_UNDERSIDE.kicad_pcb'; W=pcbnew.FromMM(.13208)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def P(f,n): return next(p for p in list(f.Pads()) if str(p.GetNumber())==str(n))
def T(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);b.Add(t)
def X(b,n,p):
 q=pcbnew.PCB_VIA(b);q.SetPosition(V(*p));q.SetWidth(pcbnew.FromMM(.5));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);q.SetNet(n);b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(B0));u=b.FindFootprintByReference('U7');j=b.FindFootprintByReference('J3');j.SetPosition(V(115,125));j.SetOrientationDegrees(0);j.SetLayer(pcbnew.B_Cu)
 up={str(p.GetNumber()):xy(p) for p in list(u.Pads())};jp={str(p.GetNumber()):xy(p) for p in list(j.Pads())}
 for name,un,jn in (('BRIDGE_SATA_TX_P','57','1'),('BRIDGE_SATA_TX_N','56','2'),('BRIDGE_SATA_RX_P','60','3'),('BRIDGE_SATA_RX_N','59','4')):
  n=b.FindNet('/STORAGE/'+name);P(u,un).SetNet(n);P(j,jn).SetNet(n)
 # TX approaches the two adjacent connector pads from the right.
 n=b.FindNet('/STORAGE/BRIDGE_SATA_TX_P');T(b,n,up['57'],(112,114),pcbnew.F_Cu);T(b,n,(112,114),(112,117.5),pcbnew.F_Cu);T(b,n,(112,117.5),(107.75,117.5),pcbnew.F_Cu);X(b,n,(107.75,117.5));T(b,n,(107.75,117.5),jp['1'],pcbnew.B_Cu)
 n=b.FindNet('/STORAGE/BRIDGE_SATA_TX_N');T(b,n,up['56'],(113,114),pcbnew.F_Cu);T(b,n,(113,114),(113,125.5),pcbnew.F_Cu);T(b,n,(113,125.5),(108,125.5),pcbnew.F_Cu);X(b,n,(108,125.5));T(b,n,(108,125.5),jp['2'],pcbnew.B_Cu)
 # RX approaches the same pad rows from the left on B.Cu.
 for name,un,jn,src,via,turn in (('BRIDGE_SATA_RX_P','60','3',(109,113),(104,113),(103,119.725)),('BRIDGE_SATA_RX_N','59','4',(109.5,114),(104.5,114),(103.5,127.275))):
  n=b.FindNet('/STORAGE/'+name);T(b,n,up[un],src,pcbnew.F_Cu);X(b,n,via);T(b,n,src,via,pcbnew.F_Cu);T(b,n,via,turn,pcbnew.B_Cu);T(b,n,turn,jp[jn],pcbnew.B_Cu)
 b.BuildListOfNets();b.Save(str(O));print(O)
if __name__=='__main__':main()
