#!/usr/bin/env python3
"""V2: route isolated lane-0 fixture around M.2 mounting hole M1."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
BASE=ROOT/'PHASE24_PATHA_M2_LANE0_LAUNCH_ISOLATED_V1.kicad_pcb'
OUT=ROOT/'PHASE24_PATHA_M2_LANE0_LAUNCH_ISOLATED_V2.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): q=p.GetPosition(); return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def tr(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def path(b,n,pts,l):
 for a,z in zip(pts,pts[1:]):tr(b,n,a,z,l)
def via(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.6));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(BASE)); U=b.FindFootprintByReference('U13'); J=b.FindFootprintByReference('J3')
 nets={
  'TXP':('M2_SATA_A_P_PCIE_TXP0','2','49',(176,146.5),[(190,132),(218.5,132),(218.5,151)]),
  'TXN':('M2_SATA_A_N_PCIE_TXN0','3','47',(176,147.6),[(192,136),(217,136),(217,151)]),
  'RXN':('M2_SATA_B_P_PCIE_RXN0','6','41',(176,148.8),[(205,164),(205,154),(214,154)]),
  'RXP':('M2_SATA_B_N_PCIE_RXP0','7','43',(176,149.8),[(206.5,166),(206.5,154),(215.5,154)]),
 }
 for name,up,jp,sv,bc in nets.values():
  n=b.FindNet(name)
  for item in list(b.GetTracks()):
   if item.GetNetname()==name:b.RemoveNative(item)
  src=xy(U.FindPadByNumber(up));dst=xy(J.FindPadByNumber(jp))
  path(b,n,[src,(177.2,src[1]),sv],F);via(b,n,sv);path(b,n,[sv]+bc,B);via(b,n,bc[-1]);path(b,n,[bc[-1],dst],F)
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
