#!/usr/bin/env python3
"""Route the six remaining U11/U12 USB3 support links on the east island."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'PHASE24_STORAGE_MKEY_USB3_U12_EAST_COORDINATED_20260912.kicad_pcb'
OUT=ROOT/'PHASE24_STORAGE_MKEY_USB3_EAST_SUPPORT_20260912.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z,l=pcbnew.F_Cu):
 q=b.FindNet(n); t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.13208)); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
b=pcbnew.LoadBoard(str(BASE))
if b is None: raise SystemExit('cannot load base')
c86=b.FindFootprintByReference('C86'); c87=b.FindFootprintByReference('C87')
if c86 is None or c87 is None: raise SystemExit('missing C86/C87')
c86.SetPosition(V(150,145)); c87.SetPosition(V(150,149))
# Actual pad locations after the coherent capacitor move.
# U11-to-cap legs remain short and on F.Cu; cap-to-U12 legs use the open
# east-side corridor and approach the actual right-side bridge pads.
tr(b,'USB_TXP1',(141.4,138.6),(149.5,145))
tr(b,'JMS_USB3_TXP',(150.5,145),(160,145)); tr(b,'JMS_USB3_TXP',(160,145),(166.5,137.0))
tr(b,'USB_TXN1',(141.0,138.6),(149.5,149))
tr(b,'JMS_USB3_TXN',(150.5,149),(161,149)); tr(b,'JMS_USB3_TXN',(161,149),(166.5,137.4))
# Direct U11/U12 RX pair takes a lower, parallel corridor.
tr(b,'USB_RXP1',(139.4,138.6),(139.4,151)); tr(b,'USB_RXP1',(139.4,151),(165,151)); tr(b,'USB_RXP1',(165,151),(166.5,137.8))
tr(b,'USB_RXN1',(139.0,138.6),(138.8,153)); tr(b,'USB_RXN1',(138.8,153),(165.6,153)); tr(b,'USB_RXN1',(165.6,153),(166.5,138.2))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
