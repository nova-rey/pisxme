"""Disposable B.Cu chain for the separated bridge-3V3 capacitor field."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_BRIDGE_1V1_R19_JOIN.kicad_pcb'; OUT=R/'PHASE24_BRIDGE_3V3_CAP_CHAIN_V2.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('/REGULATORS/BRIDGE_3V3')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def tr(layer,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetLayer(layer);t.SetNet(n);t.SetWidth(pcbnew.FromMM(.20));t.SetStart(V(*a));t.SetEnd(V(*z));b.Add(t)
def via(x,y):
    q=pcbnew.PCB_VIA(b);q.SetPosition(V(x,y));q.SetWidth(pcbnew.FromMM(.50));q.SetDrill(pcbnew.FromMM(.30));q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);q.SetNet(n);b.Add(q)
centers=[]
for ref in ['C16','C17','C19']:
    p=next(p for p in b.FindFootprintByReference(ref).Pads() if p.GetNumber()=='1');q=p.GetPosition();x=q.x/1e6;y=q.y/1e6;c=(x-1.45,y);centers.append(c);tr(pcbnew.F_Cu,(x,y),c);via(*c)
for a,z in zip(centers,centers[1:]): tr(pcbnew.B_Cu,a,z)
pcbnew.ZONE_FILLER(b).Fill(b.Zones());b.Save(str(OUT));print(OUT)
