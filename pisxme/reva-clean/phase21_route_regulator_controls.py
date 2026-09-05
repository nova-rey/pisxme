"""Place the remaining regulator control passives in open acreage and route them."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "PHASE21_CONTROLS_FB3V3_REFILLED.kicad_pcb"
OUTPUT = ROOT / "PHASE21_CONTROLS_REGULATOR_CONTROLS.kicad_pcb"

def P(x, y): return pcbnew.VECTOR2I_MM(x, y)
def tr(b, n, a, z, layer=pcbnew.F_Cu, width=.20):
    t = pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z));
    t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(width)); t.SetNet(n); b.Add(t)
def via(b, n, xy):
    v = pcbnew.PCB_VIA(b); v.SetPosition(P(*xy)); v.SetWidth(pcbnew.FromMM(.55));
    v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); v.SetNet(n); b.Add(v)
def fp(b, ref):
    return next(f for f in b.GetFootprints() if f.GetReference() == ref)

def main():
    b = pcbnew.LoadBoard(str(INPUT))
    nrt3 = b.FindNet('/REGULATORS/RT_BRIDGE_3V3')
    nrt1 = b.FindNet('/REGULATORS/RT_BRIDGE_1V1')
    nfb1 = b.FindNet('/REGULATORS/FB_BRIDGE_1V1')
    assert nrt3 and nrt1 and nfb1
    existing_tracks = list(b.GetTracks())

    # Re-home PG3V3 after moving the passives; the existing F.Cu PG vertical
    # blocks every right-side escape from U4.
    npg3 = b.FindNet('/REGULATORS/PG_BRIDGE_3V3')
    # U4 RT12 -> R13, right/bottom corridor, separated from PG3V3.
    r13 = fp(b, 'R13'); r13.SetPosition(P(218, 115)); r13.SetOrientationDegrees(0)
    r21 = fp(b, 'R21'); r21.SetPosition(P(246,90)); r21.SetOrientationDegrees(0)
    r19 = fp(b, 'R19'); r19.SetPosition(P(242,118)); r19.SetOrientationDegrees(90)
    r20 = fp(b, 'R20'); r20.SetPosition(P(246,118)); r20.SetOrientationDegrees(0)
    for item in existing_tracks:
        if item.GetNetCode() == npg3.GetNetCode(): b.Remove(item)
    tr(b, npg3, (227.25,104.75), (226,104.75), width=.13208)
    tr(b, npg3, (226,104.75), (226,102))
    via(b, npg3, (226,102))
    tr(b, npg3, (226,102), (220.5,102), pcbnew.B_Cu, .13208)
    tr(b, npg3, (220.5,102), (220.5,113), pcbnew.B_Cu, .13208)
    via(b, npg3, (220.5,113))
    tr(b, npg3, (220.5,113), (220.5,115), width=.13208)
    tr(b, nrt3, (227.25,105.25), (230,105.25))
    tr(b, nrt3, (230,105.25), (230,120))
    via(b, nrt3, (230,120))
    tr(b, nrt3, (230,120), (218,120), pcbnew.B_Cu)
    via(b, nrt3, (218,120))
    tr(b, nrt3, (218,120), (217.5,115))

    # Re-home PG1V1 to a small B.Cu loop so the three U5 right-side controls
    # have independent F.Cu escapes.
    npg1 = b.FindNet('/REGULATORS/PG_BRIDGE_1V1')
    for item in existing_tracks:
        if item.GetNetCode() == npg1.GetNetCode(): b.Remove(item)
    tr(b, npg1, (237.25,104.75), (238.5,104.75), width=.13208)
    tr(b, npg1, (238.5,104.75), (238.5,103.0))
    via(b, npg1, (238.5,103.0))
    tr(b, npg1, (238.5,103.0), (240.5,103.0), pcbnew.B_Cu, .13208)
    tr(b, npg1, (240.5,103.0), (240.5,113.5), pcbnew.B_Cu, .13208)
    via(b, npg1, (240.5,113.5))
    tr(b, npg1, (240.5,113.5), (240.5,115), width=.13208)

    # U5 RT12 -> R21, east/up corridor, clear of PG1V1.
    tr(b, nrt1, (237.25,105.25), (240.5,105.25))
    tr(b, nrt1, (240.5,105.25), (240.5,101))
    via(b, nrt1, (240.5,101))
    tr(b, nrt1, (240.5,101), (246,101), pcbnew.B_Cu)
    tr(b, nrt1, (246,101), (246,91), pcbnew.B_Cu)
    via(b, nrt1, (246,91))
    tr(b, nrt1, (246,91), (245.5,90))

    # U5 FB10 -> R19.2 -> R20.1, east/down corridor.
    tr(b, nfb1, (237.25,106.25), (242.5,106.25))
    tr(b, nfb1, (242.5,106.25), (242.5,117.5))
    tr(b, nfb1, (242.5,117.5), (242,117.5))
    tr(b, nfb1, (242,117.5), (242,116))
    tr(b, nfb1, (242,116), (245.5,116))
    tr(b, nfb1, (245.5,116), (245.5,118))
    b.Save(str(OUTPUT)); print(OUTPUT)

if __name__ == '__main__': main()
