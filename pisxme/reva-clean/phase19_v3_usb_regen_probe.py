from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
src=R/'ACREAGE_PHASE19_STORAGE_MIDACREAGE_SATA_LAUNCH_V3.kicad_pcb'
out=R/'ACREAGE_PHASE19_STORAGE_V3_USB_REGEN_V4.kicad_pcb'
b=pcbnew.LoadBoard(str(src)); MM=pcbnew.FromMM; V=lambda x,y:pcbnew.VECTOR2I_MM(x,y)
def fp(r): return next(f for f in b.GetFootprints() if f.GetReference()==r)
def pad(f,n): return next(p for p in f.Pads() if str(p.GetNumber())==str(n))
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def seg(n,a,z,l=pcbnew.B_Cu):
 if a!=z:
  t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(MM(.20));t.SetNet(n);b.Add(t)
def via(n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(MM(.50));v.SetDrill(MM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);b.Add(v)
j,u=fp('J7'),fp('U7')
# Source breakouts are the exact validated Phase 18 endpoints. Columns
# decrease with increasing lane y, preventing staggered horizontals from
# cutting through an earlier vertical.
# Columns are ordered from the U7 pad field outward and clear the existing
# C18/C19 regulator support at y=120.
lanes=[('CM5_USB3_RX_N','128','42',(103,103),(114,140)),('CM5_USB3_RX_P','130','43',(103,105),(110,140.5)),('CM5_USB3_TX_N','140','45',(103,107),(106,141.5)),('CM5_USB3_TX_P','142','46',(82,112),(104,142))]
netmap={name:b.FindNet('/CORE_CM5/'+name) for name,*_ in lanes}
padmap={(name,'j'):pad(j,jp) for name,jp,up,start,landing in lanes}
padmap.update({(name,'u'):pad(u,up) for name,jp,up,start,landing in lanes})
posmap={k:xy(v) for k,v in padmap.items()}
# Remove only the four obsolete U7 tails. Preserve the native Phase 18 source
# segments and vias (including their DRC exclusions) while retaining the V3
# SATA graph. Resolve footprints and nets before the board mutation.
stale={
 tuple(sorted(((103.0,103.0),(105.5,105.0)))),
 tuple(sorted(((103.0,105.0),(105.5,105.5)))),
 tuple(sorted(((103.0,107.0),(105.5,106.5)))),
 tuple(sorted(((82.0,112.0),(105.5,107.0)))),
}
for t in list(b.GetTracks()):
 if t.GetNetname().startswith('/CORE_CM5/CM5_USB3_') and t.Type()!=14:
  a=(round(pcbnew.ToMM(t.GetStart().x),3),round(pcbnew.ToMM(t.GetStart().y),3))
  z=(round(pcbnew.ToMM(t.GetEnd().x),3),round(pcbnew.ToMM(t.GetEnd().y),3))
  if tuple(sorted((a,z))) in stale: b.Remove(t)
for name,jp,up,start,landing in lanes:
 n=netmap[name]
 if n is None: raise RuntimeError('missing '+name)
 sp=padmap[(name,'j')]; dp=padmap[(name,'u')]; sp.SetNet(n);sp.SetNetCode(n.GetNetCode());dp.SetNet(n);dp.SetNetCode(n.GetNetCode())
 sx,sy=start; lx,ly=landing
 # Leave the native source via on F.Cu and use four ordered F.Cu columns.
 # This keeps the continuation off the inherited B.Cu PCIe corridor.
 seg(n,start,(lx,sy),pcbnew.F_Cu)
 seg(n,(lx,sy),landing,pcbnew.F_Cu)
 seg(n,landing,posmap[(name,'u')],pcbnew.F_Cu)
# Refill inherited reference planes so native DRC evaluates the newly added
# transitions against real copper geometry rather than stale zone outlines.
_zones=list(b.Zones()); _filler=pcbnew.ZONE_FILLER(b); _filler.Fill(_zones)
b.Save(str(out)); print(out)
