"""Apply the native Phase 20 SERVICE net authority to a PCB candidate.

This is deliberately limited to the CM5 service USB2/UFP island.  It keeps
the inherited placement and all unrelated routed geometry unchanged while
making the board pad mapping agree with the corrected native schematic.
"""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
IN = ROOT / "PHASE19_V3_USB_PROVEN_SPLIT_SATA_TX_MATCH_REFILL.kicad_pcb"
OUT = ROOT / "PHASE20_SERVICE_AUTHORITY_BASE.kicad_pcb"

NETS = {
    "DP": "/CORE_CM5/SERVICE_USB2_DP",
    "DM": "/CORE_CM5/SERVICE_USB2_DM",
    "VBUS": "/SERVICE/SERVICE_VBUS_SENSE",
    "GND": "/SERVICE/SERVICE_GND",
    "RDA": "/SERVICE/SERVICE_RD_A",
    "RDB": "/SERVICE/SERVICE_RD_B",
}

def net(board, name):
    n = board.FindNet(name)
    if n is None:
        n = pcbnew.NETINFO_ITEM(board, name)
        board.Add(n)
    return n

def fp(board, ref):
    f = board.FindFootprintByReference(ref)
    if f is None:
        raise RuntimeError(f"missing footprint {ref}")
    return f

def setpad(board, ref, padno, n):
    p = fp(board, ref).FindPadByNumber(str(padno))
    if p is None:
        raise RuntimeError(f"missing {ref}.{padno}")
    p.SetNet(n)

def main():
    b = pcbnew.LoadBoard(str(IN))
    ns = {k: net(b, v) for k, v in NETS.items()}

    # CM5 J7 USB2 mapping: A-side USB2_N is pad 103, USB2_P is pad 105.
    setpad(b, "J7", 103, ns["DM"])
    setpad(b, "J7", 105, ns["DP"])

    # Amphenol USB-C receptacle aliases, from its manufacturer footprint.
    for p in ("A6", "B6"):
        setpad(b, "J4", p, ns["DP"])
    for p in ("A7", "B7"):
        setpad(b, "J4", p, ns["DM"])
    for p in ("A4", "A9", "B4", "B9"):
        setpad(b, "J4", p, ns["VBUS"])
    for p in ("A1", "A12", "B1", "B12"):
        setpad(b, "J4", p, ns["GND"])
    setpad(b, "J4", "A5", ns["RDA"])
    setpad(b, "J4", "B5", ns["RDB"])

    setpad(b, "U8", 1, ns["DP"])
    setpad(b, "U8", 2, ns["DM"])
    setpad(b, "U8", 3, ns["GND"])
    setpad(b, "R1", 1, ns["RDA"])
    setpad(b, "R1", 2, ns["GND"])
    setpad(b, "R2", 1, ns["RDB"])
    setpad(b, "R2", 2, ns["GND"])
    b.Save(str(OUT))
    print(f"wrote {OUT}")

if __name__ == "__main__":
    main()
