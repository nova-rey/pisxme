#!/usr/bin/env python3
"""V14: V13 geometry at the approved 0.15-mm minimum track width."""
import phase24_sata_m2_launch_isolated_v13 as v
import pcbnew
v.W = pcbnew.FromMM(.15)
v.OUT = v.ROOT / 'PHASE24_PATHA_M2_LANE0_LAUNCH_ISOLATED_V14.kicad_pcb'
v.main()
