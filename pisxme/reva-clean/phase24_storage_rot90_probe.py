"""Disposable Phase 24 discriminator: rotate U7 to free its clock edge.

This intentionally removes only the storage high-speed copper and re-adds the
authoritative clock support.  USB3/SATA are left for the next coordinated pass.
"""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb'; OUT=R/'PHASE24_STORAGE_ROT90_PROBE.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def P(f,n): return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def N(b,s):
 n=b.FindNet(s)
 if n is None: n=pcbnew.NETINFO_ITEM(b,s); n.SetNetCode(b.GetNetCount()+1); b.Add(n)
 return n
def S(b,n,a,z,l=pcbnew.F_Cu,w=.1321):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); b.Add(t)
def X(b,n,p):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
MAP={'Y1':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC','3':'/STORAGE/BRIDGE_XO','4':'/STORAGE/BRIDGE_VSSOSC'},'R23':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_XO'},'C42':{'1':'/STORAGE/BRIDGE_XI','2':'/STORAGE/BRIDGE_VSSOSC'},'C43':{'1':'/STORAGE/BRIDGE_XO','2':'/STORAGE/BRIDGE_VSSOSC'}}
LIB={'Y1':'Crystal_3225_4Pad','R23':'R_0402_1005Metric','C42':'C_0402_1005Metric','C43':'C_0402_1005Metric'}
def main():
 b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U7')
 u.SetOrientationDegrees(90)
 u_pads={str(q.GetNumber()):q for q in list(u.Pads())}
 names=set(v for m in MAP.values() for v in m.values()); ns={s:N(b,s) for s in names}
 io=pcbnew.PCB_IO_KICAD_SEXPR(); fs={}
 for ref,(x,y) in {'Y1':(140,145),'R23':(155,165),'C42':(125,165),'C43':(210,165)}.items():
  f=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),LIB[ref]); f.SetReference(ref); f.SetPosition(V(x,y)); f.SetLayer(pcbnew.B_Cu); f.SetOrientationDegrees(270 if ref=='Y1' else 0); b.Add(f); fs[ref]=f
  for q in f.Pads(): q.SetNet(ns[MAP[ref][str(q.GetNumber())]]); q.SetNetCode(ns[MAP[ref][str(q.GetNumber())]].GetNetCode())
 ps={r:{str(q.GetNumber()):xy(q) for q in list(f.Pads())} for r,f in fs.items()}
 # Rotate U7's storage side only; all old storage signal copper is obsolete.
 # Footprints are loaded before deletion because KiCad's SWIG wrapper can
 # invalidate a PCB_IO loader during board-owned item removal.
 # Remove all inherited copper.  This discriminator must contain only the
 # post-rotation U7 clock/support topology authored below.
 for t in list(b.GetTracks()):
  b.Remove(t)
 # This discriminator isolates the clock geometry; full-board plane and
 # return validation is performed only after a clean local route exists.
 for z in list(b.Zones()): b.Remove(z)
 for num,s in [('52','/STORAGE/BRIDGE_XI'),('53','/STORAGE/BRIDGE_VSSOSC'),('54','/STORAGE/BRIDGE_XO')]:
  q=u_pads[num]; q.SetNet(ns[s]); q.SetNetCode(ns[s].GetNetCode())
 # Rot90 actual clock row is the right edge: 52=(124.5,143),
 # 53=(124.5,142.5), 54=(124.5,142).  The three F.Cu dogbones leave the
 # lead field first, then transition to independent B.Cu lanes.
 XI,VS,XO=(ns[s] for s in ('/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_VSSOSC','/STORAGE/BRIDGE_XO'))
 # Complete the spread support network with explicit planar corridors.
 # U7-to-Y1 source legs are derived from the post-rotation pad positions and
 # leave the U7 lead field before changing layers.
 S(b,XO,(124.5,142),(127,140)); S(b,XO,(127,140),(134,140)); X(b,XO,(134,140)); S(b,XO,(134,140),(136,140),pcbnew.F_Cu); S(b,XO,(136,140),(136,146.1),pcbnew.F_Cu); X(b,XO,(136,146.1)); S(b,XO,(136,146.1),(137,146.1),pcbnew.B_Cu); X(b,XO,(137,146.1)); S(b,XO,(137,146.1),ps['Y1']['3'],pcbnew.F_Cu)
 S(b,VS,(124.5,142.5),(128,142.5)); X(b,VS,(128,142.5)); S(b,VS,(128,142.5),(132,142.5),pcbnew.B_Cu); S(b,VS,(132,142.5),(132,143.9),pcbnew.B_Cu); S(b,VS,(132,143.9),(139.15,143.9),pcbnew.B_Cu); X(b,VS,(139.15,143.9)); S(b,VS,(139.15,143.9),ps['Y1']['2'],pcbnew.F_Cu)
 S(b,XI,(124.5,143),(127,145.5)); X(b,XI,(130,145.5)); S(b,XI,(127,145.5),(130,145.5),pcbnew.B_Cu); S(b,XI,(130,145.5),(126,145.5),pcbnew.B_Cu); S(b,XI,(126,145.5),(126,145),pcbnew.B_Cu); S(b,XI,(126,145),(140.85,145),pcbnew.B_Cu); X(b,XI,(140.85,145)); S(b,XI,(140.85,145),ps['Y1']['1'],pcbnew.F_Cu)
 S(b,XO,(137,146.1),(137,158),pcbnew.B_Cu); X(b,XO,(137,158)); S(b,XO,(137,158),(155,158),pcbnew.F_Cu); X(b,XO,(155,158)); S(b,XO,(155,158),(156,165),pcbnew.B_Cu); X(b,XO,(156,165)); S(b,XO,(156,165),ps['R23']['2'],pcbnew.F_Cu); S(b,XO,(155,158),(210,158),pcbnew.F_Cu); X(b,XO,(210,158)); S(b,XO,(210,158),(209,164.5),pcbnew.B_Cu); X(b,XO,(209,164.5)); S(b,XO,(209,164.5),ps['C43']['1'],pcbnew.F_Cu)
 S(b,VS,(132,143.9),(115,143.9),pcbnew.B_Cu); S(b,VS,(115,143.9),(115,170),pcbnew.B_Cu); S(b,VS,(115,170),(126,170),pcbnew.B_Cu); X(b,VS,(126,170)); S(b,VS,(126,170),ps['C42']['2'],pcbnew.F_Cu)
 S(b,VS,ps['Y1']['4'],(145,146.1)); X(b,VS,(145,146.1)); S(b,VS,(145,146.1),(145,140),pcbnew.B_Cu); S(b,VS,(145,140),(195,140),pcbnew.B_Cu); S(b,VS,(195,140),(195,170),pcbnew.B_Cu); S(b,VS,(195,170),(212.5,170),pcbnew.B_Cu); X(b,VS,(212.5,170)); S(b,VS,(212.5,170),(212.5,165),pcbnew.F_Cu); S(b,VS,(212.5,165),ps['C43']['2'],pcbnew.F_Cu)
 S(b,XI,ps['Y1']['1'],(150,145)); X(b,XI,(150,145)); S(b,XI,(150,145),(150,165),pcbnew.B_Cu); S(b,XI,(150,165),(154,165),pcbnew.B_Cu); X(b,XI,(154,165)); S(b,XI,(154,165),ps['R23']['1'],pcbnew.F_Cu); S(b,XI,(150,160),(124,160),pcbnew.B_Cu); S(b,XI,(124,160),(124,164.5),pcbnew.B_Cu); X(b,XI,(124,164.5)); S(b,XI,(124,164.5),ps['C42']['1'],pcbnew.F_Cu)
 # Regulator capacitor materialization is intentionally a separate experiment.
 if b.Zones(): pcbnew.ZONE_FILLER(b).Fill(b.Zones())
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
