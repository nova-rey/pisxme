#!/usr/bin/env python3
"""Disposable overlay of proven bridge regulator support copper only."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_SELECTED_MACRO_STORAGE_PROVEN_USB3_SATA_RXN_STITCH_CAPS_BOTTOM.kicad_pcb'
ORACLE=R/'PHASE24_U5_INTEGRATED_LAYERED.kicad_pcb'
OUT=R/'PHASE24_SELECTED_MACRO_STORAGE_PROVEN_USB3_SATA_RXN_STITCH_CAPS_BOTTOM_POWER_ORACLE.kicad_pcb'
NETS={'/REGULATORS/BRIDGE_1V1','/REGULATORS/BRIDGE_3V3','/REGULATORS/FB_BRIDGE_3V3',
      '/REGULATORS/PG_BRIDGE_3V3','/REGULATORS/RT_BRIDGE_3V3','/STORAGE/BRIDGE_RESET',
      '/STORAGE/BRIDGE_3V3'}
b=pcbnew.LoadBoard(str(BASE)); o=pcbnew.LoadBoard(str(ORACLE))
for item in o.GetTracks():
    name=str(item.GetNetname())
    if name not in NETS: continue
    net=b.FindNet(name)
    if net is None: continue
    if isinstance(item,pcbnew.PCB_VIA):
        x=pcbnew.PCB_VIA(b); x.SetPosition(item.GetPosition()); x.SetWidth(item.GetWidth(pcbnew.F_Cu)); x.SetDrill(item.GetDrill()); x.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu)
    else:
        x=pcbnew.PCB_TRACK(b); x.SetStart(item.GetStart()); x.SetEnd(item.GetEnd()); x.SetLayer(item.GetLayer()); x.SetWidth(item.GetWidth())
    x.SetNet(net); b.Add(x)
b.Save(str(OUT)); print(OUT)
