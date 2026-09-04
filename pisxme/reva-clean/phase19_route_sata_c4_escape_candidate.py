"""Fan SATA around the existing C4 support, then clear frozen trunks."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb'; OUT=ROOT/'ACREAGE_PHASE19_SATA_C4_ESCAPE.kicad_pcb'; W=pcbnew.FromMM(.15)
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
 # The first dogleg clears C4; all long runs are above PER0 and the PCIe clock.
 specs=(
  ('BRIDGE_SATA_RX_P','60','3',(107,99),(120,83),(166,70)),
  ('BRIDGE_SATA_RX_N','59','4',(108,98.5),(122,84),(168,71)),
  ('BRIDGE_SATA_TX_P','57','1',(113,98.5),(124,85),(167,72)),
  ('BRIDGE_SATA_TX_N','56','2',(113.5,99),(126,86),(169,73)))
 for name,up,jp,dog,esc,via_pt in specs:
  n=b.FindNet('/STORAGE/'+name); a,z=pad(u,up),pad(j,jp); a.SetNet(n); z.SetNet(n)
  tr(b,n,xy(a),dog,pcbnew.F_Cu); tr(b,n,dog,esc,pcbnew.F_Cu); tr(b,n,esc,via_pt,pcbnew.F_Cu); via(b,n,*via_pt)
  tr(b,n,via_pt,(218,via_pt[1]),pcbnew.B_Cu); tr(b,n,(218,via_pt[1]),xy(z),pcbnew.B_Cu)
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
