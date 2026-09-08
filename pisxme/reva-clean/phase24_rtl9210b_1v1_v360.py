"""V360: 1V1-first co-allocation probe; neighboring support copper is disposable."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent; BASE=H/'PHASE24_RTL9210B_RTL3V3_ROUTE_V342.kicad_pcb'; OUT=H/'PHASE24_RTL9210B_RTL1V1_COALLOCATE_V360.kicad_pcb'
F,B,L=pcbnew.F_Cu,pcbnew.B_Cu,pcbnew.In2_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def s(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b); t.SetStart(P(*a)); t.SetEnd(P(*z)); t.SetLayer(l); t.SetWidth(W); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
def v(b,n,q):
 x=pcbnew.PCB_VIA(b); x.SetPosition(P(*q)); x.SetWidth(pcbnew.FromMM(.60)); x.SetDrill(pcbnew.FromMM(.30)); x.SetLayerPair(F,B); x.SetNet(n); x.SetNetCode(n.GetNetCode()); b.Add(x)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('RTL_1V1')
 for x in list(b.GetTracks()):
  if x.GetNetname() in ('RTL_3V3','RSET','XTAL_IN','XTAL_OUT'): b.RemoveNative(x)
 esc=[((103.2,58.05),(103.2,56.8)),((102.05,61.6),(100.8,61.6)),((103.2,65.95),(103.2,67.2)),((104.8,65.95),(104.8,67.2)),((108.8,65.95),(108.8,67.2)),((109.95,64),(111.2,64)),((109.95,62),(111.2,62)),((109.95,60.8),(111.2,60.8)),((113.2,53),(113.2,51.5))]
 for a,z in esc: s(b,n,F,a,z); v(b,n,z)
 z=pcbnew.ZONE(b); z.SetLayer(L); z.SetNet(n); z.SetNetCode(n.GetNetCode()); z.SetPadConnection(pcbnew.ZONE_CONNECTION_THERMAL); z.SetLocalClearance(pcbnew.FromMM(.25)); z.SetMinThickness(pcbnew.FromMM(.20))
 poly=pcbnew.SHAPE_POLY_SET(); c=pcbnew.SHAPE_LINE_CHAIN()
 for q in [(97,50),(115,50),(115,71),(97,71)]: c.Append(P(*q))
 c.SetClosed(True); poly.AddOutline(c); z.SetOutline(poly); b.Add(z); b.BuildListOfNets()
 try: b.FillZones()
 except Exception: pass
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
