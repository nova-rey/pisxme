"""V1160: V1159 with exact RTL_3V3 source-branch pruning."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_XTAL_STAGGERED_V1159.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_XTAL_STAGGERED_V1160.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_3V3').GetNetCode()
def near(p):
    return (abs(p[0]-93.0)<.001 and abs(p[1]-66.8)<.001) or (abs(p[0]-94.05)<.001 and abs(p[1]-66.8)<.001) or (abs(p[0]-100.9)<.001 and abs(p[1]-68.4)<.001)
def ps(x):
    if type(x).__name__=='PCB_VIA': return [(x.GetX()/1e6,x.GetY()/1e6)]
    a=x.GetStart(); z=x.GetEnd(); return [(a.x/1e6,a.y/1e6),(z.x/1e6,z.y/1e6)]
old=[x for x in list(b.GetTracks()) if x.GetNetCode()==n and any(near(p) for p in ps(x))]
assert len(old)>=3,len(old)
for x in old: b.Remove(x)
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT,'removed RTL_3V3',len(old))
