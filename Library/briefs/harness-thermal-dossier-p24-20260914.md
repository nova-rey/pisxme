# P24 Harness and installation thermal evidence

Package: `P24-HARNESS-THERMAL-DOSSIER`  
Retrieved: 2026-09-14  
Status: `EVIDENCE_PACKET_READY_WITH_PRODUCT_ASSEMBLY_GAPS`

## Indexed evidence

The existing Library was checked first. Its Molex 5556/5569 brief and
`MOLEX_0039300020_AUTHORITY.md` establish the selected 0039300020 / 39-30-0020
two-position 5569 right-angle header, selected 5556 phosphor-bronze terminals
39000079/39000080, and the manufacturer family limits. The new bounded source
set adds:

- Molex `PS-5556-001-001` (current PS-5556-001, 2026-06-22 extraction):
  16-AWG stranded copper, 3.15 mm maximum insulation diameter; phosphor-bronze
  16-AWG table 8 A at 2–3 circuits, 7 A at 4–6, 6 A at 7–10 and 5 A at
  12–24; 30 °C maximum rise over ambient test basis. Molex requires application
  derating for ambient, PCB copper/trace size, adjacent heat, wire size,
  stranding/coating/length and crimp quality.
- Molex `PS-5556-004-001` Rev B1, ECM 851282 (2026-03-24): same 16-AWG/8-A
  and 30 °C rise basis, with phosphor-bronze operating range −40 to +105 °C.
- Molex `55560010-TS-000` (2019-11-01): family test summary including 5569,
  39012020 and 39000079. Its samples use 18–22 AWG and header 39281023, so it
  is family/test-method evidence only; the listed initial contact resistance
  requirement is 10 mΩ maximum.
- Molex current 5569/5557 series charts: right-angle through-hole 4.20 mm
  pitch family, 1.78 mm recommended PCB thickness, −40 to +105 °C family
  range; 39012020 is the two-circuit polarized/locking housing.
- Belden 39116 manufacturer record: possible 16-AWG wire class, 26x30 tinned
  copper, nominal 4.0 Ω/1000 ft DCR, 105 °C UL and −40 to +105 °C dry. This is
  a reference, not a selected PiSXMe cable.
- Southwire P50002-1A manufacturer record: 19-strand 16-AWG two-conductor
  reference with 4.181 Ω/1000 ft at 25 °C. It is not a selected PiSXMe cable.
- NIST Copper Wire Tables: standard copper temperature coefficient 0.00393/°C
  at 20 °C over the cited 10–100 °C interval.

URLs and retrieval metadata are recorded in `Library/provenance/sources.json`.
No external PDF, CAD model or restricted material was copied into the Library.
The Molex PDFs were browser-extracted; exact byte hashes remain unavailable.

## Reusable calculation and boundary

For the Southwire reference only, applying the NIST coefficient to 4.181
Ω/1000 ft at 25 °C gives 4.906 Ω/1000 ft at 70 °C, 5.148 at 85 °C and 5.470
at 105 °C. If V2.2's 20 mΩ harness limit means copper wire only, the maximum
one-way wire length before terminal/crimp allowance is 2.038 ft at 70 °C,
1.943 ft at 85 °C and 1.828 ft at 105 °C. At 6.4 A, a 20 mΩ loop dissipates
0.819 W; at 5.8 A it dissipates 0.673 W. These are screens, not measurements.

The V2.2 packet separately lists a 20 mΩ connector-loop screen. Power/Package
Authority must explicitly bind whether the harness limit excludes connector
contacts/crimps. If it is a complete-loop limit, their resistance must be
subtracted before cable length is accepted.

## Remaining product-specific gap

The sources do not establish the exact six cable MPNs/lengths, hot loop values,
PiSXMe ambient or airflow class, six header placement/spacing, adjacent heat,
local copper/solder temperature, or six-loop temperature margins. Resume the
package when Package/Power Authority signs a six-row harness schedule and
installation/thermal packet with those fields. This evidence does not
authorize CAD or claim fabricated-hardware qualification.
