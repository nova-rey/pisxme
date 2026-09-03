"""Disposable TI ESDS311DYFR eight-line Ethernet ESD fixture."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent; W=.13208
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def XY(p): return (float(p[0])/1e6,float(p[1])/1e6)
def N(b,n): return b.FindNet(n) or b.FindNet('/ETHERNET/'+n)
def seg(b,a,z,n,l=pcbnew.F_Cu):
    t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(W));t.SetNet(N(b,n));b.Add(t)
def via(b,p,n):
    q=pcbnew.PCB_VIA(b);q.SetPosition(V(*p));q.SetWidth(pcbnew.FromMM(.5));q.SetDrill(pcbnew.FromMM(.3));q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);q.SetNet(N(b,n));b.Add(q)
def path(b,pts,n,l):
    for a,z in zip(pts,pts[1:]):seg(b,a,z,n,l)
def main():
    b=pcbnew.LoadBoard(str(ROOT/'SP3019_ETHERNET_FIXTURE_BASE.kicad_pcb'))
    if b.FindNet('/ETHERNET/ETH_GND') is None:b.Add(pcbnew.NETINFO_ITEM(b,'/ETHERNET/ETH_GND'))
    j7=b.FindFootprintByReference('J7');j7.SetPosition(V(100,160))
    j2=b.FindFootprintByReference('J2');j2.SetPosition(V(100,60));j2.SetOrientationDegrees(0)
    f=pcbnew.FootprintLoad(str(ROOT/'PiSXMe_RevA_Clean.pretty'),'ESDS311DYFR_SOD323')
    nets=['CM5_GBE_TD3_P','CM5_GBE_TD3_N','CM5_GBE_TD2_N','CM5_GBE_TD2_P','CM5_GBE_TD1_P','CM5_GBE_TD1_N','CM5_GBE_TD0_N','CM5_GBE_TD0_P']
    src={'CM5_GBE_TD3_P':(97.96,129.1),'CM5_GBE_TD3_N':(97.96,129.5),'CM5_GBE_TD2_N':(97.96,130.3),'CM5_GBE_TD2_P':(97.96,130.7),'CM5_GBE_TD1_P':(101.04,129.1),'CM5_GBE_TD1_N':(101.04,129.5),'CM5_GBE_TD0_N':(101.04,130.3),'CM5_GBE_TD0_P':(101.04,130.7)}
    dst={n:XY(next(p.GetPosition() for p in j2.Pads() if p.GetNetname()==n)) for n in nets}
    # Put the shunt parts immediately at the connector boundary, with each
    # line on a monotonic lane. Signal pad 1 is the line; pad 2 is GND.
    placements=[(n,(90+i*3,54 if i<4 else 66)) for i,n in enumerate(nets)]
    via_x={'CM5_GBE_TD3_P':94,'CM5_GBE_TD3_N':93,'CM5_GBE_TD2_N':92,'CM5_GBE_TD2_P':91,
           'CM5_GBE_TD1_P':106,'CM5_GBE_TD1_N':107,'CM5_GBE_TD0_N':108,'CM5_GBE_TD0_P':109}
    for i,(n,(x,y)) in enumerate(placements):
        fp=pcbnew.FOOTPRINT(f);fp.SetReference('D'+str(30+i));fp.SetValue('ESDS311DYFR');fp.SetPosition(V(x,y));b.Add(fp)
        fp.FindPadByNumber('1').SetNet(N(b,n));fp.FindPadByNumber('2').SetNet(N(b,'ETH_GND'))
        line=(x-1.1,y); gv=(x+1.1,y+2.0);via(b,gv,'ETH_GND');path(b,[line,gv],'ETH_GND',pcbnew.F_Cu)
        # Connector-side shunt branch, then a conservative source-to-launch
        # proof path. Full route acceptance remains native-DRC gated.
        path(b,[dst[n],line],n,pcbnew.F_Cu)
        sv=(via_x[n],src[n][1]); dv=(x-2.0,y); via(b,sv,n); via(b,dv,n)
        path(b,[line,dv],n,pcbnew.F_Cu)
        path(b,[src[n],sv,(x-2.0,y)],n,pcbnew.B_Cu)
    out=ROOT/'ESDS311_ETHERNET_DISPOSABLE_FIXTURE.kicad_pcb';b.Save(str(out));print(out)
if __name__=='__main__':main()
