# Phase 24 storage-island upgrade blocker

Status: `PISXME_REVA_CLEAN_BLOCKED` for the authorized SATA/NVMe upgrade only.
The prior SATA-only board is preserved; this is not a claim that the original
board architecture is electrically impossible.

## Exact unresolved item

`NVME_BRIDGE_AUTHORITY_ASM2362`

The requested one-socket dual-mode implementation cannot be promoted because
the NVMe bridge is not qualified. The official ASMedia ASM2362 page confirms
function, interface class, QFN64 9 x 9 package, SPI external ROM, and several
protocol features, but it does not expose the exact pad-level pin map, package
land pattern, reference schematic, firmware/configuration image or authorized
programming workflow. No exact ASM2362 procurement record from DigiKey,
Mouser, Arrow/Newark, LCSC, or another traceable mainstream channel was
captured. A product page, marketplace listing, or guessed family footprint is
not enough for this project’s authority gate.

## Why implementation stops here

The NVMe device is the electrical owner of the PCIe and USB sides of the new
storage path. Guessing its pads, rails, reset/clock/flash wiring, or firmware
would create an unreviewable schematic and make native PCB parity meaningless.
The user explicitly required rejecting a bridge whose chip or firmware
ecosystem is impractical. Therefore no mystery ASM2362 symbol, footprint,
selector wiring, or PCB-only net repair was authored.

The M-key connector direction is also not yet production-closed: JAE
`SM3ZS067U215BMR1500` is manufacturer-listed as a key-M 67-position part, but
the exact drawing and pad-by-pad local land-pattern capture still must be
obtained. The existing J3 (`SM3ZS067U410ABR1000`) is explicitly a B-key SATA
socket and is not a valid substitute.

## Sources checked

- ASMedia ASM2362 official product page and its published feature/package
  information.
- TI TUSB9261 official product page, datasheet/programming resources, and
  exact DigiKey/Mouser records.
- TI HD3SS6126 official product page/datasheet and exact distributor pages.
- TI HD3SS3412 official product page/datasheet, including package pinout and
  electrical limits.
- JAE SM3 manufacturer series page and exact M-key family listing.
- Existing repo authority for JMS578, ASM1153E, the B-key JAE socket, and
  TUSB9261 firmware/configuration.

An independent read-only hardware review also inspected the captured ASMedia
page and prior repo evaluations. It reached the same conclusion for
ASM2362/ASM2364/ASM2464, JMS583/JMS586/JMS580, and RTL9210B: marketplace
availability does not substitute for manufacturer-authoritative pinout,
land-pattern, reference-circuit, firmware/configuration, programming, and
traceable procurement evidence. This corroborates the blocker without
relaxing any gate.

## Shortest human action to unblock

Obtain from ASMedia or an authorized design partner the ASM2362 design pack:
exact orderable suffix and datasheet/pinout, recommended schematic/land
pattern/3D data, firmware/configuration image and programming rights/tool,
and a prototype-quantity authorized supply quote. In parallel, obtain the
released JAE M-key drawing for `SM3ZS067U215BMR1500` (or a fully documented
equivalent). Once those are supplied, the storage island can be edited and
validated without reopening the board macro-floorplan.

## Continuation options

1. **Recommended:** user supplies the ASM2362 design pack and JAE M-key
   drawing/procurement confirmation; continue the authorized storage-island
   implementation and then resume Phase 24.
2. Qualify another NVMe bridge only if its manufacturer documentation,
   firmware/configuration path, exact package/land pattern, and two-channel
   procurement evidence are all available. This is a bounded component
   substitution, not an invitation to repeat the JMS578 hunt.
3. If dual-mode storage is dropped by user decision, retain the existing
   TUSB9261 + B-key SATA design and resume the original SATA-only Phase 24
   closure; that would materially change the latest objective and is not
   assumed here.
