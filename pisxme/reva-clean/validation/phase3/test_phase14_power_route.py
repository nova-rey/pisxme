from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
PCBNEW_PY = "/home/nyx/pisxme-toolchain-environment/bin/pisxme-pcbnew-python"


def main():
    result = subprocess.run([PCBNEW_PY, str(ROOT / "phase14_power_route.py")],
                            cwd=ROOT, check=True, text=True,
                            capture_output=True)
    assert "nineteen B.Cu power segments" in result.stdout
    probe = r'''
import pcbnew
b = pcbnew.LoadBoard("ACREAGE_POWER_PHASE14.kicad_pcb")
zones = {z.GetZoneName(): z for z in b.Zones()}
assert set(zones) == {"V100_PROTECTED_FEED", "V100_RETURN_PLANE_L2", "V100_RETURN_PLANE_L5"}
assert zones["V100_PROTECTED_FEED"].GetNetname() == "12V_PROTECTED"
assert zones["V100_RETURN_PLANE_L2"].GetNetname() == "POWER_GND"
assert zones["V100_RETURN_PLANE_L5"].GetNetname() == "POWER_GND"
assert zones["V100_RETURN_PLANE_L2"].GetLayer() == pcbnew.In1_Cu
assert zones["V100_RETURN_PLANE_L5"].GetLayer() == pcbnew.In4_Cu
assert all(z.IsFilled() for z in zones.values())
q1 = b.FindFootprintByReference("Q1"); q2 = b.FindFootprintByReference("Q2")
j1 = b.FindFootprintByReference("J1")
assert q1 and q2 and j1
assert any(p.GetNetname() == "12V_PROTECTED" for p in q1.Pads())
assert any(p.GetNetname() == "12V_PROTECTED" for p in q2.Pads())
assert sum(p.GetNetname() == "12V_PROTECTED" for p in j1.Pads()) == 130
tracks = list(b.GetTracks())
assert len(tracks) == 19
assert all(t.GetLayer() == pcbnew.B_Cu for t in tracks)
assert all(t.GetWidth() == pcbnew.FromMM(2.0) for t in tracks)
def pos(ref, number, net):
    fp = b.FindFootprintByReference(ref)
    pad = next(p for p in fp.Pads()
               if str(p.GetNumber()) == number and p.GetNetname() == net)
    return (pad.GetPosition().x, pad.GetPosition().y)
expected = {
    frozenset((pos("J5", "1", "/POWER_INPUT/12V_IN_A"),
               pos("F1", "1", "/POWER_INPUT/12V_IN_A"))),
    frozenset((pos("F1", "1", "/POWER_INPUT/12V_IN_A"), pos("F1", "2", "/POWER_INPUT/12V_IN_A"))),
    frozenset((pos("F1", "1", "/POWER_INPUT/12V_IN_A"), pos("F1", "3", "/POWER_INPUT/12V_IN_A"))),
    frozenset((pos("F1", "1", "/POWER_INPUT/12V_IN_A"), pos("F1", "4", "/POWER_INPUT/12V_IN_A"))),
    frozenset((pos("J6", "1", "/POWER_INPUT/12V_IN_B"), (pcbnew.VECTOR2I_MM(20, 45).x, pcbnew.VECTOR2I_MM(20, 45).y))),
    frozenset(((pcbnew.VECTOR2I_MM(20, 45).x, pcbnew.VECTOR2I_MM(20, 45).y),
               (pcbnew.VECTOR2I_MM(20, 90).x, pcbnew.VECTOR2I_MM(20, 90).y))),
    frozenset(((pcbnew.VECTOR2I_MM(20, 90).x, pcbnew.VECTOR2I_MM(20, 90).y),
               (pcbnew.VECTOR2I_MM(45, 90).x, pcbnew.VECTOR2I_MM(45, 90).y))),
    frozenset(((pcbnew.VECTOR2I_MM(45, 90).x, pcbnew.VECTOR2I_MM(45, 90).y),
               pos("F2", "1", "/POWER_INPUT/12V_IN_B"))),
    frozenset((pos("F2", "1", "/POWER_INPUT/12V_IN_B"), pos("F2", "2", "/POWER_INPUT/12V_IN_B"))),
    frozenset((pos("F2", "1", "/POWER_INPUT/12V_IN_B"), pos("F2", "3", "/POWER_INPUT/12V_IN_B"))),
    frozenset((pos("F2", "1", "/POWER_INPUT/12V_IN_B"), pos("F2", "4", "/POWER_INPUT/12V_IN_B"))),
    frozenset((pos("F1", "5", "/POWER_INPUT/FUSED_12V_A"), pos("F1", "6", "/POWER_INPUT/FUSED_12V_A"))),
    frozenset((pos("F1", "5", "/POWER_INPUT/FUSED_12V_A"), pos("F1", "7", "/POWER_INPUT/FUSED_12V_A"))),
    frozenset((pos("F1", "5", "/POWER_INPUT/FUSED_12V_A"), pos("F1", "8", "/POWER_INPUT/FUSED_12V_A"))),
    frozenset((pos("F1", "5", "/POWER_INPUT/FUSED_12V_A"),
               pos("Q1", "1", "/POWER_INPUT/FUSED_12V_A"))),
    frozenset((pos("F2", "5", "/POWER_INPUT/FUSED_12V_B"), pos("F2", "6", "/POWER_INPUT/FUSED_12V_B"))),
    frozenset((pos("F2", "5", "/POWER_INPUT/FUSED_12V_B"), pos("F2", "7", "/POWER_INPUT/FUSED_12V_B"))),
    frozenset((pos("F2", "5", "/POWER_INPUT/FUSED_12V_B"), pos("F2", "8", "/POWER_INPUT/FUSED_12V_B"))),
    frozenset((pos("F2", "5", "/POWER_INPUT/FUSED_12V_B"),
               pos("Q2", "1", "/POWER_INPUT/FUSED_12V_B"))),
}
actual = set()
for track in tracks:
    assert track.GetNetname() in {
        "/POWER_INPUT/12V_IN_A", "/POWER_INPUT/12V_IN_B",
        "/POWER_INPUT/FUSED_12V_A", "/POWER_INPUT/FUSED_12V_B",
    }
    actual.add(frozenset((tuple((track.GetStart().x, track.GetStart().y)),
                          tuple((track.GetEnd().x, track.GetEnd().y)))))
assert actual == expected, (actual, expected)
zone = zones["V100_PROTECTED_FEED"]
filled = zone.GetFilledPolysList(pcbnew.F_Cu)
for ref in ("Q1", "Q2"):
    pad = b.FindFootprintByReference(ref).FindPadByNumber("2")
    assert pad.GetNetname() == "12V_PROTECTED"
    assert filled.PointInside(pad.GetPosition())
assert all(track.GetNetname() != "12V_PROTECTED" for track in tracks)
'''
    subprocess.run([PCBNEW_PY, "-c", probe], cwd=ROOT, check=True,
                    text=True)
    print("Phase 14 power-route candidate: PASS; protected zone and two return planes filled")


if __name__ == "__main__":
    main()
