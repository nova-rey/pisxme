"""Disposable native U7 SATA RX-N repeated-pad stitch on current basis."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_POWER_GND_CURRENT_LOCAL.kicad_pcb'; OUT=R/'PHASE24_U7_RXN_CURRENT_LOCAL.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/STORAGE/BRIDGE_SATA_RX_N')
V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
def t(a,z,l=pcbnew.F_Cu):
    q=pcbnew.PCB_TRACK(b); q.SetStart(V(*a)); q.SetEnd(V(*z)); q.SetLayer(l); q.SetWidth(pcbnew.FromMM(.20)); q.SetNet(n); b.Add(q)
def via(q):
    v=pcbnew.PCB_VIA(b); v.SetPosition(V(*q)); v.SetWidth(pcbnew.FromMM(.50)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
# Stitch the five same-net U7 pads, then use the existing external pad at U7.59.
for y1,y2 in zip((142.5,142.0,141.5,141.0),(142.0,141.5,141.0,140.5)): t((124.5,y1),(124.5,y2))
t((124.5,140.5),(127.5,140.5)); via((127.5,140.5)); t((127.5,140.5),(127.5,132.0),pcbnew.B_Cu); t((127.5,132.0),(119.5,132.0),pcbnew.B_Cu); t((119.5,132.0),(119.5,134.5),pcbnew.B_Cu); via((119.5,134.5)); t((119.5,134.5),(119.5,135.5))
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
