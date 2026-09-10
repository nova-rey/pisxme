# RTL9210B-CG Path-B design authority package

Status: serious isolated parallel qualification candidate; **not
production-CAD authority**. Recommendation at V1560: **CONTINUE BOTH** with
Path A protected as fallback.
Updated 2026-09-10.

## Live CAD update — 2026-09-10

The corrected local QFN land pattern is now machine-audited against the
native integrated Path-B candidate by
`phase24_rtl9210b_landpattern_audit.py`: 69 pads are SMD on F.Cu, exposed
pad 69 is GND at 4.8 x 4.8 mm, and the source module has explicit `attr smd`
with no `through_hole` metadata. This closes the isolated CAD/DFM check for
the local qualification footprint. It does not replace the still-open
manufacturer/traceable-production land-pattern confirmation required before
production promotion.

## Identity and package

| Item | Current evidence | Status |
|---|---|---|
| Controller | Realtek `RTL9210B-CG` | Candidate |
| Package | QFN-68, nominal 8 x 8 mm, 0.4-mm pitch, exposed chip pad 69 | CLOSED at technical qualification; verify against an authorized production drawing before release |
| Local footprint | `RTL9210B-CG_QUALIFICATION.kicad_mod` | SMD, 69 pads, exposed pad 69, 4.8-mm EP, conservative 4.6-mm body/courtyard basis |
| Corroborating footprint | HynixCJR/LZ-1 source footprint | Rejected as direct authority: it carries incorrect `through_hole` metadata |
| Procurement lead | JLC/LCSC `C5143573` | Identity/SMT lead retained; live stock, price, and lead time remain unverified |

The local footprint is deliberately recreated from the corroborating QFN
geometry rather than copied unchanged. It must not be promoted until the
package drawing and solder-land pattern are cross-checked with Realtek or a
traceable assembly source.

The isolated integrated candidate now also restores the V12-style `TP6`
`RESET_N` bring-up endpoint. Its local F.Cu route passes native DRC and an
actual-trace-removal negative control; this is fixture/support evidence and
does not imply production schematic promotion.

## Pin and support facts

| Function | RTL9210B-CG pins | Path-B treatment | Evidence/status |
|---|---:|---|---|
| USB 3 TX/RX | 41/42 and 46/47 | CM5 USB3 source | Rev. 1.1 document + native corroborating XML; CLOSED technically |
| USB 2 D+/D- | 37/38 | CM5 USB2 storage connection | Same; CLOSED technically |
| Shared lane-0 TX | 68 `TXOP`, 67 `TXON` | Socket contacts 49/47 | Rev. 1.1 pin table + M-key platform convention; mapping corrected and audited |
| Shared lane-0 RX | 64 `RXIP`, 65 `RXIN` | Socket contacts 43/41 | Rev. 1.1 pin table + M-key platform convention; mapping corrected and audited |
| PCIe reference clock | 61/62 | Socket contacts 55/53 in NVMe mode | Technical evidence; final AC coupling/termination remains open |
| PCIe reset | 14 | Socket PERST# | Sideband ownership open pending application circuit |
| PCIe clock request | 13 | Socket CLKREQ# | Pull-up/idle-state implementation open |
| PEDET / CONFIG1 | 8 `GPIO6` | Socket contact 69 | Technical mode concept closed; empty-socket and exact pull network open |
| Reset input | 3 | Local reset/test access via TP6 in isolated candidate | TP6 topology closed in fixture; production application ownership open |
| SPI flash | 18/19/21/22/23/24 | Local flash with accessible programming points | Ecosystem evidence exists; production image/provenance open |
| Reference clock | 52–54 | 25-MHz crystal/reference network | Value/layout cross-check open |
| RSET | 51 | Local resistor | Corroborating designs indicate 12 kOhm; authorized value/layout still open |
| Main power/input | 17/33/34 and internal rails | Local 5-V input and documented internal regulator support | Complete application circuit required |
| PCIe/SATA isolation control | 12 | Must sequence the nonselected interface | Exact timing and SSD power relationship open |
| Exposed chip pad | 69 | GND plane/via field | Not M.2 contact 69; explicit distinction CLOSED |

The M.2 contact 69 is the socket-side PEDET/CONFIG1 contact. It is not the
RTL9210B exposed chip pad 69. The WIP community root schematic reverses the
lane associations and is quarantined as negative evidence.

## Provenance classes

1. **Technical primary candidate:** retained `community-lz1/rtl9210b.pdf`,
   Rev. 1.1 copy; requires Realtek/OEM confirmation for production.
2. **Corroborating CAD:** `community-lz1/RTL9210b_0.kicad_sch`, its native XML,
   and the independent support-netlist extraction. The source repository
   labels its PCB work in progress.
3. **Corroborating firmware ecosystem:** retained `bensuperpc/rtl9210` and
   `damnnfo/rtl9210b-firmware` artifacts. These demonstrate technical
   update/recovery tooling exists but do not grant redistribution rights or
   prove virgin-chip compatibility.
4. **Platform contact authority:** M-key contact convention and PEDET usage
   cross-checked against the retained M.2 platform reference material.

## Promotion gates

Path B may not replace Path A until all of these have evidence:

- authorized/current application circuit and package/land-pattern review;
- complete support BOM and local layout;
- correct SATA and NVMe mode-aware M.2 sideband ownership;
- SSD 3.3-V power, inrush, and thermal budget;
- traceable RTL9210B-CG lot and a repeatable virgin-part programming path;
- firmware/configuration hashes, provenance, and redistribution disposition;
- isolated hardware validation in SATA, NVMe, AUTO/PEDET, empty, reset, and
  inactive/unpowered states.

Until then this package is a serious comparison candidate and a safe source
for a disposable bring-up fixture, not permission to alter the clean board.
