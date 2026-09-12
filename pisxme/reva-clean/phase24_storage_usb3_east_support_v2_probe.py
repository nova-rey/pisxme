#!/usr/bin/env python3
"""Second support route: short U11 escapes, B.Cu long legs, separated returns."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'PHASE24_STORAGE_MKEY_USB3_U12_EAST_COORDINATED_20260912.kicad_pcb'
OUT=ROOT/'PHASE24_STORAGE_MKEY_USB3_EAST_SUPPORT_V2_20260912.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z,l=pcbnew.F_Cu):
 q=b.FindNet(n); t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.13208)); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
def vi(b,n,p):
 q=b.FindNet(n); v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetNet(q); v.SetNetCode(q.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(BASE))
if b is None: raise SystemExit('cannot load base')
c86=b.FindFootprintByReference('C86'); c87=b.FindFootprintByReference('C87')
if c86 is None or c87 is None: raise SystemExit('missing C86/C87')
c86.SetPosition(V(145,145)); c87.SetPosition(V(145,149))
for f in (b.FindFootprintByReference('U11'), b.FindFootprintByReference('U12')):
 for p in f.Pads(): p.SetLocalClearance(pcbnew.FromMM(.15))
# U11 TX pair: pad-field-aware short escapes into C86/C87.
tr(b,'USB_TXP1',(141.4,138.6),(142.2,138.0)); tr(b,'USB_TXP1',(142.2,138.0),(144.5,145))
tr(b,'USB_TXN1',(141.0,138.6),(140.0,138.6)); tr(b,'USB_TXN1',(140.0,138.6),(140.0,149)); tr(b,'USB_TXN1',(140.0,149),(144.5,149))
# Bridge-side TX legs cross CM5_PERST on B.Cu and return at distinct, clear vias.
tr(b,'JMS_USB3_TXP',(145.5,145),(146.0,145)); vi(b,'JMS_USB3_TXP',(146.0,145)); tr(b,'JMS_USB3_TXP',(146.0,145),(164.0,142),pcbnew.B_Cu); vi(b,'JMS_USB3_TXP',(164.0,142)); tr(b,'JMS_USB3_TXP',(164.0,142),(166.5,137.0))
tr(b,'JMS_USB3_TXN',(145.5,149),(146.5,149)); vi(b,'JMS_USB3_TXN',(146.5,149)); tr(b,'JMS_USB3_TXN',(146.5,149),(164.8,143),pcbnew.B_Cu); vi(b,'JMS_USB3_TXN',(164.8,143)); tr(b,'JMS_USB3_TXN',(164.8,143),(166.5,137.4))
# U11/U12 RX pair uses a lower B.Cu corridor, with short U11 fanout vias.
tr(b,'USB_RXP1',(139.4,138.6),(138.0,140)); vi(b,'USB_RXP1',(138.0,140)); tr(b,'USB_RXP1',(138.0,140),(163.8,145),pcbnew.B_Cu); vi(b,'USB_RXP1',(163.8,145)); tr(b,'USB_RXP1',(163.8,145),(166.5,137.8))
tr(b,'USB_RXN1',(139.0,138.6),(137.4,141)); vi(b,'USB_RXN1',(137.4,141)); tr(b,'USB_RXN1',(137.4,141),(164.6,146),pcbnew.B_Cu); vi(b,'USB_RXN1',(164.6,146)); tr(b,'USB_RXN1',(164.6,146),(166.5,138.2))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
