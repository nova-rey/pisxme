"""Transplant the preserved native Phase 19 SATA island into Phase 24.

This is a disposable reference-layout experiment.  It copies only actual
KiCad tracks/vias for the four bridge and four socket SATA nets, and moves the
saved U7/J3/coupling footprints as one coherent island.  No expected graph
edges or synthetic connectivity are authored.
"""
from pathlib import Path
import os
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_SELECTED_MACRO_ETH_SUPPORT_V15.kicad_pcb'
DONOR=R/'PHASE19_V3_USB_PROVEN_SPLIT_SATA_REFILL.kicad_pcb'
OUT=R/os.environ.get('PISXME_SATA_TRANSPLANT_OUT','PHASE24_SELECTED_MACRO_SATA_PROVEN_TRANSPLANT.kicad_pcb')

def net_is_sata(name):
    return ('BRIDGE_SATA_' in name) or ('SATA_M2_' in name)

def V(p): return pcbnew.VECTOR2I(p.x,p.y)

b=pcbnew.LoadBoard(str(BASE)); d=pcbnew.LoadBoard(str(DONOR))
if b is None or d is None: raise RuntimeError('unable to load base or donor')

# Preserve the donor's coherent local island placement and orientation.
for ref in ('U7','J3','C30','C31','C32','C33'):
    src=d.FindFootprintByReference(ref); dst=b.FindFootprintByReference(ref)
    if src is None or dst is None: raise RuntimeError(f'missing footprint {ref}')
    dst.SetPosition(V(src.GetPosition()))
    dst.SetOrientationDegrees(src.GetOrientationDegrees())

# Remove only inherited SATA copper from the base.
for t in list(b.GetTracks()):
    if net_is_sata(t.GetNetname()): b.Remove(t)

# Recreate donor copper with the base board's actual net objects.
for t in d.GetTracks():
    name=t.GetNetname()
    if not net_is_sata(name): continue
    n=b.FindNet(name)
    if n is None: raise RuntimeError(f'missing base net {name}')
    if isinstance(t,pcbnew.PCB_VIA):
        q=pcbnew.PCB_VIA(b);q.SetPosition(V(t.GetPosition()))
        # PCB_VIA::GetWidth requires an explicit copper layer in KiCad 10.
        # Use the donor's top layer to preserve the native via geometry.
        q.SetWidth(t.GetWidth(t.TopLayer()));q.SetDrill(t.GetDrill());q.SetLayerPair(t.TopLayer(),t.BottomLayer());q.SetNet(n);b.Add(q)
    else:
        q=pcbnew.PCB_TRACK(b);q.SetStart(V(t.GetStart()));q.SetEnd(V(t.GetEnd()))
        q.SetLayer(t.GetLayer());q.SetWidth(t.GetWidth());q.SetNet(n);b.Add(q)

b.Save(str(OUT)); print(OUT)
