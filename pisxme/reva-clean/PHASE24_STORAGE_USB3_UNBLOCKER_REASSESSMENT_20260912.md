# Phase 24 storage USB3 blocker reassessment — 2026-09-12

The integrated Path-A M-key USB3 support issue is classified as an internal domain-authority blocker. V121, local-rule, CM5_PERST B.Cu, and east-handoff attempts preserved focused endpoint checks but failed integrated DRC through real U12/corridor or rule violations. The V6 topology is the best current route basis: ten links and the trace-removal negative control pass without USB3-specific shorts/crossings, but it uses 0.15-mm U11 fanout outside the current XIN/XOUT-only rule scope and retains U12/channel clearance findings.

Required authority decision: determine whether a narrowly windowed U11 USB3 fanout may use 0.15-mm traces and define exact U12 local clearance/via limits from the fabrication contract and land patterns. No global rule relaxation, suppression, architecture change, or alternative storage implementation is authorized.

After that decision, run one V6-based native Light discriminator with all ten endpoint checks, the trace-removal negative control, zero new shorts/crossings, and a fresh integrated report. Independent ERC, DFM, power, J1, and Path-B evidence work remains available.

Fresh blocker metrics: V6 native DRC 428/421 (fresh Light 430/421); U11 0.15-mm fanout violates the board-wide 0.20-mm rule, while U12 retains 0.0348-mm pad clearance, 0.1846-mm pair clearance, and 0.1211-mm via-pair clearance. No further same-class variants are authorized pending numeric DFM/package limits.
