"""Move the complete storage island into open acreage above frozen routing."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb'; OUT=ROOT/'ACREAGE_PHASE19_STORAGE_TOP_ISLAND.kicad_pcb'; W=pcbnew.FromMM(.15)
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def pad(f,n): return next(p for p in list(f.Pads()) if str(p.GetNumber())==str(n))
def tr(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); b.Add(t)
def via(b,n,x,y):
 q=pcbnew.PCB_VIA(b); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.5)); q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)
def main():
 b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U7'); j=b.FindFootprintByReference('J3'); src=b.FindFootprintByReference('J7')
 u.SetPosition(V(130,60)); u.SetOrientationDegrees(180); j.SetPosition(V(180,60)); j.SetOrientationDegrees(0)
 src_pos={str(p.GetNumber()):xy(p) for p in list(src.Pads())}
 u_pos={str(p.GetNumber()):xy(p) for p in list(u.Pads())}
 j_pos={str(p.GetNumber()):xy(p) for p in list(j.Pads())}
 # Remove only the old phase-18 USB3 copper; the storage schematic authority is unchanged.
 for t in list(b.GetTracks()):
  if 'USB3' in t.GetNetname(): b.Remove(t)
 # Rebuild CM5->bridge USB3 through a high top-edge corridor.
 usb=(('CM5_USB3_RX_N','128','42',(74,103.9),(74,40)),('CM5_USB3_RX_P','130','43',(76,104.3),(76,41)),('CM5_USB3_TX_N','140','45',(78,106.3),(78,42)),('CM5_USB3_TX_P','142','46',(80,106.7),(80,43)))
 for name,sp,up,src_pt,via_pt in usb:
  n=b.FindNet('/CORE_CM5/'+name); a,z=src_pos[sp],u_pos[up]
  tr(b,n,a,src_pt,pcbnew.F_Cu); tr(b,n,src_pt,(src_pt[0],via_pt[1]),pcbnew.F_Cu)
  via(b,n,*via_pt); tr(b,n,via_pt,(120,via_pt[1]),pcbnew.B_Cu)
  via(b,n,120,via_pt[1]); tr(b,n,(120,via_pt[1]),z,pcbnew.F_Cu)
 # SATA is now a short monotonic launch, with pair lanes separated by side/layer.
 sata=(('BRIDGE_SATA_TX_P','57','1',(129.5,48),(170.75,54.73),pcbnew.F_Cu),('BRIDGE_SATA_RX_P','60','3',(129,49),(171.25,54.73),pcbnew.B_Cu),('BRIDGE_SATA_TX_N','56','2',(130.5,50),(171,62.27),pcbnew.F_Cu),('BRIDGE_SATA_RX_N','59','4',(130,51),(171.5,62.27),pcbnew.B_Cu))
 for name,up,jp,turn,end,layer in sata:
  n=b.FindNet('/STORAGE/'+name); a,z=u_pos[up],j_pos[jp]
  tr(b,n,a,turn,pcbnew.F_Cu)
  if layer==pcbnew.B_Cu: via(b,n,*turn); tr(b,n,turn,end,layer)
  else: tr(b,n,turn,end,layer)
 b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
