"""V1303: transplant the accepted V1165 crystal pair onto V1279."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb'; DONOR=H/'PHASE24_RTL9210B_CRYSTAL_POCKET_RELOCATED_V1165.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_V1165_CRYSTAL_ON_V1279_V1303.kicad_pcb'; NETS={'XTAL_IN','XTAL_OUT'}
def copy_item(b,item,n):
 if type(item).__name__=='PCB_VIA':
  q=pcbnew.PCB_VIA(b); q.SetPosition(item.GetPosition()); q.SetWidth(item.GetWidth(pcbnew.F_Cu)); q.SetDrill(item.GetDrill()); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu)
 else:
  q=pcbnew.PCB_TRACK(b); q.SetStart(item.GetStart()); q.SetEnd(item.GetEnd()); q.SetLayer(item.GetLayer()); q.SetWidth(item.GetWidth())
 q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b=pcbnew.LoadBoard(str(BASE)); d=pcbnew.LoadBoard(str(DONOR))
for q in list(b.GetTracks()):
 if q.GetNetname() in NETS: b.RemoveNative(q)
for q in d.GetTracks():
 if q.GetNetname() in NETS: copy_item(b,q,b.FindNet(q.GetNetname()))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
