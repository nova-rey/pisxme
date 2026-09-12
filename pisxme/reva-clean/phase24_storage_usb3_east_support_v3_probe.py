#!/usr/bin/env python3
"""Support V3: local U11 fine escape plus four ordered B.Cu support lanes."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'PHASE24_STORAGE_MKEY_USB3_U12_EAST_COORDINATED_20260912.kicad_pcb'
OUT=ROOT/'PHASE24_STORAGE_MKEY_USB3_EAST_SUPPORT_V3_20260912.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z,l=pcbnew.F_Cu,w=.13208):
 q=b.FindNet(n); t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
def vi(b,n,p):
 q=b.FindNet(n); v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetNet(q); v.SetNetCode(q.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(BASE))
if b is None: raise SystemExit('cannot load base')
c86=b.FindFootprintByReference('C86'); c87=b.FindFootprintByReference('C87')
if c86 is None or c87 is None: raise SystemExit('missing C86/C87')
c86.SetPosition(V(145,145)); c87.SetPosition(V(145,149))
for f in (b.FindFootprintByReference('U11'),b.FindFootprintByReference('U12')):
 for p in f.Pads(): p.SetLocalClearance(pcbnew.FromMM(.10))
# Local U11 TX escape uses 0.10 mm trace/0.10 mm pad clearance only at the
# fine-pitch source.  Cap pads are actual post-transform positions.
tr(b,'USB_TXP1',(141.4,138.6),(141.4,137.7),w=.10); tr(b,'USB_TXP1',(141.4,137.7),(144.5,145))
tr(b,'USB_TXN1',(141.0,138.6),(141.0,139.6),w=.10); tr(b,'USB_TXN1',(141.0,139.6),(144.5,149))
# Long TX legs: B.Cu channels at y=141/143; target returns approach U12
# from the right, outside the exposed/power pad envelope.
tr(b,'JMS_USB3_TXP',(145.5,145),(146,145)); vi(b,'JMS_USB3_TXP',(146,145)); tr(b,'JMS_USB3_TXP',(146,145),(146,141),pcbnew.B_Cu); tr(b,'JMS_USB3_TXP',(146,141),(168,141),pcbnew.B_Cu); tr(b,'JMS_USB3_TXP',(168,141),(168,137.0),pcbnew.B_Cu); vi(b,'JMS_USB3_TXP',(168,137)); tr(b,'JMS_USB3_TXP',(168,137),(166.5,137.0))
tr(b,'JMS_USB3_TXN',(145.5,149),(146.6,149)); vi(b,'JMS_USB3_TXN',(146.6,149)); tr(b,'JMS_USB3_TXN',(146.6,149),(146.6,143),pcbnew.B_Cu); tr(b,'JMS_USB3_TXN',(146.6,143),(168.6,143),pcbnew.B_Cu); tr(b,'JMS_USB3_TXN',(168.6,143),(168.6,137.4),pcbnew.B_Cu); vi(b,'JMS_USB3_TXN',(168.6,137.4)); tr(b,'JMS_USB3_TXN',(168.6,137.4),(166.5,137.4))
# RX U11 fine escapes, then ordered lower B.Cu lanes.  Their horizontal
# corridors begin below the TX source returns, so no same-layer crossing.
tr(b,'USB_RXP1',(139.4,138.6),(138.0,140),w=.10); vi(b,'USB_RXP1',(138.0,140)); tr(b,'USB_RXP1',(138.0,140),(170.0,151),pcbnew.B_Cu); vi(b,'USB_RXP1',(170.0,151)); tr(b,'USB_RXP1',(170.0,151),(166.5,137.8))
tr(b,'USB_RXN1',(139.0,138.6),(137.4,140.6),w=.10); vi(b,'USB_RXN1',(137.4,140.6)); tr(b,'USB_RXN1',(137.4,140.6),(170.6,151.6),pcbnew.B_Cu); vi(b,'USB_RXN1',(170.6,151.6)); tr(b,'USB_RXN1',(170.6,151.6),(166.5,138.2))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
