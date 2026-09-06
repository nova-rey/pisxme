#!/usr/bin/env python3
"""Apply the previously validated native J1 protected-field geometry."""
from collections import defaultdict
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_POWER_INPUT_PLANES_PROBE.kicad_pcb'
OUT=R/'PHASE24_J1_PROTECTED_FIELD_CURRENT.kicad_pcb'
b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('12V_PROTECTED'); j=b.FindFootprintByReference('J1')
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(layer,a,z,w):
 t=pcbnew.PCB_TRACK(b); t.SetLayer(layer); t.SetNet(n); t.SetWidth(pcbnew.FromMM(w)); t.SetStart(V(*a)); t.SetEnd(V(*z)); b.Add(t)
cols=defaultdict(list)
for p in j.Pads():
 if p.GetNetCode()==n.GetNetCode(): cols[round(pcbnew.ToMM(p.GetPosition().x),6)].append(pcbnew.ToMM(p.GetPosition().y))
if len(cols)!=13 or any(len(v)!=10 for v in cols.values()): raise SystemExit(sorted((x,len(y)) for x,y in cols.items()))
for x,ys in sorted(cols.items()):
 lo,hi=min(ys),max(ys); add(pcbnew.F_Cu,(x,lo),(x,hi),.50); add(pcbnew.F_Cu,(x,hi),(x,98.0),.50)
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(x,98.0)); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
 add(pcbnew.B_Cu,(x,98.0),(x,98.5),.50)
xs=sorted(cols); add(pcbnew.B_Cu,(xs[0],98.5),(xs[-1],98.5),.50)
b.Save(str(OUT)); print(OUT)
