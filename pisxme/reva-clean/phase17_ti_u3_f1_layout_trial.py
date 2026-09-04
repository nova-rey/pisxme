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
U3_TARGET = tuple(float(x) for x in os.environ.get("PISXME_U3_TARGET", "60,165").split(","))
AUX_DX = float(os.environ.get("PISXME_AUX_DX", "50"))
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

def main():
    b = pcbnew.LoadBoard(str(BASE))
    local = {"12V_PROTECTED", "POWER_GND", "/REGULATORS/CM5_5V",
             "/CORE_CM5/CM5_5V", "/REGULATORS/FB_CM5_5V",
             "/REGULATORS/RT_CM5_5V", "/REGULATORS/PG_CM5_5V"}
    for item in list(b.GetTracks()):
        if item.GetNetname() in local or item.GetNetname() in {
                "/POWER_INPUT/12V_IN_A", "/POWER_INPUT/FUSED_12V_A"}:
            b.Remove(item)

    # F1 is translated as one coherent power-entry component.
    f1 = b.FindFootprintByReference("F1"); f1.SetPosition(V(*F1_TARGET))
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
    for ref, p0, angle in (("C5",(47,76),180),("C6",(47,78.25),180),
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
    P(b, outn, [u["8"], (U3_TARGET[0]-6,U3_TARGET[1]+2),
                (U3_TARGET[0]-6,U3_TARGET[1]+8), (c71[0],U3_TARGET[1]+8), c71], width=.25)
    P(b, outn, [u["9"], (U3_TARGET[0]+5,U3_TARGET[1]+2),
                (U3_TARGET[0]+5,U3_TARGET[1]+10), c81], width=.25)
    P(b, outn, [c71, (c71[0],c71[1]+3), (c81[0],c81[1]+1), c81], width=.25)
    P(b, outn, [c81, (c81[0]+4,c81[1]), (c92[0]+4,c92[1]), c92], pcbnew.B_Cu, .25)

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
    pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(f"saved {OUT}; F1={F1_TARGET}; U3={U3_TARGET}")

if __name__ == "__main__": main()
