"""V674: all-pad U1.39 source-escape rotation discriminator.

Unlike V666, every neighboring U1 pad retains its saved net identity.  Each
rotation gets one native U1.39 escape and an ordinary through-via; this is a
package/source-field discriminator, not a production Path-B board.
"""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_V35_U2_LEFT_RAILS_5V_PLUS_3V3_PROBE.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def track(b,n,l,a,z):
 q=pcbnew.PCB_TRACK(b); q.SetStart(a); q.SetEnd(z); q.SetLayer(l); q.SetWidth(W)
 q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b); v.SetPosition(q); v.SetWidth(pcbnew.FromMM(.60)); v.SetDrill(pcbnew.FromMM(.30))
 v.SetLayerPair(F,B); v.SetNet(n); v.SetNetCode(n.GetNetCode()); b.Add(v)
for angle in (0,90,180,270):
 b=pcbnew.LoadBoard(str(BASE))
 for f in list(b.GetFootprints()):
  if f.GetReference()!='U1': b.RemoveNative(f)
 for q in list(b.GetTracks()): b.RemoveNative(q)
 for z in list(b.Zones()): b.RemoveNative(z)
 u=b.FindFootprintByReference('U1'); u.SetOrientationDegrees(angle)
 p=u.FindPadByNumber('39').GetPosition()
 # Use a fixed outward-west escape from the native transformed pad.  The
 # rotation sweep changes the actual neighboring-pad geometry; the route is
 # deliberately identical in electrical width and via construction.
 a=p; e=P(p.x/1e6-1.6,p.y/1e6)
 n=b.FindNet('RTL_3V3'); track(b,n,F,a,e); via(b,n,e); track(b,n,B,e,P(e.x/1e6-5.0,e.y/1e6))
 out=H/f'PHASE24_RTL9210B_U139_ROTATION_{angle}_V674.kicad_pcb'
 b.BuildListOfNets(); b.Save(str(out)); print(out)
