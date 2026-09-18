BINDING_DECISION
Originating work package: P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER
Decision: PISXME-P24-MOLEX-NINE-BRANCH-MPA-20260918-R1

Anchors (top copper, 0 deg, unchanged): J1=(150,90); J5=(12,25); J6=(12,50); J9=(12,75). Remove/replace legacy OLD_J5 and OLD_J6 two-pin footprints and their obsolete copper; there shall be exactly one footprint per J5/J6/J9. J5/J6/J9 pin contract is pads 1,2,3 positive and pads 4,5,6 return, paired 1-4, 2-5, 3-6. Do not use the rejected alternating-pad assignment.

Exact support placement (top side, all 0 deg unless stated):
F1=(36,26.25), F2=(64,26.25), F3=(92,26.25)
F4=(36,51.25), F5=(64,51.25), F6=(92,51.25)
F7=(36,76.25), F8=(64,76.25), F9=(92,76.25)
D1=(108,10), C3=(108,29), U1=(108,34), Q1=(111,42)
U2=(108,62), Q2=(111,70), C4=(108,77), D2=(108,96)
TP2=(114,60), after source authority binds its probe net to 12V_BRANCH_JOIN; it is not allowed inside any J9/fuse courtyard. If its old FUSED_12V_A net is retained, source owner must provide that alias before copper is made.

Ownership/corridors:
- Connector positive pad escapes are short F.Cu only, then ordinary through-via arrays to In2.Cu. B1..B3 from J5 to F1..F3; B4..B6 J6 to F4..F6; B7..B9 J9 to F7..F9. Use ordered lanes, no F.Cu crossing neighboring PTH pads; keep positive pads 1-3 and return pads 4-6 distinct.
- Connector return pads 4-6 escape to ordinary through vias and nine distinct In4.Cu return lanes to POWER_RETURN_JOIN at x>=104. No return uses a signal route or a single neck. In1.Cu remains continuous POWER_GND under high-speed corridors; In4 local clearances are limited to these branch return lanes.
- Raw positive branch lanes occupy ordered In2 channels from each header to the west input pad group of its fuse. F1/F4/F7 are branch 1, F2/F5/F8 branch 2, F3/F6/F9 branch 3. Fuse pads 1-4 are raw and 5-8 are fused; use separate ordinary-via fanouts and no connector/fuse courtyard crossing.
- Fused outputs remain nine separate ordered In2 lanes from each fuse east pad group to a pre-protection 12V_BRANCH_JOIN at x=104..106. The join feeds the source/protection authority's U1/Q1 primary cohort. U2/Q2/D2/C4 stay physically separated and electrically non-credited unless the signed source contract explicitly binds them; no passive parallel-bus or N-1 credit.
- U1/Q1 primary source edge is west, protected edge east; Q1 output transitions through a multi-via array at x>=115 to In3.Cu. U2/Q2 has the same local orientation but its output remains a separate authority-controlled leg; never merge on F.Cu. D1/C3 and D2/C4 have local short positive/return/control loops; TVS returns go to nearby POWER_GND return vias.
- In3.Cu is the sole post-protection 12V_PROTECTED plane. Start at the Q1 post-protection via field x>=115, continue around the left side of the J1 courtyard, and approach the mapped J1 12-V field from x=116.5..124 then into only the already-authorized mapped contacts. Use parallel ordinary through-via arrays; no via-in-pad, unknown J1 contact, or narrow F.Cu trunk.
- In1.Cu and In4.Cu retain the existing POWER_GND return hierarchy. Join nine returns at a broad x>=104 POWER_RETURN_JOIN with multiple ground stitching arrays; preserve J1 ground-field assignments.
- F.Cu is limited to connector/fuse pad escapes, local protection/control loops, and probe access. Do not retain the rejected F.Cu star fanout to x=120 or the long raw/fused tracks. Existing 12V_IN_A/FUSED_12V_A stubs and all rejected B*_P_RAW/B*_P_PROTECTED tracks are producer-owned replaceable copper; delete only those named power nets and do not touch unrelated routes.
- Preserve J1/high-speed/clock/USB3/Ethernet/storage/CM5 copper and return structures. No new F.Cu/B.Cu high-current run may enter the J1 signal field, CM5 B.Cu corridors near y=76/80/82, or any validated differential corridor. Existing POWER_GND zones remain; make only footprint-specific legal clearance islands for new PTHs/NPTHs and no global rule relaxation.

Rationale: the rejected producer put fuses at (45,67,89) with 22-mm spacing, causing courtyard overlaps, kept OLD_J5/OLD_J6 under new headers, assigned alternating connector pads, put all nine raw/fused branches on one F.Cu star with unavoidable crossings and shorts, and drove a protected track through J9 and D2. The 28-mm fuse columns above leave 4-mm courtyard gaps and three 27-mm row bands leave 3-mm gaps. Each header's three contacts fan out into ordered inner-layer lanes, so no same-row PTH crossing is required; returns have their own In4 lanes. The protection column stays between fuse right edge x=104 and J1 courtyard left x=116.5, while post-protection copper enters In3 only after the Q1/Q2 transition. This changes physical ownership and layer allocation rather than replaying the rejected route.

Non-negotiable constraints: six-layer roles unchanged (F.Cu/In1 GND/In2 PWR/In3 PROTECTED_12V/In4 GND/B.Cu); ordinary through vias only; nine positive/return contract and 40A continuous/45A 100-ms source contract unchanged; no passive sharing credit; complete hot path <=10 mOhm and current/thermal/via evidence required; no J1 unknown/no-connect changes; no global rule/clearance relaxation; no orientation search or alternate placement after this decision. Producer must assert every coordinate and net/pad mapping before routing, return native connectivity/DRC and complete path/thermal extraction, then fresh Light validation at candidate SHA.

AUTHORITATIVE BASELINE DECLARATION: For P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER, this is the sole binding local placement/corridor plan. J1/J5/J6/J9 anchors remain at the exact coordinates above; F1-F9 use the 3x3 28-mm/25-mm grid; the protection cohort uses the exact left-of-J1 column; branch positives use ordered In2 source/fused lanes, branch returns use ordered In4 lanes, and only post-protection output transitions to the In3 J1 plane. No alternate placement or routing variant is authorized.
