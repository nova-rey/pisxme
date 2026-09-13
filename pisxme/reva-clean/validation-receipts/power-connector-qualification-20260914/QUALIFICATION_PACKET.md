# Six-loop power connector qualification packet

Status: **CANDIDATE_READY_WITH_OPEN_QUALIFICATION**. Base `daaf6d3b`; no CAD changed.

The proposed six-loop assembly is six Molex `0039300020`/5569 two-position right-angle headers, each carrying one 12-V contact and one return, mated to Molex 5557-family housings with 5556 phosphor-bronze tin-plated terminals `39000079` (reel) or `39000080` (bag), using 16-AWG stranded copper. The applicable public specification is Molex `PS-5556-004-001` Rev B1, ECM 851282, dated 2026-03-24. Its 16-AWG phosphor-bronze 2–3-circuit table gives an 8-A/circuit maximum guideline, 10-mΩ initial contact resistance, and 30 °C maximum rise basis with required application derating.

Closed evidence: exact header family, terminal material/parts, wire gauge class, current screen, contact resistance screen, 30 °C test basis, and private Library provenance (`c27ee33f`, `Library/briefs/molex-5556-ps004-v21-20260913.md`).

Open qualification fields: selected mating housing/terminal plating variant, crimp tooling and crimp acceptance, complete harness length and loop resistance at operating temperature, ambient/airflow installation, branch fuse I²t coordination, exact connector footprint/thermal installation for six headers, and byte hash of the public PDF (the direct fetch returned a non-equivalent response; no substitute hash is claimed).

These gaps are a package/procurement qualification dependency. They do not authorize CAD routing or a fabricated-hardware claim. The numeric V2.2 architecture remains conditionally signed by Power Authority; MPA/producer work waits for this qualification and the HPQ corridor dependency.
