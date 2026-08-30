# Architecture sanity decision

## Decision

**SWITCH_FAST_PORTS_TO_USB_A**

Architecture classification: **SIMPLIFICATION_RECOMMENDED_BEFORE_EXTERNAL_REVIEW**

This recommendation applies to a future PiSXMe architecture revision. The
active board and schematic were not modified by this audit.

## Basis

1. Raspberry Pi’s official CM5IO routes both native 5 Gbps CM5 USB3 ports
   directly to Type-A, with an explicit P/N naming swap for routing.
2. The official CM5 documentation makes the two USB3 ports independent; the
   connector shape does not reduce their rate or consume PCIe bandwidth.
3. The disposable two-port direct Type-A trial achieved 0 signal vias, 0
   unconnected items, and 0 DRC violations with maximum SuperSpeed skew
   0.109838 mm.
4. The active reversible Type-C design uses 80 USB3 signal vias, two muxes,
   duplicated connector-side branches, CC/source support, and four
   SuperSpeed ESD placements. Those are functional Type-C costs, not CM5
   transport requirements.
5. FAST-A storage and FAST-B commodity 2.5GbE are fully supported by ordinary
   USB3 Type-A at 5 Gbps. No USB-PD, reversible insertion, or PCIe storage
   path is required by the product requirement.

## Quantified simplification opportunity

For the two FAST ports, a fixed-host USB-A revision can remove:

- 2 HD3SS3212 muxes;
- 2 Type-C FAST CC/source control paths, subject to retaining suitable host
  VBUS switches;
- 2 of the 4 active SuperSpeed ESD branch devices if one SS ESD array per
  port is retained, or all 4 if the future protection review follows the
  official CM5IO USB3 sheet;
- 64 connector-side SuperSpeed signal vias, before any rerouting choice;
- the duplicated reversible branch conductors and local fanout constraints.

The focused trial removes 80 signal vias relative to the active two-port
USB3 signal-via total, but it omits final power/ESD and therefore must not be
used as a manufacturing BOM delta. A future schematic must re-add and verify
VBUS current limiting, USB2 companion behavior, ESD, connector footprints,
and the complete CM5 net mapping.

## Function lost

The only confirmed product-level loss is reversible USB-C plug orientation.
USB3 bandwidth, independent-port operation, storage use, optional 2.5GbE
USB-NIC use, and PCIe allocation are preserved. An internal dual-USB3 header
remains a valid enclosure-specific alternative but shifts SI/mechanical risk
into a cable and daughterboard, so it is not the primary recommendation.

## Active-board boundary

The active Type-C PiSXMe files remain byte-identical to the baseline. This
decision is a recommendation for the next design revision, not permission to
silently rewrite the current external-review package.
