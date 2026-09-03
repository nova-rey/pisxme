"""Fresh large-acreage ESDS304 Ethernet escape experiment.

This is disposable Phase 17 evidence only.  The two protectors are placed
between the CM5/J7 source and J2 so the four pairs have monotonic, separated
F.Cu/B.Cu corridors.  It intentionally does not modify the clean PCB.
"""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
W = 0.13208

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def N(b, name):
    q = b.FindNet(name) or b.FindNet('/ETHERNET/' + name)
    if q is None: raise RuntimeError(name)
    return q
def seg(b, a, z, name, layer=pcbnew.F_Cu):
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z));
    t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(W)); t.SetNet(N(b, name)); b.Add(t)
def path(b, pts, name, layer):
    for a, z in zip(pts, pts[1:]): seg(b, a, z, name, layer)
def via(b, p, name):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50));
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    q.SetNet(N(b, name)); b.Add(q)

def main():
    b = pcbnew.LoadBoard(str(ROOT/'SP3019_ETHERNET_FIXTURE_BASE.kicad_pcb'))
    if b.FindNet('/ETHERNET/ETH_GND') is None:
        b.Add(pcbnew.NETINFO_ITEM(b, '/ETHERNET/ETH_GND'))
    j7 = b.FindFootprintByReference('J7'); j7.SetPosition(V(100,160))
    j2 = b.FindFootprintByReference('J2'); j2.SetPosition(V(100,60)); j2.SetOrientationDegrees(0)
    f = pcbnew.FootprintLoad(str(ROOT/'PiSXMe_RevA_Clean.pretty'),'ESDS304DBVR_SOT23_5')
    u9, u6 = pcbnew.FOOTPRINT(f), pcbnew.FOOTPRINT(f)
    for ref, fp, x, names in [
        ('U9',u9,80,('CM5_GBE_TD3_P','CM5_GBE_TD3_N','CM5_GBE_TD2_P','CM5_GBE_TD2_N')),
        ('U6',u6,120,('CM5_GBE_TD1_P','CM5_GBE_TD1_N','CM5_GBE_TD0_P','CM5_GBE_TD0_N'))]:
        fp.SetReference(ref); fp.SetValue('ESDS304DBVR'); fp.SetPosition(V(x,110)); b.Add(fp)
        for p, n in zip(('1','3','4','5'), names): fp.FindPadByNumber(p).SetNet(N(b,n))
        fp.FindPadByNumber('2').SetNet(N(b,'ETH_GND'))

    # Correct pad coordinates: U9 left pads 1/2/3 = (78.7,109.05/110/110.95),
    # right pads 5/4 = (81.3,109.525/110.475); U6 is translated +40 mm.
    # F.Cu pair TD3 source escape and connector launch.
    path(b,[(97.96,129.10),(94,129.10),(94,106),(78.7,106),(78.7,109.05)],'CM5_GBE_TD3_P',pcbnew.F_Cu)
    path(b,[(97.96,129.50),(93,129.50),(93,114),(77.0,114),(77.0,110.95),(78.7,110.95)],'CM5_GBE_TD3_N',pcbnew.F_Cu)
    path(b,[(78.7,109.05),(76.0,109.05),(76.0,52),(94.285,56.17)],'CM5_GBE_TD3_P',pcbnew.F_Cu)
    path(b,[(78.7,110.95),(75.0,110.95),(75.0,50),(96.825,57.44)],'CM5_GBE_TD3_N',pcbnew.F_Cu)

    # F.Cu TD1 source and lower connector launch, kept on its own acreage lanes.
    path(b,[(101.04,129.10),(106,129.10),(106,106),(118.7,106),(118.7,109.05)],'CM5_GBE_TD1_P',pcbnew.F_Cu)
    path(b,[(101.04,129.50),(107,129.50),(107,114),(120.0,114),(120.0,110.95),(118.7,110.95)],'CM5_GBE_TD1_N',pcbnew.F_Cu)
    path(b,[(118.7,109.05),(116.0,109.05),(116.0,70),(95.91,64.06)],'CM5_GBE_TD1_P',pcbnew.F_Cu)
    path(b,[(118.7,110.95),(115.0,110.95),(115.0,72),(98.45,64.06)],'CM5_GBE_TD1_N',pcbnew.F_Cu)

    # B.Cu TD2: source vias, dogbones, and an upper launch shelf.
    for p,n in [((97.96,130.30),'CM5_GBE_TD2_N'),((97.96,130.70),'CM5_GBE_TD2_P')]: via(b,p,n)
    via(b,(83,109.525),'CM5_GBE_TD2_N'); via(b,(84,110.475),'CM5_GBE_TD2_P')
    path(b,[(97.96,130.30),(86,130.30),(86,105),(83,105),(83,109.525)],'CM5_GBE_TD2_N',pcbnew.B_Cu)
    path(b,[(97.96,130.70),(88,130.70),(88,115),(84,115),(84,110.475)],'CM5_GBE_TD2_P',pcbnew.B_Cu)
    path(b,[(81.3,109.525),(83,109.525)],'CM5_GBE_TD2_N',pcbnew.F_Cu)
    path(b,[(81.3,110.475),(84,110.475)],'CM5_GBE_TD2_P',pcbnew.F_Cu)
    path(b,[(83,109.525),(83,80),(107,80),(107,52),(105.715,57.44)],'CM5_GBE_TD2_N',pcbnew.B_Cu)
    path(b,[(84,110.475),(84,78),(103,78),(103,52),(104.285,56.17)],'CM5_GBE_TD2_P',pcbnew.B_Cu)

    # B.Cu TD0: lower launch shelf, separated from the TD2 upper shelf.
    for p,n in [((101.04,130.30),'CM5_GBE_TD0_N'),((101.04,130.70),'CM5_GBE_TD0_P')]: via(b,p,n)
    via(b,(117,109.525),'CM5_GBE_TD0_N'); via(b,(118,110.475),'CM5_GBE_TD0_P')
    path(b,[(101.04,130.30),(114,130.30),(114,105),(117,105),(117,109.525)],'CM5_GBE_TD0_N',pcbnew.B_Cu)
    path(b,[(101.04,130.70),(116,130.70),(116,115),(118,115),(118,110.475)],'CM5_GBE_TD0_P',pcbnew.B_Cu)
    path(b,[(121.3,109.525),(117,109.525)],'CM5_GBE_TD0_N',pcbnew.F_Cu)
    path(b,[(121.3,110.475),(118,110.475)],'CM5_GBE_TD0_P',pcbnew.F_Cu)
    path(b,[(117,109.525),(117,84),(99,84),(99,68),(101.55,64.06)],'CM5_GBE_TD0_N',pcbnew.B_Cu)
    path(b,[(118,110.475),(118,86),(102,86),(102,68),(104.09,64.06)],'CM5_GBE_TD0_P',pcbnew.B_Cu)

    # Local ground returns only; no shared signal-layer spine.
    for p in ((78.7,110),(118.7,110)):
        q=(p[0]-3,p[1]); path(b,[p,q],'ETH_GND',pcbnew.F_Cu); via(b,q,'ETH_GND')
    b.Save(str(ROOT/'ESDS304_ETHERNET_CLEAN_DISPOSABLE_FIXTURE.kicad_pcb'))
    print('saved')
if __name__ == '__main__': main()
