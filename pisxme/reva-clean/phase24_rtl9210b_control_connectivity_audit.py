#!/usr/bin/env python3
"""Audit V12 control/SPI connectivity from native KiCad copper objects."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
PCB=ROOT/'PHASE24_RTL9210B_CONTROL_SUPPORT_LOCAL_V12.kicad_pcb'
EXPECTED={
  'PEDET':[('U1','8'),('R2','1'),('J1','69')],
  'CLKREQ_N':[('U1','13'),('R3','1'),('J1','52')],
  'PERST_N':[('U1','14'),('J1','50')],
  'RESET_N':[('U1','3'),('TP6','1')],
  'SPICS':[('U1','24'),('U2','1')],
  'SPISO':[('U1','23'),('U2','2')],
  'SPISI':[('U1','18'),('U2','5')],
  'SPICLK':[('U1','19'),('U2','6')],
}
def pad(b,ref,num): return b.FindFootprintByReference(ref).FindPadByNumber(num)
def connected_pad_keys(b,p):
    c=b.GetConnectivity(); out=set()
    for item in c.GetConnectedItems(p):
        if isinstance(item,pcbnew.PAD):
            fp=item.GetParentFootprint(); out.add((fp.GetReference(),item.GetNumber()))
    out.add((p.GetParentFootprint().GetReference(),p.GetNumber()))
    return out
def audit(b):
    b.BuildConnectivity()
    for net, endpoints in EXPECTED.items():
        anchor=pad(b,*endpoints[0]); got=connected_pad_keys(b,anchor)
        for ep in endpoints:
            if ep not in got: raise AssertionError(f'{net}: {ep} not connected to {endpoints[0]}')
    print('PASS native RTL9210B control/U1-U2 SPI endpoint connectivity')
def negative_control():
    b=pcbnew.LoadBoard(str(PCB)); n=b.FindNet('PEDET')
    removed=0
    for item in list(b.GetTracks()):
        if item.GetNetname()=='PEDET': b.RemoveNative(item); removed+=1
    if not removed: raise AssertionError('negative control found no PEDET copper')
    try: audit(b)
    except AssertionError: print('PASS negative control: removed PEDET copper fails')
    else: raise AssertionError('negative control unexpectedly passed')
if __name__=='__main__':
    b=pcbnew.LoadBoard(str(PCB)); audit(b); negative_control()
