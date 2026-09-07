"""Disposable local RTL_1V1 power-zone probe around the QFN pad field."""
from pathlib import Path
import pcbnew

BASE = Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V5_NO_FIXTURE_STUBS.kicad_pcb")
OUT = Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V8_1V1_ZONE.kicad_pcb")

def main():
    b = pcbnew.LoadBoard(str(BASE)); n = b.FindNet("RTL_1V1")
    if n is None: raise SystemExit("missing RTL_1V1")
    z = pcbnew.ZONE(b); z.SetLayer(pcbnew.F_Cu); z.SetNet(n); z.SetNetCode(n.GetNetCode())
    z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL)
    poly = pcbnew.VECTOR_VECTOR2I()
    for x, y in ((75.4, 57.6), (83.4, 57.6), (83.4, 66.8), (75.4, 66.8)):
        poly.append(pcbnew.VECTOR2I_MM(x, y))
    z.AddPolygon(poly); b.Add(z); pcbnew.ZONE_FILLER(b).Fill(b.Zones())
    b.Save(str(OUT)); print(OUT)

if __name__ == "__main__": main()
