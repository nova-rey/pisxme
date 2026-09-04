"""Disposable Phase-17 top-edge Ethernet island with regenerated copper."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "ACREAGE_PHASE17_F1RIGHT40_ETH_GROUND_FIXED.kicad_pcb"
OUT = ROOT / "ACREAGE_PHASE17_TOP_EDGE_REGENERATED.kicad_pcb"
W = pcbnew.FromMM(.13208)

def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.x), pcbnew.ToMM(p.y)
def N(b,n):
    q=b.FindNet(n) or b.FindNet("/ETHERNET/"+n) or b.FindNet("/"+n)
    if q is None: raise RuntimeError(n)
    return q
def P(b,ref,num):
    f=b.FindFootprintByReference(ref); p=f.FindPadByNumber(str(num))
    if p is None: raise RuntimeError(f"{ref}.{num}")
    return xy(p.GetPosition())
def move(b,ref,pos,angle):
    f=b.FindFootprintByReference(ref); f.SetPosition(V(*pos)); f.SetOrientationDegrees(angle)
def T(b,n,a,z,layer=pcbnew.F_Cu):
    q=pcbnew.PCB_TRACK(b); q.SetStart(V(*a)); q.SetEnd(V(*z)); q.SetLayer(layer); q.SetWidth(W); q.SetNet(n); b.Add(q)
def R(b,n,pts,layer=pcbnew.F_Cu):
    for a,z in zip(pts,pts[1:]): T(b,n,a,z,layer)
def via(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)

b=pcbnew.LoadBoard(str(BASE))
# Stagger the two authoritative ESD packages beside the fixed J7 launch and
# put the tall connector on the open top edge. Support remains local to J2.
move(b,"U9",(24,97),180); move(b,"U6",(28,103),180); move(b,"J2",(150,12.5),180)
for ref,pos in (("CCT",(150,28)),("CCT1",(140,25)),("CCT2",(160,25)),
                ("CCT3",(140,35)),("CCT4",(160,35)),("RCT1",(140,30)),
                ("RCT2",(160,30)),("RCT3",(140,40)),("RCT4",(160,40))): move(b,ref,pos,180)

# Capture every endpoint before removing copper; KiCad 10 can invalidate
# footprint proxies while board tracks are removed.
src={"CM5_GBE_TD3_P":P(b,"J7",3),"CM5_GBE_TD3_N":P(b,"J7",5),
     "CM5_GBE_TD2_N":P(b,"J7",9),"CM5_GBE_TD2_P":P(b,"J7",11),
     "CM5_GBE_TD1_P":P(b,"J7",4),"CM5_GBE_TD1_N":P(b,"J7",6),
     "CM5_GBE_TD0_N":P(b,"J7",10),"CM5_GBE_TD0_P":P(b,"J7",12)}
esd={"CM5_GBE_TD3_P":P(b,"U9",5),"CM5_GBE_TD3_N":P(b,"U9",4),
     "CM5_GBE_TD2_P":P(b,"U9",1),"CM5_GBE_TD2_N":P(b,"U9",2),
     "CM5_GBE_TD1_P":P(b,"U6",5),"CM5_GBE_TD1_N":P(b,"U6",4),
     "CM5_GBE_TD0_P":P(b,"U6",1),"CM5_GBE_TD0_N":P(b,"U6",2)}
dst={n:P(b,"J2",num) for n,num in (("CM5_GBE_TD0_P",1),("CM5_GBE_TD0_N",2),
 ("CM5_GBE_TD1_P",3),("CM5_GBE_TD1_N",6),("CM5_GBE_TD2_P",7),
 ("CM5_GBE_TD2_N",8),("CM5_GBE_TD3_P",9),("CM5_GBE_TD3_N",10))}
j2aux={str(num):P(b,"J2",num) for num in (11,12,13,14,19,20)}
support={("CCT",str(num)):P(b,"CCT",num) for num in (1,2)}
for i in range(1,5):
    support[(f"CCT{i}","1")]=P(b,f"CCT{i}",1)
    support[(f"CCT{i}","2")]=P(b,f"CCT{i}",2)
    support[(f"RCT{i}","1")]=P(b,f"RCT{i}",1)
    support[(f"RCT{i}","2")]=P(b,f"RCT{i}",2)
for item in list(b.GetTracks()):
    if item.GetNetname().split("/")[-1].startswith(("CM5_GBE_TD","ETH_","GBE_")): b.Remove(item)

# Local J7 escape: TD3/TD1 on F.Cu; interleaved TD2/TD0 on B.Cu with
# ordinary transitions away from both the J7 and ESD pads.
fpaths={
 "CM5_GBE_TD3_P":[src["CM5_GBE_TD3_P"],(30,98),(27,98),esd["CM5_GBE_TD3_P"]],
 "CM5_GBE_TD3_N":[src["CM5_GBE_TD3_N"],(29,99),(26,99),esd["CM5_GBE_TD3_N"]],
 "CM5_GBE_TD1_P":[src["CM5_GBE_TD1_P"],(40,102),(34,102),esd["CM5_GBE_TD1_P"]],
 "CM5_GBE_TD1_N":[src["CM5_GBE_TD1_N"],(41,103),(35,103),esd["CM5_GBE_TD1_N"]]}
for n,pts in fpaths.items(): R(b,N(b,n),pts)
bpaths={
 "CM5_GBE_TD2_N":[src["CM5_GBE_TD2_N"],(22,100.3),(22,92),(24,90),esd["CM5_GBE_TD2_N"]],
 "CM5_GBE_TD2_P":[src["CM5_GBE_TD2_P"],(21,100.7),(21,91),(23,90),esd["CM5_GBE_TD2_P"]],
 "CM5_GBE_TD0_N":[src["CM5_GBE_TD0_N"],(44,100.3),(44,94),(30,94),esd["CM5_GBE_TD0_N"]],
 "CM5_GBE_TD0_P":[src["CM5_GBE_TD0_P"],(45,100.7),(45,95),(31,95),esd["CM5_GBE_TD0_P"]]}
for n,pts in bpaths.items():
    q=N(b,n); via(b,q,pts[1]); R(b,q,[pts[1]]+pts[2:],pcbnew.B_Cu); via(b,q,pts[-1]); T(b,q,pts[-1],esd[n])

# Connector-side pair corridors rise to the top edge in monotonic pair order.
for n in ("CM5_GBE_TD3_P","CM5_GBE_TD3_N","CM5_GBE_TD1_P","CM5_GBE_TD1_N"):
    R(b,N(b,n),[esd[n],(esd[n][0],70),(70,70),(70,45),dst[n]],pcbnew.F_Cu)
for n in ("CM5_GBE_TD2_P","CM5_GBE_TD2_N","CM5_GBE_TD0_P","CM5_GBE_TD0_N"):
    q=N(b,n); v=(esd[n][0]+(2 if esd[n][0]<30 else -2),70); via(b,q,v)
    R(b,q,[esd[n],v,(90,70),(90,45),dst[n]],pcbnew.B_Cu); via(b,q,(90,45)); T(b,q,(90,45),dst[n])

# Rebuild complete CT/termination/shield support around the relocated J2.
for i in range(1,5):
    q=N(b,f"ETH_CT{i}"); R(b,q,[j2aux[str(10+i)],(130+i*5,18),(130+i*5,25),support[(f"CCT{i}","1")]])
    q=N(b,f"ETH_CT_BRANCH_{i}"); R(b,q,[support[(f"CCT{i}","2")],(130+i*5,30),support[(f"RCT{i}","1")]])
    q=N(b,"ETH_CT_COMMON"); R(b,q,[support[(f"RCT{i}","2")],(150,32),support[("CCT","1")]])
q=N(b,"GBE_SHIELD"); R(b,q,[j2aux["19"],(175,18),support[("CCT","2")]]); via(b,q,(175,18));
R(b,q,[j2aux["20"],(125,18),support[("CCT","2")]])
pcbnew.ZONE_FILLER(b).Fill(b.Zones()); pcbnew.SaveBoard(str(OUT),b)
print(f"saved {OUT}; regenerated MDI and CT/shield topology")
