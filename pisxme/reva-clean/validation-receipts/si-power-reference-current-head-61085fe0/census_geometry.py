#!/usr/bin/env python3
"""Read-only KiCad PCB geometry census for the Phase-24 SI/power package.

This intentionally parses serialized objects only.  Native DRC/zone refill is
run separately in the qualified KiCad Light receipt; this script never saves a
board and never treats a serialized zone as proof of filled-copper continuity.
"""
import hashlib
import json
import math
import re
import sys
from pathlib import Path


def blocks(text, token):
    """Yield balanced top-level-ish blocks whose first atom is token."""
    needle = "(" + token
    pos = 0
    while True:
        start = text.find(needle, pos)
        if start < 0:
            return
        # Avoid matching a token in a quoted string or an embedded identifier.
        if start and text[start - 1] not in "\n\r\t ":
            pos = start + 1
            continue
        depth = 0
        quote = False
        escaped = False
        end = None
        for i in range(start, len(text)):
            c = text[i]
            if quote:
                if escaped:
                    escaped = False
                elif c == "\\":
                    escaped = True
                elif c == '"':
                    quote = False
                continue
            if c == '"':
                quote = True
            elif c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end is None:
            raise ValueError(f"unbalanced {token} block at {start}")
        yield text[start:end]
        pos = end


def first(pattern, text, default=None):
    m = re.search(pattern, text, re.S)
    return m.group(1) if m else default


def net_ref(block):
    """Return the KiCad 10 serialized net name (or a legacy numeric ID)."""
    name = first(r'\(net\s+"([^"]*)"', block)
    if name is not None:
        return name
    return first(r'\(net\s+(\d+)', block)


def xy(block, atom):
    m = re.search(r"\(" + re.escape(atom) + r"\s+([-+0-9.eE]+)\s+([-+0-9.eE]+)", block)
    return (float(m.group(1)), float(m.group(2))) if m else None


def abs_pos(local, origin, rotation):
    x, y = local
    a = math.radians(rotation)
    return (origin[0] + x * math.cos(a) - y * math.sin(a),
            origin[1] + x * math.sin(a) + y * math.cos(a))


def footprint_data(text):
    out = []
    for block in blocks(text, "footprint"):
        origin = xy(block, "at")
        if origin is None:
            continue
        at = re.search(r"\(at\s+[-+0-9.eE]+\s+[-+0-9.eE]+(?:\s+([-+0-9.eE]+))?", block)
        rot = float(at.group(1) or 0) if at else 0.0
        ref = first(r'\(property\s+"Reference"\s+"([^"]+)"', block)
        name = first(r'^\(footprint\s+"([^"]+)"', block)
        pads = []
        for p in blocks(block, "pad"):
            num = first(r'^\(pad\s+"([^"]+)"', p)
            local = xy(p, "at")
            net = net_ref(p)
            if num is not None and local is not None:
                pads.append({"number": num, "net": net or "", "local": local,
                             "absolute": abs_pos(local, origin, rot)})
        out.append({"reference": ref, "footprint": name, "origin": origin,
                    "rotation_deg": rot, "pads": pads})
    return out


def net_map(text):
    return {int(n): name for n, name in re.findall(r'^\s*\(net\s+(\d+)\s+"([^"]*)"\)', text, re.M)}


def routed_data(text, nets):
    segments = []
    for b in blocks(text, "segment"):
        s = xy(b, "start")
        e = xy(b, "end")
        layer = first(r'\(layer\s+"([^"]+)"', b)
        width = first(r'\(width\s+([-+0-9.eE]+)', b)
        n = net_ref(b)
        if s and e and layer and width and n:
            segments.append({"start": s, "end": e, "layer": layer,
                             "width_mm": float(width), "net_id": int(n) if n.isdigit() else None,
                             "net": nets.get(int(n), "") if n.isdigit() else n,
                             "length_mm": math.dist(s, e)})
    vias = []
    for b in blocks(text, "via"):
        p = xy(b, "at")
        n = net_ref(b)
        if p and n:
            vias.append({"at": p, "net_id": int(n) if n.isdigit() else None,
                         "net": nets.get(int(n), "") if n.isdigit() else n})
    return segments, vias


def zones_data(text, nets):
    zones = []
    for b in blocks(text, "zone"):
        layer = first(r'\(layer\s+"([^"]+)"', b)
        n = net_ref(b)
        name = first(r'\(net_name\s+"([^"]*)"', b)
        if layer:
            zones.append({"layer": layer, "net_id": int(n) if n and n.isdigit() else None,
                          "net": name or (nets.get(int(n), "") if n and n.isdigit() else (n or ""))})
    return zones


def distances(fps, refs):
    pos = {x["reference"]: x["origin"] for x in fps if x["reference"]}
    result = {}
    for module, cohort in refs.items():
        if module not in pos:
            continue
        vals = []
        for ref in cohort:
            if ref in pos:
                vals.append({"reference": ref, "distance_mm": math.dist(pos[module], pos[ref]),
                             "position": pos[ref]})
        result[module] = {"module_position": pos[module], "members": vals,
                          "max_distance_mm": max((x["distance_mm"] for x in vals), default=None)}
    return result


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: census_geometry.py BOARD OUTPUT_JSON")
    board, output = map(Path, sys.argv[1:])
    text = board.read_text()
    nets = net_map(text)
    fps = footprint_data(text)
    segs, vias = routed_data(text, nets)
    zones = zones_data(text, nets)
    counts = {}
    for s in segs:
        counts[s["layer"]] = counts.get(s["layer"], 0) + 1
    by_net = {}
    for s in segs:
        by_net.setdefault(s["net"], {"segments": 0, "vias": 0, "length_mm": 0.0,
                                      "layers": set(), "widths_mm": set()})
        x = by_net[s["net"]]
        x["segments"] += 1
        x["length_mm"] += s["length_mm"]
        x["layers"].add(s["layer"])
        x["widths_mm"].add(s["width_mm"])
    for v in vias:
        by_net.setdefault(v["net"], {"segments": 0, "vias": 0, "length_mm": 0.0,
                                      "layers": set(), "widths_mm": set()})["vias"] += 1
    for x in by_net.values():
        x["length_mm"] = round(x["length_mm"], 6)
        x["layers"] = sorted(x["layers"])
        x["widths_mm"] = sorted(x["widths_mm"])
    refs = {
        "U3": ["C5", "C6", "C7", "C8", "C9", "R3", "R4", "R5", "R6"],
        "U4": ["C14", "C15", "C16", "C17", "C19", "C18", "R11", "R12", "R13", "R14"],
        "U5": ["C23", "C24", "C25", "C26", "C27", "C28", "C29", "C34", "C35", "C36", "C37", "C38", "C39", "C40", "C41", "C44", "C45", "C46", "C47", "R19", "R20", "R21", "R22"],
    }
    result = {
        "board": board.name,
        "board_sha256": hashlib.sha256(board.read_bytes()).hexdigest(),
        "parse_method": "read-only serialized KiCad 10 s-expression segment/via/zone/footprint census",
        "layers": {"F.Cu": "signal", "In1.Cu": "signal / In1.GND", "In2.Cu": "signal / In2.PWR",
                   "In3.Cu": "signal / In3.PROTECTED_12V", "In4.Cu": "signal / In4.GND", "B.Cu": "signal"},
        "counts": {"footprints": len(fps), "segments": len(segs), "vias": len(vias), "zones": len(zones)},
        "segments_by_layer": counts,
        "net_summary": {k: v for k, v in sorted(by_net.items()) if k},
        "power_return": {k: by_net.get(k, {"segments": 0, "vias": 0, "length_mm": 0.0})
                         for k in ["POWER_GND", "12V_PROTECTED", "BRIDGE_3V3", "BRIDGE_1V1", "CM5_5V"]},
        "regulator_support_distances": distances(fps, refs),
        "zones": zones,
        "regulator_packages": {x["reference"]: {"footprint": x["footprint"], "origin": x["origin"],
                                                  "rotation_deg": x["rotation_deg"], "pad_count": len(x["pads"])}
                                for x in fps if x["reference"] in {"U3", "U4", "U5"}},
    }
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
