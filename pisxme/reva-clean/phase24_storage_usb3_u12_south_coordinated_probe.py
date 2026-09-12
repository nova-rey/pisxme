#!/usr/bin/env python3
"""Coordinated south U12 migration preserving the accepted source escape."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'PHASE24_STORAGE_MKEY_USB3_U12_LEFT_R80_MOVE_20260912.kicad_pcb'
OUT=ROOT/'PHASE24_STORAGE_MKEY_USB3_U12_SOUTH_COORDINATED_20260912.kicad_pcb'
NETS=('CM5_USB3_RX_N','CM5_USB3_RX_P','CM5_USB3_TX_N','CM5_USB3_TX_P')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z,l=pcbnew.F_Cu):
 q=b.FindNet(n); t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.13208)); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
def vi(b,n,p):
 q=b.FindNet(n); v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetNet(q); v.SetNetCode(q.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(BASE))
if b is None: raise SystemExit('cannot load base')
for x in list(b.GetTracks()):
 if isinstance(x,pcbnew.PCB_VIA) or x.GetNetname() not in NETS: continue
 a,z=x.GetStart(),x.GetEnd(); ax,ay,zx,zy=map(pcbnew.ToMM,(a.x,a.y,z.x,z.y))
 if max(ay,zy)>112 and min(ax,zx)>140: b.RemoveNative(x)
u=b.FindFootprintByReference('U12')
if u is None: raise SystemExit('missing U12')
u.SetPosition(u.GetPosition()+V(0,20))
for p in u.Pads(): p.SetLocalClearance(pcbnew.FromMM(.15))
# RX F.Cu: source RX_N is the straight lane; RX_P turns below it.
tr(b,'CM5_USB3_RX_N',(145,100),(145,157.8)); tr(b,'CM5_USB3_RX_N',(145,157.8),(148.5,157.8))
tr(b,'CM5_USB3_RX_P',(147,104),(147,154)); tr(b,'CM5_USB3_RX_P',(147,154),(145.6,154)); tr(b,'CM5_USB3_RX_P',(145.6,154),(145.6,157.4)); tr(b,'CM5_USB3_RX_P',(145.6,157.4),(148.5,157.4))
# TX B.Cu: separate source turns and west return vias keep the pair away from
# the exposed/power pad field and from the RX F.Cu corridors.
tr(b,'CM5_USB3_TX_N',(149,108),(149,150)); vi(b,'CM5_USB3_TX_N',(149,150)); tr(b,'CM5_USB3_TX_N',(149,150),(146.2,150),pcbnew.B_Cu); tr(b,'CM5_USB3_TX_N',(146.2,150),(146.2,154.5),pcbnew.B_Cu); vi(b,'CM5_USB3_TX_N',(146.2,154.5)); tr(b,'CM5_USB3_TX_N',(146.2,154.5),(148.5,156.2))
tr(b,'CM5_USB3_TX_P',(151,112),(151,152),pcbnew.F_Cu); vi(b,'CM5_USB3_TX_P',(151,152)); tr(b,'CM5_USB3_TX_P',(151,152),(146.8,152),pcbnew.B_Cu); tr(b,'CM5_USB3_TX_P',(146.8,152),(146.8,154),pcbnew.B_Cu); vi(b,'CM5_USB3_TX_P',(146.8,154)); tr(b,'CM5_USB3_TX_P',(146.8,154),(148.3,155.8))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
