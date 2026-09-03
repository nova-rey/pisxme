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
    # Match the board's ordinary-through-via minimums; these are deliberately
    # not placed in any SMD pad or pad courtyard.
    q = pcbnew.PCB_VIA(b); q.SetPosition(v(*p)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30))
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
    j7.SetPosition(v(100, 160))
    j2 = b.FindFootprintByReference("J2")
    j2.SetPosition(v(100, 80))
    j2.SetOrientationDegrees(0)
    # FootprintLoad is process-global in this KiCad 10 Flatpak ABI, so load
    # once and duplicate the native object for the second instance. Pad
    # assignment below uses FindPadByNumber, which is safe on the duplicate.
    # The native FOOTPRINT copy constructor preserves pads and attributes.
    sp3019(b, "U9", 90, 130, {"1":"CM5_GBE_TD3_P", "3":"CM5_GBE_TD3_N", "4":"CM5_GBE_TD2_N", "6":"CM5_GBE_TD2_P", "2":"ETH_GND"}, f9)
    sp3019(b, "U6", 110, 130, {"1":"CM5_GBE_TD1_P", "3":"CM5_GBE_TD1_N", "4":"CM5_GBE_TD0_N", "6":"CM5_GBE_TD0_P", "2":"ETH_GND"}, f6)
    def nt(a,z,name,layer): tr(b,a,z,name,layer,W)
    # Pair-separated monotonic corridors. Pair 3/1 use F.Cu and pair 2/0
    # use B.Cu, so the two CM5 source columns never share a route layer.
    paths = {
      "CM5_GBE_TD3_P":(((97.96,129.10),(93,129.10),(93,129.05),(89.05,129.05)),pcbnew.F_Cu),
      "CM5_GBE_TD3_N":(((97.96,129.50),(94,129.50),(94,130.95),(89.05,130.95)),pcbnew.F_Cu),
      "CM5_GBE_TD1_P":(((101.04,129.10),(106,129.10),(106,129.05),(119.05,129.05)),pcbnew.F_Cu),
      "CM5_GBE_TD1_N":(((101.04,129.50),(107,129.50),(107,130.95),(119.05,130.95)),pcbnew.F_Cu),}
    bpaths = {
      "CM5_GBE_TD2_N":(((97.96,130.30),(95,130.30),(95,132),(92,132),(92,130.95)),(96,130.30),(92,130.95),(90.95,130.95)),
      "CM5_GBE_TD2_P":(((97.96,130.70),(96,130.70),(96,133),(91,133),(91,129.05)),(97,130.70),(91,129.05),(90.95,129.05)),
      "CM5_GBE_TD0_N":(((101.04,130.30),(105,130.30),(105,132),(108,132),(108,130.95)),(104,130.30),(108,130.95),(120.95,130.95)),
      "CM5_GBE_TD0_P":(((101.04,130.70),(104,130.70),(104,133),(109,133),(109,129.05)),(103,130.70),(109,129.05),(120.95,129.05)),}
    for name,(pts,layer) in paths.items():
        for a,z in zip(pts,pts[1:]): nt(a,z,name,layer)
    for name,(pts,src_via,esd_via,pad) in bpaths.items():
        # F.Cu source breakout -> ordinary through-via -> B.Cu corridor.
        nt(pts[0],src_via,name,pcbnew.F_Cu)
        via(b,src_via,name)
        for a,z in zip([src_via]+list(pts[1:]),list(pts[1:])+[esd_via]):
            if a != z: nt(a,z,name,pcbnew.B_Cu)
        via(b,esd_via,name)
        nt(esd_via, pad, name, pcbnew.F_Cu)
    # ESD-to-MagJack corridors. These are intentionally long and separated so
    # the fixture tests topology and launch correctness before acreage packing.
    out_paths = {
      "CM5_GBE_TD3_P":(((89.05,129.05),(88,129.05),(88,77.44),(96.825,77.44)),pcbnew.F_Cu),
      "CM5_GBE_TD3_N":(((89.05,130.95),(87,130.95),(87,76.17),(94.285,76.17)),pcbnew.F_Cu),
      "CM5_GBE_TD1_P":(((119.05,129.05),(112,129.05),(112,84.06),(95.91,84.06)),pcbnew.F_Cu),
      "CM5_GBE_TD1_N":(((119.05,130.95),(111,130.95),(111,84.06),(93.37,84.06)),pcbnew.F_Cu),
      "CM5_GBE_TD2_P":(((91,129.05),(98,129.05),(98,76.17),(105.715,76.17)),pcbnew.B_Cu),
      "CM5_GBE_TD2_N":(((92,130.95),(94,130.95),(94,77.44),(103.175,77.44)),pcbnew.B_Cu),
      "CM5_GBE_TD0_P":(((109,129.05),(109,84.06),(106.63,84.06)),pcbnew.B_Cu),
      "CM5_GBE_TD0_N":(((108,130.95),(107,130.95),(107,84.06),(104.09,84.06)),pcbnew.B_Cu),
    }
    for name,(pts,layer) in out_paths.items():
        for a,z in zip(pts,pts[1:]): nt(a,z,name,layer)
    # Complete the disposable return/connector support proof.  The ESD
    # grounds leave their SMD pads on short F.Cu branches to ordinary GND
    # stitching vias; the two authoritative shield pads are tied together.
    for pad, vp in [((89.05,130.0),(86.5,130.0)), ((109.05,130.0),(106.5,130.0))]:
        nt(pad,vp,'ETH_GND',pcbnew.F_Cu); via(b,vp,'ETH_GND')
    nt((86.5,130.0),(86.5,140.0),'ETH_GND',pcbnew.B_Cu)
    nt((86.5,140.0),(106.5,140.0),'ETH_GND',pcbnew.B_Cu)
    nt((106.5,140.0),(106.5,130.0),'ETH_GND',pcbnew.B_Cu)
    nt((94.285,71.11),(95.555,73.65),'GBE_SHIELD',pcbnew.F_Cu)
    out = ROOT / "SP3019_ETHERNET_DISPOSABLE_FIXTURE.kicad_pcb"; b.Save(str(out)); print(out)
if __name__ == "__main__": main()
