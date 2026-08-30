"""Materialize the native schematic into a disposable routed-board candidate.

This script deliberately writes ``ACREAGE_CANDIDATE.kicad_pcb`` rather than
the floorplan.  It is the single bridge from the native schematic netlist to
pcbnew for Phases 14/15; missing footprints or pads are hard failures.
"""
from pathlib import Path
import subprocess
import sys
import os
import xml.etree.ElementTree as ET

import pcbnew

ROOT = Path(__file__).resolve().parent
BOARD_IN = ROOT / "ACREAGE_FLOORPLAN.kicad_pcb"
BOARD_OUT = ROOT / "ACREAGE_CANDIDATE.kicad_pcb"
NETLIST = ROOT / "materialize.xml"
PRETTY = ROOT / "PiSXMe_RevA_Clean.pretty"

POSITIONS = {
    "J1": (150, 90), "J2": (270, 45), "U6": (250, 45), "U9": (250, 58),
    "C1": (235, 54), "C2": (245, 54), "U7": (250, 105),
    "U4": (225, 105), "U5": (235, 105), "J3": (260, 160),
    "J4": (25, 145), "U8": (42, 145), "R1": (55, 140),
    "R2": (55, 150), "U1": (20, 75), "U2": (20, 95),
    # Keep the eight-hole FLR holders outside the conservative V100 cooler
    # reservation (x >= 75 mm), while retaining a short, direct branch into
    # each ideal-diode/FET island.
    "F1": (55, 40), "F2": (50, 120), "Q1": (215, 30), "Q2": (215, 150),
    "C3": (110, 55), "C4": (110, 95),
    "D1": (110, 32), "D2": (110, 72),
    "U3": (52, 78), "J5": (12, 25), "J6": (12, 45), "J7": (35, 130),
    # Regulator support passives are kept in deterministic local rows for
    # schematic-to-PCB parity; detailed vendor-layout placement remains gated
    # until the routed regulator phase.
    "C5": (70, 70), "C6": (78, 70), "C7": (86, 70), "C8": (94, 70), "C9": (102, 70),
    "R3": (70, 82), "R4": (78, 82), "R5": (86, 82), "R6": (94, 82),
    "C14": (70, 120), "C15": (78, 120), "C16": (86, 120), "C17": (94, 120), "C18": (102, 120), "C19": (110, 120),
    "R11": (70, 132), "R12": (78, 132), "R13": (86, 132), "R14": (94, 132),
    "C23": (70, 170), "C24": (78, 170), "C25": (86, 170),
    "R19": (94, 170), "R20": (102, 170), "R21": (110, 170), "R22": (118, 170),
    **{f"C{n}": (150 + ((n - 26) % 8) * 8, 150 + ((n - 26) // 8) * 8) for n in range(26, 42)},
}

PAD_ALIASES = {
    # Public hardware reverse-engineering map; not NVIDIA/Amphenol authority.
    # It is retained as explicit Rev-A empirical risk so the feed is not
    # collapsed onto one guessed SXM2 contact.
    "J1": {
        "PWR": tuple(f"{col}{row}" for row in (22, 23, 25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40)
                      for col in "ABCDEFGHJK"),
        "GND": tuple(f"{col}{row}" for row in (21, 24, 27, 30, 33, 36, 39)
                     for col in "ABCDEFGHJK"),
    },
    "J4": {
        "1": ("A6", "B6"), "2": ("A7", "B7"),
        "3": ("A4", "A9", "B4", "B9"), "4": ("A1", "A12", "B1", "B12"),
        "5": ("A5",), "6": ("B5",),
    },
    # Littelfuse FLR has eight solder holes: 1-4 are the input contact and
    # 5-8 are the output contact.  The schematic's two logical pins are
    # projected onto representative physical pads 1 and 5 respectively.
    "F1": {"1": ("1", "2", "3", "4"), "2": ("5", "6", "7", "8")},
    "F2": {"1": ("1", "2", "3", "4"), "2": ("5", "6", "7", "8")},
}


def export_netlist() -> None:
    if os.environ.get("PISXME_USE_EXISTING_NETLIST") == "1":
        if not NETLIST.exists() or NETLIST.stat().st_size == 0:
            raise SystemExit("PISXME_USE_EXISTING_NETLIST=1 but materialize.xml is absent/empty")
        return
    if Path('/.flatpak-info').exists():
        raise SystemExit(
            "Flatpak pcbnew cannot launch host Xvfb; export materialize.xml with "
            "host KiCad under xvfb-run, then set PISXME_USE_EXISTING_NETLIST=1"
        )
    # KiCad 10's hierarchical resolver is deterministic only when it has a
    # display backend.  The project validation path already uses Xvfb; keep
    # materialization on that same native KiCad path so support symbols are
    # not silently omitted in a headless shell.
    subprocess.run([
        "/usr/bin/xvfb-run", "-a", "kicad-cli", "sch", "export", "netlist",
        "--format", "kicadxml", "--output=materialize.xml",
        "PiSXMe_RevA_Clean.kicad_sch",
    ], cwd=ROOT, check=True)


def main() -> None:
    export_netlist()
    tree = ET.parse(NETLIST).getroot()
    components = {}
    for comp in tree.find("components"):
        fp = comp.findtext("footprint", "")
        if fp.startswith("PiSXMeRevAClean:"):
            components[comp.attrib["ref"]] = fp.split(":", 1)[1]
        elif fp.startswith("Capacitor_SMD:"):
            components[comp.attrib["ref"]] = "C_0805_2012Metric"
    missing_positions = sorted(set(components) - set(POSITIONS))
    if missing_positions:
        raise SystemExit(f"no deterministic placement for refs: {missing_positions}")

    board = pcbnew.LoadBoard(str(BOARD_IN))
    board.SetCopperLayerCount(6)
    for layer, name in ((pcbnew.F_Cu, "F.Cu"), (pcbnew.In1_Cu, "In1.GND"),
                        (pcbnew.In2_Cu, "In2.PWR"),
                        (pcbnew.In3_Cu, "In3.PROTECTED_12V"),
                        (pcbnew.In4_Cu, "In4.GND"), (pcbnew.B_Cu, "B.Cu")):
        board.SetLayerName(layer, name)

    io = pcbnew.PCB_IO_KICAD_SEXPR()
    refs = {fp.GetReference(): fp for fp in board.GetFootprints() if fp.GetReference()}
    for fp in board.GetFootprints():
        if fp.GetReference() == "REF**" and "Raspberry_Pi_5_Compute_Module" in str(fp.GetFPID().GetLibItemName()):
            fp.SetReference("J7")
            refs["J7"] = fp
    for ref, name in components.items():
        fp = refs.get(ref)
        # J5/J6 may already exist in the acreage donor.  Always reload the
        # project-local Molex authority so a corrected land pattern cannot be
        # shadowed by the stale donor-era embedded footprint.
        if ref in ("J5", "J6") and fp is not None:
            board.Remove(fp)
            refs.pop(ref, None)
            fp = None
        if fp is None:
            fp = io.FootprintLoad(str(PRETTY), name)
            if fp is None:
                raise SystemExit(f"footprint load failed: {name} for {ref}")
            board.Add(fp)
            refs[ref] = fp
        fp.SetReference(ref)
        fp.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(POSITIONS[ref][0]),
                                       pcbnew.FromMM(POSITIONS[ref][1])))

    # The acreage floorplan contains donor-era placeholder net assignments on
    # some multi-pad footprints.  Clear them before applying the authoritative
    # native netlist, otherwise an alias such as J1.PWR can be overwritten by
    # a stale signal net on the same pad.
    for ref in components:
        for pad in refs[ref].Pads():
            pad.SetNet(None)
            pad.SetNetCode(0)

    nets = {}
    unresolved = []
    for net in tree.find("nets"):
        name = net.attrib.get("name", "")
        if not name:
            continue
        nets[name] = board.FindNet(name)
        if nets[name] is None:
            nets[name] = pcbnew.NETINFO_ITEM(board, name)
            board.Add(nets[name])
        for node in net.findall("node"):
            ref, pin = node.attrib.get("ref"), node.attrib.get("pin")
            if ref in refs:
                if ref in PAD_ALIASES:
                    aliases = PAD_ALIASES[ref].get(pin, ())
                    pads = [candidate for candidate in refs[ref].Pads()
                            if candidate.GetNumber() in aliases] if aliases else [
                                candidate for candidate in refs[ref].Pads()
                                if candidate.GetNumber() == pin]
                else:
                    pads = [candidate for candidate in refs[ref].Pads()
                            if candidate.GetNumber() == pin]
                if not pads:
                    if ref == "J1" and pin in ("PWR", "GND"):
                        unresolved.append(f"{ref}.{pin}")
                        continue
                    raise SystemExit(f"netlist pad missing: {ref}.{pin} on {name}")
                for pad in pads:
                    pad.SetNet(nets[name])

    for ref, fp in refs.items():
        if ref in components and len(fp.Pads()) == 0:
            raise SystemExit(f"zero-pad footprint: {ref}")
    board.Save(str(BOARD_OUT))
    if unresolved:
        print("abstract connector pins not assigned to a physical pad: " + ", ".join(unresolved))
    print(f"materialized {len(components)} components, {len(nets)} nets, 6 copper layers")


if __name__ == "__main__":
    main()
