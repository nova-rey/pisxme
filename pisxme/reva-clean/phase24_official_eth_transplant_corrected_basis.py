"""Transplant the official CM5IO MDI route onto a clean acreage copy.

This is a disposable routing oracle: the official fixture supplies geometry,
while the corrected acreage board supplies the real neighboring obstacles and
native net identities. No expected graph or synthetic edge is added.
"""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'PHASE24_CORRECTED_MACRO_PLACEMENT.kicad_pcb'
ORACLE=ROOT/'CM5IO_DIRECT_J7_ETHERNET_FIXTURE.kicad_pcb'
OUT=ROOT/'PHASE24_OFFICIAL_ETH_TRANSPLANT_CORRECTED_BASIS.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
b=pcbnew.LoadBoard(str(BASE));o=pcbnew.LoadBoard(str(ORACLE))
for ref in ('J2','U6','U9'):
    src=o.FindFootprintByReference(ref); dst=b.FindFootprintByReference(ref)
    dst.SetPosition(src.GetPosition());dst.SetOrientationDegrees(src.GetOrientationDegrees())
for item in list(b.GetTracks()):
    if 'CM5_GBE_' in item.GetNetname(): b.Remove(item)
count=0
for item in o.GetTracks():
    short=item.GetNetname().rsplit('/',1)[-1]
    if not short.startswith('CM5_GBE_TD'): continue
    net=b.FindNet(short)
    if net is None: raise RuntimeError(short)
    if isinstance(item,pcbnew.PCB_VIA):
        x,y=xy(item.GetPosition());v=pcbnew.PCB_VIA(b);v.SetPosition(V(x,y));v.SetWidth(item.GetWidth());v.SetDrill(item.GetDrill());v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(net);b.Add(v)
    else:
        t=pcbnew.PCB_TRACK(b);t.SetStart(V(*xy(item.GetStart())));t.SetEnd(V(*xy(item.GetEnd())));t.SetLayer(item.GetLayer());t.SetWidth(max(item.GetWidth(), pcbnew.FromMM(0.13208)));t.SetNet(net);b.Add(t)
    count+=1
b.BuildListOfNets();b.Save(str(OUT));print(OUT,'items',count)
