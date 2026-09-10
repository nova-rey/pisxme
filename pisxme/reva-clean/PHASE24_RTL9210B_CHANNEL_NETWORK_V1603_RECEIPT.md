# Phase 24 RTL9210B channel-network receipt — V1603

Date: 2026-09-10  
Status: ACCEPTED AS PATH-B LAUNCH PRIMITIVE (not production integration)

V1603 starts from the accepted V1601 staggered U1 handoff and uses a
physical-envelope-aware channel plan: ordered B.Cu channels, separated
ordinary through-via transitions, and monotonic separated F.Cu dogbones into
the native J1/M.2 contacts. Track width is 0.20 mm, clearance is 0.20 mm,
and vias are 0.60 mm diameter with 0.30 mm drill. No plane-layer signal
routing or via-in-pad is used.

Native DRC (`PHASE24_RTL9210B_CHANNEL_NETWORK_V1603-drc.rpt`) reports two
inherited isolated-copper warnings and zero high-speed crossings, shorts,
clearance violations, dangling tracks, or footprint errors. The saved-board
audit (`phase24_rtl9210b_channel_network_v1603_audit.py`) connects all six
U1-to-J1 nets using actual pads/tracks/vias and passes six source-track
removal negative controls. The fixture is intentionally stripped to U1/J1/JH1,
so its 19 unrelated support/control/rail opens are not evidence against this
six-net primitive.

Mapping: `REFCLK_P -> J1.55`, `REFCLK_N -> J1.53`, `LANE0_RXP -> J1.43`,
`LANE0_RXN -> J1.41`, `LANE0_TXN -> J1.47`, `LANE0_TXP -> J1.49`.

V1603 closes the bounded launch experiment as a reusable local primitive. It
does not close Phase 24 or authorize production promotion; complete Path-B
support and acreage integration remain open.
