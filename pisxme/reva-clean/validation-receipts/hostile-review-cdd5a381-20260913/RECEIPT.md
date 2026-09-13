# Phase 24 independent hostile review

- Review date: 2026-09-13
- Review type: design verification / hostile review of one exact integrated candidate
- Candidate commit content: `cdd5a381` PCB bytes; documentation head `2ae2664ffeb21e759099dfc02b0244a002fce503`
- PCB SHA-256: `9938f35c69c9f314fe91498a4858022a4b4d75611d89c68a79c48fd09a11856e`
- Schematic: `PiSXMe_RevA_Clean.kicad_sch`
- Fixture: fresh detached checkout from `HEAD` using qualified `pisxme-kicad-light:v1`
- KiCad: `10.0.6`
- Sample count: one integrated board candidate; no fabricated hardware was tested.
- Instrument/calibration: native KiCad checker and pcbnew connectivity engine; calibration and measurement uncertainty are not applicable to this static design check.

## Commands and retained outputs

```text
kicad-cli pcb drc --severity-all --format json --exit-code-violations \
  --output hostile-drc.json \
  PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb
python3 phase24_patha_native_storage_census.py \
  PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb hostile-patha-census.json
python3 validation/phase24_power_return_census.py \
  PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb > hostile-power-census.json
kicad-cli sch export netlist --format kicadxml \
  --output hostile-native-netlist.xml PiSXMe_RevA_Clean.kicad_sch
python3 phase24_schematic_pcb_pad_parity_audit.py \
  PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb hostile-native-netlist.xml
```

Raw reports, return codes, tool version, native netlist, and focused census are
retained beside this receipt. The DRC command returned code `5` because the
violation threshold was exceeded; netlist export and parity returned `0`.
The parity process emitted three KiCad `PROPERTY_ENUM` assertions while
loading the board, but completed with zero mismatches; these assertions remain
an evidence limitation rather than a waiver.

## Results

### Integrated native DRC and physical shorts

The fresh DRC found `302` violations and `499` unconnected items. Classes:

- `clearance`: 138
- `track_width`: 118
- `copper_edge_clearance`: 15
- `track_dangling`: 9
- `via_dangling`: 7
- `courtyards_overlap`: 6
- `pth_inside_courtyard`: 5
- `holes_co_located`: 2
- `tracks_crossing`: 2
- `shorting_items`: 0

The two inherited `tracks_crossing` findings are between existing B.Cu
`JMS_AVDDL` segments and the `USB_RXN1` segment near `(151.0,148.0)`.
Zero `shorting_items` is a scoped observation only; the board fails the
zero-violation and zero-required-open acceptance criteria.

Five checker classes are reported as ignored by native DRC:
`missing_courtyard`, `track_not_centered_on_via`,
`tuning_profile_track_geometries`, `footprint_filters_mismatch`, and
`footprint_type_mismatch`. No explicit project DRC exclusion or severity
waiver was found. They remain acceptance gaps and were not treated as passes.

### Path-A storage connectivity

The native census inspected 292 pads across `U7/U11/U12/U13/U14/J3` and 26
required endpoint pairs. Eleven pairs pass; 15 remain open:

- U7 to C30-C33 bridge SATA capacitor pads: 4 opens;
- C30-C33 to U13 SATA pads: 4 opens;
- U13 to J3 M-key SATA pads: 4 opens;
- `STORAGE_SEL` U14.4 to U12.9 and U13.9: 2 opens;
- `AUTO_PEDET` J3.69 to U14.2: 1 open.

These are required physical connectivity checks, not synthetic expected-edge
checks. They fail the Path-A storage and native DRC acceptance rows. RTL9210B
Path B was not consumed by this review.

### Branch-B power delivery

The independent serialized object census found:

- `12V_IN_B`: 7 pads, 0 segments, 0 vias;
- `FUSED_12V_B`: 7 pads, 0 segments, 0 vias;
- `12V_PROTECTED`: 151 pads, 6 segments, 1 via.

Branch-B input and fused delivery therefore remain physically unrouted. This
fails power delivery closure; no current, transient, thermal, or hardware
result is implied.

### Netlist and pad binding

Fresh native schematic export succeeded with `--format kicadxml`. The
schematic-to-PCB pad-net audit found 814 authoritative schematic nodes, 1262
PCB pads, and zero expected-pad mismatches. It recorded 65 nonphysical-X
nodes, 2 J1 placeholder nodes, 8 J3 key-gap nodes, and the existing alias
contracts. This confirms ownership parity only; it does not prove copper
connectivity, surplus-pad correctness, SI, or manufacturing readiness. The
older checked-in XML is not used as the source of truth for this result.

## Disposition and triage

**FAIL / OPEN.** This review does not close any Phase 24 acceptance row and
does not authorize Phase 25 freeze. The immediate physical triage is the
binding Macro Placement Authority storage/power corridor decision requested by
Root. Preserve the two crossing coordinates, 15 Path-A endpoint list, and
Branch-B power census as the discriminating failure evidence. After any MPA
producer candidate, rerun focused connectivity and full DRC in a fresh Light
checkout; reject any candidate with a new short, crossing, manufacturing defect,
or unchanged required open. No hardware or field observation was performed.
