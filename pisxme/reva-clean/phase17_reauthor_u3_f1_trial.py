"""Disposable Phase-17 complete-island reauthoring trial.

Starts from the corrected, PCIe-only boundary and reauthors the U3 island
from the Phase-15 local copper contract.  F1 is moved as one power-entry
element.  This file never writes a release board.
"""
from pathlib import Path
import json
import os
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = Path(os.environ.get("PISXME_BASE", ROOT / "ACREAGE_PHASE16_PCIE_ONLY_BOUNDARY2.kicad_pcb"))
SNAP = ROOT / "phase16_copper_snapshot.json"
OUT = Path(os.environ.get("PISXME_OUT", ROOT / "ACREAGE_PHASE17_U3_F1_REAUTHOR.kicad_pcb"))
F1_TARGET = tuple(float(x) for x in os.environ.get("PISXME_F1_TARGET", "100,20").split(","))
U3_TARGET = tuple(float(x) for x in os.environ.get("PISXME_U3_TARGET", "90,165").split(","))
OLD_U3 = (52.0, 78.0)
OLD_F1 = (55.0, 40.0)
U3_REFS = {"U3", "C5", "C6", "C7", "C8", "C9", "R3", "R4", "R5", "R6"}
U3_NETS = {
    "/REGULATORS/CM5_5V": "/CORE_CM5/CM5_5V",
    "/REGULATORS/FB_CM5_5V": "/REGULATORS/FB_CM5_5V",
    "/REGULATORS/PG_CM5_5V": "/REGULATORS/PG_CM5_5V",
    "/REGULATORS/RT_CM5_5V": "/REGULATORS/RT_CM5_5V",
    "POWER_GND": "POWER_GND",
    "12V_PROTECTED": "12V_PROTECTED",
}

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def mm(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def net(b, name):
    n = b.FindNet(name)
    if n is None: raise RuntimeError(f"missing net {name}")
    return n
def add_track(b, n, a, z, layer=pcbnew.F_Cu, width=0.3):
    q = pcbnew.PCB_TRACK(b); q.SetStart(V(*a)); q.SetEnd(V(*z)); q.SetLayer(layer)
    q.SetWidth(pcbnew.FromMM(width)); q.SetNet(n); b.Add(q)
def add_via(b, n, p):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(0.55))
    q.SetDrill(pcbnew.FromMM(0.30)); q.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    q.SetNet(n); b.Add(q)
def path(b, n, points, layer=pcbnew.F_Cu, width=0.3):
    for a, z in zip(points, points[1:]): add_track(b, n, a, z, layer, width)
def pad(b, ref, number):
    f = b.FindFootprintByReference(ref)
    for p in f.Pads():
        if p.GetNumber() == str(number): return mm(p.GetPosition())
    raise RuntimeError(f"missing {ref}.{number}")

def main():
    b = pcbnew.LoadBoard(str(BASE))
    # Remove any trial copper for the nets being reauthored, while retaining
    # the validated PCIe copper and all zones/mechanics.
    for item in list(b.GetTracks()):
        if item.GetNetname() in set(U3_NETS) | set(U3_NETS.values()) | {
                "/POWER_INPUT/12V_IN_A", "/POWER_INPUT/FUSED_12V_A"}:
            b.Remove(item)

    # F1 coherent translation and direct entry/load doglegs.
    f1 = b.FindFootprintByReference("F1")
    f1.SetPosition(V(*F1_TARGET))
    dx, dy = F1_TARGET[0] - OLD_F1[0], F1_TARGET[1] - OLD_F1[1]
    old_p = {str(p.GetNumber()): mm(p.GetPosition()) for p in f1.Pads()}
    # old_p is already post-translation; derive new coordinates from the
    # known donor-relative pad coordinates captured before moving.
    # The standard FLR footprint has its input/output groups on fixed lands.
    in1 = (F1_TARGET[0] - 6.4, F1_TARGET[1] - 1.25)
    out5 = (F1_TARGET[0] + 2.9, F1_TARGET[1] - 1.25)
    ni, no = net(b, "/POWER_INPUT/12V_IN_A"), net(b, "/POWER_INPUT/FUSED_12V_A")
    add_track(b, ni, in1, (12.0, 25.0), pcbnew.B_Cu, 2.0)
    add_track(b, no, out5, (212.46, 30.0), pcbnew.B_Cu, 2.0)

    # Move the complete regulator island as a coherent block.
    udx, udy = U3_TARGET[0] - OLD_U3[0], U3_TARGET[1] - OLD_U3[1]
    for ref in U3_REFS:
        f = b.FindFootprintByReference(ref)
        p = f.GetPosition(); f.SetPosition(V(pcbnew.ToMM(p.x) + udx, pcbnew.ToMM(p.y) + udy))

    # Reauthor the complete local boundary from pad coordinates.  The old
    # Phase-16 copper is deliberately not translated: it used the obsolete
    # rail name and long shared corridors that caused the integration failure.
    vin = net(b, "12V_PROTECTED")
    outn = net(b, "/CORE_CM5/CM5_5V")
    u1, u5, u8, u9 = (pad(b, "U3", n) for n in ("1", "5", "8", "9"))
    u10, u12, u13, u16 = (pad(b, "U3", n) for n in ("10", "12", "13", "16"))
    c51, c61 = pad(b, "C5", "1"), pad(b, "C6", "1")
    # VIN/VLDOIN input capacitors, kept above the output escape.
    path(b, vin, [u1, (U3_TARGET[0]-2.25, U3_TARGET[1]-10),
                  (U3_TARGET[0]+16.9, U3_TARGET[1]-10), c51], width=0.8)
    path(b, vin, [u16, (U3_TARGET[0]+2.25, U3_TARGET[1]-12),
                  (U3_TARGET[0]+24.9, U3_TARGET[1]-12), c61], width=0.8)
    # The output bank uses a separate lower corridor around the package; it
    # never traverses the adjacent ground pads.
    c71, c81, c92 = pad(b, "C7", "1"), pad(b, "C8", "1"), pad(b, "C9", "2")
    output_lane = U3_TARGET[1] - 10
    path(b, outn, [u5, (U3_TARGET[0]-5, U3_TARGET[1]),
                   (U3_TARGET[0]-5, output_lane), (c71[0], output_lane),
                   (c71[0], c71[1]-2)], width=0.25)
    path(b, outn, [u8, (U3_TARGET[0]-4, U3_TARGET[1]+2),
                   (U3_TARGET[0]-4, output_lane+1), (c71[0], output_lane+1),
                   (c71[0], c71[1]-2)], width=0.25)
    path(b, outn, [c71, (c71[0], c71[1]-2), (c81[0], c81[1]-2), c81], width=0.25)
    path(b, outn, [c81, (c81[0], c81[1]-2), (c92[0], c92[1]-2), c92], width=0.25)
    # Feedback remains a short, quiet F.Cu loop above the output bank.
    fb = net(b, "/REGULATORS/FB_CM5_5V")
    c91, r41 = pad(b, "C9", "1"), pad(b, "R4", "1")
    path(b, fb, [u10, (u10[0]-1, u10[1]+2), (u10[0]-1, U3_TARGET[1]+6),
                 (r41[0], U3_TARGET[1]+6), r41], width=0.2)
    path(b, fb, [c91, (c91[0], U3_TARGET[1]-14), (u10[0]-1, U3_TARGET[1]-14),
                 (u10[0]-1, U3_TARGET[1]+6)], width=0.2)
    # RT and PG leave on B.Cu through ordinary vias, avoiding the F.Cu
    # output/capacitor corridor.
    rt, pg = net(b, "/REGULATORS/RT_CM5_5V"), net(b, "/REGULATORS/PG_CM5_5V")
    rt_a, rt_z = (u12[0]+2.5, u12[1]), (pad(b, "R5", "1")[0], pad(b, "R5", "1")[1]-1.0)
    pg_a, pg_z = (u13[0]+2.5, u13[1]), (pad(b, "R6", "2")[0], pad(b, "R6", "2")[1]-1.0)
    for n, a, z in ((rt, rt_a, rt_z), (pg, pg_a, pg_z)):
        add_track(b, n, (u12 if n is rt else u13), a, pcbnew.F_Cu, 0.2)
        add_via(b, n, a); add_via(b, n, z); path(b, n, [a, (a[0], U3_TARGET[1]-2),
                                                        (z[0], U3_TARGET[1]-2), z], pcbnew.B_Cu, 0.2)
    # A direct B.Cu protected-12V trunk joins the nearest ideal-diode output.
    pwr_via = (U3_TARGET[0]-1, U3_TARGET[1]-8)
    add_track(b, vin, u1, pwr_via, pcbnew.F_Cu, 0.8); add_via(b, vin, pwr_via)
    path(b, vin, [pwr_via, (pwr_via[0], 140), (215, 140), (215, 150)], pcbnew.B_Cu, 1.0)
    pcbnew.ZONE_FILLER(b).Fill(b.Zones())
    b.Save(str(OUT))
    print(f"saved {OUT}; F1={F1_TARGET}; U3={U3_TARGET}")

if __name__ == "__main__": main()
