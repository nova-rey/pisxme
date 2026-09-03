"""Disposable TI ESDS304DBVR Ethernet ESD candidate fixture."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def net(b,n):
    q=b.FindNet(n)
    if q is None and not n.startswith('/') : q=b.FindNet('/ETHERNET/'+n)
    if q is None: raise RuntimeError('missing net '+n)
    return q
def track(b,a,z,n,layer=pcbnew.F_Cu,w=.13208):
    t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(w)); t.SetNet(net(b,n)); b.Add(t)
def via(b,p,n):
    q=pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30))
    q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(net(b,n)); b.Add(q)
def main():
    b=pcbnew.LoadBoard(str(ROOT/'SP3019_ETHERNET_FIXTURE_BASE.kicad_pcb'))
    if b.FindNet('/ETHERNET/ETH_GND') is None: b.Add(pcbnew.NETINFO_ITEM(b,'/ETHERNET/ETH_GND'))
    j7=b.FindFootprintByReference('J7'); j7.SetPosition(V(100,160))
    j2=b.FindFootprintByReference('J2'); j2.SetPosition(V(100,80)); j2.SetOrientationDegrees(0)
    f=pcbnew.FootprintLoad(str(ROOT/'PiSXMe_RevA_Clean.pretty'),'ESDS304DBVR_SOT23_5')
    u9=pcbnew.FOOTPRINT(f); u6=pcbnew.FOOTPRINT(f)
    for ref,fp,x,names in [('U9',u9,90,('CM5_GBE_TD3_P','CM5_GBE_TD3_N','CM5_GBE_TD2_P','CM5_GBE_TD2_N')),
                            ('U6',u6,110,('CM5_GBE_TD1_P','CM5_GBE_TD1_N','CM5_GBE_TD0_P','CM5_GBE_TD0_N'))]:
        fp.SetReference(ref); fp.SetValue('ESDS304DBVR'); fp.SetPosition(V(x,130)); b.Add(fp)
        for p,n in zip(['1','3','4','5'],names): fp.FindPadByNumber(p).SetNet(net(b,n))
        fp.FindPadByNumber('2').SetNet(net(b,'ETH_GND'))
    # Source-to-ESD proof: each pair is kept together; alternate pairs use B.Cu
    # with ordinary transitions outside the SOT-23 pads.
    fpaths={'CM5_GBE_TD3_P':((97.96,129.10),(88.70,129.05),pcbnew.F_Cu),
            'CM5_GBE_TD3_N':((97.96,129.50),(88.70,130.95),pcbnew.F_Cu),
            'CM5_GBE_TD1_P':((101.04,129.10),(108.70,129.05),pcbnew.F_Cu),
            'CM5_GBE_TD1_N':((101.04,129.50),(108.70,130.95),pcbnew.F_Cu)}
    for n,(a,z,l) in fpaths.items(): track(b,a,z,n,l)
    bpaths={'CM5_GBE_TD2_P':((97.96,130.70),(91.30,130.475),(93.0,128.0)),
            'CM5_GBE_TD2_N':((97.96,130.30),(91.30,129.525),(94.0,132.0)),
            'CM5_GBE_TD0_P':((101.04,130.70),(111.30,130.475),(107.0,132.0)),
            'CM5_GBE_TD0_N':((101.04,130.30),(111.30,129.525),(106.0,128.0))}
    for n,(src,pad,vp) in bpaths.items():
        via(b,src,n); track(b,src,vp,n,pcbnew.B_Cu); via(b,vp,n); track(b,vp,pad,n,pcbnew.F_Cu)
    # Complete all eight ESD-to-MagJack paths on separated, conservative lanes.
    outs={'CM5_GBE_TD3_N':((88.70,130.95),(84.285,76.17)),
          'CM5_GBE_TD3_P':((88.70,129.05),(86.825,77.44)),
          'CM5_GBE_TD2_N':((94.0,132.0),(93.175,77.44)),
          'CM5_GBE_TD2_P':((93.0,128.0),(95.715,76.17)),
          'CM5_GBE_TD1_N':((108.70,130.95),(93.37,84.06)),
          'CM5_GBE_TD1_P':((108.70,129.05),(95.91,84.06)),
          'CM5_GBE_TD0_N':((106.0,128.0),(104.09,84.06)),
          'CM5_GBE_TD0_P':((107.0,132.0),(106.63,84.06))}
    for n,(a,z) in outs.items(): track(b,a,(a[0],75),n,pcbnew.B_Cu if 'TD2' in n or 'TD0' in n else pcbnew.F_Cu); track(b,(a[0],75),z,n,pcbnew.B_Cu if 'TD2' in n or 'TD0' in n else pcbnew.F_Cu)
    for p in [(88.70,130),(108.70,130)]: track(b,p,(p[0]-2.5,130),'ETH_GND'); via(b,(p[0]-2.5,130),'ETH_GND')
    track(b,(86.55,130),(106.55,140),'ETH_GND',pcbnew.B_Cu); track(b,(106.55,140),(106.55,130),'ETH_GND',pcbnew.B_Cu)
    out=ROOT/'ESDS304_ETHERNET_DISPOSABLE_FIXTURE.kicad_pcb'; b.Save(str(out)); print(out)
if __name__=='__main__': main()
