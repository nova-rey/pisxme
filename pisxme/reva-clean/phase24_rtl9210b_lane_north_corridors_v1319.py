"""V1319: develop lanes around the V1058 support field, not through it."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_ROTATE_U2_SPI_V1058.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V1058_SUPPORT_LANE_NORTH_CORRIDORS_V1319.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
W=pcbnew.FromMM(.20); VW=pcbnew.FromMM(.60); VD=pcbnew.FromMM(.30)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
b=pcbnew.LoadBoard(str(BASE))
lanes={
 'LANE0_RXN':((94.05,72.0),(96.0,72.0),(125.0,34.0),(133.75,62.725)),
 'LANE0_RXP':((94.05,71.6),(97.0,71.6),(127.0,36.0),(134.25,62.725)),
 'LANE0_TXN':((94.05,72.8),(98.0,72.8),(129.0,38.0),(135.25,62.725)),
 'LANE0_TXP':((94.05,73.2),(99.0,73.2),(131.0,40.0),(135.75,62.725)),
}
for name in lanes:
 for t in list(b.GetTracks()):
  if t.GetNetname()==name: b.RemoveNative(t)
 n=b.FindNet(name)
 (pad,sv,fv,end)=lanes[name]
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*pad)); t.SetEnd(P(*sv)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*sv)); v.SetWidth(VW); v.SetDrill(VD); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*sv)); t.SetEnd(P(*fv)); t.SetLayer(B); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
 v=pcbnew.PCB_VIA(b); v.SetPosition(P(*fv)); v.SetWidth(VW); v.SetDrill(VD); v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*fv)); t.SetEnd(P(*end)); t.SetLayer(F); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
