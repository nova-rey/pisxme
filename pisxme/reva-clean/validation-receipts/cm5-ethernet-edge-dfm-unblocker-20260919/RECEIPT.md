# CM5/Ethernet edge DFM Unblocker reassessment

Outcome: `SELF_UNBLOCK`.

The retained candidate was produced from stale base `b483f077` and without the canonical `Package_SON` footprint-table context or the authorized local fine-escape `.kicad_dru`. Its two library findings and seven XIN/XOUT width findings are validation-context failures, not physical impossibility. The candidate must not be integrated directly.

Resume: derive only the declared C48-C51, C8, CM5_5V track/via delta onto current HEAD `7280badc`; bind canonical `fp-lib-table`, `sym-lib-table`, and local rules; produce a fresh Light candidate with current-head base and scoped hashes. No protected-bus, J1, high-speed, global-rule, or HPQ changes are authorized.
