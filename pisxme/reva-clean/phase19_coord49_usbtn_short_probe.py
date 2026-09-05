from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
src=R/'PHASE19_RELOC_U270J190_COORD49_FULL.kicad_pcb'; out=R/'PHASE19_RELOC_U270J190_COORD49_USB_SHORT.kicad_pcb'
b=pcbnew.LoadBoard(str(src)); MM=pcbnew.FromMM; V=lambda x,y:pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def fp(r): return next(f for f in b.GetFootprints() if f.GetReference()==r)
def pad(f,n): return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def seg(n,a,z,l=pcbnew.F_Cu):
 if a!=z:
  t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(MM(.2)); t.SetNet(n); b.Add(t)
def via(n,p):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(MM(.5)); v.SetDrill(MM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
# Remove only the old CM5->U7 TX_N copper and its vias.
for t in list(b.GetTracks()):
 if t.GetNetname().endswith('CM5_USB3_TX_N'): b.Remove(t)
n=b.FindNet('/CORE_CM5/CM5_USB3_TX_N') or b.FindNet('CM5_USB3_TX_N'); s=xy(pad(fp('J7'),'140')); d=xy(pad(fp('U7'),'45'))
# Actual serialized endpoints; lower B.Cu corridor stays clear of the
# existing RX lanes, TX_P lane, and the SATA B.Cu launch.
seg(n,s,(71.2,s[1])); seg(n,(71.2,s[1]),(90,110)); via(n,(90,110)); seg(n,(90,110),(270,110),pcbnew.B_Cu); seg(n,(270,110),(270,104),pcbnew.B_Cu); via(n,(270,104)); seg(n,(270,104),d,pcbnew.F_Cu)
b.Save(str(out)); print(out)
