# Phase 24 USB3 U12 monotonic V118 receipt

V118 is a disposable route-class experiment from the alias-clean V116
storage base. It retained only native J7 and U12 footprints, removed donor
copper/zones, and authored four pad-aware dogbones with ordinary through-vias
using the JLC 0.15 mm / 0.13208 mm profile.

The candidate was rejected by native DRC: 14 violations / 63 unconnected
items, including an RX-N/RX-P short at the source transition, one TX pair
crossing, and several local clearance/dangling-via findings. The source
escape itself is therefore not yet valid. This is route implementation
evidence, not placement or electrical-architecture evidence.

The next experiment must separate each pair's source transition from its
neighboring via field and assign the two pairs to non-crossing permitted
layers/corridors before entering the U12 pad field.
