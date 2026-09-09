"""V1260: restore only V1243 support segments clear of the V1258 lane path."""
from pathlib import Path
import pcbnew

H = Path(__file__).resolve().parent
BASE = H / "PHASE24_RTL9210B_J1_PAD_ALIGNED_LAUNCH_V1258.kicad_pcb"
DONOR = H / "PHASE24_RTL9210B_RAILS_REFCLK_FIXED_V1243.kicad_pcb"
OUT = H / "PHASE24_RTL9210B_SUPPORT_FILTERED_LANE_V1260.kicad_pcb"
SUPPORT = {"RTL_1V1", "RTL_3V3", "GND", "RTL_5V"}

def mm(p):
    return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)

def box(q):
    a, b = mm(q.GetStart()), mm(q.GetEnd())
    return min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1])

def overlap(a, b, margin=0.22):
    return not (a[2] + margin < b[0] or b[2] + margin < a[0] or
                a[3] + margin < b[1] or b[3] + margin < a[1])

base = pcbnew.LoadBoard(str(BASE))
donor = pcbnew.LoadBoard(str(DONOR))
lane_boxes = [box(q) for q in base.GetTracks()
              if q.GetNetname() in {"LANE0_RXP", "LANE0_RXN", "LANE0_TXP", "LANE0_TXN"}]
added = rejected = 0
for q in donor.GetTracks():
    if q.GetNetname() not in SUPPORT:
        continue
    if any(overlap(box(q), lb) for lb in lane_boxes):
        rejected += 1
        continue
    base.Add(q.Duplicate())
    added += 1
base.BuildListOfNets()
pcbnew.ZONE_FILLER(base).Fill(base.Zones())
base.Save(str(OUT))
print(f"{OUT} added={added} filtered={rejected}")
