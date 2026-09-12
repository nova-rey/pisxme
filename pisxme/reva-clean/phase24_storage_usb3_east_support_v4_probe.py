#!/usr/bin/env python3
"""Support V4: directional U11 escape and separated right-side U12 returns."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'PHASE24_STORAGE_MKEY_USB3_U12_EAST_COORDINATED_20260912.kicad_pcb'
OUT=ROOT/'PHASE24_STORAGE_MKEY_USB3_EAST_SUPPORT_V4_20260912.kicad_pcb'
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
# Directional local U11 escapes avoid the adjacent pad row.
tr(b,'USB_TXP1',(141.4,138.6),(141.4,137.4),w=.10); tr(b,'USB_TXP1',(141.4,137.4),(143.0,136.4),w=.10); tr(b,'USB_TXP1',(143.0,136.4),(144.5,145))
tr(b,'USB_TXN1',(141.0,138.6),(141.0,140.0),w=.10); tr(b,'USB_TXN1',(141.0,140.0),(144.5,149))
tr(b,'USB_RXP1',(139.4,138.6),(139.4,137.4),w=.10); tr(b,'USB_RXP1',(139.4,137.4),(138.0,139.0),w=.10); vi(b,'USB_RXP1',(138.0,139.0)); tr(b,'USB_RXP1',(138.0,139.0),(172.0,151),pcbnew.B_Cu); vi(b,'USB_RXP1',(172.0,151)); tr(b,'USB_RXP1',(172.0,151),(166.5,137.8))
tr(b,'USB_RXN1',(139.0,138.6),(139.0,140.0),w=.10); tr(b,'USB_RXN1',(139.0,140.0),(137.4,141.0),w=.10); vi(b,'USB_RXN1',(137.4,141.0)); tr(b,'USB_RXN1',(137.4,141.0),(172.6,151.6),pcbnew.B_Cu); vi(b,'USB_RXN1',(172.6,151.6)); tr(b,'USB_RXN1',(172.6,151.6),(166.5,138.2))
# Bridge-side legs cross CM5_PERST on B.Cu and return on the right of U12.
tr(b,'JMS_USB3_TXP',(145.5,145),(146,145)); vi(b,'JMS_USB3_TXP',(146,145)); tr(b,'JMS_USB3_TXP',(146,145),(146,141),pcbnew.B_Cu); tr(b,'JMS_USB3_TXP',(146,141),(169.5,141),pcbnew.B_Cu); tr(b,'JMS_USB3_TXP',(169.5,141),(169.5,137),pcbnew.B_Cu); vi(b,'JMS_USB3_TXP',(169.5,137)); tr(b,'JMS_USB3_TXP',(169.5,137),(166.5,137))
tr(b,'JMS_USB3_TXN',(145.5,149),(146.6,149)); vi(b,'JMS_USB3_TXN',(146.6,149)); tr(b,'JMS_USB3_TXN',(146.6,149),(146.6,143),pcbnew.B_Cu); tr(b,'JMS_USB3_TXN',(146.6,143),(170.5,143),pcbnew.B_Cu); tr(b,'JMS_USB3_TXN',(170.5,143),(170.5,137.4),pcbnew.B_Cu); vi(b,'JMS_USB3_TXN',(170.5,137.4)); tr(b,'JMS_USB3_TXN',(170.5,137.4),(166.5,137.4))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
