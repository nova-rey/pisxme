# Fixture plan and qualification boundary

Date: 2026-09-06

## Scope and non-goals

In scope is qualification planning for an isolated `CM5 USB2/USB3 ->
RTL9210B-CG -> TE 1-2199230-4 M-key` concept. The work product is a plan and
evidence artifact only.

Out of scope are production integration, replacement of the Path-A storage
island, edits to `STORAGE.kicad_sch`, edits to any production or candidate
PCB, library promotion, BOM/CPL/Gerber release, firmware redistribution, and
commit creation.

## Decision

Do not author a complete native Path-B KiCad fixture yet. A pin-identity
harness could be drawn from the retained facts, but it would not be a valid
Path-B qualification fixture until the support circuit, direct sidebands,
land pattern, power behavior, and provisioning gates below are closed.

## Authority hierarchy

1. The retained RTL9210B-CG Rev. 1.1 PDF is the strongest available Path-B
   electrical source, but is community-hosted and says to follow the latest
   schematic circuit for configuration.
2. The community KiCad schematic is corroborating CAD and pin-name evidence,
   not a manufacturer application-circuit oracle. It is for a different WIP
   host design and contains unresolved author notes.
3. The community QFN footprint is not reusable unchanged: it declares
   `through_hole` for an all-SMD package. The retained qualification copy is a
   review candidate, not released land-pattern authority.
4. The current M-key authority is the TE `1-2199230-4` candidate and its
   manufacturer material, with SATA-IO TP-053 contact naming. That authority
   describes the socket/contact side; it does not settle direct RTL9210B
   sideband loading, pull-ups, sequencing, or empty-socket behavior.
5. The current six-layer fabrication basis is usable as a future routing
   constraint, not proof that this Path-B concept is electrically released.

## Safe technical facts for a future harness

These facts are safe to record as pin identity, not as a complete design:

| RTL9210B pin(s) | Function in retained Rev. 1.1 evidence | Fixture implication |
|---|---|---|
| 8 | PEDET/GPIO6; `1 = PCIe`, `0 = SATA` | Expose as an observed/controlled mode node; do not choose its pull-up or latch topology yet. |
| 13 | CLKREQB, open-drain capable, active low | Expose to a test point and M-key contact 52 only after the application circuit defines pull-up and ownership. |
| 14 | PERSTB, active-low 3.3 V output | Expose to a test point and M-key contact 50 only after sideband direction/sequence is confirmed. |
| 61/62 | PCIe REFCLK P/N output, 100 MHz | Route as a future differential pair; termination, coupling, and load remain application-circuit gates. |
| 64/65 | PCIe RX lane 0 / SATA RX pair | Shared lane-0 receive identity is corroborated; do not connect both protocol interpretations simultaneously. |
| 67/68 | PCIe TX lane 0 / SATA TX pair | Shared lane-0 transmit identity is corroborated; do not connect both protocol interpretations simultaneously. |
| 10 | PCIe HOT_PLUG input / GPIO8 share | M-key PEWAKE/DAS/hot-plug treatment is unresolved; do not silently wire it. |
| 12 | ISOLATEB output; controls PCIe or SATA power by mode | Board power switch/inrush implementation is unresolved. |
| 3 | Active-low RST_INPIN | Bring out reset access; exact RC/host ownership is not closed. |
| 33/17 | 5 V input pins for internal LDO/SWR | Provide named future power entry only; do not infer regulator decoupling or rail current from the pin table. |
| 34/16 | Internal 3.3 V / 1.1 V regulator outputs | Retained PDF says these are controller-internal; do not distribute them to the SSD or other loads. |
| 51 | RSET reference input | Requires authoritative resistor value and placement. |
| 52/53/54 | XTAL_AVDD33, XTAL_IN, XTAL_OUT | 25 MHz reference is identified; crystal load/circuit values need the approved application circuit. |
| 18/19/21/22/23/24 | SPI data/clock/quad/CS pins | Provide programming access, but flash MPN, image, configuration, and rights remain open. |
| 69 | RTL9210B exposed ground pad | Must be kept distinct from M.2 socket contact 69. |

## Current M-key correspondence

The current project authority uses TE `1-2199230-4`, a 67-position M-code
right-angle SMT socket. Native inspection of the current placement candidate
found 71 pads: 67 numbered contacts plus four mechanical pads (`M1`, `M2`,
`S1`, `S2`), with the contact pads represented as SMD.

The current contact naming is:

| M-key contact(s) | Current project name/function | Path-B disposition |
|---|---|---|
| 41/43 | SATA-B pair or PCIe PER lane 0 | Candidate shared receive pair; direct RTL mapping must be confirmed independently. |
| 47/49 | SATA-A pair or PCIe PET lane 0 | Candidate shared transmit pair; direct RTL mapping must be confirmed independently. |
| 50 | PERST# | Sideband contract open. |
| 52 | CLKREQ# | Pull-up, direction, and power sequencing open. |
| 53/55 | REFCLK-/REFCLK+ | Direct RTL output/load and AC/termination details open. |
| 54 | PEWAKE# | No safe RTL9210B pin assignment is established by the retained evidence. |
| 69 | CONFIG1 / PEDET convention | Socket-side convention is documented, but direct RTL9210B mode-control implementation is open. |
| 10, 38, 68 | DAS/DSS, DEVSLP, SUSCLK | Do not copy Path-A labels into Path B without direct RTL application guidance. |
| 1, 21, 75 | CONFIG contacts | Required inactive/default handling is not closed for Path B. |

The current Path-A mode matrix is not a Path-B wiring authority. It contains
selector-mediated ownership and must not be copied into a direct RTL9210B
fixture.

## Why a complete native fixture is stopped

The community schematic includes plausible values such as 12 kOhm RSET,
25 MHz crystal parts, decoupling, pull-ups, and power switches. Those values
are not accepted as Path-B authority because the retained qualification record
explicitly leaves exact support BOM/layout, M-key sidebands, SSD 3.3 V
inrush, empty/unpowered behavior, and firmware/provisioning open. The source
footprint also has a known metadata defect. Encoding these items in native
KiCad would make the artifact look more authoritative than its evidence.

## Precise gates before authoring the next native fixture

| Gate | Required evidence | Stop condition |
|---|---|---|
| B1 application circuit | Realtek/OEM-authorized current schematic or application circuit covering every power, reset, clock, RSET, flash, GPIO/share, and ISOLATEB connection | Any support value, power connection, or shared-pin mode remains inferred from community CAD. |
| B2 sidebands | Explicit RTL-to-M-key table for contacts 50, 52, 53/55, 54, 69, plus contacts 10/38/68 and config contacts 1/21/75; polarity, pull-ups, direction, power-off defaults, and empty-socket state | Any sideband is left as `TBD`, or Path-A selector rules are being reused. |
| B3 land pattern | Released package drawing/CAD or traceable manufacturer evidence, independently checked for 68 perimeter pads, exposed pad 69, mask/paste, courtyard, and model | Only community/auto-converted geometry is available. |
| B4 power and thermal | SSD 3.3 V current/inrush envelope, ISOLATEB load behavior, regulator rail budget, thermal assumptions, and measurement plan | The fixture could energize an SSD or alternate interface without a bounded current/thermal case. |
| B5 provisioning | Traceable RTL9210B lot, authorized firmware/config/updater, rights, supported flash MPN, and repeatable virgin-chip programming procedure | Only community binaries/configs or a working enclosure recovery path are available. |
| B6 native authoring | Standalone KiCad project, copied only into a disposable directory, with symbol/footprint provenance and no Path-A references | Any edit would land in the production project or silently reuse Path-A authority. |

## Smallest next fixture after B1-B5

Author one standalone native KiCad schematic/PCB pair for bench bring-up,
not a board-level Path-A replacement:

- one RTL9210B-CG symbol and independently gated QFN-68 footprint;
- the authorized support network and exact values from B1;
- 5 V/3.3 V inputs with current monitoring and bounded SSD 3.3 V switching;
- 25 MHz reference, reset, RSET, SPI flash footprint plus accessible flash
  pads, UART/JTAG pads, and an unambiguous recovery connector;
- CM5 USB2/USB3 boundary test pads or connector;
- TE M-key socket or a controlled socket-side test interface, with every
  sideband separately testable;
- mode controls for forced SATA, forced PCIe/NVMe, AUTO/PEDET, and empty
  socket, only if B2 specifies their electrical behavior;
- no integration with `PiSXMe_RevA_Clean.kicad_sch`, no Path-A selector
  symbols, and no production release outputs.

## Native validation acceptance for that future fixture

1. KiCad 10.0.5 loads and saves the standalone project without parse errors.
2. Schematic ERC is reviewed by class; no assumed `no-connect` marker may hide
   an unresolved support or sideband.
3. Netlist inspection proves every RTL pin and every M-key sideband endpoint.
4. PCB DRC runs with the six-layer stack/rules basis and separately reports
   intentional fixture omissions from real violations.
5. `--schematic-parity` proves the board matches the standalone schematic.
6. Mode-state checks cover forced SATA, forced NVMe, AUTO, empty socket,
   reset/startup, inactive interface isolation, ISOLATEB power behavior, and
   recovery access.
7. Firmware/image/config hashes, chip marking, flash MPN, and USB descriptors
   are recorded before any Path-B promotion discussion.
