# Phase 24 storage U12 package-local power fanout — V1574

Status: REJECTED as an integrated route candidate; useful package-rule evidence

V1574 tested the manufacturer-authoritative TI RUA0042A package treatment: the
existing 0.25 mm pad width on 0.40 mm pitch was given a 0.15 mm local copper
clearance, while the global 0.20 mm rule remained unchanged. U12.13 escaped
with a standard 0.20 mm F.Cu dogbone to an ordinary 0.80/0.40 mm via at
(149.0,136.6), then to the In2 storage rail.

Native KiCad DRC reduced the disposable descendant to 460 findings / 335
unconnected pads, but the saved route still crosses the existing CM5_PERST
corridor. The fixture also intentionally omits the R81 attachment, so it is
not a complete storage-support candidate. No severity was waived and no
production board or schematic was changed.

The result supports retaining the package-local clearance treatment for a
future coherent source-field regeneration, but rejects this exact U12
placement/corridor.
