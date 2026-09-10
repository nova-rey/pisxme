# MIC2545A-1YM support switch authority for RTL9210B `ISOLATEB`

Status: `CLOSED` for the device pin/application facts; `OPEN` for promotion
of any existing RTL9210B support PCB until its pins are corrected and native
checked.

## Authoritative source

Microchip/Micrel, **MIC2545A/2549A Programmable Current-Limit High-Side
Switch**, document `M9999-062711-A`, June 2011:

<https://ww1.microchip.com/downloads/en/DeviceDoc/mic2545a.pdf>

The current Microchip product page identifies MIC2545A as an in-production
programmable high-side switch:

<https://www.microchip.com/en-us/product/mic2545a>

## Verified 8-pin SOP mapping

| Pin | Name | Required ownership |
|---:|---|---|
| 1 | EN | Active-high for `MIC2545A-1YM`; must not float |
| 2 | FLG | Active-low open-drain fault output; optional, may remain NC only if the design explicitly accepts no fault indication |
| 3 | GND | Ground return |
| 4 | ILIM | Current-limit resistor to GND |
| 5 | IN | Supply input; must be externally joined to pin 7 |
| 6 | OUT | Switched output; must be externally joined to pin 8 |
| 7 | IN | Supply input; must be externally joined to pin 5 |
| 8 | OUT | Switched output; must be externally joined to pin 6 |

The datasheet specifies 2.7–5.5 V operation, adjustable 0.5–3 A current
limit, and a 35 mΩ typical / 50 mΩ maximum on-resistance. It recommends a
0.1–1 µF bypass capacitor from `IN` to GND close to the part. The nominal
current limit is `I_LIMIT = 230 / R_SET`, with `R_SET` between 76.8 Ω and
459 Ω; the existing 76.8 Ω value is therefore nominally about 3 A, subject
to the datasheet tolerance and thermal checks.

## Package-drawing limitation

The same document's package-information page identifies the 8-pin SOIC (M)
body and 1.27 mm lead pitch, but it is a mechanical package drawing rather
than a recommended PCB land-pattern table. It therefore establishes package
identity and pin pitch, not the final pad length, toe/heel allowance,
solder-mask expansion, paste reduction, or courtyard. The disposable fixture
receipt records this limitation; a production footprint must be sourced from
an explicit manufacturer recommendation or independently reviewed against the
assembly-house rules before promotion.

## Reconciliation against retained corroborating evidence

The retained community RTL9210B XML is useful evidence that pin 12
`ISOLATEB` was used to control an MIC2545A-class SSD 3.3-V switch, but its
pin-function export is not authoritative for the duplicated `IN`/`OUT`
pins. In particular, it must not be used to infer that pins 5 and 7 are
different functional nodes or to omit either required external join.

The current PiSXMe isolated candidate does not promote this MIC2545A
network into production authority. Before promotion, instantiate a corrected
SOP-8 footprint/symbol network with both input pins tied to the source rail,
both output pins tied to `SSD_3V3`, `ILIM` tied through the selected 1%
resistor to GND, `EN` owned by `ISOLATEB`, and a nearby input bypass. Then
run native DRC and a saved-board endpoint audit, including a negative control
that removes one duplicated-pin join and proves the audit fails.

## Exact PiSXMe decision

This closes the MIC2545A device pin/application fact needed for the
`ISOLATEB` support decision. It does **not** close the RTL9210B production
support network, SSD power/inrush budget, or the final choice to promote
MIC2545A. Those remain explicit downstream gates rather than hidden
assumptions.
