#!/usr/bin/env python3
"""Read-only audit of the selected U11/U12 project footprints.
This does not edit CAD or assert that an implementation candidate is valid.
"""
from __future__ import annotations
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FPDIR = ROOT / "PiSXMe_RevA_Clean.pretty"
PAD_RE = re.compile(r'\(pad\s+"([^"]+)"\s+([^\s]+).*?\(at\s+(-?[0-9.]+)\s+(-?[0-9.]+)(?:\s+(-?[0-9.]+))?\).*?\(size\s+(-?[0-9.]+)\s+(-?[0-9.]+)\).*?\(layers\s+([^)]*)\)', re.S)
RECT_RE = re.compile(r'\(fp_rect\s+\(start\s+(-?[0-9.]+)\s+(-?[0-9.]+)\).*?\(end\s+(-?[0-9.]+)\s+(-?[0-9.]+)\).*?\(.*?\)\s+\(fill\s+none\)\s+\(layer\s+"F\.CrtYd"\)', re.S)

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def footprint(name: str):
    path = FPDIR / name
    text = path.read_text()
    pads = []
    for m in PAD_RE.finditer(text):
        pads.append({"id": m.group(1), "kind": m.group(2), "x": float(m.group(3)), "y": float(m.group(4)), "rot": float(m.group(5) or 0), "sx": float(m.group(6)), "sy": float(m.group(7)), "layers": [x.strip(chr(34)) for x in m.group(8).split()]})
    rect = RECT_RE.search(text)
    courtyard = None if not rect else {"x0":float(rect.group(1)),"y0":float(rect.group(2)),"x1":float(rect.group(3)),"y1":float(rect.group(4)),"width":abs(float(rect.group(3))-float(rect.group(1))),"height":abs(float(rect.group(4))-float(rect.group(2)))}
    return path, text, pads, courtyard

def pitch(vals):
    vals = sorted(set(round(v, 6) for v in vals))
    if len(vals) < 2: return None
    return round(sum(b-a for a,b in zip(vals, vals[1:]))/(len(vals)-1), 6)

def report_u12():
    path,text,pads,cy = footprint("HD3SS6126_RUA0042A.kicad_mod")
    signal=[p for p in pads if p["id"] != "43"]
    left=[p for p in signal if 1 <= int(p["id"]) <= 17]
    right=[p for p in signal if 22 <= int(p["id"]) <= 38]
    top=[p for p in signal if 18 <= int(p["id"]) <= 21]
    bottom=[p for p in signal if 39 <= int(p["id"]) <= 42]
    return {
      "file": str(path.relative_to(ROOT)), "sha256": sha(path), "pad_count": len(pads), "signal_pad_count": len(signal), "thermal_pad": next((p for p in pads if p["id"]=="43"),None),
      "actual": {"side_row_pitch_y": pitch([p["y"] for p in left]), "end_row_pitch_x": pitch([p["x"] for p in top]), "side_row_center_x": sorted(set(p["x"] for p in left+right)), "side_row_span_y": [min(p["y"] for p in left),max(p["y"] for p in left)], "end_row_span_x": [min(p["x"] for p in top),max(p["x"] for p in top)], "courtyard": cy, "signal_sizes": sorted(set((p["sx"],p["sy"]) for p in signal)), "paste_mask_on_all_pads": all("F.Paste" in p["layers"] and "F.Mask" in p["layers"] for p in pads)},
      "authoritative_contract": {"source": "TI SLAS975A / RUA0042A drawing 4219139/A 03/2020", "side_row_pitch_mm": 0.5, "end_row_pitch_mm": 0.5, "side_row_center_spacing_mm": 3.3, "signal_size_mm": [0.6,0.25], "thermal_size_mm": [2.05,7.55]},
      "status": "CONFLICT_CURRENT_FOOTPRINT_REJECTED_FOR_ROUTING"
    }

def report_u11():
    path,text,pads,cy = footprint("JMS583_QFN64_8x8.kicad_mod")
    signal=[p for p in pads if p["id"] != "65"]
    groups=[[p for p in signal if 1 <= int(p["id"]) <= 16],[p for p in signal if 17 <= int(p["id"]) <= 32],[p for p in signal if 33 <= int(p["id"]) <= 48],[p for p in signal if 49 <= int(p["id"]) <= 64]]
    return {
      "file": str(path.relative_to(ROOT)), "sha256": sha(path), "pad_count": len(pads), "signal_pad_count": len(signal), "thermal_pad": next((p for p in pads if p["id"]=="65"),None),
      "actual": {"edge_pitches": [pitch([p["y"] for p in groups[0]]),pitch([p["x"] for p in groups[1]]),pitch([p["y"] for p in groups[2]]),pitch([p["x"] for p in groups[3]])], "courtyard": cy, "signal_sizes": sorted(set((p["sx"],p["sy"]) for p in signal)), "paste_mask_on_all_pads": all("F.Paste" in p["layers"] and "F.Mask" in p["layers"] for p in pads), "thermal_paste_is_full_pad": any(p["id"]=="65" and p["sx"]==4.46 and p["sy"]==4.46 and "F.Paste" in p["layers"] for p in pads)},
      "authoritative_contract": {"source": "JMicron PDS-17001 Rev 2.1 Figure 4", "pitch_mm": 0.4, "terminal_width_range_mm": [0.15,0.25], "terminal_length_range_mm": [0.3,0.5], "body_mm": [8.0,8.0], "exposed_pad_range_mm": [[4.36,4.56],[4.36,4.56]], "exposed_pad_nominal_mm": [4.46,4.46], "land_treatment_guidance": "TI SLUA271C general QFN guidance: NSMD preferred; 0.2 mm pad width guide at 0.4 mm pitch; window EP paste to approximately 50-70%"},
      "status": "PROTOTYPE_LAND_AUTHORIZED_EP_STENCIL_WINDOW_REQUIRED"
    }

def main():
    out={"schema":"pisxme.p24.u11-u12.geometry-audit.v1","read_only":True,"u11":report_u11(),"u12":report_u12()}
    Path(sys.argv[1] if len(sys.argv)>1 else "geometry-audit.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
if __name__ == "__main__": main()
