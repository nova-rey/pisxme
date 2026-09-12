#!/usr/bin/env python3
"""Coordinated east U12 migration with a B.Cu four-lane USB3 funnel."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'PHASE24_STORAGE_MKEY_USB3_U12_LEFT_R80_MOVE_20260912.kicad_pcb'
OUT=ROOT/'PHASE24_STORAGE_MKEY_USB3_U12_EAST_COORDINATED_20260912.kicad_pcb'
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
u.SetPosition(u.GetPosition()+V(15,0))
for p in u.Pads(): p.SetLocalClearance(pcbnew.FromMM(.15))
# All four lanes cross the intervening F.Cu-only PERST corridor on B.Cu.
tr(b,'CM5_USB3_RX_N',(145,100),(145,120)); vi(b,'CM5_USB3_RX_N',(145,120)); tr(b,'CM5_USB3_RX_N',(145,120),(160.0,120),pcbnew.B_Cu); tr(b,'CM5_USB3_RX_N',(160.0,120),(160.0,137.8),pcbnew.B_Cu); vi(b,'CM5_USB3_RX_N',(160.0,137.8)); tr(b,'CM5_USB3_RX_N',(160.0,137.8),(163.5,137.8))
tr(b,'CM5_USB3_RX_P',(147,104),(147,118)); vi(b,'CM5_USB3_RX_P',(147,118)); tr(b,'CM5_USB3_RX_P',(147,118),(160.6,118),pcbnew.B_Cu); tr(b,'CM5_USB3_RX_P',(160.6,118),(160.6,137.4),pcbnew.B_Cu); vi(b,'CM5_USB3_RX_P',(160.6,137.4)); tr(b,'CM5_USB3_RX_P',(160.6,137.4),(163.5,137.4))
tr(b,'CM5_USB3_TX_N',(149,108),(149,116)); vi(b,'CM5_USB3_TX_N',(149,116)); tr(b,'CM5_USB3_TX_N',(149,116),(161.2,116),pcbnew.B_Cu); tr(b,'CM5_USB3_TX_N',(161.2,116),(161.2,136.2),pcbnew.B_Cu); vi(b,'CM5_USB3_TX_N',(161.2,136.2)); tr(b,'CM5_USB3_TX_N',(161.2,136.2),(163.5,136.2))
# The accepted source escape already owns the TX_P via at (151,112).
tr(b,'CM5_USB3_TX_P',(151,112),(161.8,112),pcbnew.B_Cu); tr(b,'CM5_USB3_TX_P',(161.8,112),(161.8,135.8),pcbnew.B_Cu); vi(b,'CM5_USB3_TX_P',(161.8,135.8)); tr(b,'CM5_USB3_TX_P',(161.8,135.8),(163.5,135.8))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
