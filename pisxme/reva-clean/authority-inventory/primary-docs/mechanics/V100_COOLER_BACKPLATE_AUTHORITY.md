# V100 SXM2 cooler and backplate authority

Date checked: 2026-08-29.

No public NVIDIA production CAD for the complete V100 SXM2 cooler, backplate,
fasteners, and surrounding chassis was found. NVIDIA public material provides
the module and 300 W-class thermal context, not a standalone carrier cooler
interface. Commercial water blocks and adapter photographs are not
dimensionally authoritative.

The safe Rev-A mechanical contract is the existing project reference envelope
in `design/BOARD_ZONES_AND_KEEPOUTS.md`: top cooler reservation x=10..160 mm,
y=22.5..117.5 mm; matching XY reservation underneath for backplate, bolts,
nuts, and washers; 150 x 95 mm area; 220 x 140 mm board service outline; and
at least +45 mm above the board as the conservative external-cooling volume in
`design/BOARD_ARCHITECTURE_V1.md`. F1/Q1 must remain outside this reservation
until a physical assembly check.

Candidates considered: NVIDIA public V100 documentation (electrical/thermal
authority only); commercial V100 water-block listings (availability/context
only); and the existing project measurements/zone contract (usable Rev-A
envelope). No proprietary model was copied.

Decision: `REV_A_EMPIRICAL_RISK`. The missing proprietary assembly CAD cannot
reasonably be closed from public sources, but the conservative measured XY and
vertical reservation are sufficient to prevent a false fit claim. Before
manufacture, measure the actual V100, cooler, backplate, fastener head, and
connector stack and record a clearance receipt. This residual risk must not be
hidden by calling a generic cooler model authoritative.

Provenance: NVIDIA V100 datasheet; project-authored clean-room envelope and
human-factors review; commercial listings are non-authoritative context.
