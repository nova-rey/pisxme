# M2 service producer candidate receipt

Base SHA: `be293bb74b7cb85d40ee4b25edc43075be7391b3`.

Candidate board: `PHASE24_M2_SERVICE_PRODUCER.kicad_pcb`.

Changes audited against the base:

- J8 moved from `(245,150)` to `(205,140)`, 0 degrees, top side.
- TE M-key provenance is recorded for fixed J3 at `(220,165)`.
- Full `MECH_M2_2280` card envelope remains fixed at `(260,160)`; separate `MECH_M2_2280_CARD_BODY` and `MECH_M2_2280_CONNECTOR_MATING` mechanical representations are present.
- Existing pad/net contract is unchanged: 1,270 pads in both base and candidate; all pre-existing reference/pad/net signatures match. Added mechanical footprints contain no pads.

Targeted native Light DRC on the candidate returned exit 0 with KiCad 10.0.6: 273 violations and 393 unconnected items. Raw report: `m2-candidate-drc.json`. This is a producer result, not integrated closure.
