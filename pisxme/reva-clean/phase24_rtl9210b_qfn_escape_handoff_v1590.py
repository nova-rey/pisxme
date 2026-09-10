"""V1590: fixed-orientation QFN source escape to explicit west handoffs."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_U155_REHOME_V1517.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_QFN_ESCAPE_HANDOFF_V1590.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
V=lambda x,y: pcbnew.VECTOR2I_MM(float(x),float(y))
NETS=(('REFCLK_P','61',70.4),('REFCLK_N','62',70.8),('LANE0_RXP','64',71.6),('LANE0_RXN','65',72.0),('LANE0_TXN','67',72.8),('LANE0_TXP','68',73.2))
b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U1')
for p in u.Pads(): p.SetLocalClearance(pcbnew.FromMM(.15))
def local(q):
 pts=[q.GetPosition()] if type(q).__name__=='PCB_VIA' else [q.GetStart(),q.GetEnd()]
 return any(87<=pcbnew.ToMM(p.x)<=106 and 63<=pcbnew.ToMM(p.y)<=80 for p in pts)
for q in list(b.GetTracks()):
 if q.GetNetname() in {n for n,_,_ in NETS} or local(q): b.RemoveNative(q)

fp=pcbnew.FOOTPRINT(b); fp.SetReference('JH1'); fp.SetValue('QFN_ESCAPE_HANDOFF'); fp.SetPosition(V(0,0)); fp.SetLayer(F); b.Add(fp)
for name,num,y in NETS:
 p=pcbnew.PAD(fp); p.SetNumber(num); p.SetPosition(V(85,y)); p.SetSize(V(.6,.2)); p.SetShape(pcbnew.PAD_SHAPE_RECT); p.SetAttribute(pcbnew.PAD_ATTRIB_SMD); ls=pcbnew.LSET(); ls.AddLayer(F); p.SetLayerSet(ls); p.SetNet(b.FindNet(name)); p.SetNetCode(b.FindNet(name).GetNetCode()); fp.Add(p)
for name,num,y in NETS:
 net=b.FindNet(name); src=next(p for p in u.Pads() if p.GetNumber()==num); a=src.GetPosition(); z=V(85,y)
 t=pcbnew.PCB_TRACK(b); t.SetStart(a); t.SetEnd(z); t.SetLayer(F); t.SetWidth(W); t.SetNet(net); t.SetNetCode(net.GetNetCode()); b.Add(t)
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
