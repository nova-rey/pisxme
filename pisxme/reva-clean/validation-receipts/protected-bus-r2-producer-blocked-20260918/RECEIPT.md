# Protected-bus R2 producer blocker

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Workstream: `protected-bus-r2-impl2`
- Base: `34dbf5dcc9a22faf398ca2ed20722a1cd31bc7e1`
- Required R2 authority: `PISXME-P24-PROTECTED-BUS-UPSTREAM-AUTHORITY-20260918-R2`
- Toolchain: `pisxme-kicad-light:v1`, KiCad `10.0.6`
- Result: **BLOCKED — approved R2 topology is absent from the assigned source state**
- Canonical CAD: unchanged
- Candidate: none

## Exact bounded commands and results

The qualified Light launcher was used with the allocated workspace
`/home/nyx/eda-workspaces/protected-bus-r2-impl2`:

```text
pisxme-worker start kicad-light protected-bus-r2-impl2 \
  /home/nyx/eda-workspaces/protected-bus-r2-impl2 1 1g -- bash -lc 'set +e; mkdir -p /workspace/output; \
  kicad-cli version > /workspace/output/kicad-version.txt 2> /workspace/output/kicad-version.stderr; vrc=$?; \
  kicad-cli pcb drc --format json --severity-all \
    --output /workspace/output/baseline-drc.json --exit-code-violations \
    /workspace/project/pisxme/reva-clean/PHASE24_FCU_POWER_GND_WIDTH_NORMALIZED.kicad_pcb \
    > /workspace/output/baseline-drc.stdout 2> /workspace/output/baseline-drc.stderr; drc_rc=$?; \
  kicad-cli sch export netlist --format kicadxml \
    --output /workspace/output/native-netlist.xml \
    /workspace/project/pisxme/reva-clean/PiSXMe_RevA_Clean.kicad_sch \
    > /workspace/output/netlist.stdout 2> /workspace/output/netlist.stderr; nrc=$?; \
  printf "VERSION_RC=%s\\nDRC_RC=%s\\nNETLIST_RC=%s\\n" "$vrc" "$drc_rc" "$nrc" \
    > /workspace/output/returncodes.txt; exit 0'
```

Raw results:

```text
VERSION_RC=0
DRC_RC=5
NETLIST_RC=0
Found 300 violations
Found 499 unconnected items
```

The native schematic netlist was written successfully and is 290280 bytes.
The raw DRC JSON, netlist, return codes, KiCad version, and machine-readable
topology census are retained under `raw/` and covered by `SHA256SUMS`.

## Binding topology contradiction

The R2 authority requires J5/J6/J9 and nine distinct fuse-holder branches:

```text
F1/F2/F3 at (36,15)/(64,15)/(92,15)
F4/F5/F6 at (36,40)/(64,40)/(92,40)
F7/F8/F9 at (36,65)/(64,65)/(92,65)
```

The assigned native PCB contains only these relevant references:

```text
J1  (150,90)   J5  (12,25)   J6  (12,45)
F1  (240,40)   F2  (50,120)
D1  (110,32)   D2  (110,72)
U1  (20,75)    U2  (20,95)   Q1 (30,78)   Q2 (10,108)
C3  (15,70)    C4  (15,90)  TP2 (22.5,80)
```

`J9` and `F3` through `F9` are absent from the PCB. The native schematic
netlist likewise contains only `J5`, `J6`, `F1`, and `F2` for this source
path. Its relevant electrical nodes are:

```text
12V_IN_A:        C3.2 F1.1 J5.1 U1.3 X4.1
12V_IN_B:        C4.2 F2.1 J6.1 U2.3 X4.2
FUSED_12V_A:     D1.1 F1.2 Q1.1 U1.6
FUSED_12V_B:     D2.1 F2.2 Q2.1 U2.6
```

The current source therefore has two input pairs, two fuse nets, and two
protection branches. Implementing R2 would require adding the missing J9 and
F3--F9 electrical symbols, branch net names, footprints, and protection
contracts, which exceeds the approved corridor-only scope and would invent
topology. Moving the existing F1/F2 or adding unconnected footprints would not
implement the nine-branch R2 specification and would fail connectivity.

## Stopping decision

No PCB edit, schematic edit, footprint guess, rule edit, R1 retry, alternate
placement search, or six-loop regulation was performed. Resistance, copper/
via/current, thermal, DFM, and targeted post-change DRC evidence cannot be
truthfully produced because the required branch topology is not present in the
assigned source state. This package returns **BLOCKED** to Product/Power
Authority for an explicit source-topology decision; no candidate is emitted.
