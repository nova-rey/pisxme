"""Transplant the official CM5IO MDI geometry onto PiSXMe local footprints."""
from pathlib import Path
import os
import pcbnew

ROOT = Path(__file__).resolve().parent
ORACLE = ROOT / "authority-inventory/cm5io-rev2/CM5IO.kicad_pcb"
PRETTY = ROOT / "PiSXMe_RevA_Clean.pretty"
DIRECT_SHIFT = 5.0 if os.environ.get("PISXME_DIRECT_J7") == "1" else 0.0
SUP_DX = float(os.environ.get("PISXME_SUPPORT_DX", "0"))
CT_TIES = os.environ.get("PISXME_CT_TIES") == "1"
OUT = ROOT / ("CM5IO_DIRECT_J7_ETHERNET_FIXTURE.kicad_pcb" if DIRECT_SHIFT else "CM5IO_PISXME_ETHERNET_TRANSPLANT_FIXTURE.kicad_pcb")

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def N(b, name):
    n = b.FindNet(name)
    if n is None: n = pcbnew.NETINFO_ITEM(b, name); b.Add(n)
    return n
def T(x, y):
    # 180-degree rigid transform aligning official Module1 Ethernet pads to
    # the PiSXMe J7 source at (30,100), while preserving all official vectors.
    return (225.5 + DIRECT_SHIFT - x, 203.5 - y)
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
def route(b, points, n, layer=pcbnew.F_Cu, shift=True):
    if DIRECT_SHIFT and shift:
        points=[(x+DIRECT_SHIFT,y) for x,y in points]
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
    j7=addfp(b,"PiSXMeRevAClean_Raspberry_Pi_5_Compute_Module","J7",30 + DIRECT_SHIFT,130,0)
    j2=addfp(b,"EDAC_A70_112_331N126","J2",72.5 + DIRECT_SHIFT,53,180)
    oj9=oracle.FindFootprintByReference("J9"); oc1=oracle.FindFootprintByReference("C1")
    j9=None
    ties=[]
    branch_caps=[]
    branch_res=[]
    cct=None
    if os.environ.get("PISXME_OMIT_SUPPORT") != "1" and not CT_TIES:
        j9=copyfp(b,oj9,"J9",*T(*xy(oj9.GetPosition())),0)
    if os.environ.get("PISXME_OMIT_SUPPORT") != "1" and CT_TIES:
        # EDAC's manufacturer circuit: four separate 22 nF/100 V plus 75 ohm
        # series branches from VC1..VC4 to a common termination node, then a
        # 1 nF/2 kV shield return. These are disposable support footprints.
        ct2_x = 62 if SUP_DX else 88
        for ref, x, netname in (("RCT4",52,"ETH_CT4"),("RCT3",57,"ETH_CT3"),
                                ("RCT2",ct2_x,"ETH_CT2"),("RCT1",67,"ETH_CT1")):
            cap=addfp(b,"C_0603_1608Metric",ref.replace("R","C") ,x + DIRECT_SHIFT + SUP_DX,45,0)
            res=addfp(b,"R_0402_1005Metric",ref,x + DIRECT_SHIFT + SUP_DX,40,0)
            cap.SetLayerAndFlip(pcbnew.B_Cu)
            res.SetLayerAndFlip(pcbnew.B_Cu)
            branch=f"ETH_CT_BRANCH_{netname[-1]}"
            names_for_branch=nets.get(branch) or N(b,branch); nets[branch]=names_for_branch
            assign(cap,{1:netname,2:branch},nets)
            assign(res,{1:branch,2:"ETH_CT_COMMON"},nets)
            branch_caps.append(cap); branch_res.append(res)
        cct=addfp(b,"C_0603_1608Metric","CCT",72 + DIRECT_SHIFT + SUP_DX,40,0)
        cct.SetLayerAndFlip(pcbnew.B_Cu)
        assign(cct,{1:"ETH_CT_COMMON",2:"GBE_SHIELD"},nets)
    # C1 is an official CM5IO-local support part, but the clean Ethernet
    # authority has no corresponding capacitor or common CT net.  Do not
    # invent that topology in this exact EDAC fixture.
    for g in list(j2.GraphicalItems()):
        if g.GetLayer() == pcbnew.F_SilkS: g.SetLayer(pcbnew.F_Fab)
    # Official 10-pin USON footprints and the CM5IO flow-through pin map.
    ou1=oracle.FindFootprintByReference("U1"); ou2=oracle.FindFootprintByReference("U2")
    # Official U1 carries TD3/TD2 and lands at the left position; production
    # U9 owns that pair group. Official U2 carries TD1/TD0 and lands at the
    # right position; production U6 owns that group. The 180-degree board
    # transform changes the physical escape side, so use 270 degrees with
    # the clean schematic's native pad mapping rather than swapping net
    # labels onto a 90-degree footprint.
    u1=copyfp(b,ou1,"U9",*T(*xy(ou1.GetPosition())),270)
    u2=copyfp(b,ou2,"U6",*T(*xy(ou2.GetPosition())),270)
    assign(j7,{3:"CM5_GBE_TD3_P",4:"CM5_GBE_TD1_P",5:"CM5_GBE_TD3_N",6:"CM5_GBE_TD1_N",9:"CM5_GBE_TD2_N",10:"CM5_GBE_TD0_N",11:"CM5_GBE_TD2_P",12:"CM5_GBE_TD0_P"},nets)
    assign(u1,{1:"CM5_GBE_TD2_P",2:"CM5_GBE_TD2_N",3:"ETH_GND",4:"CM5_GBE_TD3_N",5:"CM5_GBE_TD3_P",6:"CM5_GBE_TD3_P",7:"CM5_GBE_TD3_N",8:"ETH_GND",9:"CM5_GBE_TD2_N",10:"CM5_GBE_TD2_P"},nets)
    assign(u2,{1:"CM5_GBE_TD0_P",2:"CM5_GBE_TD0_N",3:"ETH_GND",4:"CM5_GBE_TD1_N",5:"CM5_GBE_TD1_P",6:"CM5_GBE_TD1_P",7:"CM5_GBE_TD1_N",8:"ETH_GND",9:"CM5_GBE_TD0_N",10:"CM5_GBE_TD0_P"},nets)
    # The production magnetics support is a common center-tap node. Keep the
    # four physical tap lands explicit in the footprint, but make their
    # fixture net authority the one common node so the support bus cannot
    # manufacture artificial crossings between equivalent taps.
    # EDAC pads 4 and 5 are NC.  Pads 11..14 are the four manufacturer
    # center-tap contacts and must retain the clean schematic's distinct
    # ETH_CT1..ETH_CT4 authority; the common support node is not a pad net.
    assign(j2,{1:"CM5_GBE_TD0_P",2:"CM5_GBE_TD0_N",3:"CM5_GBE_TD1_P",6:"CM5_GBE_TD1_N",7:"CM5_GBE_TD2_P",8:"CM5_GBE_TD2_N",9:"CM5_GBE_TD3_P",10:"CM5_GBE_TD3_N",11:"ETH_CT1",12:"ETH_CT2",13:"ETH_CT3",14:"ETH_CT4",15:"GBE_LED_Y_A",16:"GBE_LED_Y_K",17:"GBE_LED_G_A",18:"GBE_LED_G_K",19:"GBE_SHIELD",20:"GBE_SHIELD"},nets)
    if j9 is not None:
        # J9 is retained only as a disposable, individually-labelled CT
        # witness. Its ordering follows the physical escape experiment.
        assign(j9,{1:"ETH_CT4",2:"ETH_CT2",3:"ETH_CT3",4:"ETH_CT1"},nets)
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
        # Reuse the official local USON GND escape as geometry authority.
        # This is deliberately limited to the two ESD footprints' source
        # neighborhood; it does not import unrelated board copper.
        for tr in oracle.GetTracks():
            if tr.GetNetname() != "GND": continue
            a=xy(tr.GetStart()); z=xy(tr.GetEnd())
            if not all(145 <= p[0] <= 160 and 136 <= p[1] <= 142 for p in (a,z)): continue
            if a == z: continue
            item=pcbnew.PCB_TRACK(b); item.SetStart(V(*T(*a))); item.SetEnd(V(*T(*z)))
            item.SetLayer(tr.GetLayer()); item.SetWidth(tr.GetWidth()); item.SetNet(nets["ETH_GND"]); b.Add(item)
        gvia=[]
        for p in ((149.4,137.2),(151.6,137.8),(155.467559,137.292894),
                  (155.4,139.4),(149.4,139.4),(153.0,137.8)):
            vp=T(*p); gvia.append(vp)
            q=pcbnew.PCB_VIA(b); q.SetPosition(V(*vp)); q.SetWidth(pcbnew.FromMM(.45)); q.SetDrill(pcbnew.FromMM(.20)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(nets["ETH_GND"]); b.Add(q)
        # The clean EDAC authority exposes four distinct center-tap nets.
        # Route each to the disposable support header without a common-node
        # shortcut; all segments are ordinary B.Cu traces.
        # The two pairs of support traces occupy opposite permitted copper
        # layers.  This is a normal through-via-equivalent escape at the
        # through-hole parts, and avoids inventing a common CT bus.
        if CT_TIES:
            def actual(f, number):
                return xy(f.FindPadByNumber(str(number)).GetPosition())
            def via_actual(x,y,net):
                q=pcbnew.PCB_VIA(b); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.45)); q.SetDrill(pcbnew.FromMM(.20)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(net); b.Add(q)
            # Four pair-specific B.Cu escapes into the manufacturer RC
            # branches. The branch footprints are on B.Cu, so no via is
            # required at an SMT pad and the official F.Cu MDI graph remains
            # isolated from this low-speed support network.
            for i,(source,cap,res,srcpad) in enumerate(zip(
                    ("ETH_CT4","ETH_CT3","ETH_CT2","ETH_CT1"),
                    branch_caps,branch_res,(14,13,12,11))):
                a=actual(j2,srcpad); z=actual(cap,1)
                path=[a,(68.0,60.0),(58.0,60.0),z] if source == "ETH_CT4" else [a,z]
                if SUP_DX:
                    # When the low-speed RC island is moved away from the
                    # fuse, give the through-hole CT lands explicit staggered
                    # escapes before entering the remote support row.
                    escape = {"ETH_CT4": (68.0, 60.0),
                              "ETH_CT2": (84.0, 62.0),
                              "ETH_CT1": (88.0, 62.0)}.get(source)
                    if escape:
                        via_actual(*escape, nets[source])
                        route(b,[a,escape],nets[source],pcbnew.F_Cu,shift=False)
                        route(b,[escape,(escape[0],50.0),z],nets[source],pcbnew.B_Cu,shift=False)
                    else:
                        route(b,path,nets[source],pcbnew.B_Cu,shift=False)
                else:
                    route(b,path,nets[source],pcbnew.B_Cu,shift=False)
                ca=actual(cap,2); rb=actual(res,1)
                route(b,[ca,(ca[0],42+i*.5),(rb[0],42+i*.5),rb],nets[f"ETH_CT_BRANCH_{source[-1]}"],pcbnew.B_Cu,shift=False)
                rr=actual(res,2); route(b,[rr,(rr[0],37),(75,37)],nets["ETH_CT_COMMON"],pcbnew.B_Cu,shift=False)
            c1=actual(cct,1); route(b,[c1,(c1[0],37),(75,37)],nets["ETH_CT_COMMON"],pcbnew.B_Cu,shift=False)
            c2=actual(cct,2); sv=(c2[0]-.8,c2[1]+.8); via_actual(*sv,nets["GBE_SHIELD"])
            route(b,[c2,sv],nets["GBE_SHIELD"],pcbnew.B_Cu,shift=False)
            route(b,[sv,(96 + SUP_DX,36),(96 + SUP_DX,56.05),(96,56.05)],nets["GBE_SHIELD"],pcbnew.F_Cu,shift=False)
        else:
            route(b,[(66.785,56.83),(83.73,51.73)],nets["ETH_CT4"],pcbnew.F_Cu)
            route(b,[(75.675,55.56),(75.675,59.0),(82.5,59.0),(82.5,50.5),(86.27,50.5),(86.27,51.73)],nets["ETH_CT2"],pcbnew.F_Cu)
            route(b,[(69.325,55.56),(83.73,54.27)],nets["ETH_CT3"],pcbnew.B_Cu)
            route(b,[(78.215,56.83),(79.0,59.5),(84.0,59.5),(84.0,53.5),(86.27,53.5),(86.27,54.27)],nets["ETH_CT1"],pcbnew.F_Cu)
        # Shield return is kept as its declared GBE_SHIELD net until the
        # final schematic net-tie decision; both physical shield lands tie.
        s1=xy(j2.FindPadByNumber("19").GetPosition()); s2=xy(j2.FindPadByNumber("20").GetPosition())
        s1=(s1[0]-DIRECT_SHIFT,s1[1]); s2=(s2[0]-DIRECT_SHIFT,s2[1])
        route(b,[s1,(96,56.05),(96,38),(52,38),(52,56.05),s2],nets["GBE_SHIELD"],pcbnew.F_Cu)
        # The detached fixture's C1 return joins the copied GND escape with
        # ordinary through-via and B.Cu spine; no via is placed in a pad.
        q=pcbnew.PCB_VIA(b); q.SetPosition(V(98 + DIRECT_SHIFT,50)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(nets["ETH_GND"]); b.Add(q)
        route(b,[(98,50),(98,72),(70,72),(70.1,64.1)],nets["ETH_GND"],pcbnew.B_Cu)
        route(b,[(70.1,64.1),(70.0324,66.2071),(72.5,65.7),(73.9,65.7),(76.1,66.3),(76.1,64.1)],nets["ETH_GND"],pcbnew.B_Cu)
    outline(b,8,35,100,125)
    if os.environ.get("PISXME_OMIT_SUPPORT") != "1":
        pcbnew.ZONE_FILLER(b).Fill(b.Zones())
    b.Save(str(OUT)); print(f"{OUT} ({count} official MDI segments transplanted)")
if __name__=="__main__": main()
