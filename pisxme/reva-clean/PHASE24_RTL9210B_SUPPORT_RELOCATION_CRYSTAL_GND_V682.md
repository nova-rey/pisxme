# RTL9210B Path-B V682 — intermediate crystal GND correction

V682 started from the native-clean V2 support relocation and added ordinary
GND stitching vias beside C1 and C2. Native DRC still reported one C1
starved-thermal finding because the C1 pad had no physical track to its via.
V682 is retained as an intermediate diagnostic, not a passing basis.
