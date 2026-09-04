# V100 SXM2 cooler and backplate authority

Date checked: 2026-08-29.

No public NVIDIA production CAD for the complete V100 SXM2 cooler, backplate,
fasteners, and surrounding chassis was found. NVIDIA public material provides
the module and 300 W-class thermal context, not a standalone carrier cooler
interface. Commercial water blocks and adapter photographs are not
dimensionally authoritative.

The revised Rev-A mechanical contract assumes a standard air or liquid cooler
mounted to the SXM2 V100 module itself. The board reserves the actual SXM2
module, connector, mounting-hole/standoff, CM5/M.2, enclosure-floor, and
connector-access geometry only. No carrier-board cooler/backplate pattern or
generic underside exclusion is authoritative. The former 150 x 95 mm drawing
is a top-side cooling datum only; B.Cu and underside component/routing space
remains available unless a verified obstruction applies.

Candidates considered: NVIDIA public V100 documentation (electrical/thermal
authority only); commercial V100 water-block listings (availability/context
only); and the existing project measurements/zone contract (usable Rev-A
envelope). No proprietary model was copied.

Decision: `CLOSED_WITH_REV_A_CONTRACT`. Proprietary cooler CAD is outside the
Rev-A carrier-board contract. Any future custom carrier-mounted backplate is a
new mechanical requirement and must not silently constrain this design.

Provenance: NVIDIA V100 datasheet; project-authored clean-room envelope and
human-factors review; commercial listings are non-authoritative context.
