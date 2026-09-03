"""Transplant the official CM5IO MDI geometry onto PiSXMe local footprints."""
from pathlib import Path
import os
import pcbnew

ROOT = Path(__file__).resolve().parent
ORACLE = ROOT / "authority-inventory/cm5io-rev2/CM5IO.kicad_pcb"
PRETTY = ROOT / "PiSXMe_RevA_Clean.pretty"
OUT = ROOT / "CM5IO_PISXME_ETHERNET_TRANSPLANT_FIXTURE.kicad_pcb"

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def N(b, name):
    n = b.FindNet(name)
    if n is None: n = pcbnew.NETINFO_ITEM(b, name); b.Add(n)
    return n
def T(x, y):
    # 180-degree rigid transform aligning official Module1 Ethernet pads to
    # the PiSXMe J7 source at (30,100), while preserving all official vectors.
    return (225.5 - x, 203.5 - y)
def addfp(b, name, ref, x, y, rot=0):
    f = pcbnew.PCB_IO_KICAD_SEXPR().FootprintLoad(str(PRETTY), name)
    if f is None: raise RuntimeError(name)
    f.SetReference(ref); f.SetPosition(V(x,y)); f.SetOrientationDegrees(rot); b.Add(f); return f
def copyfp(b, src, ref, x, y, rot):
    f = pcbnew.FOOTPRINT(src); f.SetReference(ref); f.SetPosition(V(x,y)); f.SetOrientationDegrees(rot); b.Add(f); return f
def assign(f, mapping, nets):
    for number, name in mapping.items():
        p=f.FindPadByNumber(str(number))
        if p is None: raise RuntimeError(f"{f.GetReference()}.{number}")
        p.SetNet(nets[name])
def route(b, points, n, layer=pcbnew.F_Cu):
    for a,z in zip(points,points[1:]):
        item=pcbnew.PCB_TRACK(b); item.SetStart(V(*a)); item.SetEnd(V(*z)); item.SetLayer(layer); item.SetWidth(pcbnew.FromMM(.30) if layer != pcbnew.F_Cu else pcbnew.FromMM(.127)); item.SetNet(n); b.Add(item)
def xy(p): return (pcbnew.ToMM(p.x), pcbnew.ToMM(p.y))

def rectangle_zone(board, net, layer, x0, y0, x1, y1, name):
    z = pcbnew.ZONE(board); z.SetLayer(layer); z.SetNet(net)
    z.SetNetCode(net.GetNetCode()); z.SetIsRuleArea(False)
    z.SetMinThickness(pcbnew.FromMM(0.20)); z.SetPadConnection(pcbnew.ZONE_CONNECTION_FULL)
    z.SetZoneName(name)
    pts = pcbnew.VECTOR_VECTOR2I()
    for p in ((x0,y0),(x1,y0),(x1,y1),(x0,y1)): pts.append(V(*p))
    z.AddPolygon(pts); board.Add(z)

def outline(board, x0, y0, x1, y1):
    for a, z in (((x0,y0),(x1,y0)), ((x1,y0),(x1,y1)),
                 ((x1,y1),(x0,y1)), ((x0,y1),(x0,y0))):
        s = pcbnew.PCB_SHAPE(board); s.SetShape(pcbnew.SHAPE_T_SEGMENT)
        s.SetLayer(pcbnew.Edge_Cuts); s.SetStart(V(*a)); s.SetEnd(V(*z))
        s.SetWidth(pcbnew.FromMM(0.05)); board.Add(s)

def main():
    oracle=pcbnew.LoadBoard(str(ORACLE)); b=pcbnew.NewBoard(""); b.SetCopperLayerCount(6)
    for layer,name in ((pcbnew.F_Cu,"F.Cu"),(pcbnew.In1_Cu,"In1.GND"),(pcbnew.In2_Cu,"In2.PWR"),(pcbnew.In3_Cu,"In3.PROTECTED_12V"),(pcbnew.In4_Cu,"In4.GND"),(pcbnew.B_Cu,"B.Cu")): b.SetLayerName(layer,name)
    names=("CM5_GBE_TD0_P","CM5_GBE_TD0_N","CM5_GBE_TD1_P","CM5_GBE_TD1_N","CM5_GBE_TD2_P","CM5_GBE_TD2_N","CM5_GBE_TD3_P","CM5_GBE_TD3_N","ETH_GND","ETH_POWER","GBE_SHIELD","ETH_CT_COMMON","ETH_CT1","ETH_CT2","ETH_CT3","ETH_CT4","GBE_LED_Y_A","GBE_LED_Y_K","GBE_LED_G_A","GBE_LED_G_K")
    nets={n:N(b,n) for n in names}
    # The local CM5 footprint origin is 30 mm below the Ethernet contact row;
    # this places its physical contacts at the transformed oracle coordinates.
    j7=addfp(b,"PiSXMeRevAClean_Raspberry_Pi_5_Compute_Module","J7",30,130,0)
    j2=addfp(b,"EDAC_A70_112_331N126","J2",72.5,53,180)
    oj9=oracle.FindFootprintByReference("J9"); oc1=oracle.FindFootprintByReference("C1")
    j9=copyfp(b,oj9,"J9",*T(*xy(oj9.GetPosition())),0)
    c1=copyfp(b,oc1,"C1",92,48,0)
    # Official 10-pin USON footprints and the CM5IO flow-through pin map.
    ou1=oracle.FindFootprintByReference("U1"); ou2=oracle.FindFootprintByReference("U2")
    u1=copyfp(b,ou1,"U6",*T(*xy(ou1.GetPosition())),90)
    u2=copyfp(b,ou2,"U9",*T(*xy(ou2.GetPosition())),90)
    assign(j7,{3:"CM5_GBE_TD3_P",4:"CM5_GBE_TD1_P",5:"CM5_GBE_TD3_N",6:"CM5_GBE_TD1_N",9:"CM5_GBE_TD2_N",10:"CM5_GBE_TD0_N",11:"CM5_GBE_TD2_P",12:"CM5_GBE_TD0_P"},nets)
    assign(u1,{1:"CM5_GBE_TD3_P",2:"CM5_GBE_TD3_N",3:"ETH_GND",4:"CM5_GBE_TD2_N",5:"CM5_GBE_TD2_P",6:"CM5_GBE_TD2_P",7:"CM5_GBE_TD2_N",8:"ETH_GND",9:"CM5_GBE_TD3_N",10:"CM5_GBE_TD3_P"},nets)
    assign(u2,{1:"CM5_GBE_TD1_P",2:"CM5_GBE_TD1_N",3:"ETH_GND",4:"CM5_GBE_TD0_N",5:"CM5_GBE_TD0_P",6:"CM5_GBE_TD0_P",7:"CM5_GBE_TD0_N",8:"ETH_GND",9:"CM5_GBE_TD1_N",10:"CM5_GBE_TD1_P"},nets)
    # The production magnetics support is a common center-tap node. Keep the
    # four physical tap lands explicit in the footprint, but make their
    # fixture net authority the one common node so the support bus cannot
    # manufacture artificial crossings between equivalent taps.
    assign(j2,{1:"CM5_GBE_TD0_P",2:"CM5_GBE_TD0_N",3:"CM5_GBE_TD1_P",4:"ETH_CT_COMMON",5:"ETH_CT_COMMON",6:"CM5_GBE_TD1_N",7:"CM5_GBE_TD2_P",8:"CM5_GBE_TD2_N",9:"CM5_GBE_TD3_P",10:"CM5_GBE_TD3_N",11:"ETH_CT_COMMON",12:"ETH_CT_COMMON",13:"ETH_CT_COMMON",14:"ETH_CT_COMMON",15:"GBE_LED_Y_A",16:"GBE_LED_Y_K",17:"GBE_LED_G_A",18:"GBE_LED_G_K",19:"GBE_SHIELD",20:"GBE_SHIELD"},nets)
    assign(j9,{1:"ETH_CT_COMMON",2:"ETH_CT_COMMON",3:"ETH_CT_COMMON",4:"ETH_CT_COMMON"},nets)
    assign(c1,{1:"ETH_CT_COMMON",2:"ETH_GND"},nets)
    # Copy only official TRD0..TRD3 tracks. Their endpoints align with the
    # transformed J7/U6/U9/J2 pads exactly; no synthetic route is introduced.
    mapping={f"TRD{i}_{p}":f"CM5_GBE_TD{i}_{p}" for i in range(4) for p in "PN"}
    count=0
    for tr in oracle.GetTracks():
        name=tr.GetNetname()
        short=name.rsplit("/",1)[-1]
        if short not in mapping: continue
        a=xy(tr.GetStart()); z=xy(tr.GetEnd()); aa=T(*a); zz=T(*z)
        item=pcbnew.PCB_TRACK(b); item.SetStart(V(*aa)); item.SetEnd(V(*zz)); item.SetLayer(tr.GetLayer()); item.SetWidth(tr.GetWidth()); item.SetNet(nets[mapping[short]]); b.Add(item); count+=1
    if os.environ.get("PISXME_OMIT_SUPPORT") != "1":
        # The CM5IO support is a common center-tap island. A dedicated In2
        # copper island connects all EDAC/J9 through-hole lands and the
        # relocated C1 pad through normal plated-hole access without routing
        # a support trace through the F.Cu MDI corridor.
        # Same-net B.Cu fanout around the EDAC hole field. Keeping these
        # segments explicit avoids a detached-zone fill across NPTH holes.
        ct = nets["ETH_CT_COMMON"]
        route(b,[(66.785,56.83),(69.325,55.56),(75.675,55.56),(78.215,56.83)],ct,pcbnew.B_Cu)
        route(b,[(78.215,56.83),(82.0,54.0),(83.73,54.27)],ct,pcbnew.B_Cu)
        route(b,[(75.675,55.56),(82.0,52.0),(86.27,51.73)],ct,pcbnew.B_Cu)
        route(b,[(69.325,55.56),(82.0,50.0),(86.27,51.73)],ct,pcbnew.B_Cu)
        route(b,[(66.785,56.83),(82.0,48.5),(83.73,51.73)],ct,pcbnew.B_Cu)
        route(b,[(83.73,51.73),(86.27,51.73),(86.27,54.27),(83.73,54.27)],ct,pcbnew.B_Cu)
        c1p=xy(c1.FindPadByNumber("1").GetPosition())
        route(b,[c1p,(94,48),(94,46),(88,46),(86.27,51.73)],ct,pcbnew.B_Cu)
        # Shield return is kept as its declared GBE_SHIELD net until the
        # final schematic net-tie decision; both physical shield lands tie.
        s1=xy(j2.FindPadByNumber("19").GetPosition()); s2=xy(j2.FindPadByNumber("20").GetPosition())
        route(b,[s1,(96,56.05),(96,38),(52,38),(52,56.05),s2],nets["GBE_SHIELD"],pcbnew.B_Cu)
        # ESD grounds are landed directly into the local F.Cu GND copper;
        # In1/B.Cu pours provide the reference/return planes without
        # introducing dogbones across the MDI pad fields.
        # Compact pours terminate at ordinary return vias; they do not cover
        # the EDAC NPTH field or board edge.
        rectangle_zone(b,nets["ETH_GND"],pcbnew.F_Cu,68,63,72,68,"ETH_GND_U6_F_Cu")
        rectangle_zone(b,nets["ETH_GND"],pcbnew.F_Cu,74,63,78,68,"ETH_GND_U9_F_Cu")
        rectangle_zone(b,nets["ETH_GND"],pcbnew.F_Cu,90,46,95,50,"ETH_GND_C1_F_Cu")
        rectangle_zone(b,nets["ETH_GND"],pcbnew.In1_Cu,68,63,78,68,"ETH_GND_In1")
        for vp in ((68,68),(78,68),(95,50)):
            q=pcbnew.PCB_VIA(b); q.SetPosition(V(*vp)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(nets["ETH_GND"]); b.Add(q)
        route(b,[(68,68),(68,74),(78,74),(78,68)],nets["ETH_GND"],pcbnew.B_Cu)
        route(b,[(78,74),(95,74),(95,50)],nets["ETH_GND"],pcbnew.B_Cu)
    outline(b,8,35,100,125)
    if os.environ.get("PISXME_OMIT_SUPPORT") != "1":
        pcbnew.ZONE_FILLER(b).Fill(b.Zones())
    b.Save(str(OUT)); print(f"{OUT} ({count} official MDI segments transplanted)")
if __name__=="__main__": main()
