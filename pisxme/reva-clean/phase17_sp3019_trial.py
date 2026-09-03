"""Disposable SP3019-04HTG geometry trial; never used as production input."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "SP3019_ETHERNET_FIXTURE_BASE.kicad_pcb"
W = pcbnew.FromMM(0.13208)

def v(x, y): return pcbnew.VECTOR2I_MM(x, y)
def N(b, name):
    found = b.FindNet(name)
    if found is None and not name.startswith('/'):
        found = b.FindNet('/ETHERNET/' + name)
    if found is None: raise RuntimeError('missing net ' + name)
    return found
def tr(b, a, z, name, layer, width=W):
    t = pcbnew.PCB_TRACK(b); t.SetStart(v(*a)); t.SetEnd(v(*z)); t.SetLayer(layer)
    t.SetWidth(width); t.SetNet(N(b, name)); b.Add(t)
def via(b, p, name):
    q = pcbnew.PCB_VIA(b); q.SetPosition(v(*p)); q.SetWidth(pcbnew.FromMM(.45)); q.SetDrill(pcbnew.FromMM(.25))
    q.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); q.SetNet(N(b, name)); b.Add(q)

def sp3019(b, ref, x, y, nets, template=None):
    old = b.FindFootprintByReference(ref)
    if old is not None:
        b.Remove(old)
    f = template if template is not None else pcbnew.FootprintLoad(str(ROOT / "PiSXMe_RevA_Clean.pretty"), "SP3019_04HTG_SOT23_6L")
    f.SetReference(ref); f.SetValue("SP3019-04HTG"); f.SetPosition(v(x, y))
    b.Add(f)
    # KiCad's Flatpak Python ABI exposes Pads() as a SWIG container that is
    # not reliably iterable across KiCad 10 builds.  FindPadByNumber is the
    # native, stable lookup and also makes the pin-map explicit.
    for number, name in nets.items():
        p = f.FindPadByNumber(number)
        if p is None:
            raise RuntimeError(f'{ref}: missing pad {number}')
        if name:
            p.SetNet(N(b, name))
    return f

def main():
    b = pcbnew.LoadBoard(str(INPUT))
    if b.FindNet('/ETHERNET/ETH_GND') is None:
        b.Add(pcbnew.NETINFO_ITEM(b, '/ETHERNET/ETH_GND'))
    f9 = pcbnew.FootprintLoad(str(ROOT / "PiSXMe_RevA_Clean.pretty"), "SP3019_04HTG_SOT23_6L")
    f6 = pcbnew.FOOTPRINT(f9)
    # Keep the source board's authoritative J7/J2 footprints and board setup;
    # candidate-specific evidence is separated from the acreage DRC baseline.
    j2 = b.FindFootprintByReference("J2")
    j2.SetPosition(v(90, 105))
    j2.SetOrientationDegrees(0)
    # FootprintLoad is process-global in this KiCad 10 Flatpak ABI, so load
    # once and duplicate the native object for the second instance. Pad
    # assignment below uses FindPadByNumber, which is safe on the duplicate.
    # The native FOOTPRINT copy constructor preserves pads and attributes.
    sp3019(b, "U9", 25, 100, {"1":"CM5_GBE_TD3_P", "3":"CM5_GBE_TD3_N", "4":"CM5_GBE_TD2_P", "6":"CM5_GBE_TD2_N", "2":"ETH_GND"}, f9)
    sp3019(b, "U6", 29, 106, {"1":"CM5_GBE_TD1_P", "3":"CM5_GBE_TD1_N", "4":"CM5_GBE_TD0_P", "6":"CM5_GBE_TD0_N", "2":"ETH_GND"}, f6)
    def nt(a,z,name,layer): tr(b,a,z,name,layer,W)
    # Pair-separated monotonic corridors. Pair 3/1 use F.Cu and pair 2/0
    # use B.Cu, so the two CM5 source columns never share a route layer.
    paths = {
      "CM5_GBE_TD3_P":(((32.96,99.10),(31.8,99.10),(31.8,98.4),(24.05,98.4),(24.05,99.05)),pcbnew.F_Cu),
      "CM5_GBE_TD3_N":(((32.96,99.50),(31.4,99.50),(31.4,101.6),(24.05,101.6),(24.05,100.95)),pcbnew.F_Cu),
      "CM5_GBE_TD2_N":(((32.96,100.30),(31.0,100.30),(31.0,98.0),(25.95,98.0),(25.95,99.05)),pcbnew.B_Cu),
      "CM5_GBE_TD2_P":(((32.96,100.70),(30.6,100.70),(30.6,102.0),(25.95,102.0),(25.95,100.95)),pcbnew.B_Cu),
      "CM5_GBE_TD1_P":(((36.04,99.10),(35.4,99.10),(35.4,103.8),(28.05,103.8),(28.05,105.05)),pcbnew.F_Cu),
      "CM5_GBE_TD1_N":(((36.04,99.50),(34.8,99.50),(34.8,107.8),(28.05,107.8),(28.05,106.95)),pcbnew.F_Cu),
      "CM5_GBE_TD0_N":(((36.04,100.30),(34.2,100.30),(34.2,103.2),(29.95,103.2),(29.95,105.05)),pcbnew.B_Cu),
      "CM5_GBE_TD0_P":(((36.04,100.70),(33.6,100.70),(33.6,108.6),(29.95,108.6),(29.95,106.95)),pcbnew.B_Cu),}
    for name,(pts,layer) in paths.items():
        for a,z in zip(pts,pts[1:]): nt(a,z,name,layer)
    # ESD-to-MagJack corridors. These are intentionally long and separated so
    # the fixture tests topology and launch correctness before acreage packing.
    out_paths = {
      "CM5_GBE_TD3_N":(((47.05,100.45),(55,100.45),(55,96.17),(84.285,96.17)),pcbnew.F_Cu),
      "CM5_GBE_TD3_P":(((47.05,98.55),(56,98.55),(56,97.44),(86.825,97.44)),pcbnew.F_Cu),
      "CM5_GBE_TD2_N":(((48.95,98.55),(58,98.55),(58,95.0),(92,95.0),(92,97.44),(93.175,97.44)),pcbnew.F_Cu),
      "CM5_GBE_TD2_P":(((48.95,100.45),(59,100.45),(59,94.0),(94,94.0),(94,96.17),(95.715,96.17)),pcbnew.F_Cu),
      "CM5_GBE_TD1_N":(((47.05,107.45),(63,107.45),(63,109.06),(83.37,109.06)),pcbnew.F_Cu),
      "CM5_GBE_TD1_P":(((47.05,105.55),(64,105.55),(64,110.0),(85.91,110.0),(85.91,109.06)),pcbnew.F_Cu),
      "CM5_GBE_TD0_N":(((48.95,105.55),(67,105.55),(67,111.0),(94.09,111.0),(94.09,109.06)),pcbnew.F_Cu),
      "CM5_GBE_TD0_P":(((48.95,107.45),(68,107.45),(68,112.0),(96.63,112.0),(96.63,109.06)),pcbnew.F_Cu),
    }
    for name,(pts,layer) in out_paths.items():
        for a,z in zip(pts,pts[1:]): nt(a,z,name,layer)
    out = ROOT / "SP3019_ETHERNET_DISPOSABLE_FIXTURE.kicad_pcb"; b.Save(str(out)); print(out)
if __name__ == "__main__": main()
