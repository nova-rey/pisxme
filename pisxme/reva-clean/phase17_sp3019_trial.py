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
    j7 = b.FindFootprintByReference("J7")
    j7.SetPosition(v(100, 130))
    j2 = b.FindFootprintByReference("J2")
    j2.SetPosition(v(100, 40))
    j2.SetOrientationDegrees(90)
    # FootprintLoad is process-global in this KiCad 10 Flatpak ABI, so load
    # once and duplicate the native object for the second instance. Pad
    # assignment below uses FindPadByNumber, which is safe on the duplicate.
    # The native FOOTPRINT copy constructor preserves pads and attributes.
    sp3019(b, "U9", 90, 100, {"1":"CM5_GBE_TD3_P", "3":"CM5_GBE_TD3_N", "4":"CM5_GBE_TD2_P", "6":"CM5_GBE_TD2_N", "2":"ETH_GND"}, f9)
    sp3019(b, "U6", 110, 100, {"1":"CM5_GBE_TD1_P", "3":"CM5_GBE_TD1_N", "4":"CM5_GBE_TD0_P", "6":"CM5_GBE_TD0_N", "2":"ETH_GND"}, f6)
    def nt(a,z,name,layer): tr(b,a,z,name,layer,W)
    # Pair-separated monotonic corridors. Pair 3/1 use F.Cu and pair 2/0
    # use B.Cu, so the two CM5 source columns never share a route layer.
    paths = {
      "CM5_GBE_TD3_P":(((97.96,99.10),(93,99.10),(93,99.05),(89.05,99.05)),pcbnew.F_Cu),
      "CM5_GBE_TD3_N":(((97.96,99.50),(94,99.50),(94,100.95),(89.05,100.95)),pcbnew.F_Cu),
      "CM5_GBE_TD1_P":(((101.04,99.10),(106,99.10),(106,99.05),(119.05,99.05)),pcbnew.F_Cu),
      "CM5_GBE_TD1_N":(((101.04,99.50),(107,99.50),(107,100.95),(119.05,100.95)),pcbnew.F_Cu),}
    bpaths = {
      "CM5_GBE_TD2_N":(((97.96,100.30),(93,100.30),(93,98.0),(91.95,98.0),(91.95,99.05)),(90.95,99.05),(90.95,99.05)),
      "CM5_GBE_TD2_P":(((97.96,100.70),(94,100.70),(94,102.0),(91.95,102.0),(91.95,100.95)),(90.95,100.95),(90.95,100.95)),
      "CM5_GBE_TD0_N":(((101.04,100.30),(107,100.30),(107,98.0),(108.05,98.0),(108.05,99.05)),(109.05,99.05),(109.05,99.05)),
      "CM5_GBE_TD0_P":(((101.04,100.70),(108,100.70),(108,102.0),(108.05,102.0),(108.05,100.95)),(109.05,100.95),(109.05,100.95)),}
    for name,(pts,layer) in paths.items():
        for a,z in zip(pts,pts[1:]): nt(a,z,name,layer)
    for name,(pts,src_via,esd_via) in bpaths.items():
        # F.Cu source breakout -> ordinary through-via -> B.Cu corridor.
        nt(pts[0],src_via,name,pcbnew.F_Cu)
        via(b,src_via,name)
        for a,z in zip([src_via]+list(pts[1:]),list(pts[1:])+[esd_via]):
            if a != z: nt(a,z,name,pcbnew.B_Cu)
        via(b,esd_via,name)
        nt(esd_via, (90.95,99.05) if name.endswith("TD2_N") else (90.95,100.95) if name.endswith("TD2_P") else (120.95,99.05) if name.endswith("TD0_N") else (120.95,100.95), name, pcbnew.F_Cu)
    # ESD-to-MagJack corridors. These are intentionally long and separated so
    # the fixture tests topology and launch correctness before acreage packing.
    out_paths = {
      "CM5_GBE_TD3_P":(((89.05,99.05),(88,99.05),(88,43.175),(97.44,43.175)),pcbnew.F_Cu),
      "CM5_GBE_TD3_N":(((89.05,100.95),(87,100.95),(87,45.715),(96.17,45.715)),pcbnew.F_Cu),
      "CM5_GBE_TD1_P":(((119.05,99.05),(112,99.05),(112,44.09),(104.06,44.09)),pcbnew.F_Cu),
      "CM5_GBE_TD1_N":(((119.05,100.95),(111,100.95),(111,46.63),(104.06,46.63)),pcbnew.F_Cu),
      "CM5_GBE_TD2_N":(((90.95,99.05),(92,99.05),(92,36.825),(97.44,36.825)),pcbnew.B_Cu),
      "CM5_GBE_TD2_P":(((90.95,100.95),(90.95,104),(98,104),(98,34.285),(96.17,34.285)),pcbnew.B_Cu),
      "CM5_GBE_TD0_N":(((120.95,99.05),(118,99.05),(118,35.91),(104.06,35.91)),pcbnew.B_Cu),
      "CM5_GBE_TD0_P":(((120.95,100.95),(120.95,104),(102,104),(102,33.37),(104.06,33.37)),pcbnew.B_Cu),
    }
    for name,(pts,layer) in out_paths.items():
        for a,z in zip(pts,pts[1:]): nt(a,z,name,layer)
    out = ROOT / "SP3019_ETHERNET_DISPOSABLE_FIXTURE.kicad_pcb"; b.Save(str(out)); print(out)
if __name__ == "__main__": main()
