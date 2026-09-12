#!/usr/bin/env python3
"""Support V6: separate TX/RX layer channels and preserve pair order."""
from pathlib import Path
import pcbnew
ROOT = Path(__file__).resolve().parent
BASE = ROOT/'PHASE24_STORAGE_MKEY_USB3_U12_EAST_COORDINATED_20260912.kicad_pcb'
OUT = ROOT/'PHASE24_STORAGE_MKEY_USB3_EAST_SUPPORT_V6_20260912.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(b,n,a,z,l=pcbnew.F_Cu,w=.20):
    q=b.FindNet(n); t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(q); t.SetNetCode(q.GetNetCode()); b.Add(t)
def via(b,n,p):
    q=b.FindNet(n); v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetNet(q); v.SetNetCode(q.GetNetCode()); b.Add(v)
b=pcbnew.LoadBoard(str(BASE))
if b is None: raise SystemExit('cannot load base')
c86=b.FindFootprintByReference('C86'); c87=b.FindFootprintByReference('C87')
if c86 is None or c87 is None: raise SystemExit('missing C86/C87')
c86.SetPosition(V(146,141.5)); c87.SetPosition(V(146,143.5))
for ref in ('U11','U12'):
    for p in b.FindFootprintByReference(ref).Pads(): p.SetLocalClearance(pcbnew.FromMM(.10))

# U11 bottom row escapes outward; these immediate fanout segments use 0.15 mm,
# the least aggressive width that still provides margin at the 0.4 mm pitch.
tr(b,'USB_TXP1',(141.4,138.6),(141.4,139.8),w=.15); tr(b,'USB_TXP1',(141.4,139.8),(142.2,140.4),w=.15); tr(b,'USB_TXP1',(142.2,140.4),(145.5,141.5))
tr(b,'USB_TXN1',(141.0,138.6),(141.0,139.8),w=.15); tr(b,'USB_TXN1',(141.0,139.8),(140.2,141.0),w=.15); tr(b,'USB_TXN1',(140.2,141.0),(145.5,143.5))

# TX support owns the upper B.Cu channel.
tr(b,'JMS_USB3_TXP',(146.5,141.5),(148.0,141.5)); via(b,'JMS_USB3_TXP',(148.0,141.5)); tr(b,'JMS_USB3_TXP',(148.0,141.5),(169.0,140.2),pcbnew.B_Cu); tr(b,'JMS_USB3_TXP',(169.0,140.2),(169.0,135.8),pcbnew.B_Cu); via(b,'JMS_USB3_TXP',(169.0,135.8)); tr(b,'JMS_USB3_TXP',(169.0,135.8),(166.5,137.0))
tr(b,'JMS_USB3_TXN',(146.5,143.5),(149.0,143.5)); via(b,'JMS_USB3_TXN',(149.0,143.5)); tr(b,'JMS_USB3_TXN',(149.0,143.5),(170.0,141.6),pcbnew.B_Cu); tr(b,'JMS_USB3_TXN',(170.0,141.6),(170.0,136.4),pcbnew.B_Cu); via(b,'JMS_USB3_TXN',(170.0,136.4)); tr(b,'JMS_USB3_TXN',(170.0,136.4),(166.5,137.4))

# RX pair uses a lower B.Cu channel, entering it after the CM5_PERST obstacle.
tr(b,'USB_RXP1',(139.4,138.6),(139.4,140.0),w=.15); via(b,'USB_RXP1',(139.4,140.0)); tr(b,'USB_RXP1',(139.4,140.0),(151.0,147.0),pcbnew.B_Cu); tr(b,'USB_RXP1',(151.0,147.0),(171.5,147.0),pcbnew.B_Cu); tr(b,'USB_RXP1',(171.5,147.0),(171.5,137.2),pcbnew.B_Cu); via(b,'USB_RXP1',(171.5,137.2)); tr(b,'USB_RXP1',(171.5,137.2),(166.5,137.8))
tr(b,'USB_RXN1',(139.0,138.6),(139.0,140.8),w=.15); via(b,'USB_RXN1',(139.0,140.8)); tr(b,'USB_RXN1',(139.0,140.8),(151.0,148.0),pcbnew.B_Cu); tr(b,'USB_RXN1',(151.0,148.0),(172.5,148.0),pcbnew.B_Cu); tr(b,'USB_RXN1',(172.5,148.0),(172.5,138.8),pcbnew.B_Cu); via(b,'USB_RXN1',(172.5,138.8)); tr(b,'USB_RXN1',(172.5,138.8),(166.5,138.2))
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
