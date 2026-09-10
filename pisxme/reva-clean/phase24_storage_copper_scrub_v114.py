"""V114: scrub storage-owned donor copper after native placement regeneration."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_STORAGE_REGEN_JLC_V113.kicad_pcb'
OUT=R/'PHASE24_STORAGE_COPPER_SCRUBBED_V114.kicad_pcb'
PREFIXES=('CM5_USB3_','CM5_STORAGE_USB2_','USB_RXP1','USB_RXN1','USB_TXP1','USB_TXN1',
          'JMS_','TUSB_','M2_','BRIDGE_','STORAGE_','FORCE_','AUTO_PEDET','MODE_IN')
def owned(name):
    # Saved donor boards may retain hierarchical aliases such as
    # /CORE_CM5/CM5_USB3_RX_N.  Match the canonical leaf name so aliases
    # cannot leave stale plane-layer copper in a supposedly scrubbed island.
    leaf=name.rsplit('/',1)[-1]
    return any(leaf==p or leaf.startswith(p) for p in PREFIXES)
b=pcbnew.LoadBoard(str(BASE)); removed=0
for item in list(b.GetTracks()):
 if owned(item.GetNetname()): b.RemoveNative(item); removed+=1
for z in list(b.Zones()):
 if owned(z.GetNetname()): b.RemoveNative(z); removed+=1
b.Save(str(OUT)); print(OUT, 'removed', removed, 'storage copper objects')
