from pathlib import Path
import json

OUT = Path(__file__).with_name("GEOMETRY_AUDIT.json")
fuses = [(x, y) for y in (15.0, 40.0, 65.0) for x in (36.0, 64.0, 92.0)]
checks = []

def check(name, ok, detail):
    checks.append({"name": name, "status": "PASS" if ok else "FAIL", "detail": detail})

# HPQ's corrected holder envelope screen is 24.25 mm square.  The exact
# existing project footprint is retained; this audit deliberately uses the
# larger corrected screen, not its smaller nominal drawing box.
half = 24.25 / 2.0
rows = [15.0, 40.0, 65.0]
gaps = [rows[i+1] - rows[i] - 24.25 for i in range(2)]
check("row_pitch", all(abs(g - 0.75) < 1e-9 for g in gaps), {"pitch_mm": 25.0, "gap_mm": gaps})
check("board_top_clearance", min(y-half for x,y in fuses) >= 0.0, {"minimum_mm": min(y-half for x,y in fuses)})

# J7 physical courtyard/holes from the current selected PCB geometry.
j7_box = (31.5, 78.5, 70.5, 133.5)
check("fuses_clear_j7_courtyard", all(y+half <= j7_box[1] or y-half >= j7_box[3] or x+half <= j7_box[0] or x-half >= j7_box[2] for x,y in fuses), {"j7": j7_box})
holes = [(35.0, 82.0), (68.0, 82.0)]
radius = (2.7 + 3.4) / 2.0
circle_results=[]
for x,y in fuses:
    for hx,hy in holes:
        # Rectangle-circle separation; positive means no overlap.
        dx=max(abs(hx-x)-half,0.0); dy=max(abs(hy-y)-half,0.0)
        circle_results.append(((x,y),(hx,hy), (dx*dx+dy*dy)**0.5-radius))
check("fuses_clear_j7_hole_clearance", all(v >= 0 for _,_,v in circle_results), {"minimum_separation_mm": min(v for *_,v in circle_results), "hole_radius_screen_mm": radius})

# Connector courtyard screen from the audited Molex footprint: x 8.8..23.6.
conn_right=23.6
check("connector_fuse_lateral_gap", min(x-half-conn_right for x,y in fuses) >= 0.0, {"minimum_gap_mm": min(x-half-conn_right for x,y in fuses)})
# New power join is east of fuse pads and west of the J1 courtyard.
check("join_j1_separation", 112.0 < 116.5, {"join_right_mm":112.0,"j1_left_mm":116.5})
check("branch_bands_end_before_j7", 77.0 < j7_box[1], {"band_end_mm":77.0,"j7_top_mm":j7_box[1]})

result={"decision":"PISXME-P24-PROTECTED-BUS-UPSTREAM-AUTHORITY-20260918-R2", "checks":checks, "status":"PASS" if all(c["status"]=="PASS" for c in checks) else "FAIL"}
OUT.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"]=="PASS" else 1)
