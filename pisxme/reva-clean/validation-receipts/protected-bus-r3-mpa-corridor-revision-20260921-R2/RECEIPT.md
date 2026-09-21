# R2 MPA decision receipt

This receipt records a binding authority decision only. No CAD was edited and no
hardware was operated.

- Decision: `PISXME-P24-PROTECTED-BUS-MPA-20260921-R2`
- Work package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Decision: retain R1 local coordinates and R3 contract; clip the full-board F.Cu
  `POWER_GND` zone from the protected-bus corridors.
- Source failure evidence: R1 full candidate `426bc7e1050e6edfe0f04387cb928aa26b2f53bf`,
  1220 DRC / 391 unconnected; retained report shows repeated `solder_mask_bridge`
  violations against the global F.Cu zone.
- Required next owner: isolated producer, then serialized integration and fresh
  KiCad Light validation.
- Status: `BINDING_DECISION_FOR_PRODUCER; REQUIRES_PROTOTYPE_VALIDATION`.
