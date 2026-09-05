"""Inventory Phase 21 low-speed/control nets from the Phase 20 board."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "PHASE20_SERVICE_RD_OUTER_REFILLED.kicad_pcb"
OUTPUT = ROOT / "PHASE21_CONTROL_INVENTORY.md"

KEYWORDS = ("PG", "FAULT", "RESET", "PERST", "GATE", "VCAP", "RT_", "FB_",
            "RECOVERY", "UART", "FAN", "PUMP", "PWM", "TACH", "THERM", "LED")

def main():
    board = pcbnew.LoadBoard(str(INPUT))
    rows = []
    for net in board.GetNetsByName().values():
        name = net.GetNetname()
        if not name or not any(k in name.upper() for k in KEYWORDS):
            continue
        pads = []
        tracks = 0
        for fp in board.GetFootprints():
            for pad in fp.Pads():
                if pad.GetNetCode() == net.GetNetCode():
                    pads.append(f"{fp.GetReference()}.{pad.GetNumber()}")
        for track in board.GetTracks():
            if track.GetNetCode() == net.GetNetCode() and track.Type() != pcbnew.PCB_VIA_T:
                tracks += 1
        if len(pads) > 1:
            rows.append((name, pads, tracks))
    rows.sort()
    lines = ["# Phase 21 control inventory", "", "Generated from `PHASE20_SERVICE_RD_OUTER_REFILLED.kicad_pcb` with KiCad pcbnew.", "", "| Net | Pads | Existing tracks |", "|---|---|---:|"]
    for name, pads, tracks in rows:
        lines.append(f"| `{name}` | {', '.join(pads)} | {tracks} |")
    OUTPUT.write_text("\n".join(lines) + "\n")
    print(OUTPUT)

if __name__ == "__main__":
    main()
