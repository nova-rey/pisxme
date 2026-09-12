#!/usr/bin/env python3
from pathlib import Path
import pcbnew
BASE=Path('/workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb')
OUT=Path('/workspace/output/PHASE24_POWER_DELIVERY_CANDIDATE.kicad_pcb')
b=pcbnew.LoadBoard(str(BASE))
FC=pcbnew.F_Cu

def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(netname,a,z,w=0.20):
    n=b.FindNet(netname)
    if n is None: raise RuntimeError(netname)
    t=pcbnew.PCB_TRACK(b); t.SetLayer(FC); t.SetNet(n); t.SetWidth(pcbnew.FromMM(w)); t.SetStart(P(*a)); t.SetEnd(P(*z)); b.Add(t)

# U3/U4/U5 exposed-field joins.  Pad-derived centers are from the selected
# committed PCB; the pad-14 dogleg approaches from the side to avoid NC pad 15.
for ox,oy in ((60.0,165.0),(225.0,105.0),(235.0,105.0)):
    add('12V_PROTECTED',(ox-2.25,oy-2.0),(ox+2.25,oy-2.0))
    add('12V_PROTECTED',(ox+2.25,oy-2.0),(ox+1.20,oy-2.0))
    add('12V_PROTECTED',(ox+1.20,oy-2.0),(ox+1.20,oy-0.75))
    add('12V_PROTECTED',(ox+1.20,oy-0.75),(ox+2.25,oy-0.75))
    add('POWER_GND',(ox,oy-1.125),(ox,oy+1.125))
    add('POWER_GND',(ox-2.25,oy+0.75),(ox,oy+0.75))
    add('POWER_GND',(ox,oy+0.75),(ox+2.25,oy+0.75))

# Complete the existing U3 protected-field leg from pad 16 to pad 14.
add('12V_PROTECTED',(62.25,163.0),(62.25,164.25))

# Low-voltage BRIDGE_3V3 capacitor bus, restricted to the row of actual
# same-net pad centers.
for a,z in [((93.65,112.0),(99.65,112.0)),((99.65,112.0),(105.65,112.0))]:
    add('BRIDGE_3V3',a,z)
# BRIDGE_1V1 capacitor buses on the two rows of actual same-net pads.
for a,z in [
    ((148.65,160.0),(156.65,160.0)),((156.65,160.0),(164.65,160.0)),((164.65,160.0),(172.65,160.0)),
    ((148.65,168.0),(156.65,168.0)),((156.65,168.0),(164.65,168.0)),((164.65,168.0),(172.65,168.0)),
    ((172.65,168.0),(180.65,168.0)),((180.65,168.0),(188.65,168.0)),((188.65,168.0),(196.65,168.0)),
    ((196.65,168.0),(204.65,168.0)),
]: add('BRIDGE_1V1',a,z)

pcbnew.ZONE_FILLER(b).Fill(b.Zones())
b.Save(str(OUT))
print(OUT)
