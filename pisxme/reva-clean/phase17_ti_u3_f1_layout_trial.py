"""Disposable TI-style U3 island / F1 floorplan trial for Phase 17.

The control geometry is the accepted Phase-15 contract translated as one
island.  This is a diagnostic candidate only; it is never a release board.
"""
from pathlib import Path
import os
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = Path(os.environ.get("PISXME_BASE", ROOT / "ACREAGE_PHASE16_PCIE_ONLY_BOUNDARY2.kicad_pcb"))
OUT = Path(os.environ.get("PISXME_OUT", ROOT / "ACREAGE_PHASE17_TI_U3_F1_LAYOUT.kicad_pcb"))
F1_TARGET = tuple(float(x) for x in os.environ.get("PISXME_F1_TARGET", "100,20").split(","))
F2_TARGET = tuple(float(x) for x in os.environ.get("PISXME_F2_TARGET", "50,120").split(","))
U3_TARGET = tuple(float(x) for x in os.environ.get("PISXME_U3_TARGET", "60,165").split(","))
AUX_DX = float(os.environ.get("PISXME_AUX_DX", "50"))
BRIDGE_DY = float(os.environ.get("PISXME_BRIDGE_DY", "10"))
OLD_U3 = (52.0, 78.0)
OLD_F1 = (55.0, 40.0)

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def xy(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def N(b, name):
    n = b.FindNet(name)
    if n is None: raise RuntimeError(f"missing net {name}")
    return n
def T(b, n, a, z, layer=pcbnew.F_Cu, width=0.2):
    q = pcbnew.PCB_TRACK(b); q.SetStart(V(*a)); q.SetEnd(V(*z)); q.SetLayer(layer)
    q.SetWidth(pcbnew.FromMM(width)); q.SetNet(n); b.Add(q)
def P(b, n, points, layer=pcbnew.F_Cu, width=0.2):
    for a, z in zip(points, points[1:]): T(b, n, a, z, layer, width)
def via(b, n, p):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); q.SetNet(n); b.Add(q)
def pad(b, ref, num):
    f = b.FindFootprintByReference(ref)
    for p in f.Pads():
        if p.GetNumber() == str(num): return xy(p.GetPosition())
    raise RuntimeError(f"missing {ref}.{num}")

def add_ground_plane(b, layer):
    z = pcbnew.ZONE(b)
    z.SetLayer(layer)
    z.SetNet(N(b, "POWER_GND"))
    z.SetMinThickness(pcbnew.FromMM(.035))
    z.SetLocalClearance(pcbnew.FromMM(.15))
    outline = pcbnew.SHAPE_LINE_CHAIN()
    for point in ((1, 1), (299, 1), (299, 179), (1, 179)):
        outline.Append(V(*point))
    outline.SetClosed(True)
    z.Outline().AddOutline(outline)
    b.Add(z)

def main():
    b = pcbnew.LoadBoard(str(BASE))
    # Current JLC multilayer capability supports 0.15 mm trace/space.  The
    # Phase-17 disposable candidate therefore carries the fabrication-rule
    # floor used by the current 100-ohm Ethernet basis instead of inheriting
    # the older 0.20 mm scaffold minimum.
    ds = b.GetDesignSettings()
    ds.m_TrackMinWidth = pcbnew.FromMM(0.13208)
    ds.m_MinClearance = pcbnew.FromMM(0.15)
    default_nc = ds.m_NetSettings.GetDefaultNetclass()
    default_nc.SetTrackWidth(pcbnew.FromMM(0.13208))
    default_nc.SetClearance(pcbnew.FromMM(0.15))
    default_nc.SetViaDiameter(pcbnew.FromMM(0.50))
    default_nc.SetViaDrill(pcbnew.FromMM(0.30))
    local = {"12V_PROTECTED", "POWER_GND", "/REGULATORS/CM5_5V",
             "/CORE_CM5/CM5_5V", "/REGULATORS/FB_CM5_5V",
             "/REGULATORS/RT_CM5_5V", "/REGULATORS/PG_CM5_5V"}
    for item in list(b.GetTracks()):
        if item.GetNetname() in local or item.GetNetname() in {
                "/POWER_INPUT/12V_IN_A", "/POWER_INPUT/FUSED_12V_A",
                "/POWER_INPUT/12V_IN_B", "/POWER_INPUT/FUSED_12V_B"}:
            b.Remove(item)

    # F1 is translated as one coherent power-entry component.
    f1 = b.FindFootprintByReference("F1"); f1.SetPosition(V(*F1_TARGET))
    # F2 is the local power-entry obstruction in the recovered acreage floorplan.
    # Move the complete holder only when explicitly requested; this keeps the
    # default comparable to the lower-island baseline and makes the experiment
    # reproducible without changing the electrical topology.
    f2 = b.FindFootprintByReference("F2"); f2.SetPosition(V(*F2_TARGET))
    ni, no = N(b, "/POWER_INPUT/12V_IN_A"), N(b, "/POWER_INPUT/FUSED_12V_A")
    P(b, ni, [(F1_TARGET[0]-6.4, F1_TARGET[1]-1.25), (12,25)], pcbnew.B_Cu, 2.0)
    P(b, no, [(F1_TARGET[0]+2.9, F1_TARGET[1]-1.25), (212.46,30)], pcbnew.B_Cu, 2.0)

    # Move U3 and its complete TI support island.  The support coordinates are
    # the Phase-15 vendor-style escape rows, translated below the PERST lane.
    dx, dy = U3_TARGET[0]-OLD_U3[0], U3_TARGET[1]-OLD_U3[1]
    for ref in ("U3", "C5", "C6", "C7", "C8", "C9", "R3", "R4", "R5", "R6"):
        f = b.FindFootprintByReference(ref); p0 = xy(f.GetPosition())
        f.SetPosition(V(p0[0]+dx, p0[1]+dy))
    for ref in ("C23", "C24", "C25", "R19", "R20", "R21", "R22"):
        f = b.FindFootprintByReference(ref); p0 = xy(f.GetPosition())
        f.SetPosition(V(p0[0] + AUX_DX, p0[1]))
    # The complete bridge-output capacitor acreage is the remaining object
    # at the CM5_PERST terminus.  Translate it coherently, preserving the
    # regulator topology while clearing that frozen PCIe corridor.
    for ref in tuple(f"C{n}" for n in range(26, 42)):
        f = b.FindFootprintByReference(ref); p0 = xy(f.GetPosition())
        f.SetPosition(V(p0[0], p0[1] + BRIDGE_DY))
    for ref, p0, angle in (("C5",(44,76),180),("C6",(44,78.25),180),
                           ("C7",(57,81.5),0),("C8",(57,83.5),0),
                           ("C9",(73,62),0),("R3",(78,62),180),
                           ("R4",(82,62),0),("R5",(61,66),0),
                           ("R6",(73,69),180)):
        extra = 15 if ref in ("C9","R3","R4","R5","R6") else 0
        f = b.FindFootprintByReference(ref); f.SetPosition(V(p0[0]+dx,p0[1]+dy+extra)); f.SetOrientationDegrees(angle)

    vin, outn = N(b,"12V_PROTECTED"), N(b,"/CORE_CM5/CM5_5V")
    # TI-style VIN/VOUT pad-edge escapes.  Pin 5 is VLDOIN and deliberately
    # joins the output rail, not the protected input rail.
    u = {str(i):pad(b,"U3",str(i)) for i in (1,5,8,9,10,12,13,16)}
    for ref, target in (("C5",u["1"]),("C6",u["16"])):
        active = next(p for p in b.FindFootprintByReference(ref).Pads() if p.GetNetname()=="12V_PROTECTED")
        a = xy(active.GetPosition())
        # C6's direct lower-row escape would pass the corrected VLDOIN pad 5;
        # dogleg it above the package before reaching VIN2.
        if ref == "C6":
            P(b, vin, [a, (a[0], U3_TARGET[1]-3),
                       (target[0], U3_TARGET[1]-3), target], width=.30)
        else:
            T(b, vin, a, target, pcbnew.F_Cu, .30)
    # Output perimeter and corrected VLDOIN tie.
    c71, c81, c92 = pad(b,"C7","1"), pad(b,"C8","1"), pad(b,"C9","2")
    # Keep both VOUT pad escapes inside the package's south perimeter.  The
    # former long rectangular loops crossed the relocated PG/FB corridors and
    # were not part of the TI local escape geometry.
    P(b, outn, [u["5"], (u["5"][0],165.25), (54.5,165.25),
                (54.5,168.0), (u["8"][0],168.0), u["8"]],
      pcbnew.F_Cu, .25)
    P(b, outn, [u["8"], (u["8"][0], c71[1]), c71], width=.25)
    P(b, outn, [u["9"], (u["9"][0], c81[1]), c81], width=.25)
    P(b, outn, [c71, c81], width=.25)
    # Keep the output-capacitor tie on the local F.Cu perimeter.  The earlier
    # B.Cu tie occupied the same quiet return corridor as translated FB/PG.
    # C8's ground pad is immediately to its east; leave C8 to the west,
    # transition with ordinary vias, and use the quiet corridor below the
    # translated FB/PG rows before returning to the feedback capacitor.
    ct_a, ct_b = (60.0, 180.0), (78.0, 180.0)
    P(b, outn, [c81, ct_a], pcbnew.F_Cu, .25)
    via(b, outn, ct_a); via(b, outn, ct_b)
    P(b, outn, [ct_a, ct_b], pcbnew.B_Cu, .25)
    P(b, outn, [ct_b, (81.5,180.0), (81.5,171.0)], pcbnew.F_Cu, .25)
    P(b, outn, [c92, (83.0,164.0), (83.0,180.0), ct_b],
      pcbnew.F_Cu, .25)
    # Approach R3 pad 1 from the east so the adjacent FB pad 2 is not crossed.
    P(b, outn, [c92, (81.95,166.0), (86.5,166.0), (86.5,164.0)],
      pcbnew.F_Cu, .25)

    fb, rt, pg = (N(b,x) for x in ("/REGULATORS/FB_CM5_5V",
                                   "/REGULATORS/RT_CM5_5V",
                                   "/REGULATORS/PG_CM5_5V"))
    # Quiet FB/RT/PG corridors are direct translations of Phase-15 controls.
    def tr(p0): return (p0[0]+dx,p0[1]+dy+10)
    for a,z in [((54.70,79.25),(56,79.25)),((56,79.25),(56,60)),
                ((56,60),(81.5,60)),((81.5,61),(81.5,60)),
                ((71.65,61),(71.65,60)),((77.5,61),(77.5,60))]: T(b,fb,tr(a),tr(z),pcbnew.B_Cu if a[1]==60 or z[1]==60 else pcbnew.F_Cu,.20)
    for p0 in ((56,79.25),(71.65,61),(77.5,61),(81.5,61)):
        via(b,fb,tr(p0))
    for a,z in [((54.70,78.25),(58,78.25)),((58,78.25),(58,66)),((58,66),(60.5,65))]: T(b,rt,tr(a),tr(z),pcbnew.B_Cu if a[1]!=78.25 or z[1]!=78.25 else pcbnew.F_Cu,.20)
    via(b,rt,tr((58,78.25))); via(b,rt,tr((60.5,65)))
    for a,z in [((54.7,77.75),(55.5,77.75)),((55.5,77.75),(62,77.75)),((62,77.75),(62,69)),((62,69),(72.5,70))]: T(b,pg,tr(a),tr(z),pcbnew.B_Cu if a[1]!=77.75 or z[1]!=77.75 else pcbnew.F_Cu,.20)
    via(b,pg,tr((62,77.75))); via(b,pg,tr((72.5,70)))
    # Explicit CM5 +5 V boundary: bus all six J7 input lands, then use one
    # ordinary-via B.Cu trunk to the relocated output capacitor.  This keeps
    # the high-current/CM5 handoff visible and avoids plane-layer signal
    # routing or relying on a zone to bridge hierarchy boundaries.
    cm5 = N(b, "/CORE_CM5/CM5_5V")
    j7 = b.FindFootprintByReference("J7")
    j5 = [xy(p.GetPosition()) for p in j7.Pads() if p.GetNumber() in {"77","79","81","83","85","87"}]
    j5.sort(key=lambda p:p[1])
    for a,z in zip(j5,j5[1:]): T(b, cm5, a, z, pcbnew.F_Cu, .20)
    # Launch from the uppermost +5 V land toward the free side of the CM5
    # footprint; launching below pad 87 collides with adjacent WiFi land 89.
    jvia = (j5[0][0]+4.0, j5[0][1])
    # Escape to the narrow east-side edge of the CM5 power column, then use
    # the outer corridor beside (not through) the F2 holder.  The west escape
    # hit J7 pad 75 and the J4 shell; the former x=50 trunk hit quiet controls.
    # Raspberry Pi's official CM5IO fanout uses 0.20 mm traces on this
    # 0.4 mm-pitch power row.  The earlier 0.25 mm launch cannot meet the
    # neighboring-pad clearance even though its centerline is correct.
    # Stop before the opposite J7 pad column; x=35.3 leaves the official
    # 0.20 mm trace plus 0.20 mm clearance to pad 78, then escapes below the
    # connector body before turning toward the power island.
    P(b, cm5, [j5[0], (35.2, j5[0][1])], pcbnew.F_Cu, .20)
    via(b, cm5, (35.2, j5[0][1]))
    P(b, cm5, [(35.2, j5[0][1]), (40,120), (40,155)], pcbnew.B_Cu, .20)
    via(b, cm5, (40,155))
    P(b, cm5, [(40,155), (40,168.5), c71], pcbnew.F_Cu, .20)
    # The Phase-16 boundary is intentionally a copper/placement ancestor;
    # instantiate the frozen solid GND planes here so native connectivity
    # validation does not misclassify every ground pad as a scaffold open.
    if not list(b.Zones()):
        add_ground_plane(b, pcbnew.In1_Cu)
        add_ground_plane(b, pcbnew.In4_Cu)
    pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(f"saved {OUT}; F1={F1_TARGET}; F2={F2_TARGET}; U3={U3_TARGET}")

if __name__ == "__main__": main()
