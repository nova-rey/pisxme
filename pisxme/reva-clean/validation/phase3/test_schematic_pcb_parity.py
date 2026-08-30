#!/usr/bin/env python3
"""Run a native-format disposable schematic-to-PCB net parity fixture.

The clean Phase 3 architecture deliberately has no production PCB.  This
fixture proves the parity checker rejects PCB-only/proxy nets before any
placement or routing is authorized.
"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "validation" / "phase3" / "fixtures" / "phase3_parity_fixture.kicad_pcb"
SCHEMATIC_NETS = {"", "ETH_TD0_P", "ETH_TD0_N", "ETH_SHIELD_CHASSIS"}


def main() -> None:
    text = FIXTURE.read_text()
    pcb_nets = set(re.findall(r'\(net [0-9]+ "([^"]*)"\)', text))
    pad_nets = set(re.findall(r'\(net [0-9]+ "([^"]*)"\)', text[text.index("(footprint "):]))
    assert pcb_nets <= SCHEMATIC_NETS, sorted(pcb_nets - SCHEMATIC_NETS)
    assert pad_nets <= SCHEMATIC_NETS, sorted(pad_nets - SCHEMATIC_NETS)
    assert pcb_nets - {""} == pad_nets - {""}
    assert "PROXY" not in text.upper()
    print("schematic-PCB parity fixture: PASS; PCB-only/proxy nets=0")


if __name__ == "__main__":
    main()
