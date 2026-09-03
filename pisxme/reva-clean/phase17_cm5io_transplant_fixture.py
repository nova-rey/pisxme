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
    c1=copyfp(b,oc1,"C1",*T(*xy(oc1.GetPosition())),270)
    # Official 10-pin USON footprints and the CM5IO flow-through pin map.
    ou1=oracle.FindFootprintByReference("U1"); ou2=oracle.FindFootprintByReference("U2")
    u1=copyfp(b,ou1,"U6",*T(*xy(ou1.GetPosition())),90)
    u2=copyfp(b,ou2,"U9",*T(*xy(ou2.GetPosition())),90)
    assign(j7,{3:"CM5_GBE_TD3_P",4:"CM5_GBE_TD1_P",5:"CM5_GBE_TD3_N",6:"CM5_GBE_TD1_N",9:"CM5_GBE_TD2_N",10:"CM5_GBE_TD0_N",11:"CM5_GBE_TD2_P",12:"CM5_GBE_TD0_P"},nets)
    assign(u1,{1:"CM5_GBE_TD3_P",2:"CM5_GBE_TD3_N",3:"ETH_GND",4:"CM5_GBE_TD2_N",5:"CM5_GBE_TD2_P",6:"CM5_GBE_TD2_P",7:"CM5_GBE_TD2_N",8:"ETH_GND",9:"CM5_GBE_TD3_N",10:"CM5_GBE_TD3_P"},nets)
    assign(u2,{1:"CM5_GBE_TD1_P",2:"CM5_GBE_TD1_N",3:"ETH_GND",4:"CM5_GBE_TD0_N",5:"CM5_GBE_TD0_P",6:"CM5_GBE_TD0_P",7:"CM5_GBE_TD0_N",8:"ETH_GND",9:"CM5_GBE_TD1_N",10:"CM5_GBE_TD1_P"},nets)
    assign(j2,{1:"CM5_GBE_TD0_P",2:"CM5_GBE_TD0_N",3:"CM5_GBE_TD1_P",4:"ETH_CT_COMMON",5:"ETH_CT_COMMON",6:"CM5_GBE_TD1_N",7:"CM5_GBE_TD2_P",8:"CM5_GBE_TD2_N",9:"CM5_GBE_TD3_P",10:"CM5_GBE_TD3_N",11:"ETH_CT1",12:"ETH_CT2",13:"ETH_CT3",14:"ETH_CT4",15:"GBE_LED_Y_A",16:"GBE_LED_Y_K",17:"GBE_LED_G_A",18:"GBE_LED_G_K",19:"GBE_SHIELD",20:"GBE_SHIELD"},nets)
    assign(j9,{1:"ETH_CT2",2:"ETH_CT3",3:"ETH_CT1",4:"ETH_CT4"},nets)
    assign(c1,{1:"ETH_CT_COMMON",2:"ETH_GND"},nets)
    # Copy only official TRD0..TRD3 tracks. Their endpoints align with the
    # transformed J7/U6/U9/J2 pads exactly; no synthetic route is introduced.
    mapping={f"TRD{i}_{p}":f"CM5_GBE_TD{i}_{p}" for i in range(4) for p in "PN"}
    mapping.update({"TR0_TAP":"ETH_CT1","TR1_TAP":"ETH_CT2","TR2_TAP":"ETH_CT3","TR3_TAP":"ETH_CT4","Net-(C1-Pad1)":"ETH_CT_COMMON"})
    count=0
    for tr in oracle.GetTracks():
        name=tr.GetNetname()
        short=name.rsplit("/",1)[-1]
        if short not in mapping: continue
        a=xy(tr.GetStart()); z=xy(tr.GetEnd()); aa=T(*a); zz=T(*z)
        item=pcbnew.PCB_TRACK(b); item.SetStart(V(*aa)); item.SetEnd(V(*zz)); item.SetLayer(tr.GetLayer()); item.SetWidth(tr.GetWidth()); item.SetNet(nets[mapping[short]]); b.Add(item); count+=1
    if os.environ.get("PISXME_OMIT_SUPPORT") != "1":
        # Complete the EDAC-side support on B.Cu, away from the F.Cu MDI
        # geometry. CT1/CT2 use separate outside lanes so their staggered
        # connector pads do not cross.
        route(b,[xy(j2.FindPadByNumber("4").GetPosition()),(90,59.35),(90,56.83),xy(j2.FindPadByNumber("11").GetPosition())],nets["ETH_CT1"],pcbnew.B_Cu)
        route(b,[xy(j2.FindPadByNumber("5").GetPosition()),(60,61.89),(60,55.56),xy(j2.FindPadByNumber("12").GetPosition())],nets["ETH_CT2"],pcbnew.B_Cu)
        # Shield return is kept as its declared GBE_SHIELD net until the
        # final schematic net-tie decision; both physical shield lands tie.
        s1=xy(j2.FindPadByNumber("19").GetPosition()); s2=xy(j2.FindPadByNumber("20").GetPosition())
        route(b,[s1,(90,56.05),(90,38),(60,38),(60,56.05),s2],nets["GBE_SHIELD"],pcbnew.B_Cu)
        # ESD grounds transition to ordinary vias outside the USON pads.
        def addvia(point,n):
            q=pcbnew.PCB_VIA(b); q.SetPosition(V(*point)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)
        gv=((67,63.5),(67,66.5),(79,63.5),(79,66.5))
        for f,nums,vs in ((u1,(8,3),gv[:2]),(u2,(8,3),gv[2:])):
            for number,vp in zip(nums,vs):
                p=xy(f.FindPadByNumber(str(number)).GetPosition()); route(b,[p,vp],nets["ETH_GND"]); addvia(vp,nets["ETH_GND"])
        c1g=xy(c1.FindPadByNumber("2").GetPosition()); cv=(73.2,68.0)
        route(b,[c1g,cv],nets["ETH_GND"]); addvia(cv,nets["ETH_GND"])
        route(b,[gv[0],(67,82),(79,82),gv[2]],nets["ETH_GND"],pcbnew.B_Cu)
        route(b,[gv[1],(67,82),(79,82),gv[3]],nets["ETH_GND"],pcbnew.B_Cu)
        route(b,[cv,(73.2,82)],nets["ETH_GND"],pcbnew.B_Cu)
    b.Save(str(OUT)); print(f"{OUT} ({count} official MDI segments transplanted)")
if __name__=="__main__": main()
